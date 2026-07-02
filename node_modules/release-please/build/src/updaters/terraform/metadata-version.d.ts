import { Logger } from '../../util/logger';
import { DefaultUpdater } from '../default';
/**
 * Updates a Terraform metadata.yaml or metadata.display.yaml file(s).
 */
export declare class MetadataVersion extends DefaultUpdater {
    /**
     * Given initial file contents, return updated contents.
     * @param {string} content The initial content
     * @returns {string} The updated content
     */
    updateContent(content: string, logger?: Logger): string;
}
