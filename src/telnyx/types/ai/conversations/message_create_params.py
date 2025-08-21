# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["MessageCreateParams"]


class MessageCreateParams(TypedDict, total=False):
    role: Required[str]

    content: str

    metadata: Dict[str, Union[str, int, bool, List[Union[str, int, bool]]]]

    name: str

    sent_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    tool_call_id: str

    tool_calls: Iterable[Dict[str, object]]

    tool_choice: Union[str, object]
