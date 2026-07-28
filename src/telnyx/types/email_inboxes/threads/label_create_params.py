# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["LabelCreateParams"]


class LabelCreateParams(TypedDict, total=False):
    inbox_id: Required[str]

    labels: Required[SequenceNotStr[str]]
    """One or more labels.

    Each label is a freeform, case-sensitive string of at most 255 characters; a
    message or thread may carry at most 50 labels. The `telnyx:` prefix is a
    reserved system namespace and is rejected on customer writes.
    """
