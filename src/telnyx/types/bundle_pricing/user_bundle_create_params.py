# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["UserBundleCreateParams", "Item"]


class UserBundleCreateParams(TypedDict, total=False):
    idempotency_key: str
    """Idempotency key for the request.

    Can be any UUID, but should always be unique for each request.
    """

    items: Iterable[Item]

    authorization_bearer: str
    """Authenticates the request with your Telnyx API V2 KEY"""


class Item(TypedDict, total=False):
    billing_bundle_id: Required[str]
    """Quantity of user bundles to order."""

    quantity: Required[int]
    """Quantity of user bundles to order."""
