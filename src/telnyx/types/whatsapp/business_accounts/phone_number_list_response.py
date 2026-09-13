# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["PhoneNumberListResponse", "SyncProgress"]


class SyncProgress(BaseModel):
    """Synchronization progress.

    This object is returned only while a coexistence number is synchronizing.
    """

    contacts_status: Optional[str] = None

    history_chunk_order: Optional[int] = None

    history_phase: Optional[int] = None

    history_progress: Optional[int] = None

    history_status: Optional[str] = None


class PhoneNumberListResponse(BaseModel):
    calling_enabled: Optional[bool] = None

    coexistence_state: Optional[
        Literal[
            "pending_onboarding",
            "sync_pending",
            "syncing",
            "sync_complete",
            "active",
            "history_declined",
            "sync_deadline_expired",
            "offboarded",
            "disconnected",
        ]
    ] = None
    """Current lifecycle state for a coexistence number.

    This is null for a standard Cloud API number.
    """

    created_at: Optional[datetime] = None

    display_name: Optional[str] = None

    enabled: Optional[bool] = None

    is_on_biz_app: Optional[bool] = None
    """
    Indicates whether the number is connected to both the WhatsApp Business app and
    Cloud API through WhatsApp Coexistence.
    """

    phone_number: Optional[str] = None
    """Phone number in E164 format"""

    phone_number_id: Optional[str] = None
    """Whatsapp phone number ID"""

    quality_rating: Optional[str] = None
    """Whatsapp quality rating"""

    record_type: Optional[str] = None

    status: Optional[str] = None

    sync_deadline: Optional[datetime] = None
    """Deadline for initiating the current coexistence synchronization cycle.

    This is null when no deadline applies.
    """

    sync_progress: Optional[SyncProgress] = None
    """Synchronization progress.

    This object is returned only while a coexistence number is synchronizing.
    """

    user_id: Optional[str] = None
    """User ID"""

    waba_id: Optional[str] = None
    """WABA ID of Whatsapp business account"""
