# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionBulkDisableVoiceParams"]


class ActionBulkDisableVoiceParams(TypedDict, total=False):
    sim_card_group_id: Required[str]
