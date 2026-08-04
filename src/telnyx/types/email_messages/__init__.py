# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .recipient_list_params import RecipientListParams as RecipientListParams

if TYPE_CHECKING:
    from .email_recipient import EmailRecipient as EmailRecipient
    from .recipient_list_response import RecipientListResponse as RecipientListResponse
    from .recipient_retrieve_response import RecipientRetrieveResponse as RecipientRetrieveResponse


def __getattr__(name: str) -> Any:
    if name == "EmailRecipient":
        from .email_recipient import EmailRecipient

        return EmailRecipient
    if name == "RecipientRetrieveResponse":
        from .recipient_retrieve_response import RecipientRetrieveResponse

        return RecipientRetrieveResponse
    if name == "RecipientListResponse":
        from .recipient_list_response import RecipientListResponse

        return RecipientListResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
