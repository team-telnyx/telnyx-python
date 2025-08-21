# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from ..._models import BaseModel
from .user_bundle_resource import UserBundleResource
from .billing_bundle_summary import BillingBundleSummary

__all__ = ["UserBundle"]


class UserBundle(BaseModel):
    id: str
    """User bundle's ID, this is used to identify the user bundle in the API."""

    active: bool
    """Status of the user bundle."""

    billing_bundle: BillingBundleSummary

    created_at: date
    """Date the user bundle was created."""

    resources: List[UserBundleResource]

    user_id: str
    """The customer's ID that owns this user bundle."""

    updated_at: Optional[date] = None
    """Date the user bundle was last updated."""
