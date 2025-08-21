# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TelephonyCredentialUpdateParams"]


class TelephonyCredentialUpdateParams(TypedDict, total=False):
    connection_id: str
    """Identifies the Credential Connection this credential is associated with."""

    expires_at: str
    """ISO-8601 formatted date indicating when the credential will expire."""

    name: str

    tag: str
    """Tags a credential. A single tag can hold at maximum 1000 credentials."""
