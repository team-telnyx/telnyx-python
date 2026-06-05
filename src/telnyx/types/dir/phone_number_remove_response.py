# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PhoneNumberRemoveResponse", "Meta", "MetaError"]


class MetaError(BaseModel):
    """Per-number error returned by the bulk-delete endpoint.

    Bulk-add does not use this shape — it returns a 400 with the canonical envelope grouping numbers by failure category.
    """

    code: Literal["not_associated"]
    """Stable per-number error code.

    Currently only `not_associated` is emitted, when the number is not attached to
    this DIR.
    """

    detail: str

    phone_number: str

    title: str


class Meta(BaseModel):
    errors: List[MetaError]
    """Per-number failures that did not block the call.

    Each entry has `phone_number`, `code`, `title`, `detail`.
    """


class PhoneNumberRemoveResponse(BaseModel):
    """Bulk-delete partial-success response.

    `data` is the list of phone numbers that were soft-deleted. `meta.errors` holds per-number failures (e.g. number not associated with this DIR). When EVERY number in the request fails, the endpoint instead returns 400 with the canonical Telnyx error envelope and `data`/`meta` are absent.
    """

    data: List[str]
    """Phone numbers that were successfully soft-deleted. Bare E.164 strings."""

    meta: Meta
