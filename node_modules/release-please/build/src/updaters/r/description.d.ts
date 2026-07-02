import { DefaultUpdater } from '../default';
/**
 * Updates the DESCRIPTION file of an R package.
 */
export declare class DescriptionUpdater extends DefaultUpdater {
    /**
     * Given initial file contents, return updated contents.
     * @param {string} content The initial content
     * @returns {string} The updated content
     */
    updateContent(content: string): string;
}
