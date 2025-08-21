# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AssistantImportParams"]


class AssistantImportParams(TypedDict, total=False):
    api_key_ref: Required[str]
    """Integration secret pointer that refers to the API key for the external provider.

    This should be an identifier for an integration secret created via
    /v2/integration_secrets.
    """

    provider: Required[Literal["elevenlabs", "vapi"]]
    """The external provider to import assistants from."""
