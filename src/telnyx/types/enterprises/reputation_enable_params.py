# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .reputation_check_frequency import ReputationCheckFrequency

__all__ = ["ReputationEnableParams"]


class ReputationEnableParams(TypedDict, total=False):
    loa_document_id: Required[str]
    """
    Id of the signed Letter of Authorization document, returned by the Telnyx
    Documents API after upload (upload via `POST /v2/documents`; see
    https://developers.telnyx.com/api/documents).
    """

    check_frequency: ReputationCheckFrequency
    """
    How often Telnyx refreshes the stored reputation data for this enterprise's
    registered numbers.
    """
