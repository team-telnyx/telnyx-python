# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .email_inboxes.email_address_param import EmailAddressParam

__all__ = ["EmailAddressInputParam"]

EmailAddressInputParam: TypeAlias = Union[str, EmailAddressParam]
