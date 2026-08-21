# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from ...._types import SequenceNotStr
from .inbox_action_email_address_input_param import InboxActionEmailAddressInputParam

__all__ = ["InboxActionRecipientInputParam", "InboxRecipientAddress"]


class InboxRecipientAddress(TypedDict, total=False):
    email: Required[str]

    name: str


InboxActionRecipientInputParam: TypeAlias = Union[
    str, InboxRecipientAddress, SequenceNotStr[InboxActionEmailAddressInputParam]
]
