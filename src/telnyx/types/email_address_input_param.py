# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, ForwardRef
from typing_extensions import TypeAlias

__all__ = ["EmailAddressInputParam"]

if TYPE_CHECKING:
    EmailAddressInputParam: TypeAlias = Union[str, "EmailAddressParam"]
else:
    EmailAddressInputParam = Union[str, ForwardRef(f"__import__({__name__!r}, fromlist=('',)).EmailAddressParam")]

from .email_inboxes.email_address_param import EmailAddressParam
