# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from datetime import datetime

from ..inference_embedding import InferenceEmbedding

__all__ = ["DeletedAssistant"]


class DeletedAssistant(InferenceEmbedding):
    """
    A soft-deleted assistant in the Recently Deleted list: the full assistant configuration plus deletion metadata.
    """

    deleted_at: datetime
    """Timestamp of the soft delete."""

    permanently_deleted_at: datetime
    """
    Point after which the assistant is permanently deleted automatically and can no
    longer be restored.
    """
