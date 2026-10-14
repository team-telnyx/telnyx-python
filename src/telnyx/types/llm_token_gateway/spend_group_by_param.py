# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypeAlias

__all__ = ["SpendGroupByParam"]

SpendGroupByParam: TypeAlias = Union[Literal["token_group", "token_user", "token_key", "end_user"], str]
