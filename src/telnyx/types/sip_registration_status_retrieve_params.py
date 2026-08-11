# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SipRegistrationStatusRetrieveParams"]


class SipRegistrationStatusRetrieveParams(TypedDict, total=False):
    credential_type: Required[Literal["uac_external_credential", "telephony_credential", "sip_credential_connection"]]
    """The kind of credential to look up.

    `uac_external_credential` is keyed by `connection_id`; `telephony_credential`
    and `sip_credential_connection` are keyed by `username`.
    """

    connection_id: str
    """Identifier of the UAC connection to look up.

    Required when `credential_type` is `uac_external_credential`.
    """

    username: str
    """SIP username to look up.

    Required when `credential_type` is `telephony_credential` or
    `sip_credential_connection`.
    """
