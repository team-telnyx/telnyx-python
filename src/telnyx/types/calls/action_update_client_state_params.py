# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionUpdateClientStateParams"]


class ActionUpdateClientStateParams(TypedDict, total=False):
    client_state: Required[str]
    """Use this field to add state to every subsequent webhook.

    It must be a valid Base-64 encoded string.
    """
