# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .tracking_settings_param import TrackingSettingsParam
from .attachment_request_param import AttachmentRequestParam
from .email_address_input_param import EmailAddressInputParam

__all__ = ["EmailMessageBatchParams", "Message"]


class EmailMessageBatchParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]

    sandbox_mode: bool
    """Applies sandbox mode to all messages in the batch.

    Overrides any per-message sandbox_mode in the messages array.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


_MessageReservedKeywords = TypedDict(
    "_MessageReservedKeywords",
    {
        "from": EmailAddressInputParam,
    },
    total=False,
)


class Message(_MessageReservedKeywords, total=False):
    """A single message in a batch create request.

    This schema mirrors
    `CreateEmailRequest` EXCEPT it does not accept the reply/forward
    threading parameters (`in_reply_to_message_id`, `reply_to_all`,
    `forward_of_message_id`) — those are single-send-only in Phase 1
    (MSG-1491) and are not yet implemented on the batch endpoint. Recipient
    email addresses must be unique across `to`, `cc`, and `bcc` after
    case-insensitive normalization. Duplicate recipients return `400`.
    """

    to: Required[SequenceNotStr[EmailAddressInputParam]]

    attachments: Iterable[AttachmentRequestParam]

    bcc: SequenceNotStr[EmailAddressInputParam]

    cc: SequenceNotStr[EmailAddressInputParam]

    from_name: str
    """Optional display name for string `from`; overrides `from.name` when provided."""

    group_id: Optional[str]
    """
    Optional unsubscribe-group UUID used for group-scoped suppression checks and
    unsubscribe handling.
    """

    headers: Dict[str, str]
    """Custom email headers. Write-only; not returned in responses."""

    html_body: str
    """HTML email body.

    Returned only by `GET /email_messages/{id}`; omitted from create and list
    responses.
    """

    ignore_suppression: bool
    """
    When true, allows delivery to recipients whose suppressions explicitly permit an
    override. Hard bounces, spam complaints, and invalid-address suppressions cannot
    be overridden. Requires the `email:override` API scope.
    """

    inline_css: bool

    metadata: Dict[str, object]
    """Custom metadata. Write-only; not returned in responses."""

    reply_to: EmailAddressInputParam
    """Reply-to address.

    If provided as an object with a name, only the email is stored; the name is
    ignored.
    """

    sandbox_mode: bool

    scheduled_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Future ISO 8601 time to schedule sending.

    Invalid or past timestamps are silently ignored and the email is sent
    immediately. The legacy alias `send_at` is still accepted for backward
    compatibility; when both are provided, `scheduled_at` wins.
    """

    send_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Deprecated alias for `scheduled_at`."""

    subject: str
    """Required unless `template_id` is supplied.

    When using a template, the template's subject is rendered; if the template has
    no subject or renders empty, the request returns 400.
    """

    tags: SequenceNotStr[str]
    """Tags for categorization and reporting.

    Stored on the message and propagated to Email Detail Records. Not returned in
    API responses.
    """

    template_id: str

    template_variables: Dict[str, object]
    """Variables for Liquid template rendering.

    Non-object values may cause a 422 validation error on message creation, but are
    silently treated as an empty object for template rendering.
    """

    text_body: str
    """Plain text email body.

    Returned only by `GET /email_messages/{id}`; omitted from create and list
    responses.
    """

    tracking_settings: TrackingSettingsParam
    """Per-send open and click tracking overrides.

    Omitted properties inherit the sender domain's tracking settings.
    """
