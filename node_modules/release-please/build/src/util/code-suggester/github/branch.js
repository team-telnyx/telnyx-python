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
exports.branch = exports.createBranch = exports.existsBranchWithName = exports.getBranchHead = exports.createRef = void 0;
const logger_1 = require("../logger");
const REF_PREFIX = 'refs/heads/';
const DEFAULT_PRIMARY_BRANCH = 'main';
/**
 * Create a new branch reference with the ref prefix
 * @param {string} branchName name of the branch
 */
function createRef(branchName) {
    return REF_PREFIX + branchName;
}
exports.createRef = createRef;
/**
 * get branch commit HEAD SHA of a repository
 * Throws an error if the branch cannot be found
 * @param {Octokit} octokit The authenticated octokit instance
 * @param {RepoDomain} origin The domain information of the remote origin repository
 * @param {string} branch the name of the branch
 * @returns {Promise<string>} branch commit HEAD SHA
 */
async function getBranchHead(octokit, origin, branch) {
    const branchData = (await octokit.repos.getBranch({
        owner: origin.owner,
        repo: origin.repo,
        branch,
    })).data;
    logger_1.logger.info(`Successfully found branch HEAD sha "${branchData.commit.sha}".`);
    return branchData.commit.sha;
}
exports.getBranchHead = getBranchHead;
/**
 * Determine if there is a branch with the provided name in the remote GitHub repository
 * @param {Octokit} octokit The authenticated octokit instance
 * @param {RepoDomain} remote The domain information of the remote repository
 * @param {string} name The branch name to create on the repository
 * @returns {Promise<boolean>} if there is a branch already existing in the remote GitHub repository
 */
async function existsBranchWithName(octokit, remote, name) {
    try {
        const data = (await octokit.git.getRef({
            owner: remote.owner,
            repo: remote.repo,
            ref: `heads/${name}`,
        })).data;
        return data.ref ? true : false;
    }
    catch (err) {
        if (err.status === 404)
            return false;
        else
            throw err;
    }
}
exports.existsBranchWithName = existsBranchWithName;
/**
 * Create a branch on the remote repository if there is not an existing branch
 * @param {Octokit} octokit The authenticated octokit instance
 * @param {RepoDomain} remote The domain information of the remote origin repository
 * @param {string} name The branch name to create on the origin repository
 * @param {string} baseSha the sha that the base of the reference points to
 * @param {boolean} duplicate whether there is an existing branch or not
 * @returns {Promise<void>}
 */
async function createBranch(octokit, remote, name, baseSha, duplicate) {
    if (!duplicate) {
        const refData = (await octokit.git.createRef({
            owner: remote.owner,
            repo: remote.repo,
            ref: createRef(name),
            sha: baseSha,
        })).data;
        logger_1.logger.info(`Successfully created branch at ${refData.url}`);
    }
    else {
        logger_1.logger.info('Skipping branch creation step...');
    }
}
exports.createBranch = createBranch;
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
async function branch(octokit, origin, upstream, name, baseBranch = DEFAULT_PRIMARY_BRANCH) {
    // create branch from primary branch HEAD SHA
    try {
        const baseSha = await getBranchHead(octokit, upstream, baseBranch);
        const duplicate = await existsBranchWithName(octokit, origin, name);
        await createBranch(octokit, origin, name, baseSha, duplicate);
        return baseSha;
    }
    catch (err) {
        logger_1.logger.error('Error when creating branch');
        throw err;
    }
}
exports.branch = branch;
//# sourceMappingURL=branch.js.map