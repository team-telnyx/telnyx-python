# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["InboxActionEmailAddressInputParam", "InboxRecipientAddress"]


class InboxRecipientAddress(TypedDict, total=False):
    email: Required[str]

    name: str


InboxActionEmailAddressInputParam: TypeAlias = Union[str, InboxRecipientAddress]
