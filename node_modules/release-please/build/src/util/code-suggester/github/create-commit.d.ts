import { Octokit } from '@octokit/rest';
import { RepoDomain, CommitSigner, UserData } from '../types';
export interface CreateCommitOptions {
    signer?: CommitSigner;
    author?: UserData;
    committer?: UserData;
}
/**
 * Create a commit with a repo snapshot SHA on top of the reference HEAD
 * and resolves with the SHA of the commit.
 * Rejects if GitHub V3 API fails with the GitHub error response
 * @param {Octokit} octokit The authenticated octokit instance
 * @param {RepoDomain} origin the the remote repository to push changes to
 * @param {string} refHead the base of the new commit(s)
 * @param {string} treeSha the tree SHA that this commit will point to
 * @param {string} message the message of the new commit
 * @returns {Promise<string>} the new commit SHA
 * @see https://docs.github.com/en/rest/git/commits?apiVersion=2022-11-28#create-a-commit
 */
export declare function createCommit(octokit: Octokit, origin: RepoDomain, refHead: string, treeSha: string, message: string, options?: CreateCommitOptions): Promise<string>;
