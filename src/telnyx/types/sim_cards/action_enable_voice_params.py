# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ActionEnableVoiceParams"]


class ActionEnableVoiceParams(TypedDict, total=False):
    connection_id: str
    """The identifier of the Mobile Voice Connection to associate with this SIM card.

    The connection must be owned by the same user and of type
    <code>mobile_voice</code>. If omitted, voice is enabled without a connection
    association.
    """
