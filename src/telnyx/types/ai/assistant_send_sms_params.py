# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AssistantSendSMSParams"]


class AssistantSendSMSParams(TypedDict, total=False):
    from_: Required[Annotated[str, PropertyInfo(alias="from")]]

    to: Required[str]

    conversation_metadata: Dict[str, Union[str, int, bool]]

    should_create_conversation: bool

    text: str
