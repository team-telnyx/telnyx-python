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
exports.FileData = void 0;
/**
 * The content and the mode of a file.
 * Default file mode is a text file which has code '100644'.
 * If `content` is not null, then `content` must be the entire file content.
 * See https://developer.github.com/v3/git/trees/#tree-object for details on mode.
 */
class FileData {
    constructor(content, mode = '100644') {
        this.mode = mode;
        this.content = content;
    }
}
exports.FileData = FileData;
//# sourceMappingURL=types.js.map