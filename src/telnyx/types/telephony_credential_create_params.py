# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TelephonyCredentialCreateParams"]


class TelephonyCredentialCreateParams(TypedDict, total=False):
    connection_id: Required[str]
    """Identifies the Credential Connection this credential is associated with."""

    expires_at: str
    """ISO-8601 formatted date indicating when the credential will expire."""

    name: str

    tag: str
    """Tags a credential. A single tag can hold at maximum 1000 credentials."""
