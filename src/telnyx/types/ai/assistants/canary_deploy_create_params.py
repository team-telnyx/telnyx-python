# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo
from .rule_input_param import RuleInputParam

__all__ = ["CanaryDeployCreateParams"]


class CanaryDeployCreateParams(TypedDict, total=False):
    rules: Iterable[RuleInputParam]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
