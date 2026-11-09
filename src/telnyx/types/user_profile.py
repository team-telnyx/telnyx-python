# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UserProfile"]


class UserProfile(BaseModel):
    """The authenticated user's profile."""

    id: Optional[int] = None
    """Identifier of the user profile, distinct from the user ID."""

    address_1: Optional[str] = None
    """First line of the profile address."""

    address_2: Optional[str] = None
    """Second line of the profile address."""

    business_name: Optional[str] = None
    """Business name associated with the profile."""

    city: Optional[str] = None
    """City in the profile address."""

    country: Optional[str] = None
    """Country code in the profile address."""

    data_locality: Optional[Literal["USA", "DEU", "AUS", "UAE", "CAN"]] = None
    """
    The user's data locality: USA (United States), DEU (Germany), AUS (Australia),
    UAE (United Arab Emirates), or CAN (Canada).
    """

    data_locality_migration_status: Optional[Literal["not_started", "in_progress", "finished"]] = None
    """
    Status of the user's data locality migration, or null when no migration status
    is recorded.
    """

    data_locality_updated_at: Optional[datetime] = None
    """
    Timestamp when the user's data locality was last changed, or null if it has not
    been changed.
    """

    first_name: Optional[str] = None
    """The user's first name."""

    last_name: Optional[str] = None
    """The user's last name."""

    phone_number: Optional[str] = None
    """Contact phone number associated with the profile."""

    record_type: Optional[Literal["user_profile"]] = None
    """Identifies the type of resource."""

    state: Optional[str] = None
    """State or region in the profile address."""

    updated_at: Optional[datetime] = None
    """Timestamp of the most recent profile update."""

    user_id: Optional[str] = None
    """Identifier of the user who owns this profile."""

    zip: Optional[str] = None
    """Postal code in the profile address."""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]
