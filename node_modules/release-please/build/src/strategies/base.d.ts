import { Strategy, BuildReleaseOptions, BumpReleaseOptions } from '../strategy';
import { Scm } from '../scm';
import { VersioningStrategy } from '../versioning-strategy';
import { Repository } from '../repository';
import { ChangelogNotes, ChangelogSection } from '../changelog-notes';
import { ExtraFile } from '../manifest';
import { Update } from '../update';
import { ConventionalCommit, Commit } from '../commit';
import { Version, VersionsMap } from '../version';
import { TagName } from '../util/tag-name';
import { Release } from '../release';
import { ReleasePullRequest } from '../release-pull-request';
import { Logger } from '../util/logger';
import { PullRequestBody } from '../util/pull-request-body';
import { PullRequest } from '../pull-request';
export interface BuildUpdatesOptions {
    changelogEntry: string;
    skipChangelog?: boolean;
    commits?: ConventionalCommit[];
    newVersion: Version;
    versionsMap: VersionsMap;
    latestVersion?: Version;
}
export interface BaseStrategyOptions {
    path?: string;
    bumpMinorPreMajor?: boolean;
    bumpPatchForMinorPreMajor?: boolean;
    github: Scm;
    component?: string;
    packageName?: string;
    versioningStrategy?: VersioningStrategy;
    targetBranch: string;
    changelogPath?: string;
    changelogHost?: string;
    changelogSections?: ChangelogSection[];
    commitPartial?: string;
    headerPartial?: string;
    mainTemplate?: string;
    tagSeparator?: string;
    skipGitHubRelease?: boolean;
    skipChangelog?: boolean;
    releaseAs?: string;
    changelogNotes?: ChangelogNotes;
    includeComponentInTag?: boolean;
    includeVInTag?: boolean;
    includeVInReleaseName?: boolean;
    pullRequestTitlePattern?: string;
    pullRequestHeader?: string;
    pullRequestFooter?: string;
    componentNoSpace?: boolean;
    extraFiles?: ExtraFile[];
    versionFile?: string;
    snapshotLabels?: string[];
    skipSnapshot?: boolean;
    logger?: Logger;
    initialVersion?: string;
    extraLabels?: string[];
    dateFormat?: string;
    includeCommitAuthors?: boolean;
}
/**
 * A strategy is responsible for determining which files are
 * necessary to update in a release pull request.
 */
export declare abstract class BaseStrategy implements Strategy {
    readonly path: string;
    protected github: Scm;
    protected logger: Logger;
    protected component?: string;
    private packageName?;
    readonly versioningStrategy: VersioningStrategy;
    protected targetBranch: string;
    protected repository: Repository;
    protected changelogPath: string;
    protected changelogHost?: string;
    protected tagSeparator?: string;
    private skipGitHubRelease;
    protected skipChangelog: boolean;
    private releaseAs?;
    protected includeComponentInTag: boolean;
    protected includeVInTag: boolean;
    protected includeVInReleaseName: boolean;
    protected initialVersion?: string;
    readonly pullRequestTitlePattern?: string;
    readonly pullRequestHeader?: string;
    readonly pullRequestFooter?: string;
    readonly componentNoSpace?: boolean;
    readonly extraFiles: ExtraFile[];
    readonly extraLabels: string[];
    protected dateFormat: string;
    protected includeCommitAuthors?: boolean;
    readonly changelogNotes: ChangelogNotes;
    protected changelogSections?: ChangelogSection[];
    constructor(options: BaseStrategyOptions);
    /**
     * Specify the files necessary to update in a release pull request.
     * @param {BuildUpdatesOptions} options
     */
    protected abstract buildUpdates(options: BuildUpdatesOptions): Promise<Update[]>;
    /**
     * Return the component for this strategy. This may be a computed field.
     * @returns {string}
     */
    getComponent(): Promise<string | undefined>;
    getDefaultComponent(): Promise<string | undefined>;
    getBranchComponent(): Promise<string | undefined>;
    getPackageName(): Promise<string | undefined>;
    getDefaultPackageName(): Promise<string | undefined>;
    protected normalizeComponent(component: string | undefined): string;
    /**
     * Override this method to post process commits
     * @param {ConventionalCommit[]} commits parsed commits
     * @returns {ConventionalCommit[]} modified commits
     */
    protected postProcessCommits(commits: ConventionalCommit[]): Promise<ConventionalCommit[]>;
    protected buildReleaseNotes(conventionalCommits: ConventionalCommit[], newVersion: Version, newVersionTag: TagName, latestRelease?: Release, commits?: Commit[]): Promise<string>;
    protected buildPullRequestBody(component: string | undefined, newVersion: Version, releaseNotesBody: string, _conventionalCommits: ConventionalCommit[], _latestRelease?: Release, pullRequestHeader?: string, pullRequestFooter?: string): Promise<PullRequestBody>;
    /**
     * Builds a candidate release pull request
     * @param {Commit[]} commits Raw commits to consider for this release.
     * @param {Release} latestRelease Optional. The last release for this
     *   component if available.
     * @param {boolean} draft Optional. Whether or not to create the pull
     *   request as a draft. Defaults to `false`.
     * @returns {ReleasePullRequest | undefined} The release pull request to
     *   open for this path/component. Returns undefined if we should not
     *   open a pull request.
     */
    buildReleasePullRequest(commits: ConventionalCommit[], latestRelease?: Release, draft?: boolean, labels?: string[], bumpOnlyOptions?: BumpReleaseOptions): Promise<ReleasePullRequest | undefined>;
    private extraFilePaths;
    protected extraFileUpdates(version: Version, versionsMap: VersionsMap, dateFormat: string): Promise<Update[]>;
    protected changelogEmpty(changelogEntry: string): boolean;
    protected updateVersionsMap(versionsMap: VersionsMap, conventionalCommits: ConventionalCommit[], _newVersion: Version): Promise<VersionsMap>;
    protected buildNewVersion(conventionalCommits: ConventionalCommit[], latestRelease?: Release): Promise<Version>;
    protected buildVersionsMap(_conventionalCommits: ConventionalCommit[]): Promise<VersionsMap>;
    protected parsePullRequestBody(pullRequestBody: string): Promise<PullRequestBody | undefined>;
    /**
     * Given a merged pull request, build the candidate release.
     * @param {PullRequest} mergedPullRequest The merged release pull request.
     * @returns {Release} The candidate release.
     * @deprecated Use buildReleases() instead.
     */
    buildRelease(mergedPullRequest: PullRequest, options?: BuildReleaseOptions): Promise<Release | undefined>;
    /**
     * Given a merged pull request, build the candidate releases.
     * @param {PullRequest} mergedPullRequest The merged release pull request.
     * @returns {Release} The candidate release.
     */
    buildReleases(mergedPullRequest: PullRequest, options?: BuildReleaseOptions): Promise<Release[]>;
    isPublishedVersion(_version: Version): boolean;
    /**
     * Override this to handle the initial version of a new library.
     */
    protected initialReleaseVersion(): Version;
    /**
     * Adds a given file path to the strategy path.
     * @param {string} file Desired file path.
     * @returns {string} The file relative to the strategy.
     * @throws {Error} If the file path contains relative pathing characters, i.e. ../, ~/
     */
    protected addPath(file: string): string;
}
