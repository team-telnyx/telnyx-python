# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EmailValidationCreateParams"]


class EmailValidationCreateParams(TypedDict, total=False):
    email: Required[str]
    """Email address to validate.

    Any non-empty string is accepted; invalid syntax returns valid=false rather than
    a request error.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
