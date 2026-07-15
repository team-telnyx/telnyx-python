# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CloudfCreateParams"]


class CloudfCreateParams(TypedDict, total=False):
    name: Required[str]
    """Filesystem name, unique within your organization.

    Names are trimmed and lowercased; after normalization they may contain lowercase
    letters, numbers, `.`, `_`, and `-` only.
    """

    region: Required[Literal["us-central-1", "us-east-1", "us-west-1"]]
    """Region where the filesystem's storage and metadata are provisioned."""

    idempotency_key: Required[Annotated[str, PropertyInfo(alias="Idempotency-Key")]]
