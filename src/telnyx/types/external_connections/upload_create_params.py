# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["UploadCreateParams"]


class UploadCreateParams(TypedDict, total=False):
    number_ids: Required[List[str]]

    additional_usages: List[Literal["calling_user_assignment", "first_party_app_assignment"]]

    civic_address_id: str
    """Identifies the civic address to assign all phone numbers to."""

    location_id: str
    """Identifies the location to assign all phone numbers to."""

    usage: Literal["calling_user_assignment", "first_party_app_assignment"]
    """The use case of the upload request.

    NOTE: `calling_user_assignment` is not supported for toll free numbers.
    """
