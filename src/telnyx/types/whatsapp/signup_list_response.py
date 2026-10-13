# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SignupListResponse"]


class SignupListResponse(BaseModel):
    created_at: Optional[datetime] = None

    customer_id: Optional[str] = None
    """Tech provider customer reference submitted with the signup"""

    errors: Optional[List[str]] = None
    """Errors recorded during provisioning"""

    record_type: Optional[Literal["whatsapp_session_id"]] = None

    session_id: Optional[str] = None
    """Signup session ID"""

    state: Optional[
        Literal[
            "SUBSCRIBE_WEBHOOKS",
            "ASSIGNED_USERS",
            "SHARE_CREDIT_LINE",
            "REGISTER_PHONE_NUMBER",
            "ADD_WABA_TO_DB",
            "ADD_PHONE_NUMBERS_TO_DB",
            "COMPLETE",
        ]
    ] = None
    """Current provisioning step, or the step that failed.

    `REGISTER_PHONE_NUMBER` is skipped for coexistence signups.
    """

    status: Optional[Literal["INCOMPLETE", "PENDING", "SUCCESS", "FAILURE"]] = None
    """
    `INCOMPLETE` waits for the Meta signup code, `PENDING` is in progress, `SUCCESS`
    finished provisioning, and `FAILURE` stopped at `state`.
    """

    updated_at: Optional[datetime] = None

    user_id: Optional[str] = None
    """Telnyx user ID that owns the signup session"""

    waba_id: Optional[str] = None
    """Meta WhatsApp Business Account ID"""
