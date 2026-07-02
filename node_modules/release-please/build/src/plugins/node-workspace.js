"use strict";
// Copyright 2021 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
Object.defineProperty(exports, "__esModule", { value: true });
exports.NodeWorkspace = void 0;
const package_lock_json_1 = require("../updaters/node/package-lock-json");
const version_1 = require("../version");
const pull_request_title_1 = require("../util/pull-request-title");
const pull_request_body_1 = require("../util/pull-request-body");
const branch_name_1 = require("../util/branch-name");
const changelog_1 = require("../updaters/changelog");
const workspace_1 = require("./workspace");
const composite_1 = require("../updaters/composite");
const package_json_1 = require("../updaters/node/package-json");
const versioning_strategy_1 = require("../versioning-strategy");
/**
 * The plugin analyzed a cargo workspace and will bump dependencies
 * of managed packages if those dependencies are being updated.
 *
 * If multiple node packages are being updated, it will merge them
 * into a single node package.
 */
class NodeWorkspace extends workspace_1.WorkspacePlugin {
    constructor(github, targetBranch, repositoryConfig, options = {}) {
        super(github, targetBranch, repositoryConfig, options);
        this.strategiesByPath = {};
        this.releasesByPath = {};
        this.alwaysLinkLocal = options.alwaysLinkLocal === false ? false : true;
        this.updatePeerDependencies = options.updatePeerDependencies === true;
    }
    async buildAllPackages(candidates) {
        var _a;
        const candidatesByPath = new Map();
        for (const candidate of candidates) {
            candidatesByPath.set(candidate.path, candidate);
        }
        const candidatesByPackage = {};
        const packagesByPath = new Map();
        for (const path in this.repositoryConfig) {
            const config = this.repositoryConfig[path];
            if (config.releaseType !== 'node') {
                continue;
            }
            const candidate = candidatesByPath.get(path);
            if (candidate) {
                this.logger.debug(`Found candidate pull request for path: ${candidate.path}`);
                const packagePath = (0, workspace_1.addPath)(candidate.path, 'package.json');
                const packageUpdate = candidate.pullRequest.updates.find(update => update.path === packagePath);
                const contents = (_a = packageUpdate === null || packageUpdate === void 0 ? void 0 : packageUpdate.cachedFileContents) !== null && _a !== void 0 ? _a : (await this.github.getFileContentsOnBranch(packagePath, this.targetBranch));
                const packageJson = JSON.parse(contents.parsedContent);
                const pkg = {
                    name: packageJson.name,
                    path,
                    version: packageJson.version,
                    dependencies: packageJson.dependencies || {},
                    devDependencies: packageJson.devDependencies || {},
                    peerDependencies: packageJson.peerDependencies || {},
                    optionalDependencies: packageJson.optionalDependencies || {},
                    jsonContent: contents.parsedContent,
                };
                packagesByPath.set(candidate.path, pkg);
                candidatesByPackage[pkg.name] = candidate;
                // }
            }
            else {
                const packagePath = (0, workspace_1.addPath)(path, 'package.json');
                this.logger.debug(`No candidate pull request for path: ${path} - inspect package from ${packagePath}`);
                const contents = await this.github.getFileContentsOnBranch(packagePath, this.targetBranch);
                const packageJson = JSON.parse(contents.parsedContent);
                const pkg = {
                    name: packageJson.name,
                    path,
                    version: packageJson.version,
                    dependencies: packageJson.dependencies || {},
                    devDependencies: packageJson.devDependencies || {},
                    peerDependencies: packageJson.peerDependencies || {},
                    optionalDependencies: packageJson.optionalDependencies || {},
                    jsonContent: contents.parsedContent,
                };
                packagesByPath.set(path, pkg);
            }
        }
        const allPackages = Array.from(packagesByPath.values());
        return {
            allPackages,
            candidatesByPackage,
        };
    }
    bumpVersion(pkg) {
        const version = version_1.Version.parse(pkg.version);
        const strategy = this.strategiesByPath[pkg.path];
        if (strategy)
            return strategy.versioningStrategy.bump(version, []);
        return new versioning_strategy_1.PatchVersionUpdate().bump(version);
    }
    updateCandidate(existingCandidate, pkg, updatedVersions) {
        // Update version of the package
        const newVersion = updatedVersions.get(pkg.name);
        if (!newVersion) {
            throw new Error(`Didn't find updated version for ${pkg.name}`);
        }
        const updatedPackage = {
            ...pkg,
            version: newVersion.toString(),
        };
        const updater = new package_json_1.PackageJson({
            version: newVersion,
            versionsMap: updatedVersions,
            updatePeerDependencies: this.updatePeerDependencies,
        });
        const dependencyNotes = getChangelogDepsNotes(pkg, updatedPackage, updatedVersions, this.logger);
        existingCandidate.pullRequest.updates =
            existingCandidate.pullRequest.updates.map(update => {
                if (update.path === (0, workspace_1.addPath)(existingCandidate.path, 'package.json')) {
                    update.updater = new composite_1.CompositeUpdater(update.updater, updater);
                }
                else if (update.path === (0, workspace_1.addPath)(existingCandidate.path, 'package-lock.json')) {
                    update.updater = new package_lock_json_1.PackageLockJson({
                        version: newVersion,
                        versionsMap: updatedVersions,
                    });
                }
                else if (update.updater instanceof changelog_1.Changelog) {
                    if (dependencyNotes) {
                        update.updater.changelogEntry =
                            (0, workspace_1.appendDependenciesSectionToChangelog)(update.updater.changelogEntry, dependencyNotes, this.logger);
                    }
                }
                return update;
            });
        // append dependency notes
        if (dependencyNotes) {
            if (existingCandidate.pullRequest.body.releaseData.length > 0) {
                existingCandidate.pullRequest.body.releaseData[0].notes =
                    (0, workspace_1.appendDependenciesSectionToChangelog)(existingCandidate.pullRequest.body.releaseData[0].notes, dependencyNotes, this.logger);
            }
            else {
                existingCandidate.pullRequest.body.releaseData.push({
                    component: updatedPackage.name,
                    version: existingCandidate.pullRequest.version,
                    notes: (0, workspace_1.appendDependenciesSectionToChangelog)('', dependencyNotes, this.logger),
                });
            }
        }
        return existingCandidate;
    }
    async newCandidate(pkg, updatedVersions) {
        // Update version of the package
        const newVersion = updatedVersions.get(pkg.name);
        if (!newVersion) {
            throw new Error(`Didn't find updated version for ${pkg.name}`);
        }
        const updatedPackage = {
            ...pkg,
            version: newVersion.toString(),
        };
        const dependencyNotes = getChangelogDepsNotes(pkg, updatedPackage, updatedVersions, this.logger);
        const strategy = this.strategiesByPath[updatedPackage.path];
        const latestRelease = this.releasesByPath[updatedPackage.path];
        const basePullRequest = strategy
            ? await strategy.buildReleasePullRequest([], latestRelease, false, [], {
                newVersion,
            })
            : undefined;
        if (basePullRequest) {
            return this.updateCandidate({
                path: pkg.path,
                pullRequest: basePullRequest,
                config: {
                    releaseType: 'node',
                },
            }, pkg, updatedVersions);
        }
        const pullRequest = {
            title: pull_request_title_1.PullRequestTitle.ofTargetBranch(this.targetBranch),
            body: new pull_request_body_1.PullRequestBody([
                {
                    component: updatedPackage.name,
                    version: newVersion,
                    notes: (0, workspace_1.appendDependenciesSectionToChangelog)('', dependencyNotes, this.logger),
                },
            ]),
            updates: [
                {
                    path: (0, workspace_1.addPath)(updatedPackage.path, 'package.json'),
                    createIfMissing: false,
                    updater: new package_json_1.PackageJson({
                        version: newVersion,
                        versionsMap: updatedVersions,
                        updatePeerDependencies: this.updatePeerDependencies,
                    }),
                },
                {
                    path: (0, workspace_1.addPath)(updatedPackage.path, 'package-lock.json'),
                    createIfMissing: false,
                    updater: new package_json_1.PackageJson({
                        version: newVersion,
                        versionsMap: updatedVersions,
                        updatePeerDependencies: this.updatePeerDependencies,
                    }),
                },
                {
                    path: (0, workspace_1.addPath)(updatedPackage.path, 'CHANGELOG.md'),
                    createIfMissing: false,
                    updater: new changelog_1.Changelog({
                        version: newVersion,
                        changelogEntry: (0, workspace_1.appendDependenciesSectionToChangelog)('', dependencyNotes, this.logger),
                    }),
                },
            ],
            labels: [],
            headRefName: branch_name_1.BranchName.ofTargetBranch(this.targetBranch).toString(),
            version: newVersion,
            draft: false,
        };
        return {
            path: updatedPackage.path,
            pullRequest,
            config: {
                releaseType: 'node',
            },
        };
    }
    postProcessCandidates(candidates, _updatedVersions) {
        if (candidates.length === 0) {
            return candidates;
        }
        const [candidate] = candidates;
        // check for root lock file in pull request
        let hasRootLockFile;
        for (let i = 0; i < candidate.pullRequest.updates.length; i++) {
            if (candidate.pullRequest.updates[i].path === '.package-lock.json' ||
                candidate.pullRequest.updates[i].path === './package-lock.json' ||
                candidate.pullRequest.updates[i].path === 'package-lock.json' ||
                candidate.pullRequest.updates[i].path === '/package-lock.json') {
                hasRootLockFile = true;
                break;
            }
        }
        // if there is a root lock file, then there is no additional pull request update necessary.
        if (hasRootLockFile) {
            return candidates;
        }
        candidate.pullRequest.updates.push({
            path: 'package-lock.json',
            createIfMissing: false,
            updater: new package_lock_json_1.PackageLockJson({
                versionsMap: _updatedVersions,
            }),
        });
        return candidates;
    }
    async buildGraph(allPackages) {
        const graph = new Map();
        const workspacePackageNames = new Set(allPackages.map(packageJson => packageJson.name));
        for (const packageJson of allPackages) {
            const allDeps = Object.keys(this.combineDeps(packageJson));
            const workspaceDeps = allDeps.filter(dep => workspacePackageNames.has(dep));
            graph.set(packageJson.name, {
                deps: workspaceDeps,
                value: packageJson,
            });
        }
        return graph;
    }
    inScope(candidate) {
        return candidate.config.releaseType === 'node';
    }
    packageNameFromPackage(pkg) {
        return pkg.name;
    }
    pathFromPackage(pkg) {
        return pkg.path;
    }
    combineDeps(packageJson) {
        var _a, _b, _c, _d;
        return {
            ...((_a = packageJson.dependencies) !== null && _a !== void 0 ? _a : {}),
            ...((_b = packageJson.devDependencies) !== null && _b !== void 0 ? _b : {}),
            ...((_c = packageJson.optionalDependencies) !== null && _c !== void 0 ? _c : {}),
            ...(this.updatePeerDependencies
                ? (_d = packageJson.peerDependencies) !== null && _d !== void 0 ? _d : {}
                : {}),
        };
    }
    async preconfigure(strategiesByPath, _commitsByPath, _releasesByPath) {
        // Using preconfigure to siphon releases and strategies.
        this.strategiesByPath = strategiesByPath;
        this.releasesByPath = _releasesByPath;
        return strategiesByPath;
    }
}
exports.NodeWorkspace = NodeWorkspace;
function getChangelogDepsNotes(original, updated, updateVersions, logger) {
    var _a;
    let depUpdateNotes = '';
    const depTypes = [
        'dependencies',
        'devDependencies',
        'peerDependencies',
        'optionalDependencies',
    ];
    const updates = new Map();
    for (const depType of depTypes) {
        const depUpdates = [];
        const pkgDepTypes = updated[depType];
        if (pkgDepTypes === undefined) {
            continue;
        }
        for (const [depName, currentDepVer] of Object.entries(pkgDepTypes)) {
            const newVersion = updateVersions.get(depName);
            if (!newVersion) {
                logger.debug(`${depName} was not bumped, ignoring`);
                continue;
            }
            const origDepVer = (_a = original[depType]) === null || _a === void 0 ? void 0 : _a[depName];
            const newVersionString = (0, package_json_1.newVersionWithRange)(origDepVer, newVersion);
            if (currentDepVer.startsWith('workspace:')) {
                depUpdates.push(`\n    * ${depName} bumped to ${newVersionString}`);
            }
            else if (newVersionString !== origDepVer) {
                depUpdates.push(`\n    * ${depName} bumped from ${origDepVer} to ${newVersionString}`);
                //handle case when "workspace:" version is used
            }
        }
        if (depUpdates.length > 0) {
            updates.set(depType, depUpdates);
        }
    }
    for (const [dt, notes] of updates) {
        depUpdateNotes += `\n  * ${dt}`;
        for (const note of notes) {
            depUpdateNotes += note;
        }
    }
    if (depUpdateNotes) {
        return `* The following workspace dependencies were updated${depUpdateNotes}`;
    }
    return '';
}
//# sourceMappingURL=node-workspace.js.map