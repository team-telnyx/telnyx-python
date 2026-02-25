# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AzureVoiceSettings"]


class AzureVoiceSettings(BaseModel):
    type: Literal["azure"]
    """Voice settings provider type"""

    api_key_ref: Optional[str] = None
    """
    The `identifier` for an integration secret that refers to your Azure Speech API
    key.
    """

    deployment_id: Optional[str] = None
    """The deployment ID for a custom Azure neural voice."""

    effect: Optional[Literal["eq_car", "eq_telecomhp8k"]] = None
    """Audio effect to apply."""

    gender: Optional[Literal["Male", "Female"]] = None
    """Voice gender filter."""

    region: Optional[str] = None
    """The Azure region for the Speech service (e.g., `eastus`, `westeurope`).

    Required when using a custom API key.
    """
