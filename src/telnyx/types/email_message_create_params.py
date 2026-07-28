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

__all__ = ["EmailMessageCreateParams"]


class EmailMessageCreateParams(TypedDict, total=False):
    from_: Required[Annotated[EmailAddressInputParam, PropertyInfo(alias="from")]]

    to: Required[SequenceNotStr[EmailAddressInputParam]]

    attachments: Iterable[AttachmentRequestParam]

    bcc: SequenceNotStr[EmailAddressInputParam]

    cc: SequenceNotStr[EmailAddressInputParam]

    forward_of_message_id: Optional[str]
    """Telnyx message UUID of the message this send forwards.

    Forwarded messages start a NEW thread per RFC 5322 — NO `In-Reply-To` or
    `References` headers are set on the outbound MIME. The id is recorded in the
    message's metadata for EDR provenance only.

    The id is validated as a UUID but is NOT looked up against the message store —
    existence is the caller's responsibility (the forward is pure metadata; it does
    not affect delivery). Cannot be combined with `in_reply_to_message_id` (422).
    """

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

    in_reply_to_message_id: Optional[str]
    """Telnyx message UUID of the message this send replies to.

    When provided, the API sets RFC 5322 `In-Reply-To` and `References` headers on
    the outbound MIME so the recipient's mailbox (Gmail/Outlook) threads it
    correctly. The parent is looked up under the caller's account scope; a UUID
    belonging to another account yields a non-enumerating 404.

    Wire-only (Phase 1): the API sets the headers and does NOT resolve or mutate
    `thread_id` on the server side. Messages sent without this parameter are
    standalone (no threading headers injected).

    Cannot be combined with `forward_of_message_id` (422).
    """

    inline_css: bool

    metadata: Dict[str, object]
    """Custom metadata. Write-only; not returned in responses."""

    reply_to: EmailAddressInputParam
    """Reply-to address.

    If provided as an object with a name, only the email is stored; the name is
    ignored.
    """

    reply_to_all: Optional[bool]
    """Indicates a reply-all intent.

    In Phase 1 (wire-only) this does not change the threading headers — recipient
    selection is customer- controlled (`to`/`cc`), and a thread is not defined by
    its audience. When the referenced message has no thread context, reply-all
    degrades to a plain reply (parent ID only in `References`). The resolution
    engine (separate work) will expand the ancestor chain at a later phase with no
    API change.

    Only meaningful alongside `in_reply_to_message_id`.
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

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
