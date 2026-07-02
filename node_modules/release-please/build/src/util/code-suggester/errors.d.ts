export declare class CommitError extends Error {
    cause: Error;
    constructor(message: string, cause: Error);
}
