"use strict";
// Copyright 2026 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     https://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
Object.defineProperty(exports, "__esModule", { value: true });
exports.createPullRequest = void 0;
const logger_1 = require("./logger");
const default_options_handler_1 = require("./default-options-handler");
const retry = require("async-retry");
const branch_1 = require("./github/branch");
const fork_1 = require("./github/fork");
const commit_and_push_1 = require("./github/commit-and-push");
const open_pull_request_1 = require("./github/open-pull-request");
const labels_1 = require("./github/labels");
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
async function createPullRequest(octokit, changes, options) {
    (0, logger_1.setupLogger)(options.logger);
    // if null undefined, or the empty map then no changes have been provided.
    // Do not execute GitHub workflow
    if (changes === null || changes === undefined || changes.size === 0) {
        logger_1.logger.info('Empty change set provided. No changes need to be made. Cancelling workflow.');
        return 0;
    }
    const gitHubConfigs = (0, default_options_handler_1.addPullRequestDefaults)(options);
    logger_1.logger.info('Starting GitHub PR workflow...');
    const upstream = {
        owner: gitHubConfigs.upstreamOwner,
        repo: gitHubConfigs.upstreamRepo,
    };
    const origin = options.fork === false ? upstream : await (0, fork_1.fork)(octokit, upstream);
    if (options.fork) {
        // try to sync the fork
        await retry(async () => await octokit.repos.mergeUpstream({
            owner: origin.owner,
            repo: origin.repo,
            branch: gitHubConfigs.primary,
        }), {
            retries: options.retry,
            factor: 2.8411,
            minTimeout: 3000,
            randomize: false,
            onRetry: (e, attempt) => {
                e.message = `Error creating syncing upstream: ${e.message}`;
                logger_1.logger.error(e);
                logger_1.logger.info(`Retry attempt #${attempt}...`);
            },
        });
    }
    const originBranch = {
        ...origin,
        branch: gitHubConfigs.branch,
    };
    // The `retry` flag defaults to `5` to maintain compatibility
    options.retry = options.retry === undefined ? 5 : options.retry;
    const refHeadSha = await retry(async () => await (0, branch_1.branch)(octokit, origin, upstream, originBranch.branch, gitHubConfigs.primary), {
        retries: options.retry,
        factor: 2.8411,
        minTimeout: 3000,
        randomize: false,
        onRetry: (e, attempt) => {
            e.message = `Error creating Pull Request: ${e.message}`;
            logger_1.logger.error(e);
            logger_1.logger.info(`Retry attempt #${attempt}...`);
        },
    });
    await (0, commit_and_push_1.commitAndPush)(octokit, refHeadSha, changes, originBranch, gitHubConfigs.message, gitHubConfigs.force, options);
    const description = {
        body: gitHubConfigs.description,
        title: gitHubConfigs.title,
    };
    const prNumber = await (0, open_pull_request_1.openPullRequest)(octokit, upstream, originBranch, description, gitHubConfigs.maintainersCanModify, gitHubConfigs.primary, options.draft);
    logger_1.logger.info(`Successfully opened pull request: ${prNumber}.`);
    // addLabels will no-op if options.labels is undefined or empty.
    await (0, labels_1.addLabels)(octokit, upstream, originBranch, prNumber, options.labels);
    return prNumber;
}
exports.createPullRequest = createPullRequest;
//# sourceMappingURL=index.js.map