# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ActionEnableParams"]


class ActionEnableParams(TypedDict, total=False):
    reenable_all_connections: bool
    """
    When true, all connections owned by this managed account will automatically be
    re-enabled. Note: Any connections that do not pass validations will not be
    re-enabled.
    """
