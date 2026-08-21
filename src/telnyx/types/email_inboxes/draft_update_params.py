# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr
from ..email_address_input_param import EmailAddressInputParam

__all__ = ["DraftUpdateParams"]


class DraftUpdateParams(TypedDict, total=False):
    inbox_id: Required[str]

    attachments: Iterable[Dict[str, object]]

    bcc: SequenceNotStr[EmailAddressInputParam]

    cc: SequenceNotStr[EmailAddressInputParam]

    from_email: str

    from_name: str

    headers: Dict[str, str]

    html: str
    """Alias for `html_body`, matching the send endpoint."""

    html_body: str

    labels: SequenceNotStr[str]

    metadata: Dict[str, object]

    reply_to: str

    subject: str

    tags: SequenceNotStr[str]

    text: str
    """Alias for `text_body`, matching the send endpoint."""

    text_body: str

    to: SequenceNotStr[EmailAddressInputParam]
