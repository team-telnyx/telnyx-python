import { Logger } from '../../util/logger';
import { Version, VersionsMap } from '../../version';
import { DefaultUpdater, UpdateOptions } from '../default';
export type PackageJsonDescriptor = {
    name?: string;
    resolved?: string;
    link?: boolean;
    version: string;
    dependencies?: Record<string, string>;
    devDependencies?: Record<string, string>;
    peerDependencies?: Record<string, string>;
    optionalDependencies?: Record<string, string>;
};
export interface PackageJsonOptions extends UpdateOptions {
    updatePeerDependencies?: boolean;
}
/**
 * This updates a Node.js package.json file's main version.
 */
export declare class PackageJson extends DefaultUpdater {
    private updatePeerDependencies;
    constructor(options: PackageJsonOptions);
    /**
     * Given initial file contents, return updated contents.
     * @param {string} content The initial content
     * @param logger
     * @returns {string} The updated content
     */
    updateContent(content: string, logger?: Logger): string;
}
/**
 * Helper to coerce a new version value into a version range that preserves the
 * version range prefix of the original version.
 * @param {string} oldVersion Old semver with range
 * @param {Version} newVersion The new version to update with
 */
export declare function newVersionWithRange(oldVersion: string, newVersion: Version): string;
export declare const NPM_PROTOCOL_REGEXP: RegExp;
/**
 * Helper function to update dependency versions for all new versions specified
 * in the updated versions map. Note that this mutates the existing input.
 * @param {Record<string, string>} dependencies Entries in package.json dependencies
 *   where the key is the dependency name and the value is the dependency range
 * @param {VersionsMap} updatedVersions Map of new versions (without dependency range prefixes)
 */
export declare function updateDependencies(dependencies: Record<string, string>, updatedVersions: VersionsMap): void;
