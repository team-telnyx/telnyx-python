# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AssistantDeleteParams"]


class AssistantDeleteParams(TypedDict, total=False):
    hard_delete: bool
    """
    Permanently delete the assistant immediately instead of soft-deleting it to the
    Recently Deleted list, where it stays restorable for 30 days.
    """
