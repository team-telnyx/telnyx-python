import { Octokit } from '@octokit/rest';
import { request } from '@octokit/request';
import { Logger } from './util/code-suggester/types';
import { PullRequest } from './pull-request';
import { Repository } from './repository';
import { Release } from './release';
import { ScmRelease, ScmReleaseIteratorOptions, ScmReleaseOptions, ScmCommitIteratorOptions } from './scm';
import { HttpsProxyAgent } from 'https-proxy-agent';
import { HttpProxyAgent } from 'http-proxy-agent';
export declare const GH_API_URL = "https://api.github.com";
export declare const GH_GRAPHQL_URL = "https://api.github.com";
export type OctokitType = InstanceType<typeof Octokit>;
type RequestBuilderType = typeof request;
type DefaultFunctionType = RequestBuilderType['defaults'];
type RequestFunctionType = ReturnType<DefaultFunctionType>;
export interface OctokitAPIs {
    graphql: Function;
    request: RequestFunctionType;
    octokit: OctokitType;
}
export interface ProxyOption {
    host: string;
    port: number;
}
export interface GitHubCreateOptions {
    owner: string;
    repo: string;
    defaultBranch?: string;
    apiUrl?: string;
    graphqlUrl?: string;
    octokitAPIs?: OctokitAPIs;
    token?: string;
    logger?: Logger;
    proxy?: ProxyOption;
    fetch?: any;
}
export interface GitHubApiOptions {
    repository: Repository;
    octokitAPIs: OctokitAPIs;
    logger?: Logger;
}
export interface GraphQLCommit {
    sha: string;
    message: string;
    associatedPullRequests: {
        nodes: GraphQLPullRequest[];
    };
}
export interface GraphQLPullRequest {
    number: number;
    title: string;
    body: string;
    baseRefName: string;
    headRefName: string;
    labels: {
        nodes: {
            name: string;
        }[];
    };
    mergeCommit?: {
        oid: string;
    };
    files: {
        nodes: {
            path: string;
        }[];
        pageInfo: {
            hasNextPage: boolean;
        };
    };
}
export interface PullRequestHistory {
    pageInfo: {
        hasNextPage: boolean;
        endCursor: string | undefined;
    };
    data: PullRequest[];
}
export interface CommitHistory {
    pageInfo: {
        hasNextPage: boolean;
        endCursor: string | undefined;
    };
    data: ScmRelease[];
}
export type CommitIteratorOptions = ScmCommitIteratorOptions;
export interface GraphQLRelease {
    name: string;
    tag: {
        name: string;
    };
    tagCommit: {
        oid: string;
    };
    url: string;
    description: string;
    isDraft: boolean;
}
export interface ReleaseHistory {
    pageInfo: {
        hasNextPage: boolean;
        endCursor: string | undefined;
    };
    data: ScmRelease[];
}
export type ReleaseIteratorOptions = ScmReleaseIteratorOptions;
export declare const MAX_SLEEP_SECONDS = 20;
export declare const MAX_ISSUE_BODY_SIZE = 65536;
export declare class GitHubApi {
    readonly repository: Repository;
    readonly octokitAPIs: OctokitAPIs;
    octokit: OctokitType;
    private graphql;
    private logger;
    constructor(options: GitHubApiOptions);
    static createDefaultAgent(baseUrl: string, defaultProxy?: ProxyOption): HttpProxyAgent<`http://${string}:${number}`> | HttpsProxyAgent<`https://${string}:${number}`> | undefined;
    static create(options: GitHubCreateOptions): Promise<GitHubApi>;
    static defaultBranch(owner: string, repo: string, octokit: OctokitType): Promise<string>;
    private graphqlRequest;
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
    pullRequestIterator(targetBranch: string, status?: 'OPEN' | 'CLOSED' | 'MERGED', maxResults?: number, includeFiles?: boolean): AsyncGenerator<PullRequest, void, void>;
    /**
     * Helper implementation of pullRequestIterator that includes files via
     * the graphQL API.
     *
     * @param {string} targetBranch The base branch of the pull request
     * @param {string} status The status of the pull request
     * @param {number} maxResults Limit the number of results searched
     */
    private pullRequestIteratorWithFiles;
    /**
     * Helper implementation of pullRequestIterator that excludes files
     * via the REST API.
     *
     * @param {string} targetBranch The base branch of the pull request
     * @param {string} status The status of the pull request
     * @param {number} maxResults Limit the number of results searched
     */
    private pullRequestIteratorWithoutFiles;
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
    private pullRequestsGraphQL;
    /**
     * Iterate through releases with a max number of results scanned.
     *
     * @param {ReleaseIteratorOptions} options Query options
     * @param {number} options.maxResults Limit the number of results scanned.
     *   Defaults to unlimited.
     * @yields {ScmRelease}
     * @throws {GitHubAPIError} on an API error
     */
    releaseIterator(options?: ReleaseIteratorOptions): AsyncGenerator<ScmRelease, void, unknown>;
    private releaseGraphQL;
    createPullRequest: (pullRequest: PullRequest, targetBranch: string, options?: {
        draft?: boolean | undefined;
    } | undefined) => Promise<PullRequest>;
    /**
     * Fetch a pull request given the pull number
     * @param {number} number The pull request number
     * @returns {PullRequest}
     */
    getPullRequest: (number: number) => Promise<PullRequest>;
    updatePullRequest: (number: number, title: string, body: string) => Promise<{
        headBranchName: string;
        baseBranchName: string;
        number: number;
        title: string;
        body: string;
        files: never[];
        labels: string[];
    }>;
    /**
     * Create a GitHub release
     *
     * @param {Release} release Release parameters
     * @param {ScmReleaseOptions} options Release option parameters
     * @throws {DuplicateReleaseError} if the release tag already exists
     * @throws {GitHubAPIError} on other API errors
     */
    createRelease: (release: Release, options?: ScmReleaseOptions | undefined) => Promise<ScmRelease>;
    /**
     * Makes a comment on a issue/pull request.
     *
     * @param {string} comment - The body of the comment to post.
     * @param {number} number - The issue or pull request number.
     * @throws {GitHubAPIError} on an API error
     */
    commentOnIssue: (comment: string, number: number) => Promise<string>;
    /**
     * Removes labels from an issue/pull request.
     *
     * @param {string[]} labels The labels to remove.
     * @param {number} number The issue/pull request number.
     */
    removeIssueLabels: (labels: string[], number: number) => Promise<void>;
    /**
     * Adds label to an issue/pull request.
     *
     * @param {string[]} labels The labels to add.
     * @param {number} number The issue/pull request number.
     */
    addIssueLabels: (labels: string[], number: number) => Promise<void>;
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
     * Fork a branch from a base branch.
     */
    private forkBranch;
    /**
     * Helper to fetch the SHA of a branch
     */
    private getBranchSha;
    /**
     * Helper to create a new branch from a given SHA.
     */
    private createNewBranch;
    /**
     * Helper to update branch SHA.
     */
    private updateBranchSha;
}
export declare const wrapAsync: <T extends any[], V>(fn: (...args: T) => Promise<V>, errorHandler?: ((e: Error) => void) | undefined) => (...args: T) => Promise<V>;
export declare const sleepInMs: (ms: number) => Promise<unknown>;
export {};
