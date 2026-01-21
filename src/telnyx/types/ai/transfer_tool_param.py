# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TransferToolParam", "Transfer", "TransferTarget"]


class TransferTarget(TypedDict, total=False):
    name: str
    """The name of the target."""

    to: str
    """The destination number or SIP URI of the call."""


_TransferReservedKeywords = TypedDict(
    "_TransferReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class Transfer(_TransferReservedKeywords, total=False):
    targets: Required[Iterable[TransferTarget]]
    """The different possible targets of the transfer.

    The assistant will be able to choose one of the targets to transfer the call to.
    """


class TransferToolParam(TypedDict, total=False):
    transfer: Required[Transfer]

    type: Required[Literal["transfer"]]
