"use strict";
// Copyright 2019 Google LLC
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
exports.updateDependencies = exports.NPM_PROTOCOL_REGEXP = exports.newVersionWithRange = exports.PackageJson = void 0;
const json_stringify_1 = require("../../util/json-stringify");
const logger_1 = require("../../util/logger");
const default_1 = require("../default");
/**
 * This updates a Node.js package.json file's main version.
 */
class PackageJson extends default_1.DefaultUpdater {
    constructor(options) {
        super(options);
        this.updatePeerDependencies = false;
        this.updatePeerDependencies = options.updatePeerDependencies || false;
    }
    /**
     * Given initial file contents, return updated contents.
     * @param {string} content The initial content
     * @param logger
     * @returns {string} The updated content
     */
    updateContent(content, logger = logger_1.logger) {
        const parsed = JSON.parse(content);
        logger.info(`updating from ${parsed.version} to ${this.version}`);
        parsed.version = this.version.toString();
        // If additional dependency versions specified, then update dependency versions
        // while preserving any valid version range prefixes.
        if (this.versionsMap) {
            if (parsed.dependencies) {
                updateDependencies(parsed.dependencies, this.versionsMap);
            }
            if (parsed.devDependencies) {
                updateDependencies(parsed.devDependencies, this.versionsMap);
            }
            if (parsed.peerDependencies && this.updatePeerDependencies) {
                updateDependencies(parsed.peerDependencies, this.versionsMap);
            }
            if (parsed.optionalDependencies) {
                updateDependencies(parsed.optionalDependencies, this.versionsMap);
            }
        }
        return (0, json_stringify_1.jsonStringify)(parsed, content);
    }
}
exports.PackageJson = PackageJson;
var SUPPORTED_RANGE_PREFIXES;
(function (SUPPORTED_RANGE_PREFIXES) {
    SUPPORTED_RANGE_PREFIXES["CARET"] = "^";
    SUPPORTED_RANGE_PREFIXES["TILDE"] = "~";
    SUPPORTED_RANGE_PREFIXES["EQUAL_OR_GREATER_THAN"] = ">=";
    SUPPORTED_RANGE_PREFIXES["EQUAL_OR_LESS_THAN"] = "<=";
    SUPPORTED_RANGE_PREFIXES["GREATER_THAN"] = ">";
    SUPPORTED_RANGE_PREFIXES["LESS_THAN"] = "<";
})(SUPPORTED_RANGE_PREFIXES || (SUPPORTED_RANGE_PREFIXES = {}));
function detectRangePrefix(version) {
    return (Object.values(SUPPORTED_RANGE_PREFIXES).find(supportedRangePrefix => version.startsWith(supportedRangePrefix)) || '');
}
/**
 * Helper to coerce a new version value into a version range that preserves the
 * version range prefix of the original version.
 * @param {string} oldVersion Old semver with range
 * @param {Version} newVersion The new version to update with
 */
function newVersionWithRange(oldVersion, newVersion) {
    const prefix = detectRangePrefix(oldVersion);
    if (prefix) {
        return `${prefix}${newVersion}`;
    }
    return newVersion.toString();
}
exports.newVersionWithRange = newVersionWithRange;
exports.NPM_PROTOCOL_REGEXP = /^[a-z]+:/;
/**
 * Helper function to update dependency versions for all new versions specified
 * in the updated versions map. Note that this mutates the existing input.
 * @param {Record<string, string>} dependencies Entries in package.json dependencies
 *   where the key is the dependency name and the value is the dependency range
 * @param {VersionsMap} updatedVersions Map of new versions (without dependency range prefixes)
 */
function updateDependencies(dependencies, updatedVersions) {
    for (const depName of Object.keys(dependencies)) {
        const oldVersion = dependencies[depName];
        if (exports.NPM_PROTOCOL_REGEXP.test(oldVersion)) {
            continue;
        }
        const newVersion = updatedVersions.get(depName);
        if (newVersion) {
            dependencies[depName] = newVersionWithRange(oldVersion, newVersion);
        }
    }
}
exports.updateDependencies = updateDependencies;
//# sourceMappingURL=package-json.js.map