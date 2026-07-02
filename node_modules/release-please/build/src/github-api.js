"use strict";
// Copyright 2026 Google LLC
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
exports.sleepInMs = exports.wrapAsync = exports.GitHubApi = exports.MAX_ISSUE_BODY_SIZE = exports.MAX_SLEEP_SECONDS = exports.GH_GRAPHQL_URL = exports.GH_API_URL = void 0;
const rest_1 = require("@octokit/rest");
const request_1 = require("@octokit/request");
const request_error_1 = require("@octokit/request-error");
const errors_1 = require("./errors");
const logger_1 = require("./util/logger");
const graphql_1 = require("@octokit/graphql");
const https_proxy_agent_1 = require("https-proxy-agent");
const http_proxy_agent_1 = require("http-proxy-agent");
exports.GH_API_URL = 'https://api.github.com';
exports.GH_GRAPHQL_URL = 'https://api.github.com';
exports.MAX_SLEEP_SECONDS = 20;
exports.MAX_ISSUE_BODY_SIZE = 65536;
class GitHubApi {
    constructor(options) {
        var _a;
        this.graphqlRequest = (0, exports.wrapAsync)(async (opts, options) => {
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
                    seconds = Math.min(seconds * 2, exports.MAX_SLEEP_SECONDS);
                }
            }
            this.logger.trace('ran out of retries');
            return undefined;
        });
        this.createPullRequest = (0, exports.wrapAsync)(async (pullRequest, targetBranch, options) => {
            const pullResponseData = (await this.octokit.pulls.create({
                owner: this.repository.owner,
                repo: this.repository.repo,
                title: pullRequest.title,
                head: `${this.repository.owner}:${pullRequest.headBranchName}`,
                base: targetBranch,
                body: pullRequest.body,
                maintainer_can_modify: true,
                draft: !!(options === null || options === void 0 ? void 0 : options.draft),
            })).data;
            this.logger.info(`Successfully opened pull request available at url: ${pullResponseData.html_url}.`);
            return await this.getPullRequest(pullResponseData.number);
        });
        /**
         * Fetch a pull request given the pull number
         * @param {number} number The pull request number
         * @returns {PullRequest}
         */
        this.getPullRequest = (0, exports.wrapAsync)(async (number) => {
            const response = await this.octokit.pulls.get({
                owner: this.repository.owner,
                repo: this.repository.repo,
                pull_number: number,
            });
            return {
                headBranchName: response.data.head.ref,
                baseBranchName: response.data.base.ref,
                number: response.data.number,
                title: response.data.title,
                body: response.data.body || '',
                files: [],
                labels: response.data.labels
                    .map((label) => label.name)
                    .filter((name) => !!name),
            };
        });
        this.updatePullRequest = (0, exports.wrapAsync)(async (number, title, body) => {
            const response = await this.octokit.pulls.update({
                owner: this.repository.owner,
                repo: this.repository.repo,
                pull_number: number,
                title,
                body,
                state: 'open',
            });
            return {
                headBranchName: response.data.head.ref,
                baseBranchName: response.data.base.ref,
                number: response.data.number,
                title: response.data.title,
                body: response.data.body || '',
                files: [],
                labels: response.data.labels
                    .map((label) => label.name)
                    .filter((name) => !!name),
            };
        });
        /**
         * Create a GitHub release
         *
         * @param {Release} release Release parameters
         * @param {ScmReleaseOptions} options Release option parameters
         * @throws {DuplicateReleaseError} if the release tag already exists
         * @throws {GitHubAPIError} on other API errors
         */
        this.createRelease = (0, exports.wrapAsync)(async (release, options = {}) => {
            if (options.forceTag) {
                try {
                    await this.octokit.git.createRef({
                        owner: this.repository.owner,
                        repo: this.repository.repo,
                        ref: `refs/tags/${release.tag.toString()}`,
                        sha: release.sha,
                    });
                }
                catch (err) {
                    // ignore if tag already exists
                    if (err.status === 422) {
                        this.logger.debug(`Tag ${release.tag.toString()} already exists, skipping tag creation`);
                    }
                    else {
                        throw err;
                    }
                }
            }
            const resp = await this.octokit.repos.createRelease({
                name: release.name,
                owner: this.repository.owner,
                repo: this.repository.repo,
                tag_name: release.tag.toString(),
                body: release.notes,
                draft: !!options.draft,
                prerelease: !!options.prerelease,
                target_commitish: release.sha,
            });
            return {
                id: resp.data.id,
                name: resp.data.name || undefined,
                tagName: resp.data.tag_name,
                sha: resp.data.target_commitish,
                notes: resp.data.body_text ||
                    resp.data.body ||
                    resp.data.body_html ||
                    undefined,
                url: resp.data.html_url,
                draft: resp.data.draft,
                uploadUrl: resp.data.upload_url,
            };
        }, e => {
            if (e instanceof request_error_1.RequestError) {
                if (e.status === 422 &&
                    errors_1.GitHubAPIError.parseErrors(e).some(error => {
                        return error.code === 'already_exists';
                    })) {
                    throw new errors_1.DuplicateReleaseError(e, 'tagName');
                }
            }
        });
        /**
         * Makes a comment on a issue/pull request.
         *
         * @param {string} comment - The body of the comment to post.
         * @param {number} number - The issue or pull request number.
         * @throws {GitHubAPIError} on an API error
         */
        this.commentOnIssue = (0, exports.wrapAsync)(async (comment, number) => {
            this.logger.debug(`adding comment to https://github.com/${this.repository.owner}/${this.repository.repo}/issues/${number}`);
            const resp = await this.octokit.issues.createComment({
                owner: this.repository.owner,
                repo: this.repository.repo,
                issue_number: number,
                body: comment,
            });
            return resp.data.html_url;
        });
        /**
         * Removes labels from an issue/pull request.
         *
         * @param {string[]} labels The labels to remove.
         * @param {number} number The issue/pull request number.
         */
        this.removeIssueLabels = (0, exports.wrapAsync)(async (labels, number) => {
            if (labels.length === 0) {
                return;
            }
            this.logger.debug(`removing labels: ${labels} from issue/pull ${number}`);
            await Promise.all(labels.map(label => this.octokit.issues.removeLabel({
                owner: this.repository.owner,
                repo: this.repository.repo,
                issue_number: number,
                name: label,
            })));
        });
        /**
         * Adds label to an issue/pull request.
         *
         * @param {string[]} labels The labels to add.
         * @param {number} number The issue/pull request number.
         */
        this.addIssueLabels = (0, exports.wrapAsync)(async (labels, number) => {
            if (labels.length === 0) {
                return;
            }
            this.logger.debug(`adding labels: ${labels} from issue/pull ${number}`);
            await this.octokit.issues.addLabels({
                owner: this.repository.owner,
                repo: this.repository.repo,
                issue_number: number,
                labels,
            });
        });
        this.repository = options.repository;
        this.octokitAPIs = options.octokitAPIs;
        this.octokit = options.octokitAPIs.octokit;
        this.graphql = options.octokitAPIs.graphql;
        this.logger = (_a = options.logger) !== null && _a !== void 0 ? _a : logger_1.logger;
    }
    static createDefaultAgent(baseUrl, defaultProxy) {
        if (!defaultProxy) {
            return undefined;
        }
        const { host, port } = defaultProxy;
        if (new URL(baseUrl).protocol.replace(':', '') === 'http') {
            return new http_proxy_agent_1.HttpProxyAgent(`http://${host}:${port}`);
        }
        else {
            return new https_proxy_agent_1.HttpsProxyAgent(`https://${host}:${port}`);
        }
    }
    static async create(options) {
        var _a, _b, _c, _d;
        const apiUrl = (_a = options.apiUrl) !== null && _a !== void 0 ? _a : exports.GH_API_URL;
        const graphqlUrl = (_b = options.graphqlUrl) !== null && _b !== void 0 ? _b : exports.GH_GRAPHQL_URL;
        const releasePleaseVersion = require('../../package.json').version;
        const apis = (_c = options.octokitAPIs) !== null && _c !== void 0 ? _c : {
            octokit: new rest_1.Octokit({
                baseUrl: apiUrl,
                auth: options.token,
                request: {
                    agent: this.createDefaultAgent(apiUrl, options.proxy),
                    fetch: options.fetch,
                },
            }),
            request: request_1.request.defaults({
                baseUrl: apiUrl,
                headers: {
                    'user-agent': `release-please/${releasePleaseVersion}`,
                    Authorization: `token ${options.token}`,
                },
                fetch: options.fetch,
            }),
            graphql: graphql_1.graphql.defaults({
                baseUrl: graphqlUrl,
                request: {
                    agent: this.createDefaultAgent(graphqlUrl, options.proxy),
                    fetch: options.fetch,
                },
                headers: {
                    'user-agent': `release-please/${releasePleaseVersion}`,
                    Authorization: `token ${options.token}`,
                    'content-type': 'application/vnd.github.v3+json',
                },
            }),
        };
        const opts = {
            repository: {
                owner: options.owner,
                repo: options.repo,
                defaultBranch: (_d = options.defaultBranch) !== null && _d !== void 0 ? _d : (await GitHubApi.defaultBranch(options.owner, options.repo, apis.octokit)),
            },
            octokitAPIs: apis,
            logger: options.logger,
        };
        return new GitHubApi(opts);
    }
    static async defaultBranch(owner, repo, octokit) {
        const { data } = await octokit.repos.get({
            repo,
            owner,
        });
        return data.default_branch;
    }
    /**
     * Iterate through merged pull requests with a max number of results scanned.
     *
     * @param {string} targetBranch Target branch of commit.
     * @param {string} status The status of the pull request. Defaults to 'MERGED'.
     * @param {number} maxResults Limit the number of results searched. Defaults to
     *   unlimited.
     * @param {boolean} includeFiles Whether to fetch the list of files included in
     *   the pull request. Defaults to `true`.
     * @yields {PullRequest}
     * @throws {GitHubAPIError} on an API error
     */
    async *pullRequestIterator(targetBranch, status = 'MERGED', maxResults = Number.MAX_SAFE_INTEGER, includeFiles = true) {
        const generator = includeFiles
            ? this.pullRequestIteratorWithFiles(targetBranch, status, maxResults)
            : this.pullRequestIteratorWithoutFiles(targetBranch, status, maxResults);
        for await (const pullRequest of generator) {
            yield pullRequest;
        }
    }
    /**
     * Helper implementation of pullRequestIterator that includes files via
     * the graphQL API.
     *
     * @param {string} targetBranch The base branch of the pull request
     * @param {string} status The status of the pull request
     * @param {number} maxResults Limit the number of results searched
     */
    async *pullRequestIteratorWithFiles(targetBranch, status = 'MERGED', maxResults = Number.MAX_SAFE_INTEGER) {
        let cursor = undefined;
        let results = 0;
        while (results < maxResults) {
            const response = await this.pullRequestsGraphQL(targetBranch, status, cursor);
            // no response usually means we ran out of results
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
    /**
     * Helper implementation of pullRequestIterator that excludes files
     * via the REST API.
     *
     * @param {string} targetBranch The base branch of the pull request
     * @param {string} status The status of the pull request
     * @param {number} maxResults Limit the number of results searched
     */
    async *pullRequestIteratorWithoutFiles(targetBranch, status = 'MERGED', maxResults = Number.MAX_SAFE_INTEGER) {
        const statusMap = {
            OPEN: 'open',
            CLOSED: 'closed',
            MERGED: 'closed',
        };
        let results = 0;
        for await (const { data: pulls } of this.octokit.paginate.iterator('GET /repos/{owner}/{repo}/pulls', {
            state: statusMap[status],
            owner: this.repository.owner,
            repo: this.repository.repo,
            base: targetBranch,
            sort: 'updated',
            direction: 'desc',
        })) {
            for (const pull of pulls) {
                // The REST API does not have an option for "merged"
                // pull requests - they are closed with a `merged_at` timestamp
                if (status !== 'MERGED' || pull.merged_at) {
                    results += 1;
                    yield {
                        headBranchName: pull.head.ref,
                        baseBranchName: pull.base.ref,
                        number: pull.number,
                        title: pull.title,
                        body: pull.body || '',
                        labels: pull.labels.map((label) => label.name),
                        files: [],
                        sha: pull.merge_commit_sha || undefined,
                    };
                    if (results >= maxResults) {
                        break;
                    }
                }
            }
            if (results >= maxResults) {
                break;
            }
        }
    }
    /**
     * Return a list of merged pull requests. The list is not guaranteed to be sorted
     * by merged_at, but is generally most recent first.
     *
     * @param {string} targetBranch - Base branch of the pull request. Defaults to
     *   the configured default branch.
     * @param {number} page - Page of results. Defaults to 1.
     * @param {number} perPage - Number of results per page. Defaults to 100.
     * @returns {PullRequestHistory | null} - List of merged pull requests
     * @throws {GitHubAPIError} on an API error
     */
    async pullRequestsGraphQL(targetBranch, states = 'MERGED', cursor) {
        var _a;
        this.logger.debug(`Fetching ${states} pull requests on branch ${targetBranch} with cursor ${cursor}`);
        const response = await this.graphqlRequest({
            query: `query mergedPullRequests($owner: String!, $repo: String!, $num: Int!, $maxFilesChanged: Int, $targetBranch: String!, $states: [PullRequestState!], $cursor: String) {
        repository(owner: $owner, name: $repo) {
          pullRequests(first: $num, after: $cursor, baseRefName: $targetBranch, states: $states, orderBy: {field: CREATED_AT, direction: DESC}) {
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
            pageInfo {
              endCursor
              hasNextPage
            }
          }
        }
      }`,
            cursor,
            owner: this.repository.owner,
            repo: this.repository.repo,
            num: 25,
            targetBranch,
            states,
            maxFilesChanged: 64,
        });
        if (!((_a = response === null || response === void 0 ? void 0 : response.repository) === null || _a === void 0 ? void 0 : _a.pullRequests)) {
            this.logger.warn(`Could not find merged pull requests for branch ${targetBranch} - it likely does not exist.`);
            return null;
        }
        const pullRequests = (response.repository.pullRequests.nodes ||
            []);
        return {
            pageInfo: response.repository.pullRequests.pageInfo,
            data: pullRequests.map(pullRequest => {
                var _a, _b, _c;
                return {
                    sha: (_a = pullRequest.mergeCommit) === null || _a === void 0 ? void 0 : _a.oid,
                    number: pullRequest.number,
                    baseBranchName: pullRequest.baseRefName,
                    headBranchName: pullRequest.headRefName,
                    labels: (((_b = pullRequest.labels) === null || _b === void 0 ? void 0 : _b.nodes) || []).map(l => l.name),
                    title: pullRequest.title,
                    body: pullRequest.body + '',
                    files: (((_c = pullRequest.files) === null || _c === void 0 ? void 0 : _c.nodes) || []).map(node => node.path),
                };
            }),
        };
    }
    /**
     * Iterate through releases with a max number of results scanned.
     *
     * @param {ReleaseIteratorOptions} options Query options
     * @param {number} options.maxResults Limit the number of results scanned.
     *   Defaults to unlimited.
     * @yields {ScmRelease}
     * @throws {GitHubAPIError} on an API error
     */
    async *releaseIterator(options = {}) {
        var _a;
        const maxResults = (_a = options.maxResults) !== null && _a !== void 0 ? _a : Number.MAX_SAFE_INTEGER;
        let results = 0;
        let cursor = undefined;
        while (true) {
            const response = await this.releaseGraphQL(cursor);
            if (!response) {
                break;
            }
            for (let i = 0; i < response.data.length; i++) {
                if ((results += 1) > maxResults) {
                    break;
                }
                yield response.data[i];
            }
            if (results > maxResults || !response.pageInfo.hasNextPage) {
                break;
            }
            cursor = response.pageInfo.endCursor;
        }
    }
    async releaseGraphQL(cursor) {
        var _a, _b, _c;
        this.logger.debug(`Fetching releases with cursor ${cursor}`);
        const response = await this.graphqlRequest({
            query: `query releases($owner: String!, $repo: String!, $num: Int!, $cursor: String) {
        repository(owner: $owner, name: $repo) {
          releases(first: $num, after: $cursor, orderBy: {field: CREATED_AT, direction: DESC}) {
            nodes {
              name
              tag {
                name
              }
              tagCommit {
                oid
              }
              url
              description
              isDraft
            }
            pageInfo {
              endCursor
              hasNextPage
            }
          }
        }
      }`,
            cursor,
            owner: this.repository.owner,
            repo: this.repository.repo,
            num: 25,
        });
        if (!((_c = (_b = (_a = response === null || response === void 0 ? void 0 : response.repository) === null || _a === void 0 ? void 0 : _a.releases) === null || _b === void 0 ? void 0 : _b.nodes) === null || _c === void 0 ? void 0 : _c.length)) {
            this.logger.warn('Could not find releases.');
            return null;
        }
        const releases = response.repository.releases.nodes;
        return {
            pageInfo: response.repository.releases.pageInfo,
            data: releases
                .filter(release => !!release.tagCommit)
                .map(release => {
                if (!release.tag || !release.tagCommit) {
                    this.logger.debug(release);
                }
                return {
                    name: release.name || undefined,
                    tagName: release.tag ? release.tag.name : 'unknown',
                    sha: release.tagCommit.oid,
                    notes: release.description,
                    url: release.url,
                    draft: release.isDraft,
                };
            }),
        };
    }
    /**
     * Generate release notes from GitHub at tag
     * @param {string} tagName Name of new release tag
     * @param {string} targetCommitish Target commitish for new tag
     * @param {string} previousTag Optional. Name of previous tag to analyze commits since
     */
    async generateReleaseNotes(tagName, targetCommitish, previousTag) {
        const resp = await this.octokit.repos.generateReleaseNotes({
            owner: this.repository.owner,
            repo: this.repository.repo,
            tag_name: tagName,
            previous_tag_name: previousTag,
            target_commitish: targetCommitish,
        });
        return resp.data.body;
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
        // create or update new branch to match base branch
        await this.forkBranch(newBranchName, baseBranchName);
        // use the single file upload API
        const { data: { content }, } = await this.octokit.repos.createOrUpdateFileContents({
            owner: this.repository.owner,
            repo: this.repository.repo,
            path: filename,
            // contents need to be base64 encoded
            content: Buffer.from(contents, 'binary').toString('base64'),
            message: 'Saving release notes',
            branch: newBranchName,
        });
        return (content === null || content === void 0 ? void 0 : content.html_url) || '';
    }
    /**
     * Fork a branch from a base branch.
     */
    async forkBranch(targetBranchName, baseBranchName) {
        const baseBranchSha = await this.getBranchSha(baseBranchName);
        if (!baseBranchSha) {
            throw new errors_1.ConfigurationError(`Unable to find base branch: ${baseBranchName}`, 'core', `${this.repository.owner}/${this.repository.repo}`);
        }
        if (await this.getBranchSha(targetBranchName)) {
            const branchSha = await this.updateBranchSha(targetBranchName, baseBranchSha);
            this.logger.debug(`Updated ${targetBranchName} to match ${baseBranchName} at ${branchSha}`);
            return branchSha;
        }
        else {
            const branchSha = await this.createNewBranch(targetBranchName, baseBranchSha);
            this.logger.debug(`Created ${targetBranchName} from ${baseBranchName} at ${branchSha}`);
            return branchSha;
        }
    }
    /**
     * Helper to fetch the SHA of a branch
     */
    async getBranchSha(branchName) {
        this.logger.debug(`Looking up SHA for branch: ${branchName}`);
        try {
            const { data: { object: { sha }, }, } = await this.octokit.git.getRef({
                owner: this.repository.owner,
                repo: this.repository.repo,
                ref: `heads/${branchName}`,
            });
            this.logger.debug(`SHA for branch: ${sha}`);
            return sha;
        }
        catch (e) {
            if (e instanceof request_error_1.RequestError && e.status === 404) {
                this.logger.debug(`Branch: ${branchName} does not exist`);
                return undefined;
            }
            throw e;
        }
    }
    /**
     * Helper to create a new branch from a given SHA.
     */
    async createNewBranch(branchName, branchSha) {
        this.logger.debug(`Creating new branch: ${branchName} at ${branchSha}`);
        const { data: { object: { sha }, }, } = await this.octokit.git.createRef({
            owner: this.repository.owner,
            repo: this.repository.repo,
            ref: `refs/heads/${branchName}`,
            sha: branchSha,
        });
        this.logger.debug(`New branch: ${branchName} at ${sha}`);
        return sha;
    }
    /**
     * Helper to update branch SHA.
     */
    async updateBranchSha(branchName, branchSha) {
        this.logger.debug(`Updating branch ${branchName} to ${branchSha}`);
        const { data: { object: { sha }, }, } = await this.octokit.git.updateRef({
            owner: this.repository.owner,
            repo: this.repository.repo,
            ref: `heads/${branchName}`,
            sha: branchSha,
            force: true,
        });
        this.logger.debug(`Updated branch: ${branchName} to ${sha}`);
        return sha;
    }
}
exports.GitHubApi = GitHubApi;
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
exports.wrapAsync = wrapAsync;
const sleepInMs = (ms) => new Promise(resolve => setTimeout(resolve, ms));
exports.sleepInMs = sleepInMs;
//# sourceMappingURL=github-api.js.map