import { Logger } from './logger';
import { Version } from '../version';
export declare function generateMatchPattern(pullRequestTitlePattern?: string, componentNoSpace?: boolean, logger?: Logger): RegExp;
export declare class PullRequestTitle {
    component?: string;
    targetBranch?: string;
    version?: Version;
    pullRequestTitlePattern: string;
    matchPattern: RegExp;
    componentNoSpace?: boolean;
    private constructor();
    static parse(title: string, pullRequestTitlePattern?: string, componentNoSpace?: boolean, logger?: Logger): PullRequestTitle | undefined;
    static ofComponentVersion(component: string, version: Version, pullRequestTitlePattern?: string, componentNoSpace?: boolean): PullRequestTitle;
    static ofVersion(version: Version, pullRequestTitlePattern?: string, componentNoSpace?: boolean): PullRequestTitle;
    static ofTargetBranchVersion(targetBranch: string, version: Version, pullRequestTitlePattern?: string, componentNoSpace?: boolean): PullRequestTitle;
    static ofComponentTargetBranchVersion(component?: string, targetBranch?: string, version?: Version, pullRequestTitlePattern?: string, componentNoSpace?: boolean): PullRequestTitle;
    static ofTargetBranch(targetBranch: string, pullRequestTitlePattern?: string, componentNoSpace?: boolean): PullRequestTitle;
    getTargetBranch(): string | undefined;
    getComponent(): string | undefined;
    getVersion(): Version | undefined;
    toString(): string;
}
