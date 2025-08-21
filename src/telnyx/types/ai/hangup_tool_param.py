# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .hangup_tool_params_param import HangupToolParamsParam

__all__ = ["HangupToolParam"]


class HangupToolParam(TypedDict, total=False):
    hangup: Required[HangupToolParamsParam]

    type: Required[Literal["hangup"]]
