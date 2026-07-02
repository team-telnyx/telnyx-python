import { DefaultVersioningStrategyOptions, DefaultVersioningStrategy } from './default';
import { Version } from '../version';
import { ConventionalCommit } from '..';
import { VersionUpdater } from '../versioning-strategy';
interface PrereleaseVersioningStrategyOptions extends DefaultVersioningStrategyOptions {
    prereleaseType?: string;
    prerelease?: boolean;
}
/**
 * This versioning strategy will increment the pre-release number for patch
 * bumps if there is a pre-release number (preserving any leading 0s).
 * Example: 1.2.3-beta01 -> 1.2.3-beta02.
 */
export declare class PrereleaseVersioningStrategy extends DefaultVersioningStrategy {
    readonly prereleaseType?: string;
    readonly prerelease: boolean;
    constructor(options?: PrereleaseVersioningStrategyOptions);
    determineReleaseType(version: Version, commits: ConventionalCommit[]): VersionUpdater;
}
export {};
