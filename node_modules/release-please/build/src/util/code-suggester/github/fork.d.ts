import { RepoDomain } from '../types';
import { Octokit } from '@octokit/rest';
/**
 * Fork the GitHub owner's repository.
 * Returns the fork owner and fork repo when the fork creation request to GitHub succeeds.
 * Otherwise throws error.
 *
 * If fork already exists no new fork is created, no error occurs, and the existing Fork data is returned
 * with the `updated_at` + any historical repo changes.
 * @param {Octokit} octokit The authenticated octokit instance
 * @param {RepoDomain} upstream upstream repository information
 * @returns {Promise<RepoDomain>} the forked repository name, as well as the owner of that fork
 */
declare function fork(octokit: Octokit, upstream: RepoDomain): Promise<RepoDomain>;
export { fork };
