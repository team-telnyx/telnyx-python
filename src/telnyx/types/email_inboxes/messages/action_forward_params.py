# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from ...._types import SequenceNotStr
from .inbox_action_recipient_input_param import InboxActionRecipientInputParam
from .inbox_action_email_address_input_param import InboxActionEmailAddressInputParam

__all__ = ["ActionForwardParams", "To", "ToUnionMember1"]


class ActionForwardParams(TypedDict, total=False):
    inbox_id: Required[str]

    to: Required[To]
    """One recipient or a non-empty recipient array.

    Each recipient may be an email string or an object with `email` and optional
    `name`.
    """

    bcc: InboxActionRecipientInputParam
    """One recipient or a recipient array.

    Each recipient may be an email string or an object with `email` and optional
    `name`.
    """

    cc: InboxActionRecipientInputParam
    """One recipient or a recipient array.

    Each recipient may be an email string or an object with `email` and optional
    `name`.
    """

    html: str
    """Optional HTML note prepended to the generated forwarded-message block.

    Blank values are treated as omitted.
    """

    text: str
    """Optional plain-text note prepended to the generated forwarded-message block.

    Blank values are treated as omitted.
    """


class ToUnionMember1(TypedDict, total=False):
    email: Required[str]

    name: str


To: TypeAlias = Union[str, ToUnionMember1, SequenceNotStr[InboxActionEmailAddressInputParam]]
