import { BranchDomain, Description, RepoDomain } from '../types';
import { Octokit } from '@octokit/rest';
/**
 * Create a GitHub PR on the upstream organization's repo
 * Throws an error if the GitHub API fails
 * @param {Octokit} octokit The authenticated octokit instance
 * @param {RepoDomain} upstream The upstream repository
 * @param {BranchDomain} origin The remote origin information that contains the origin branch
 * @param {Description} description The pull request title and detailed description
 * @param {boolean} maintainersCanModify Whether or not maintainers can modify the pull request. Default is true
 * @param {string} upstreamPrimary The upstream repository's primary branch. Default is main.
 * @param draft Open a DRAFT pull request.  Defaults to false.
 * @returns {Promise<void>}
 */
declare function openPullRequest(octokit: Octokit, upstream: RepoDomain, origin: BranchDomain, description: Description, maintainersCanModify?: boolean, upstreamPrimary?: string, draft?: boolean): Promise<number>;
export { openPullRequest };
