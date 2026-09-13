# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MessagingProfileFeaturesParam"]


class MessagingProfileFeaturesParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """
    Telnyx product features the messaging customer can enable on the messaging profile. Keys map to individual feature flags; unknown keys are accepted and preserved for forward compatibility with rolling deployments.
    """

    ai_opt_out_detection_enabled: bool
    """
    Enables AI detection of inbound opt-out messages that do not follow the standard
    STOP/UNSTOP/HELP opt-out keyword pattern. When enabled, the messaging platform
    applies an AI model to identify non-standard opt-out requests (e.g.
    natural-language phrases) and treats them as opt-outs.
    """
