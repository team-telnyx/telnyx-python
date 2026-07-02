"use strict";
// Copyright 2026 Google LLC
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
exports.PythonLibrarian = void 0;
const python_1 = require("./python");
const librarian_yaml_1 = require("../updaters/librarian-yaml");
class PythonLibrarian extends python_1.Python {
    async buildUpdates(options) {
        const updates = await super.buildUpdates(options);
        // Update librarian.yaml if this package exists within it.
        updates.push({
            path: 'librarian.yaml',
            createIfMissing: false,
            updater: new librarian_yaml_1.LibrarianYamlUpdater({
                version: options.newVersion,
                packagePath: this.path,
            }),
        });
        return updates;
    }
}
exports.PythonLibrarian = PythonLibrarian;
//# sourceMappingURL=python-librarian.js.map