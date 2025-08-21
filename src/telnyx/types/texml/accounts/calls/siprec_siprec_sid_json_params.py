# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["SiprecSiprecSidJsonParams"]


class SiprecSiprecSidJsonParams(TypedDict, total=False):
    account_sid: Required[str]

    call_sid: Required[str]

    status: Annotated[Literal["stopped"], PropertyInfo(alias="Status")]
    """The new status of the resource.

    Specifying `stopped` will end the siprec session.
    """
