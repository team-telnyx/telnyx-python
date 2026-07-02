import { DefaultUpdater, UpdateOptions } from '../default';
interface ChangelogOptions extends UpdateOptions {
    changelogEntry: string;
    versionHeaderRegex?: string;
}
export declare class News extends DefaultUpdater {
    changelogEntry: string;
    readonly versionHeaderRegex: RegExp;
    constructor(options: ChangelogOptions);
    updateContent(content: string | undefined): string;
}
export {};
