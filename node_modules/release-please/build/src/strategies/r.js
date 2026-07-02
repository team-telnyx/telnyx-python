"use strict";
// Copyright 2025 Google LLC
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
exports.R = void 0;
const base_1 = require("./base");
const news_1 = require("../updaters/r/news");
const version_1 = require("../version");
const description_1 = require("../updaters/r/description");
const CHANGELOG_SECTIONS = [
    { type: 'feat', section: 'Features' },
    { type: 'fix', section: 'Bug Fixes' },
    { type: 'perf', section: 'Performance Improvements' },
    { type: 'deps', section: 'Dependencies' },
    { type: 'revert', section: 'Reverts' },
    { type: 'docs', section: 'Documentation' },
    { type: 'style', section: 'Styles', hidden: true },
    { type: 'chore', section: 'Miscellaneous Chores', hidden: true },
    { type: 'refactor', section: 'Code Refactoring', hidden: true },
    { type: 'test', section: 'Tests', hidden: true },
    { type: 'build', section: 'Build System', hidden: true },
    { type: 'ci', section: 'Continuous Integration', hidden: true },
];
class R extends base_1.BaseStrategy {
    constructor(options) {
        var _a, _b;
        options.changelogPath = (_a = options.changelogPath) !== null && _a !== void 0 ? _a : 'NEWS.md';
        options.changelogSections = (_b = options.changelogSections) !== null && _b !== void 0 ? _b : CHANGELOG_SECTIONS;
        super(options);
    }
    async buildUpdates(options) {
        const updates = [];
        const version = options.newVersion;
        updates.push({
            path: this.addPath(this.changelogPath),
            createIfMissing: true,
            updater: new news_1.News({
                version,
                changelogEntry: options.changelogEntry,
            }),
        });
        updates.push({
            path: this.addPath('DESCRIPTION'),
            createIfMissing: false,
            updater: new description_1.DescriptionUpdater({
                version,
            }),
        });
        return updates;
    }
    initialReleaseVersion() {
        return version_1.Version.parse('0.1.0');
    }
}
exports.R = R;
//# sourceMappingURL=r.js.map