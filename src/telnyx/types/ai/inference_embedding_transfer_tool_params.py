# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["InferenceEmbeddingTransferToolParams", "Target", "CustomHeader"]


class Target(BaseModel):
    name: Optional[str] = None
    """The name of the target."""

    to: Optional[str] = None
    """The destination number or SIP URI of the call."""


class CustomHeader(BaseModel):
    name: Optional[str] = None

    value: Optional[str] = None
    """The value of the header.

    Note that we support mustache templating for the value. For example you can use
    `{{#integration_secret}}test-secret{{/integration_secret}}` to pass the value of
    the integration secret.
    """


class InferenceEmbeddingTransferToolParams(BaseModel):
    from_: str = FieldInfo(alias="from")
    """Number or SIP URI placing the call."""

    targets: List[Target]
    """The different possible targets of the transfer.

    The assistant will be able to choose one of the targets to transfer the call to.
    """

    custom_headers: Optional[List[CustomHeader]] = None
    """Custom headers to be added to the SIP INVITE for the transfer command."""
