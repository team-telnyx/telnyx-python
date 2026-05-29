# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SipRegistrationStatusRetrieveParams"]


class SipRegistrationStatusRetrieveParams(TypedDict, total=False):
    connection_id: Required[str]
    """Identifier of the connection or credential to look up."""

    credential_type: Required[Literal["uac_external_credential", "telephony_credential", "sip_credential_connection"]]
    """The kind of credential to look up."""

    user_id: Required[str]
    """Owner of the connection. Used to authorize the lookup."""
