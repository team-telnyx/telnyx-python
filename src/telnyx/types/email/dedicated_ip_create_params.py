# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DedicatedIPCreateParams"]


class DedicatedIPCreateParams(TypedDict, total=False):
    idempotency_key: Required[Annotated[str, PropertyInfo(alias="Idempotency-Key")]]

    ip_version: Literal["ipv4"]
    """Allocate an IP of this address family.

    Supported value: `ipv4`. Any other value, including `ipv6` or `null`, returns
    `422`.
    """

    region: Literal["ewr-nj1"]
    """Allocate an IP in this region.

    Supported value: `ewr-nj1`. Any other value, including an empty string or
    `null`, returns `422`.
    """
