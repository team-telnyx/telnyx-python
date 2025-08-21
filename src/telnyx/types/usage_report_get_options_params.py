# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UsageReportGetOptionsParams"]


class UsageReportGetOptionsParams(TypedDict, total=False):
    product: str
    """Options (dimensions and metrics) for a given product.

    If none specified, all products will be returned.
    """

    authorization_bearer: str
    """Authenticates the request with your Telnyx API V2 KEY"""
