# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionTestConnectionParams"]


class ActionTestConnectionParams(TypedDict, total=False):
    api_key_ref: Required[str]
    """
    The identifier of the Integration Secret in your organization that Telnyx
    connects to the engine with, as a caller would.
    """

    voice_id: str
    """The voice to test.

    Default: the first voice in the engine's list. It must be in the list.
    """
