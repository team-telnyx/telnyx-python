"use strict";
// Copyright 2024 Google LLC
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
exports.Bazel = void 0;
const module_bazel_1 = require("../updaters/bazel/module-bazel");
const changelog_1 = require("../updaters/changelog");
const base_1 = require("./base");
class Bazel extends base_1.BaseStrategy {
    constructor(options) {
        var _a;
        super(options);
        this.versionFile = (_a = options.versionFile) !== null && _a !== void 0 ? _a : 'MODULE.bazel';
    }
    async buildUpdates(options) {
        const updates = [];
        const version = options.newVersion;
        !this.skipChangelog &&
            updates.push({
                path: this.addPath(this.changelogPath),
                createIfMissing: true,
                updater: new changelog_1.Changelog({
                    version,
                    changelogEntry: options.changelogEntry,
                }),
            });
        updates.push({
            path: this.addPath(this.versionFile),
            createIfMissing: false,
            updater: new module_bazel_1.ModuleBazel({
                version,
            }),
        });
        return updates;
    }
}
exports.Bazel = Bazel;
//# sourceMappingURL=bazel.js.map