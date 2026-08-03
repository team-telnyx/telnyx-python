# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypedDict

__all__ = ["EmailUnsubscribeGroupDeleteParams"]


class EmailUnsubscribeGroupDeleteParams(TypedDict, total=False):
    force: Union[Literal["true", "false"], bool]
    """Force-delete a group with active suppressions.

    Only `"true"` (string) or `true` (bool) are truthy; all other values are false.
    """
