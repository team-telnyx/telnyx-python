# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["TfVerificationStatus"]

TfVerificationStatus: TypeAlias = Literal[
    "Verified", "Rejected", "Waiting For Vendor", "Waiting For Customer", "Waiting For Telnyx", "In Progress"
]
