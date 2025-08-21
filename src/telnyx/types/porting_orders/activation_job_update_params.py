# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ActivationJobUpdateParams"]


class ActivationJobUpdateParams(TypedDict, total=False):
    id: Required[str]

    activate_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The desired activation time.

    The activation time should be between any of the activation windows.
    """
