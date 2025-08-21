# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ActionSwitchSupervisorRoleParams"]


class ActionSwitchSupervisorRoleParams(TypedDict, total=False):
    role: Required[Literal["barge", "whisper", "monitor"]]
    """The supervisor role to switch to.

    'barge' allows speaking to both parties, 'whisper' allows speaking to caller
    only, 'monitor' allows listening only.
    """
