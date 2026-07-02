import { VersioningStrategy } from '../versioning-strategy';
import { Scm } from '../scm';
export type VersioningStrategyType = string;
export interface VersioningStrategyFactoryOptions {
    type?: VersioningStrategyType;
    bumpMinorPreMajor?: boolean;
    bumpPatchForMinorPreMajor?: boolean;
    prereleaseType?: string;
    prerelease?: boolean;
    github: Scm;
}
export type VersioningStrategyBuilder = (options: VersioningStrategyFactoryOptions) => VersioningStrategy;
export declare function buildVersioningStrategy(options: VersioningStrategyFactoryOptions): VersioningStrategy;
export declare function registerVersioningStrategy(name: string, versioningStrategyBuilder: VersioningStrategyBuilder): void;
export declare function unregisterVersioningStrategy(name: string): void;
export declare function getVersioningStrategyTypes(): readonly VersioningStrategyType[];
