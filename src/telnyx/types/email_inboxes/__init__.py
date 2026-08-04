# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .draft_list_params import DraftListParams as DraftListParams
from .filter_add_params import FilterAddParams as FilterAddParams
from .draft_patch_params import DraftPatchParams as DraftPatchParams
from .thread_list_params import ThreadListParams as ThreadListParams
from .draft_create_params import DraftCreateParams as DraftCreateParams
from .draft_update_params import DraftUpdateParams as DraftUpdateParams
from .email_address_param import EmailAddressParam as EmailAddressParam
from .message_list_params import MessageListParams as MessageListParams
from .filter_replace_params import FilterReplaceParams as FilterReplaceParams
from .inbound_thread_detail import InboundThreadDetail as InboundThreadDetail
from .message_drafts_params import MessageDraftsParams as MessageDraftsParams
from .message_update_params import MessageUpdateParams as MessageUpdateParams
from .thread_retrieve_params import ThreadRetrieveParams as ThreadRetrieveParams
from .filter_delete_all_params import FilterDeleteAllParams as FilterDeleteAllParams

if TYPE_CHECKING:
    from .email_draft import EmailDraft as EmailDraft
    from .email_address import EmailAddress as EmailAddress
    from .email_message import EmailMessage as EmailMessage
    from .inbound_thread import InboundThread as InboundThread
    from .thread_message import ThreadMessage as ThreadMessage
    from .draft_list_response import DraftListResponse as DraftListResponse
    from .filter_add_response import FilterAddResponse as FilterAddResponse
    from .email_draft_response import EmailDraftResponse as EmailDraftResponse
    from .filter_list_response import FilterListResponse as FilterListResponse
    from .email_pagination_meta import EmailPaginationMeta as EmailPaginationMeta
    from .inbound_email_address import InboundEmailAddress as InboundEmailAddress
    from .message_list_response import MessageListResponse as MessageListResponse
    from .email_message_response import EmailMessageResponse as EmailMessageResponse
    from .filter_replace_response import FilterReplaceResponse as FilterReplaceResponse
    from .message_update_response import MessageUpdateResponse as MessageUpdateResponse
    from .thread_retrieve_response import ThreadRetrieveResponse as ThreadRetrieveResponse
    from .filter_delete_all_response import FilterDeleteAllResponse as FilterDeleteAllResponse
    from .inbound_thread_list_response import InboundThreadListResponse as InboundThreadListResponse


def __getattr__(name: str) -> Any:
    if name == "EmailAddress":
        from .email_address import EmailAddress

        return EmailAddress
    if name == "EmailDraft":
        from .email_draft import EmailDraft

        return EmailDraft
    if name == "EmailDraftResponse":
        from .email_draft_response import EmailDraftResponse

        return EmailDraftResponse
    if name == "EmailMessage":
        from .email_message import EmailMessage

        return EmailMessage
    if name == "EmailMessageResponse":
        from .email_message_response import EmailMessageResponse

        return EmailMessageResponse
    if name == "DraftListResponse":
        from .draft_list_response import DraftListResponse

        return DraftListResponse
    if name == "FilterListResponse":
        from .filter_list_response import FilterListResponse

        return FilterListResponse
    if name == "FilterAddResponse":
        from .filter_add_response import FilterAddResponse

        return FilterAddResponse
    if name == "FilterDeleteAllResponse":
        from .filter_delete_all_response import FilterDeleteAllResponse

        return FilterDeleteAllResponse
    if name == "FilterReplaceResponse":
        from .filter_replace_response import FilterReplaceResponse

        return FilterReplaceResponse
    if name == "MessageUpdateResponse":
        from .message_update_response import MessageUpdateResponse

        return MessageUpdateResponse
    if name == "MessageListResponse":
        from .message_list_response import MessageListResponse

        return MessageListResponse
    if name == "EmailPaginationMeta":
        from .email_pagination_meta import EmailPaginationMeta

        return EmailPaginationMeta
    if name == "InboundEmailAddress":
        from .inbound_email_address import InboundEmailAddress

        return InboundEmailAddress
    if name == "InboundThread":
        from .inbound_thread import InboundThread

        return InboundThread
    if name == "InboundThreadListResponse":
        from .inbound_thread_list_response import InboundThreadListResponse

        return InboundThreadListResponse
    if name == "ThreadMessage":
        from .thread_message import ThreadMessage

        return ThreadMessage
    if name == "ThreadRetrieveResponse":
        from .thread_retrieve_response import ThreadRetrieveResponse

        return ThreadRetrieveResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
