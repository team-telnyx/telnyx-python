# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["PolicyAttachmentCreateParams"]


class PolicyAttachmentCreateParams(TypedDict, total=False):
    policy: Required[str]
    """The policy to apply, by name."""

    default: bool
    """`true` applies the policy only to the requests no other attachment matches."""

    models: SequenceNotStr[str]
    """The models whose requests the policy applies to, by name.

    A name can use `*` as a wildcard. Empty applies the policy to every request.
    """

    priority: Optional[int]
    """An attachment with a priority applies before the others."""
