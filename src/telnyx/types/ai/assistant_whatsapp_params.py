# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AssistantWhatsappParams"]


class AssistantWhatsappParams(TypedDict, total=False):
    content: Required[str]
    """
    Instruction for the assistant, including the values for the template variables,
    e.g. `Send the login verification code 482913 to the customer.`
    """

    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """WhatsApp number on your account to send from, in E.164 format.

    Its messaging profile must have this assistant configured.
    """

    to: Required[str]
    """
    Customer to message, as an E.164 phone number or a WhatsApp business-scoped user
    ID (BSUID).
    """

    conversation_metadata: Dict[str, Union[str, int, bool]]
    """Metadata stored on the conversation.

    Keys starting with `telnyx_` and the `assistant_id` key are reserved.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
