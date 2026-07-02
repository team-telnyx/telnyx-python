import { Update } from '../update';
import { BaseStrategy, BaseStrategyOptions, BuildUpdatesOptions } from './base';
export declare class Bazel extends BaseStrategy {
    readonly versionFile: string;
    constructor(options: BaseStrategyOptions);
    protected buildUpdates(options: BuildUpdatesOptions): Promise<Update[]>;
}
