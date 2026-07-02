import { PluginType, RepositoryConfig } from '../manifest';
import { Scm } from '../scm';
import { ManifestPlugin } from '../plugin';
import { VersioningStrategyType } from './versioning-strategy-factory';
import { Logger } from '../util/logger';
export interface PluginFactoryOptions {
    type: PluginType;
    github: Scm;
    targetBranch: string;
    repositoryConfig: RepositoryConfig;
    manifestPath: string;
    separatePullRequests?: boolean;
    alwaysLinkLocal?: boolean;
    updatePeerDependencies?: boolean;
    updateAllPackages?: boolean;
    considerAllArtifacts?: boolean;
    logger?: Logger;
}
export type PluginBuilder = (options: PluginFactoryOptions) => ManifestPlugin;
export declare function buildPlugin(options: PluginFactoryOptions): ManifestPlugin;
export declare function registerPlugin(name: string, pluginBuilder: PluginBuilder): void;
export declare function unregisterPlugin(name: string): void;
export declare function getPluginTypes(): readonly VersioningStrategyType[];
