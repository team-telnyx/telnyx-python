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
    """Array of email messages to send.

    Up to 1,000 messages per batch request. Each message is validated and sent
    independently; per-message failures do not affect other messages in the batch.
    """

    sandbox_mode: bool
    """
    Applies sandbox mode to all messages in the batch and overrides any per-message
    `sandbox_mode` value — each message's effective `sandbox_mode` is exactly this
    envelope value. Reserved recipients at `test.telnyx.com` produce the
    deterministic event chains documented on CreateEmailRequest.sandbox_mode; no
    batch item is injected into the MTA or outbound Kafka path. Sandbox batch items
    are non-billable, consume no daily-send-limit quota, and feed no
    delivery-reputation signals.
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
    """Custom metadata key/value pairs.

    Stored on the message, returned on message responses, and propagated to Email
    Detail Records. Usable in `filter[metadata]` when listing messages.
    """

    reply_to: EmailAddressInputParam
    """Reply-to address.

    If provided as an object with a name, only the email is stored; the name is
    ignored.
    """

    sandbox_mode: bool
    """Per-message sandbox flag.

    The batch-level `sandbox_mode` envelope value is authoritative: it overwrites
    every message's `sandbox_mode` before processing, including the `false` default
    when the envelope omits the field. A per-item `sandbox_mode: true` inside a
    non-sandbox batch is therefore a real send. Set the envelope field to run any
    batch item in sandbox mode.
    """

    scheduled_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Future ISO 8601 delivery time.

    Invalid or non-future timestamps are rejected. Single sends return HTTP 422; in
    batch sends the invalid item is reported in the 207 per-item errors while other
    items continue. `send_at` remains a deprecated request alias. A non-null
    `scheduled_at` takes precedence over `send_at`; when `scheduled_at` is omitted
    or null, `send_at` is used.
    """

    send_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Deprecated alias for `scheduled_at`."""

    subject: str
    """Required unless `template_id` is supplied.

    When using a template, the template's subject is rendered; if the template has
    no subject or renders empty, the request returns 400.
    """

    tags: SequenceNotStr[str]
    """Tags for categorization and filtering.

    Stored on the message, returned on message responses, and propagated to Email
    Detail Records. Usable in `filter[tags]` when listing messages.
    """

    template_id: str

    template_variables: Dict[str, object]
    """Variables for Liquid template rendering.

    Non-object values may cause a 422 validation error on message creation, but are
    silently treated as an empty object for template rendering. When the template
    enables `strict_variables`, a missing required variable fails the request with
    422 (single send) or a per-item `unprocessable_entity` error (batch) naming the
    variable; no message is persisted for the failed item.
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
