# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionBulkEnableVoiceParams"]


class ActionBulkEnableVoiceParams(TypedDict, total=False):
    sim_card_group_id: Required[str]

    connection_id: str
    """The identifier of the Mobile Voice Connection to associate with the SIM cards.

    The connection must be owned by the same user and of type
    <code>mobile_voice</code>. If omitted, voice is enabled without a connection
    association.
    """
