# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["HostedSignupCreateParams"]


class HostedSignupCreateParams(TypedDict, total=False):
    app_id: Required[str]
    """Meta App ID linked to the Telnyx account. The app must be enabled."""

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """When the onboarding URL expires, in RFC 3339 format.

    Must be in the future and at most 3 days ahead. Defaults to 24 hours after
    creation.
    """

    signup_type: Literal["standard", "coexistence"]
    """Onboarding flow the hosted page launches.

    Use `coexistence` for a number that remains active in the WhatsApp Business app.
    """
