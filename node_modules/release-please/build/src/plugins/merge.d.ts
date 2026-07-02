import { ManifestPlugin } from '../plugin';
import { CandidateReleasePullRequest, RepositoryConfig } from '../manifest';
import { Scm } from '../scm';
export interface MergeOptions {
    pullRequestTitlePattern?: string;
    pullRequestHeader?: string;
    pullRequestFooter?: string;
    componentNoSpace?: boolean;
    headBranchName?: string;
    forceMerge?: boolean;
}
/**
 * This plugin merges multiple pull requests into a single
 * release pull request.
 *
 * Release notes are broken up using `<summary>`/`<details>` blocks.
 */
export declare class Merge extends ManifestPlugin {
    private pullRequestTitlePattern?;
    private pullRequestHeader?;
    private pullRequestFooter?;
    private componentNoSpace?;
    private headBranchName?;
    private forceMerge;
    constructor(github: Scm, targetBranch: string, repositoryConfig: RepositoryConfig, options?: MergeOptions);
    run(candidates: CandidateReleasePullRequest[]): Promise<CandidateReleasePullRequest[]>;
}
