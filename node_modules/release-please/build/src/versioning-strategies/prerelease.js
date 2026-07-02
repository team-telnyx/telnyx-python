"use strict";
// Copyright 2023 Google LLC
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
exports.PrereleaseVersioningStrategy = void 0;
const default_1 = require("./default");
const version_1 = require("../version");
const versioning_strategy_1 = require("../versioning-strategy");
/**
 * Regex to match the last set of numbers in a string
 * Example: 1.2.3-beta01-01 -> 01
 */
const PRERELEASE_NUMBER = /(?<number>\d+)(?=\D*$)/;
class AbstractPrereleaseVersionUpdate {
    constructor(prereleaseType) {
        this.prereleaseType = prereleaseType;
    }
    /**
     * Returns the new bumped prerelease version
     *
     * That is, if the current version is 1.2.3-beta01, the next prerelease version
     * will be 1.2.3-beta02. If no number is found, the prerelease version will be
     * 1.2.3-beta. If multiple numbers are found, the last set of numbers will be
     * incremented, e.g. 1.2.3-beta01-01 -> 1.2.3-beta01-02.
     *
     * @param {prerelease} string The current version
     * @returns {Version} The bumped version
     */
    bumpPrerelease(prerelease) {
        const match = prerelease.match(PRERELEASE_NUMBER);
        let nextPrerelease = `${prerelease}.1`;
        if (match === null || match === void 0 ? void 0 : match.groups) {
            const numberLength = match.groups.number.length;
            const nextPrereleaseNumber = Number(match.groups.number) + 1;
            const paddedNextPrereleaseNumber = `${nextPrereleaseNumber}`.padStart(numberLength, '0');
            nextPrerelease = prerelease.replace(PRERELEASE_NUMBER, paddedNextPrereleaseNumber);
        }
        return nextPrerelease;
    }
}
class PrereleasePatchVersionUpdate extends AbstractPrereleaseVersionUpdate {
    /**
     * Returns the new bumped version
     *
     * @param {Version} version The current version
     * @returns {Version} The bumped version
     */
    bump(version) {
        if (version.preRelease) {
            const nextPrerelease = this.bumpPrerelease(version.preRelease);
            return new version_1.Version(version.major, version.minor, version.patch, nextPrerelease, version.build);
        }
        return new version_1.Version(version.major, version.minor, version.patch + 1, this.prereleaseType, version.build);
    }
}
class PrereleaseMinorVersionUpdate extends AbstractPrereleaseVersionUpdate {
    /**
     * Returns the new bumped version
     *
     * @param {Version} version The current version
     * @returns {Version} The bumped version
     */
    bump(version) {
        if (version.preRelease) {
            if (version.patch === 0) {
                const nextPrerelease = this.bumpPrerelease(version.preRelease);
                return new version_1.Version(version.major, version.minor, version.patch, nextPrerelease, version.build);
            }
            return new versioning_strategy_1.MinorVersionUpdate().bump(version);
        }
        return new version_1.Version(version.major, version.minor + 1, 0, this.prereleaseType, version.build);
    }
}
class PrereleaseMajorVersionUpdate extends AbstractPrereleaseVersionUpdate {
    /**
     * Returns the new bumped version
     *
     * @param {Version} version The current version
     * @returns {Version} The bumped version
     */
    bump(version) {
        if (version.preRelease) {
            if (version.patch === 0 && version.minor === 0) {
                const nextPrerelease = this.bumpPrerelease(version.preRelease);
                return new version_1.Version(version.major, version.minor, version.patch, nextPrerelease, version.build);
            }
            return new versioning_strategy_1.MajorVersionUpdate().bump(version);
        }
        return new version_1.Version(version.major + 1, 0, 0, this.prereleaseType, version.build);
    }
}
/**
 * This versioning strategy will increment the pre-release number for patch
 * bumps if there is a pre-release number (preserving any leading 0s).
 * Example: 1.2.3-beta01 -> 1.2.3-beta02.
 */
class PrereleaseVersioningStrategy extends default_1.DefaultVersioningStrategy {
    constructor(options = {}) {
        super(options);
        this.prereleaseType = options.prereleaseType;
        this.prerelease = options.prerelease === true;
    }
    determineReleaseType(version, commits) {
        // iterate through list of commits and find biggest commit type
        let breaking = 0;
        let features = 0;
        for (const commit of commits) {
            const releaseAs = commit.notes.find(note => note.title === 'RELEASE AS');
            if (releaseAs) {
                // commits are handled newest to oldest, so take the first one (newest) found
                this.logger.debug(`found Release-As: ${releaseAs.text}, forcing version`);
                return new versioning_strategy_1.CustomVersionUpdate(version_1.Version.parse(releaseAs.text).toString());
            }
            if (commit.breaking) {
                breaking++;
            }
            else if (commit.type === 'feat' || commit.type === 'feature') {
                features++;
            }
        }
        let bumpedVersionUpdater;
        if (breaking > 0) {
            if (version.isPreMajor && this.bumpMinorPreMajor) {
                bumpedVersionUpdater = new PrereleaseMinorVersionUpdate(this.prereleaseType);
            }
            else {
                bumpedVersionUpdater = new PrereleaseMajorVersionUpdate(this.prereleaseType);
            }
        }
        else if (features > 0) {
            if (version.isPreMajor && this.bumpPatchForMinorPreMajor) {
                bumpedVersionUpdater = new PrereleasePatchVersionUpdate(this.prereleaseType);
            }
            else {
                bumpedVersionUpdater = new PrereleaseMinorVersionUpdate(this.prereleaseType);
            }
        }
        else {
            bumpedVersionUpdater = new PrereleasePatchVersionUpdate(this.prereleaseType);
        }
        if (!this.prerelease) {
            const bumpedVersion = bumpedVersionUpdater.bump(version);
            return new versioning_strategy_1.CustomVersionUpdate(version_1.Version.parse(`${bumpedVersion.major}.${bumpedVersion.minor}.${bumpedVersion.patch}`).toString());
        }
        return bumpedVersionUpdater;
    }
}
exports.PrereleaseVersioningStrategy = PrereleaseVersioningStrategy;
//# sourceMappingURL=prerelease.js.map