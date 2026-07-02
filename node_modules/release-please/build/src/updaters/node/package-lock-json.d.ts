import { Updater } from '../../update';
import { Logger } from '../../util/logger';
import { Version, VersionsMap } from '../../version';
import { UpdateOptions } from '../default';
/**
 * Updates a Node.js package-lock.json file's version and '' package
 * version (for a v2 lock file).
 */
export declare class PackageLockJson implements Updater {
    version?: Version;
    versionsMap?: VersionsMap;
    constructor(options: Partial<UpdateOptions>);
    updateContent(content: string, logger?: Logger): string;
}
