import { RepoDomain } from '../types';
import { Octokit } from '@octokit/rest';
/**
 * Create a new branch reference with the ref prefix
 * @param {string} branchName name of the branch
 */
export declare function createRef(branchName: string): string;
/**
 * get branch commit HEAD SHA of a repository
 * Throws an error if the branch cannot be found
 * @param {Octokit} octokit The authenticated octokit instance
 * @param {RepoDomain} origin The domain information of the remote origin repository
 * @param {string} branch the name of the branch
 * @returns {Promise<string>} branch commit HEAD SHA
 */
export declare function getBranchHead(octokit: Octokit, origin: RepoDomain, branch: string): Promise<string>;
/**
 * Determine if there is a branch with the provided name in the remote GitHub repository
 * @param {Octokit} octokit The authenticated octokit instance
 * @param {RepoDomain} remote The domain information of the remote repository
 * @param {string} name The branch name to create on the repository
 * @returns {Promise<boolean>} if there is a branch already existing in the remote GitHub repository
 */
export declare function existsBranchWithName(octokit: Octokit, remote: RepoDomain, name: string): Promise<boolean>;
/**
 * Create a branch on the remote repository if there is not an existing branch
 * @param {Octokit} octokit The authenticated octokit instance
 * @param {RepoDomain} remote The domain information of the remote origin repository
 * @param {string} name The branch name to create on the origin repository
 * @param {string} baseSha the sha that the base of the reference points to
 * @param {boolean} duplicate whether there is an existing branch or not
 * @returns {Promise<void>}
 */
export declare function createBranch(octokit: Octokit, remote: RepoDomain, name: string, baseSha: string, duplicate: boolean): Promise<void>;
/**
 * Create a GitHub branch given a remote origin.
 * Throws an exception if octokit fails, or if the base branch is invalid
 * @param {Octokit} octokit The authenticated octokit instance
 * @param {RepoDomain} origin The domain information of the remote origin repository
 * @param {RepoDomain} upstream The domain information of the remote upstream repository
 * @param {string} name The branch name to create on the origin repository
 * @param {string} baseBranch the name of the branch to base the new branch off of. Default is main
 * @returns {Promise<string>} the base SHA for subsequent commits to be based off for the origin branch
 */
export declare function branch(octokit: Octokit, origin: RepoDomain, upstream: RepoDomain, name: string, baseBranch?: string): Promise<string>;
