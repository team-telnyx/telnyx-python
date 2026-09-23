# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PrivacySettingsParam"]


class PrivacySettingsParam(TypedDict, total=False):
    data_retention: bool
    """If true, conversation history and insights will be stored.

    If false, they will not be stored. This in‑tool toggle governs solely the
    retention of conversation history and insights via the AI assistant. It has no
    effect on any separate recording, transcription, or storage configuration that
    you have set at the account, number, or application level. All such external
    settings remain in force regardless of your selection here.
    """

    in_transit_data_locality: bool
    """
    Requires every model call made for a web chat turn to be received and served
    inside your organization's data-locality region, rather than only stored there.
    Applies to web chat only — voice and messaging assistants are unaffected.
    Enabling it requires a data-locality region with in-region inference (USA, EU,
    AUS, UAE; see
    [Inference regions](https://developers.telnyx.com/docs/inference/models/regions))
    and Telnyx-hosted models for the assistant, its fallback, and any
    conversation-flow node that overrides the model; the request is rejected
    otherwise. Once enabled, send chat requests to your region's API hostname: a
    request entering the platform in another region is rejected rather than
    forwarded, because forwarding it would already have moved the content across the
    border. Defaults to false.
    """
