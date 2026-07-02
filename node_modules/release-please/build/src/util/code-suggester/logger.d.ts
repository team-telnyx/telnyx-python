import { Logger } from './types';
declare let logger: Logger;
declare function setupLogger(userLogger?: Logger): void;
export { logger, setupLogger };
