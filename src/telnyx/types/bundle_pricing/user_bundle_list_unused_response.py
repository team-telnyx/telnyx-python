# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .billing_bundle_summary import BillingBundleSummary

__all__ = ["UserBundleListUnusedResponse", "Data"]


class Data(BaseModel):
    billing_bundle: BillingBundleSummary

    user_bundle_ids: List[str]
    """List of user bundle IDs for given bundle."""


class UserBundleListUnusedResponse(BaseModel):
    data: List[Data]
