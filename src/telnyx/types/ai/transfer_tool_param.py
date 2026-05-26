# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TransferToolParam", "Transfer", "TransferTargetsUnionMember0"]


class TransferTargetsUnionMember0(TypedDict, total=False):
    to: Required[str]
    """The destination number or SIP URI of the call."""

    name: str
    """The name of the target."""


_TransferReservedKeywords = TypedDict(
    "_TransferReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class Transfer(_TransferReservedKeywords, total=False):
    targets: Required[Union[Iterable[TransferTargetsUnionMember0], str]]
    """The different possible targets of the transfer.

    The assistant will be able to choose one of the targets to transfer the call to.
    This can also be a dynamic variable string like `{{ targets }}` where `targets`
    is returned by the dynamic variables webhook and resolves to an array of target
    objects at runtime.
    """


class TransferToolParam(TypedDict, total=False):
    transfer: Required[Transfer]

    type: Required[Literal["transfer"]]
