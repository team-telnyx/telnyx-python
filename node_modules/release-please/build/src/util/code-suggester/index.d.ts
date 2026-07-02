import { Changes, CreatePullRequestUserOptions } from './types';
import { Octokit } from '@octokit/rest';
/**
 * Make a new GitHub Pull Request with a set of changes applied on top of primary branch HEAD.
 * The changes are committed into a new branch based on the upstream repository options using the authenticated Octokit account.
 * Then a Pull Request is made from that branch.
 *
 * Also throws error if git data from the fork is not ready in 5 minutes.
 *
 * From the docs
 * https://developer.github.com/v3/repos/forks/#create-a-fork
 * """
 * Forking a Repository happens asynchronously.
 * You may have to wait a short period of time before you can access the git objects.
 * If this takes longer than 5 minutes, be sure to contact GitHub Support or GitHub Premium Support.
 * """
 *
 * If changes are empty then the workflow will not run.
 * Rethrows an HttpError if Octokit GitHub API returns an error. HttpError Octokit access_token and client_secret headers redact all sensitive information.
 * @param {Octokit} octokit The authenticated octokit instance, instantiated with an access token having permissiong to create a fork on the target repository
 * @param {Changes | null | undefined} changes A set of changes. The changes may be empty
 * @param {CreatePullRequestUserOptions} options The configuration for interacting with GitHub provided by the user.
 * @returns {Promise<number>} the pull request number. Returns 0 if unsuccessful.
 * @throws {CommitError} on failure during commit process
 */
declare function createPullRequest(octokit: Octokit, changes: Changes | null | undefined, options: CreatePullRequestUserOptions): Promise<number>;
export { Changes, CommitData, CommitSigner } from './types';
export { createPullRequest };
