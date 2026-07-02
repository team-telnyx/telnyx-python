import { Scm, ScmRelease, ScmTag, ScmCommitIteratorOptions, ScmReleaseIteratorOptions, ScmTagIteratorOptions, ScmCreatePullRequestOptions, ScmUpdatePullRequestOptions, ScmReleaseOptions, ScmChangeSet } from './scm';
import { Repository } from './repository';
import { Commit } from './commit';
import { PullRequest } from './pull-request';
import { ReleasePullRequest } from './release-pull-request';
import { Update } from './update';
import { Release } from './release';
import { GitHubFileContents } from '@google-automations/git-file-utils';
import { GitHubApi, GitHubCreateOptions } from './github-api';
import { Logger } from './util/code-suggester/types';
export interface LocalGitHubCreateOptions extends GitHubCreateOptions {
    cloneDepth?: number;
    localRepoPath?: string;
}
/**
 * LocalGitHub implements the Scm interface using a local git clone
 * where possible, and falling back to the GitHub API for other operations.
 */
export declare class LocalGitHub implements Scm {
    readonly repository: Repository;
    private cloneDir;
    private gitHubApi;
    private logger;
    constructor(repository: Repository, gitHubApi: GitHubApi, cloneDir: string, options?: {
        logger?: Logger;
    });
    static create(options: LocalGitHubCreateOptions): Promise<LocalGitHub>;
    /**
     * Fetch the contents of a file from the configured branch
     *
     * @param {string} path The path to the file in the repository
     * @returns {GitHubFileContents}
     * @throws {GitHubAPIError} on other API errors
     */
    getFileContents(path: string): Promise<GitHubFileContents>;
    private execGitStream;
    private ensureRef;
    /**
     * Fetch the contents of a file
     *
     * @param {string} path The path to the file in the repository
     * @param {string} branch The branch to fetch from
     * @returns {GitHubFileContents}
     * @throws {FileNotFoundError} if the file cannot be found
     * @throws {GitHubAPIError} on other API errors
     */
    getFileContentsOnBranch(path: string, branch: string): Promise<GitHubFileContents>;
    getFileJson<T>(path: string, branch: string): Promise<T>;
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
    findFilesByFilename(filename: string, prefix?: string): Promise<string[]>;
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
    findFilesByFilenameAndRef(filename: string, ref: string, prefix?: string): Promise<string[]>;
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
    findFilesByGlob(glob: string, prefix?: string): Promise<string[]>;
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
    findFilesByGlobAndRef(glob: string, ref: string, prefix?: string): Promise<string[]>;
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
    findFilesByExtension(extension: string, prefix?: string): Promise<string[]>;
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
    findFilesByExtensionAndRef(extension: string, ref: string, prefix?: string): Promise<string[]>;
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
    commitsSince(targetBranch: string, filter: (commit: Commit) => boolean, options?: ScmCommitIteratorOptions): Promise<Commit[]>;
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
    mergeCommitIterator(targetBranch: string, options?: ScmCommitIteratorOptions): AsyncGenerator<Commit, void, void>;
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
    pullRequestIterator(targetBranch: string, status?: 'OPEN' | 'CLOSED' | 'MERGED', maxResults?: number, includeFiles?: boolean): AsyncGenerator<PullRequest, void, void>;
    /**
     * Iterate through releases with a max number of results scanned.
     *
     * @param {ReleaseIteratorOptions} options Query options
     * @param {number} options.maxResults Limit the number of results searched.
     *   Defaults to unlimited.
     * @yields {GitHubRelease}
     * @throws {GitHubAPIError} on an API error
     */
    releaseIterator(options?: ScmReleaseIteratorOptions): AsyncGenerator<ScmRelease, void, void>;
    /**
     * Iterate through tags with a max number of results scanned.
     *
     * @param {TagIteratorOptions} options Query options
     * @param {number} options.maxResults Limit the number of results searched.
     *   Defaults to unlimited.
     * @yields {GitHubTag}
     * @throws {GitHubAPIError} on an API error
     */
    tagIterator(options?: ScmTagIteratorOptions): AsyncGenerator<ScmTag, void, void>;
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
    createPullRequest(pullRequest: PullRequest, targetBranch: string, message: string, updates: Update[], options?: ScmCreatePullRequestOptions): Promise<PullRequest>;
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
    updatePullRequest(number: number, pullRequest: ReleasePullRequest, targetBranch: string, options?: ScmUpdatePullRequestOptions): Promise<PullRequest>;
    getPullRequest(number: number): Promise<PullRequest>;
    /**
     * Create a GitHub release
     *
     * @param {Release} release Release parameters
     * @param {ReleaseOptions} options Release option parameters
     * @throws {DuplicateReleaseError} if the release tag already exists
     * @throws {GitHubAPIError} on other API errors
     */
    createRelease(release: Release, options?: ScmReleaseOptions): Promise<ScmRelease>;
    /**
     * Makes a comment on a issue/pull request.
     *
     * @param {string} comment - The body of the comment to post.
     * @param {number} number - The issue or pull request number.
     * @throws {GitHubAPIError} on an API error
     */
    commentOnIssue(comment: string, number: number): Promise<string>;
    /**
     * Removes labels from an issue/pull request.
     *
     * @param {string[]} labels The labels to remove.
     * @param {number} number The issue/pull request number.
     */
    removeIssueLabels(labels: string[], number: number): Promise<void>;
    /**
     * Adds label to an issue/pull request.
     *
     * @param {string[]} labels The labels to add.
     * @param {number} number The issue/pull request number.
     */
    addIssueLabels(labels: string[], number: number): Promise<void>;
    /**
     * Generate release notes from GitHub at tag
     * @param {string} tagName Name of new release tag
     * @param {string} targetCommitish Target commitish for new tag
     * @param {string} previousTag Optional. Name of previous tag to analyze commits since
     */
    generateReleaseNotes(tagName: string, targetCommitish: string, previousTag?: string): Promise<string>;
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
    createFileOnNewBranch(filename: string, contents: string, newBranchName: string, baseBranchName: string): Promise<string>;
    /**
     * Given a set of proposed updates, build a changeset to suggest.
     *
     * @param {Update[]} updates The proposed updates
     * @param {string} defaultBranch The target branch
     * @return {Changes} The changeset to suggest.
     * @throws {GitHubAPIError} on an API error
     */
    buildChangeSet(updates: Update[], defaultBranch: string): Promise<ScmChangeSet>;
}
