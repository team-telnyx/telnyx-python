import { CreatePullRequest, CreatePullRequestUserOptions } from './types';
/**
 * Add defaults to GitHub Pull Request options.
 * Preserves the empty string.
 * For ESCMAScript, null/undefined values are preserved for required fields.
 * Recommended with an object validation function to check empty strings and incorrect types.
 * @param {PullRequestUserOptions} options the user-provided github pull request options
 * @returns {CreatePullRequest} git hub context with defaults applied
 */
export declare function addPullRequestDefaults(options: CreatePullRequestUserOptions): CreatePullRequest;
