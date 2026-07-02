import { BranchDomain, RepoDomain } from '../types';
import { Octokit } from '@octokit/rest';
/**
 * Create a GitHub PR on the upstream organization's repo
 * Throws an error if the GitHub API fails
 * @param {Octokit} octokit The authenticated octokit instance
 * @param {RepoDomain} upstream The upstream repository
 * @param {BranchDomain} origin The remote origin information that contains the origin branch
 * @param {number} issue_number The issue number to add labels to. Can also be a PR number
 * @param {string[]} labels The list of labels to apply to the newly created PR. Default is []. the funciton will no-op.
 * @returns {Promise<string[]>} The list of resulting labels after the addition of the given labels
 */
declare function addLabels(octokit: Octokit, upstream: RepoDomain, origin: BranchDomain, issue_number: number, labels?: string[]): Promise<string[]>;
export { addLabels };
