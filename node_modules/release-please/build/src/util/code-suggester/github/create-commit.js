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
exports.createCommit = void 0;
const logger_1 = require("../logger");
const errors_1 = require("../errors");
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
async function createCommit(octokit, origin, refHead, treeSha, message, options = {}) {
    try {
        const signature = options.signer
            ? await options.signer.generateSignature({
                message,
                tree: treeSha,
                parents: [refHead],
                author: options.author,
                committer: options.committer,
            })
            : undefined;
        const { data: { sha, url }, } = await octokit.git.createCommit({
            owner: origin.owner,
            repo: origin.repo,
            message,
            tree: treeSha,
            parents: [refHead],
            signature,
            author: options.author,
            committer: options.committer,
        });
        logger_1.logger.info(`Successfully created commit. See commit at ${url}`);
        return sha;
    }
    catch (e) {
        throw new errors_1.CommitError(`Error creating commit for: ${treeSha}`, e);
    }
}
exports.createCommit = createCommit;
//# sourceMappingURL=create-commit.js.map