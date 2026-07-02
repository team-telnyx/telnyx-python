import { CreateCommitOptions } from './github/create-commit';
export type FileMode = '100644' | '100755' | '040000' | '160000' | '120000';
/**
 * GitHub definition of tree
 */
export interface TreeObject {
    path: string;
    mode: FileMode;
    type: 'blob' | 'tree' | 'commit';
    sha?: string | null;
    content?: string;
}
/**
 * The content and the mode of a file.
 * Default file mode is a text file which has code '100644'.
 * If `content` is not null, then `content` must be the entire file content.
 * See https://developer.github.com/v3/git/trees/#tree-object for details on mode.
 */
export declare class FileData {
    readonly mode: FileMode;
    readonly content: string | null;
    constructor(content: string | null, mode?: FileMode);
}
/**
 * The map of a path to its content data.
 * The content must be the entire file content.
 */
export type Changes = Map<string, FileData>;
/**
 * The domain of a repository
 */
export interface RepoDomain {
    repo: string;
    owner: string;
}
/**
 * The domain for a branch
 */
export interface BranchDomain extends RepoDomain {
    branch: string;
}
/**
 * The descriptive properties for any entity
 */
export interface Description {
    title: string;
    body: string;
}
/**
 * The user options for creating GitHub PRs
 */
export interface CreatePullRequestUserOptions extends CreateCommitOptions {
    upstreamOwner: string;
    upstreamRepo: string;
    message: string;
    description: string;
    title: string;
    branch?: string;
    force?: boolean;
    fork?: boolean;
    primary?: string;
    maintainersCanModify?: boolean;
    labels?: string[];
    retry?: number;
    draft?: boolean;
    logger?: Logger;
    filesPerCommit?: number;
}
/**
 * GitHub data needed for creating a PR
 */
export interface CreatePullRequest {
    upstreamOwner: string;
    upstreamRepo: string;
    message: string;
    description: string;
    title: string;
    branch: string;
    force: boolean;
    primary: string;
    maintainersCanModify: boolean;
    filesPerCommit?: number;
}
interface LogFn {
    <T extends object>(obj: T, msg?: string, ...args: any[]): void;
    (msg: string, ...args: any[]): void;
}
export interface Logger {
    error: LogFn;
    warn: LogFn;
    info: LogFn;
    debug: LogFn;
    trace: LogFn;
}
export interface UserData {
    name: string;
    email: string;
}
export interface CommitData {
    message: string;
    tree: string;
    parents: string[];
    author?: UserData;
    committer?: UserData;
}
export interface CommitSigner {
    generateSignature(commit: CommitData): Promise<string>;
}
export {};
