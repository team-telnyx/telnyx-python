import { BaseStrategy, BuildUpdatesOptions, BaseStrategyOptions } from './base';
import { Update } from '../update';
import { Version } from '../version';
export declare class R extends BaseStrategy {
    constructor(options: BaseStrategyOptions);
    protected buildUpdates(options: BuildUpdatesOptions): Promise<Update[]>;
    protected initialReleaseVersion(): Version;
}
