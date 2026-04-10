# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CheckAvailabilityToolParams"]


class CheckAvailabilityToolParams(TypedDict, total=False):
    api_key_ref: Required[str]
    """Reference to an integration secret that contains your Cal.com API key.

    You would pass the `identifier` for an integration secret
    [/v2/integration_secrets](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
    that refers to your Cal.com API key.
    """

    event_type_id: Required[int]
    """Event Type ID for which slots are being fetched.

    [cal.com](https://cal.com/docs/api-reference/v2/slots/get-available-slots#parameter-event-type-id)
    """
