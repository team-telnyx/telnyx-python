import { Python } from './python';
import { BuildUpdatesOptions } from './base';
import { Update } from '../update';
export declare class PythonLibrarian extends Python {
    protected buildUpdates(options: BuildUpdatesOptions): Promise<Update[]>;
}
