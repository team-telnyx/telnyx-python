import { Changes, TreeObject, RepoDomain, BranchDomain } from '../types';
import { Octokit } from '@octokit/rest';
import { CreateCommitOptions } from './create-commit';
/**
 * Generate and return a GitHub tree object structure
 * containing the target change data
 * See https://developer.github.com/v3/git/trees/#tree-object
 * @param {Changes} changes the set of repository changes
 * @returns {TreeObject[]} The new GitHub changes
 */
export declare function generateTreeObjects(changes: Changes): TreeObject[];
/**
 * Upload and create a remote GitHub tree
 * and resolves with the new tree SHA.
 * Rejects if GitHub V3 API fails with the GitHub error response
 * @param {Octokit} octokit The authenticated octokit instance
 * @param {RepoDomain} origin the the remote repository to push changes to
 * @param {string} refHead the base of the new commit(s)
 * @param {TreeObject[]} tree the set of GitHub changes to upload
 * @returns {Promise<string>} the GitHub tree SHA
 * @throws {CommitError}
 */
export declare function createTree(octokit: Octokit, origin: RepoDomain, refHead: string, tree: TreeObject[]): Promise<string>;
/**
 * Update a reference to a SHA
 * Rejects if GitHub V3 API fails with the GitHub error response
 * @param {Octokit} octokit The authenticated octokit instance
 * @param {BranchDomain} origin the the remote branch to push changes to
 * @param {string} newSha the ref to update the commit HEAD to
 * @param {boolean} force to force the commit changes given refHead
 * @returns {Promise<void>}
 */
export declare function updateRef(octokit: Octokit, origin: BranchDomain, newSha: string, force: boolean): Promise<void>;
interface CommitAndPushOptions extends CreateCommitOptions {
    filesPerCommit?: number;
}
/**
 * Given a set of changes, apply the commit(s) on top of the given branch's head and upload it to GitHub
 * Rejects if GitHub V3 API fails with the GitHub error response
 * @param {Octokit} octokit The authenticated octokit instance
 * @param {string} refHead the base of the new commit(s)
 * @param {Changes} changes the set of repository changes
 * @param {RepoDomain} origin the the remote repository to push changes to
 * @param {string} originBranchName the remote branch that will contain the new changes
 * @param {string} commitMessage the message of the new commit
 * @param {boolean} force to force the commit changes given refHead
 * @returns {Promise<void>}
 * @throws {CommitError}
 */
export declare function commitAndPush(octokit: Octokit, refHead: string, changes: Changes, originBranch: BranchDomain, commitMessage: string, force: boolean, options?: CommitAndPushOptions): Promise<void>;
export {};
