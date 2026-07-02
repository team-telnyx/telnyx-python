import { Scm } from '../scm';
import { CandidateReleasePullRequest, RepositoryConfig } from '../manifest';
import { Version, VersionsMap } from '../version';
import { WorkspacePlugin, DependencyGraph, WorkspacePluginOptions } from './workspace';
import { Strategy } from '../strategy';
import { Commit } from '../commit';
import { Release } from '../release';
interface Package {
    path: string;
    name: string;
    version: string;
    dependencies: Record<string, string>;
    devDependencies: Record<string, string>;
    peerDependencies: Record<string, string>;
    optionalDependencies: Record<string, string>;
    jsonContent: string;
}
interface NodeWorkspaceOptions extends WorkspacePluginOptions {
    alwaysLinkLocal?: boolean;
    updatePeerDependencies?: boolean;
}
/**
 * The plugin analyzed a cargo workspace and will bump dependencies
 * of managed packages if those dependencies are being updated.
 *
 * If multiple node packages are being updated, it will merge them
 * into a single node package.
 */
export declare class NodeWorkspace extends WorkspacePlugin<Package> {
    private alwaysLinkLocal;
    private strategiesByPath;
    private releasesByPath;
    readonly updatePeerDependencies: boolean;
    constructor(github: Scm, targetBranch: string, repositoryConfig: RepositoryConfig, options?: NodeWorkspaceOptions);
    protected buildAllPackages(candidates: CandidateReleasePullRequest[]): Promise<{
        allPackages: Package[];
        candidatesByPackage: Record<string, CandidateReleasePullRequest>;
    }>;
    protected bumpVersion(pkg: Package): Version;
    protected updateCandidate(existingCandidate: CandidateReleasePullRequest, pkg: Package, updatedVersions: VersionsMap): CandidateReleasePullRequest;
    protected newCandidate(pkg: Package, updatedVersions: VersionsMap): Promise<CandidateReleasePullRequest>;
    protected postProcessCandidates(candidates: CandidateReleasePullRequest[], _updatedVersions: VersionsMap): CandidateReleasePullRequest[];
    protected buildGraph(allPackages: Package[]): Promise<DependencyGraph<Package>>;
    protected inScope(candidate: CandidateReleasePullRequest): boolean;
    protected packageNameFromPackage(pkg: Package): string;
    protected pathFromPackage(pkg: Package): string;
    private combineDeps;
    preconfigure(strategiesByPath: Record<string, Strategy>, _commitsByPath: Record<string, Commit[]>, _releasesByPath: Record<string, Release>): Promise<Record<string, Strategy>>;
}
export {};
