import { ChangelogNotes, BuildNotesOptions } from '../changelog-notes';
import { ConventionalCommit } from '../commit';
import { Scm } from '../scm';
export declare class GitHubChangelogNotes implements ChangelogNotes {
    private github;
    constructor(github: Scm);
    buildNotes(_commits: ConventionalCommit[], options: BuildNotesOptions): Promise<string>;
}
