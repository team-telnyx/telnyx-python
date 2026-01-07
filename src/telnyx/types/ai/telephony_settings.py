# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TelephonySettings", "NoiseSuppressionConfig"]


class NoiseSuppressionConfig(BaseModel):
    """Configuration for noise suppression.

    Only applicable when noise_suppression is 'deepfilternet'.
    """

    attenuation_limit: Optional[int] = None
    """Attenuation limit for noise suppression. Range: 0-100."""

    mode: Optional[Literal["advanced"]] = None
    """Mode for noise suppression configuration."""


class TelephonySettings(BaseModel):
    default_texml_app_id: Optional[str] = None
    """Default Texml App used for voice calls with your assistant.

    This will be created automatically on assistant creation.
    """

    noise_suppression: Optional[Literal["deepfilternet", "disabled"]] = None
    """The noise suppression engine to use.

    Use 'disabled' to turn off noise suppression.
    """

    noise_suppression_config: Optional[NoiseSuppressionConfig] = None
    """Configuration for noise suppression.

    Only applicable when noise_suppression is 'deepfilternet'.
    """

    supports_unauthenticated_web_calls: Optional[bool] = None
    """
    When enabled, allows users to interact with your AI assistant directly from your
    website without requiring authentication. This is required for FE widgets that
    work with assistants that have telephony enabled.
    """

    time_limit_secs: Optional[int] = None
    """Maximum duration in seconds for the AI assistant to participate on the call.

    When this limit is reached the assistant will be stopped. This limit does not
    apply to portions of a call without an active assistant (for instance, a call
    transferred to a human representative).
    """
