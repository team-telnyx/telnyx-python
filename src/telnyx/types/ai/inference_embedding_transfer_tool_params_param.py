# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["InferenceEmbeddingTransferToolParamsParam", "Target", "CustomHeader"]


class Target(TypedDict, total=False):
    name: str
    """The name of the target."""

    to: str
    """The destination number or SIP URI of the call."""


class CustomHeader(TypedDict, total=False):
    name: str

    value: str
    """The value of the header.

    Note that we support mustache templating for the value. For example you can use
    `{{#integration_secret}}test-secret{{/integration_secret}}` to pass the value of
    the integration secret.
    """


_InferenceEmbeddingTransferToolParamsParamReservedKeywords = TypedDict(
    "_InferenceEmbeddingTransferToolParamsParamReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class InferenceEmbeddingTransferToolParamsParam(
    _InferenceEmbeddingTransferToolParamsParamReservedKeywords, total=False
):
    targets: Required[Iterable[Target]]
    """The different possible targets of the transfer.

    The assistant will be able to choose one of the targets to transfer the call to.
    """

    custom_headers: Iterable[CustomHeader]
    """Custom headers to be added to the SIP INVITE for the transfer command."""
