# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AzureVoiceSettings"]


class AzureVoiceSettings(TypedDict, total=False):
    type: Required[Literal["azure"]]
    """Voice settings provider type"""

    api_key_ref: str
    """
    The `identifier` for an integration secret that refers to your Azure Speech API
    key.
    """

    deployment_id: str
    """The deployment ID for a custom Azure neural voice."""

    effect: Literal["eq_car", "eq_telecomhp8k"]
    """Audio effect to apply."""

    gender: Literal["Male", "Female"]
    """Voice gender filter."""

    region: str
    """The Azure region for the Speech service (e.g., `eastus`, `westeurope`).

    Required when using a custom API key.
    """
