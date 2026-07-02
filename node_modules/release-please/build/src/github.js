"use strict";
// Copyright 2021 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
Object.defineProperty(exports, "__esModule", { value: true });
exports.sleepInMs = exports.GitHub = void 0;
const request_error_1 = require("@octokit/request-error");
const code_suggester_1 = require("./util/code-suggester");
const errors_1 = require("./errors");
const MAX_ISSUE_BODY_SIZE = 65536;
const MAX_SLEEP_SECONDS = 20;
const logger_1 = require("./util/logger");
const manifest_1 = require("./manifest");
const github_api_1 = require("./github-api");
const signoff_commit_message_1 = require("./util/signoff-commit-message");
const git_file_utils_1 = require("@google-automations/git-file-utils");
const composite_1 = require("./updaters/composite");
class GitHub {
    constructor(options) {
        var _a;
        /**
         * Get the list of file paths modified in a given commit.
         *
         * @param {string} sha The commit SHA
         * @returns {string[]} File paths
         * @throws {GitHubAPIError} on an API error
         */
        this.getCommitFiles = wrapAsync(async (sha) => {
            this.logger.debug(`Backfilling file list for commit: ${sha}`);
            const files = [];
            for await (const resp of this.octokit.paginate.iterator('GET /repos/{owner}/{repo}/commits/{ref}', {
                owner: this.repository.owner,
                repo: this.repository.repo,
                ref: sha,
            })) {
                // Paginate plugin doesn't have types for listing files on a commit
                const data = resp.data;
                for (const f of data.files || []) {
                    if (f.filename) {
                        files.push(f.filename);
                    }
                }
            }
            if (files.length >= 3000) {
                this.logger.warn(`Found ${files.length} files. This may not include all the files.`);
            }
            else {
                this.logger.debug(`Found ${files.length} files`);
            }
            return files;
        });
        this.graphqlRequest = wrapAsync(async (opts, options) => {
            var _a;
            let maxRetries = (_a = options === null || options === void 0 ? void 0 : options.maxRetries) !== null && _a !== void 0 ? _a : 5;
            let seconds = 1;
            while (maxRetries >= 0) {
                try {
                    const response = await this.graphql(opts);
                    if (response) {
                        return response;
                    }
                    this.logger.trace('no GraphQL response, retrying');
                }
                catch (err) {
                    if (err.status !== 502) {
                        throw err;
                    }
                    if (maxRetries === 0) {
                        this.logger.warn('ran out of retries and response is required');
                        throw err;
                    }
                    this.logger.info(`received 502 error, ${maxRetries} attempts remaining`);
                    if (typeof opts.num === 'number') {
                        if (maxRetries === 1) {
                            this.logger.info('last retry, forcing batch size to 1');
                            opts.num = 1;
                        }
                        else {
                            const nextNum = Math.floor(opts.num / 2);
                            if (nextNum >= 1) {
                                this.logger.info(`halving batch size from ${opts.num} to ${nextNum}`);
                                opts.num = nextNum;
                            }
                        }
                    }
                }
                maxRetries -= 1;
                if (maxRetries >= 0) {
                    this.logger.trace(`sleeping ${seconds} seconds`);
                    await (0, exports.sleepInMs)(1000 * seconds);
                    seconds = Math.min(seconds * 2, MAX_SLEEP_SECONDS);
                }
            }
            this.logger.trace('ran out of retries');
            return undefined;
        });
        /**
         * Returns a list of paths to all files with a given name.
         *
         * If a prefix is specified, only return paths that match
         * the provided prefix.
         *
         * @param filename The name of the file to find
         * @param ref Git reference to search files in
         * @param prefix Optional path prefix used to filter results
         * @throws {GitHubAPIError} on an API error
         */
        this.findFilesByFilenameAndRef = wrapAsync(async (filename, ref, prefix) => {
            if (prefix) {
                prefix = normalizePrefix(prefix);
            }
            this.logger.debug(`finding files by filename: ${filename}, ref: ${ref}, prefix: ${prefix}`);
            return await this.fileCache.findFilesByFilename(filename, ref, prefix);
        });
        /**
         * Returns a list of paths to all files matching a glob pattern.
         *
         * If a prefix is specified, only return paths that match
         * the provided prefix.
         *
         * @param glob The glob to match
         * @param ref Git reference to search files in
         * @param prefix Optional path prefix used to filter results
         * @throws {GitHubAPIError} on an API error
         */
        this.findFilesByGlobAndRef = wrapAsync(async (glob, ref, prefix) => {
            if (prefix) {
                prefix = normalizePrefix(prefix);
            }
            this.logger.debug(`finding files by glob: ${glob}, ref: ${ref}, prefix: ${prefix}`);
            return await this.fileCache.findFilesByGlob(glob, ref, prefix);
        });
        /**
         * Returns a list of paths to all files with a given file
         * extension.
         *
         * If a prefix is specified, only return paths that match
         * the provided prefix.
         *
         * @param extension The file extension used to filter results.
         *   Example: `js`, `java`
         * @param ref Git reference to search files in
         * @param prefix Optional path prefix used to filter results
         * @returns {string[]} List of file paths
         * @throws {GitHubAPIError} on an API error
         */
        this.findFilesByExtensionAndRef = wrapAsync(async (extension, ref, prefix) => {
            if (prefix) {
                prefix = normalizePrefix(prefix);
            }
            return this.fileCache.findFilesByExtension(extension, ref, prefix);
        });
        this.repository = options.repository;
        this.octokit = options.octokitAPIs.octokit;
        this.graphql = options.octokitAPIs.graphql;
        this.fileCache = new git_file_utils_1.RepositoryFileCache(this.octokit, this.repository);
        this.logger = (_a = options.logger) !== null && _a !== void 0 ? _a : logger_1.logger;
        this.gitHubApi = new github_api_1.GitHubApi({
            repository: this.repository,
            octokitAPIs: options.octokitAPIs,
            logger: this.logger,
        });
    }
    getGitHubApi() {
        return this.gitHubApi;
    }
    static async create(options) {
        const gitHubApi = await github_api_1.GitHubApi.create(options);
        return new GitHub({
            repository: gitHubApi.repository,
            octokitAPIs: gitHubApi.octokitAPIs,
            logger: options.logger,
        });
    }
    /**
     * Returns the list of commits to the default branch after the provided filter
     * query has been satified.
     *
     * @param {string} targetBranch Target branch of commit
     * @param {CommitFilter} filter Callback function that returns whether a
     *   commit/pull request matches certain criteria
     * @param {CommitIteratorOptions} options Query options
     * @param {number} options.maxResults Limit the number of results searched.
     *   Defaults to unlimited.
     * @param {boolean} options.backfillFiles If set, use the REST API for
     *   fetching the list of touched files in this commit. Defaults to `false`.
     * @returns {Commit[]} List of commits to current branch
     * @throws {GitHubAPIError} on an API error
     */
    async commitsSince(targetBranch, filter, options = {}) {
        const commits = [];
        const generator = this.mergeCommitIterator(targetBranch, options);
        for await (const commit of generator) {
            if (filter(commit)) {
                break;
            }
            commits.push(commit);
        }
        return commits;
    }
    /**
     * Iterate through commit history with a max number of results scanned.
     *
     * @param {string} targetBranch target branch of commit
     * @param {CommitIteratorOptions} options Query options
     * @param {number} options.maxResults Limit the number of results searched.
     *   Defaults to unlimited.
     * @param {boolean} options.backfillFiles If set, use the REST API for
     *   fetching the list of touched files in this commit. Defaults to `false`.
     * @yields {Commit}
     * @throws {GitHubAPIError} on an API error
     */
    async *mergeCommitIterator(targetBranch, options = {}) {
        var _a;
        const maxResults = (_a = options.maxResults) !== null && _a !== void 0 ? _a : Number.MAX_SAFE_INTEGER;
        let cursor = undefined;
        let results = 0;
        while (results < maxResults) {
            const response = await this.mergeCommitsGraphQL(targetBranch, cursor, options);
            // no response usually means that the branch can't be found
            if (!response) {
                break;
            }
            for (let i = 0; i < response.data.length; i++) {
                results += 1;
                yield response.data[i];
            }
            if (!response.pageInfo.hasNextPage) {
                break;
            }
            cursor = response.pageInfo.endCursor;
        }
    }
    async mergeCommitsGraphQL(targetBranch, cursor, options = {}) {
        var _a, _b, _c, _d, _e, _f, _g, _h, _j, _k;
        var _l;
        this.logger.debug(`Fetching merge commits on branch ${targetBranch} with cursor: ${cursor}`);
        const query = `query pullRequestsSince($owner: String!, $repo: String!, $num: Int!, $maxFilesChanged: Int, $targetBranch: String!, $cursor: String) {
      repository(owner: $owner, name: $repo) {
        ref(qualifiedName: $targetBranch) {
          target {
            ... on Commit {
              history(first: $num, after: $cursor) {
                nodes {
                  associatedPullRequests(first: 10) {
                    nodes {
                      number
                      title
                      baseRefName
                      headRefName
                      labels(first: 10) {
                        nodes {
                          name
                        }
                      }
                      body
                      mergeCommit {
                        oid
                      }
                      files(first: $maxFilesChanged) {
                        nodes {
                          path
                        }
                        pageInfo {
                          endCursor
                          hasNextPage
                        }
                      }
                    }
                  }
                  sha: oid
                  message
                  author {
                    name
                    email
                    user {
                      login
                    }
                  }
                }
                pageInfo {
                  hasNextPage
                  endCursor
                }
              }
            }
          }
        }
      }
    }`;
        const params = {
            cursor,
            owner: this.repository.owner,
            repo: this.repository.repo,
            num: (_a = options.batchSize) !== null && _a !== void 0 ? _a : 10,
            targetBranch,
            maxFilesChanged: 100, // max is 100
        };
        const response = await this.graphqlRequest({
            query,
            ...params,
        });
        if (!response) {
            this.logger.warn(`Did not receive a response for query: ${query}`, params);
            return null;
        }
        // if the branch does exist, return null
        if (!((_b = response.repository) === null || _b === void 0 ? void 0 : _b.ref)) {
            this.logger.warn(`Could not find commits for branch ${targetBranch} - it likely does not exist.`);
            return null;
        }
        const history = response.repository.ref.target.history;
        const commits = (history.nodes || []);
        // Count the number of pull requests associated with each merge commit. This is
        // used in the next step to make sure we only find pull requests with a
        // merge commit that contain 1 merged commit.
        const mergeCommitCount = {};
        for (const commit of commits) {
            for (const pr of commit.associatedPullRequests.nodes) {
                if ((_c = pr.mergeCommit) === null || _c === void 0 ? void 0 : _c.oid) {
                    (_d = mergeCommitCount[_l = pr.mergeCommit.oid]) !== null && _d !== void 0 ? _d : (mergeCommitCount[_l] = 0);
                    mergeCommitCount[pr.mergeCommit.oid]++;
                }
            }
        }
        const commitData = [];
        for (const graphCommit of commits) {
            const commit = {
                sha: graphCommit.sha,
                message: graphCommit.message,
                author: graphCommit.author
                    ? {
                        name: graphCommit.author.name || 'Unknown',
                        email: graphCommit.author.email,
                        username: (_e = graphCommit.author.user) === null || _e === void 0 ? void 0 : _e.login,
                    }
                    : undefined,
            };
            const mergePullRequest = graphCommit.associatedPullRequests.nodes.find(pr => {
                return (
                // Only match the pull request with a merge commit if there is a
                // single merged commit in the PR. This means merge commits and squash
                // merges will be matched, but rebase merged PRs will only be matched
                // if they contain a single commit. This is so PRs that are rebased
                // and merged will have ßSfiles backfilled from each commit instead of
                // the whole PR.
                pr.mergeCommit &&
                    pr.mergeCommit.oid === graphCommit.sha &&
                    mergeCommitCount[pr.mergeCommit.oid] === 1);
            });
            const pullRequest = mergePullRequest || graphCommit.associatedPullRequests.nodes[0];
            if (pullRequest) {
                commit.pullRequest = {
                    sha: commit.sha,
                    number: pullRequest.number,
                    baseBranchName: pullRequest.baseRefName,
                    headBranchName: pullRequest.headRefName,
                    mergeCommitOid: (_f = pullRequest.mergeCommit) === null || _f === void 0 ? void 0 : _f.oid,
                    title: pullRequest.title,
                    body: pullRequest.body,
                    labels: pullRequest.labels.nodes.map(node => node.name),
                    files: (((_g = pullRequest.files) === null || _g === void 0 ? void 0 : _g.nodes) || []).map(node => node.path),
                };
            }
            if (mergePullRequest) {
                if (((_j = (_h = mergePullRequest.files) === null || _h === void 0 ? void 0 : _h.pageInfo) === null || _j === void 0 ? void 0 : _j.hasNextPage) &&
                    options.backfillFiles) {
                    this.logger.info(`PR #${mergePullRequest.number} has many files, backfilling`);
                    commit.files = await this.getCommitFiles(graphCommit.sha);
                }
                else {
                    // We cannot directly fetch files on commits via graphql, only provide file
                    // information for commits with associated pull requests
                    commit.files = (((_k = mergePullRequest.files) === null || _k === void 0 ? void 0 : _k.nodes) || []).map(node => node.path);
                }
            }
            else if (options.backfillFiles) {
                // In this case, there is no squashed merge commit. This could be a simple
                // merge commit, a rebase merge commit, or a direct commit to the branch.
                // Fallback to fetching the list of commits from the REST API. In the future
                // we can perhaps lazy load these.
                commit.files = await this.getCommitFiles(graphCommit.sha);
            }
            commitData.push(commit);
        }
        return {
            pageInfo: history.pageInfo,
            data: commitData,
        };
    }
    /**
     * Iterate through merged pull requests with a max number of results scanned.
     *
     * @param {string} targetBranch The base branch of the pull request
     * @param {string} status The status of the pull request
     * @param {number} maxResults Limit the number of results searched. Defaults to
     *   unlimited.
     * @param {boolean} includeFiles Whether to fetch the list of files included in
     *   the pull request. Defaults to `true`.
     * @yields {PullRequest}
     * @throws {GitHubAPIError} on an API error
     */
    async *pullRequestIterator(targetBranch, status = 'MERGED', maxResults = Number.MAX_SAFE_INTEGER, includeFiles = true) {
        yield* this.gitHubApi.pullRequestIterator(targetBranch, status, maxResults, includeFiles);
    }
    /**
     * Iterate through releases with a max number of results scanned.
     *
     * @param {ReleaseIteratorOptions} options Query options
     * @param {number} options.maxResults Limit the number of results searched.
     *   Defaults to unlimited.
     * @yields {GitHubRelease}
     * @throws {GitHubAPIError} on an API error
     */
    async *releaseIterator(options = {}) {
        yield* this.gitHubApi.releaseIterator(options);
    }
    /**
     * Iterate through tags with a max number of results scanned.
     *
     * @param {TagIteratorOptions} options Query options
     * @param {number} options.maxResults Limit the number of results searched.
     *   Defaults to unlimited.
     * @yields {GitHubTag}
     * @throws {GitHubAPIError} on an API error
     */
    async *tagIterator(options = {}) {
        const maxResults = options.maxResults || Number.MAX_SAFE_INTEGER;
        let results = 0;
        for await (const response of this.octokit.paginate.iterator('GET /repos/{owner}/{repo}/tags', {
            owner: this.repository.owner,
            repo: this.repository.repo,
        })) {
            for (const tag of response.data) {
                if ((results += 1) > maxResults) {
                    break;
                }
                yield {
                    name: tag.name,
                    sha: tag.commit.sha,
                };
            }
            if (results > maxResults)
                break;
        }
    }
    /**
     * Fetch the contents of a file from the configured branch
     *
     * @param {string} path The path to the file in the repository
     * @returns {GitHubFileContents}
     * @throws {GitHubAPIError} on other API errors
     */
    async getFileContents(path) {
        return await this.getFileContentsOnBranch(path, this.repository.defaultBranch);
    }
    /**
     * Fetch the contents of a file
     *
     * @param {string} path The path to the file in the repository
     * @param {string} branch The branch to fetch from
     * @returns {GitHubFileContents}
     * @throws {FileNotFoundError} if the file cannot be found
     * @throws {GitHubAPIError} on other API errors
     */
    async getFileContentsOnBranch(path, branch) {
        this.logger.debug(`Fetching ${path} from branch ${branch}`);
        try {
            return await this.fileCache.getFileContents(path, branch);
        }
        catch (e) {
            if (e instanceof git_file_utils_1.FileNotFoundError) {
                throw new errors_1.FileNotFoundError(path);
            }
            throw e;
        }
    }
    async getFileJson(path, branch) {
        const content = await this.getFileContentsOnBranch(path, branch);
        return JSON.parse(content.parsedContent);
    }
    /**
     * Returns a list of paths to all files with a given name.
     *
     * If a prefix is specified, only return paths that match
     * the provided prefix.
     *
     * @param filename The name of the file to find
     * @param prefix Optional path prefix used to filter results
     * @returns {string[]} List of file paths
     * @throws {GitHubAPIError} on an API error
     */
    async findFilesByFilename(filename, prefix) {
        return this.findFilesByFilenameAndRef(filename, this.repository.defaultBranch, prefix);
    }
    /**
     * Returns a list of paths to all files matching a glob pattern.
     *
     * If a prefix is specified, only return paths that match
     * the provided prefix.
     *
     * @param glob The glob to match
     * @param prefix Optional path prefix used to filter results
     * @returns {string[]} List of file paths
     * @throws {GitHubAPIError} on an API error
     */
    async findFilesByGlob(glob, prefix) {
        return this.findFilesByGlobAndRef(glob, this.repository.defaultBranch, prefix);
    }
    /**
     * Open a pull request
     *
     * @param {PullRequest} pullRequest Pull request data to update
     * @param {string} targetBranch The base branch of the pull request
     * @param {string} message The commit message for the commit
     * @param {Update[]} updates The files to update
     * @param {CreatePullRequestOptions} options The pull request options
     * @throws {GitHubAPIError} on an API error
     */
    async createPullRequest(pullRequest, targetBranch, message, updates, options) {
        const changes = await this.buildChangeSet(updates, targetBranch);
        const prNumber = await (0, code_suggester_1.createPullRequest)(this.octokit, changes, {
            upstreamOwner: this.repository.owner,
            upstreamRepo: this.repository.repo,
            title: pullRequest.title,
            branch: pullRequest.headBranchName,
            description: pullRequest.body,
            primary: targetBranch,
            force: true,
            fork: !!(options === null || options === void 0 ? void 0 : options.fork),
            message,
            logger: this.logger,
            draft: !!(options === null || options === void 0 ? void 0 : options.draft),
            labels: pullRequest.labels,
        });
        if (prNumber === 0) {
            this.logger.warn('no code changes detected, skipping pull request creation');
            return {
                headBranchName: pullRequest.headBranchName,
                baseBranchName: targetBranch,
                number: 0,
                title: pullRequest.title,
                body: pullRequest.body,
                labels: pullRequest.labels,
                files: [],
            };
        }
        return await this.getPullRequest(prNumber);
    }
    /**
     * Fetch a pull request given the pull number
     * @param {number} number The pull request number
     * @returns {PullRequest}
     */
    async getPullRequest(number) {
        return await this.gitHubApi.getPullRequest(number);
    }
    /**
     * Update a pull request's title and body.
     * @param {number} number The pull request number
     * @param {ReleasePullRequest} releasePullRequest Pull request data to update
     * @param {string} targetBranch The target branch of the pull request
     * @param {string} options.signoffUser Optional. Commit signoff message
     * @param {boolean} options.fork Optional. Whether to open the pull request from
     *   a fork or not. Defaults to `false`
     * @param {PullRequestOverflowHandler} options.pullRequestOverflowHandler Optional.
     *   Handles extra large pull request body messages.
     */
    async updatePullRequest(number, releasePullRequest, targetBranch, options) {
        const changes = await this.buildChangeSet(releasePullRequest.updates, targetBranch);
        let message = releasePullRequest.title.toString();
        if (options === null || options === void 0 ? void 0 : options.signoffUser) {
            message = (0, signoff_commit_message_1.signoffCommitMessage)(message, options.signoffUser);
        }
        const title = releasePullRequest.title.toString();
        const body = ((options === null || options === void 0 ? void 0 : options.pullRequestOverflowHandler)
            ? await options.pullRequestOverflowHandler.handleOverflow(releasePullRequest)
            : releasePullRequest.body)
            .toString()
            .slice(0, MAX_ISSUE_BODY_SIZE);
        const prNumber = await (0, code_suggester_1.createPullRequest)(this.octokit, changes, {
            upstreamOwner: this.repository.owner,
            upstreamRepo: this.repository.repo,
            title,
            branch: releasePullRequest.headRefName,
            description: body,
            primary: targetBranch,
            force: true,
            fork: (options === null || options === void 0 ? void 0 : options.fork) === false ? false : true,
            message,
            logger: this.logger,
            draft: releasePullRequest.draft,
        });
        if (prNumber !== number) {
            this.logger.warn(`updated code for ${prNumber}, but update requested for ${number}`);
        }
        return this.gitHubApi.updatePullRequest(number, title, body);
    }
    /**
     * Given a set of proposed updates, build a changeset to suggest.
     *
     * @param {Update[]} updates The proposed updates
     * @param {string} defaultBranch The target branch
     * @return {Changes} The changeset to suggest.
     * @throws {GitHubAPIError} on an API error
     */
    async buildChangeSet(updates, defaultBranch) {
        // Sometimes multiple updates are proposed for the same file,
        // such as when the manifest file is additionally changed by the
        // node-workspace plugin. We need to merge these updates.
        const mergedUpdates = (0, composite_1.mergeUpdates)(updates);
        const changes = new Map();
        for (const update of mergedUpdates) {
            let content;
            try {
                content = await this.getFileContentsOnBranch(update.path, defaultBranch);
            }
            catch (err) {
                if (!(err instanceof errors_1.FileNotFoundError))
                    throw err;
                // if the file is missing and create = false, just continue
                // to the next update, otherwise create the file.
                if (!update.createIfMissing) {
                    this.logger.warn(`file ${update.path} did not exist`);
                    continue;
                }
            }
            const contentText = content
                ? Buffer.from(content.content, 'base64').toString('utf8')
                : undefined;
            const updatedContent = update.updater.updateContent(contentText, this.logger);
            if (updatedContent) {
                changes.set(update.path, {
                    content: updatedContent,
                    originalContent: (content === null || content === void 0 ? void 0 : content.parsedContent) || null,
                    mode: (content === null || content === void 0 ? void 0 : content.mode) || git_file_utils_1.DEFAULT_FILE_MODE,
                });
            }
        }
        return changes;
    }
    /**
     * Returns a list of paths to all files with a given file
     * extension.
     *
     * If a prefix is specified, only return paths that match
     * the provided prefix.
     *
     * @param extension The file extension used to filter results.
     *   Example: `js`, `java`
     * @param prefix Optional path prefix used to filter results
     * @returns {string[]} List of file paths
     * @throws {GitHubAPIError} on an API error
     */
    async findFilesByExtension(extension, prefix) {
        return this.findFilesByExtensionAndRef(extension, this.repository.defaultBranch, prefix);
    }
    /**
     * Create a GitHub release
     *
     * @param {Release} release Release parameters
     * @param {ReleaseOptions} options Release option parameters
     * @throws {DuplicateReleaseError} if the release tag already exists
     * @throws {GitHubAPIError} on other API errors
     */
    async createRelease(release, options = {}) {
        return await this.gitHubApi.createRelease(release, options);
    }
    /**
     * Makes a comment on a issue/pull request.
     *
     * @param {string} comment - The body of the comment to post.
     * @param {number} number - The issue or pull request number.
     * @throws {GitHubAPIError} on an API error
     */
    async commentOnIssue(comment, number) {
        return await this.gitHubApi.commentOnIssue(comment, number);
    }
    /**
     * Removes labels from an issue/pull request.
     *
     * @param {string[]} labels The labels to remove.
     * @param {number} number The issue/pull request number.
     */
    async removeIssueLabels(labels, number) {
        return await this.gitHubApi.removeIssueLabels(labels, number);
    }
    /**
     * Adds label to an issue/pull request.
     *
     * @param {string[]} labels The labels to add.
     * @param {number} number The issue/pull request number.
     */
    async addIssueLabels(labels, number) {
        return await this.gitHubApi.addIssueLabels(labels, number);
    }
    /**
     * Generate release notes from GitHub at tag
     * @param {string} tagName Name of new release tag
     * @param {string} targetCommitish Target commitish for new tag
     * @param {string} previousTag Optional. Name of previous tag to analyze commits since
     */
    async generateReleaseNotes(tagName, targetCommitish, previousTag) {
        return await this.gitHubApi.generateReleaseNotes(tagName, targetCommitish, previousTag);
    }
    /**
     * Create a single file on a new branch based on an existing
     * branch. This will force-push to that branch.
     * @param {string} filename Filename with path in the repository
     * @param {string} contents Contents of the file
     * @param {string} newBranchName Name of the new branch
     * @param {string} baseBranchName Name of the base branch (where
     *   new branch is forked from)
     * @returns {string} HTML URL of the new file
     */
    async createFileOnNewBranch(filename, contents, newBranchName, baseBranchName) {
        return await this.gitHubApi.createFileOnNewBranch(filename, contents, newBranchName, baseBranchName);
    }
}
exports.GitHub = GitHub;
/**
 * Normalize a provided prefix by removing leading and trailing
 * slashes.
 *
 * @param prefix String to normalize
 */
function normalizePrefix(prefix) {
    const normalized = prefix.replace(/^[/\\]/, '').replace(/[/\\]$/, '');
    if (normalized === manifest_1.ROOT_PROJECT_PATH) {
        return '';
    }
    return normalized;
}
/**
 * Wrap an async method with error handling
 *
 * @param fn Async function that can throw Errors
 * @param errorHandler An optional error handler for rethrowing custom exceptions
 */
/* eslint-disable @typescript-eslint/no-explicit-any */
const wrapAsync = (fn, errorHandler) => {
    return async (...args) => {
        try {
            return await fn(...args);
        }
        catch (e) {
            if (errorHandler) {
                errorHandler(e);
            }
            if (e instanceof request_error_1.RequestError) {
                throw new errors_1.GitHubAPIError(e);
            }
            throw e;
        }
    };
};
const sleepInMs = (ms) => new Promise(resolve => setTimeout(resolve, ms));
exports.sleepInMs = sleepInMs;
//# sourceMappingURL=github.js.map