# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, ForwardRef
from typing_extensions import Required, TypeAlias, TypedDict

from ...._types import SequenceNotStr

__all__ = ["InboxActionRecipientInputParam", "InboxRecipientAddress"]


class InboxRecipientAddress(TypedDict, total=False):
    email: Required[str]

    name: str


if TYPE_CHECKING:
    InboxActionRecipientInputParam: TypeAlias = Union[
        str, InboxRecipientAddress, SequenceNotStr["InboxActionEmailAddressInputParam"]
    ]
else:
    InboxActionRecipientInputParam = Union[
        str,
        InboxRecipientAddress,
        SequenceNotStr[ForwardRef(f"__import__({__name__!r}, fromlist=('',)).InboxActionEmailAddressInputParam")],
    ]

from .inbox_action_email_address_input_param import InboxActionEmailAddressInputParam
