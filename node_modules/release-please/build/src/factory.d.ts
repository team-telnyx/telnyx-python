import { Scm } from './scm';
import { ReleaserConfig } from './manifest';
import { BaseStrategyOptions } from './strategies/base';
import { Strategy } from './strategy';
export * from './factories/changelog-notes-factory';
export * from './factories/plugin-factory';
export * from './factories/versioning-strategy-factory';
export type ReleaseType = string;
export type ReleaseBuilder = (options: BaseStrategyOptions) => Strategy;
export interface StrategyFactoryOptions extends ReleaserConfig {
    github: Scm;
    path?: string;
    targetBranch?: string;
}
export declare function buildStrategy(options: StrategyFactoryOptions): Promise<Strategy>;
export declare function registerReleaseType(name: string, strategyBuilder: ReleaseBuilder): void;
export declare function unregisterReleaseType(name: string): void;
export declare function getReleaserTypes(): readonly ReleaseType[];
