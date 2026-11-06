# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["MeetingUpdateParams"]


class MeetingUpdateParams(TypedDict, total=False):
    id: Required[str]

    bot_will_join: Required[Optional[bool]]
    """True opts in, false opts out, null follows connection policy.

    A supported meeting URL is still required.
    """
