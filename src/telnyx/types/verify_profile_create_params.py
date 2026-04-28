# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["VerifyProfileCreateParams", "Call", "Flashcall", "SMS", "Whatsapp"]


class VerifyProfileCreateParams(TypedDict, total=False):
    name: Required[str]

    call: Call

    daily_spend_limit: float
    """The maximum daily spend allowed on this verify profile, in USD."""

    daily_spend_limit_enabled: bool
    """Whether the daily spend limit is enforced for this verify profile."""

    flashcall: Flashcall

    language: str

    sms: SMS

    webhook_failover_url: str

    webhook_url: str

    whatsapp: Whatsapp


class Call(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    app_name: str
    """
    The name that identifies the application requesting 2fa in the verification
    message.
    """

    code_length: int
    """The length of the verify code to generate."""

    default_verification_timeout_secs: int
    """
    For every request that is initiated via this Verify profile, this sets the
    number of seconds before a verification request code expires. Once the
    verification request expires, the user cannot use the code to verify their
    identity.
    """

    messaging_template_id: str
    """The message template identifier selected from /verify_profiles/templates"""

    whitelisted_destinations: SequenceNotStr[str]
    """Enabled country destinations to send verification codes.

    The elements in the list must be valid ISO 3166-1 alpha-2 country codes. If set
    to `["*"]`, all destinations will be allowed. **Conditionally required:** this
    field must be provided when your organization is configured to require explicit
    whitelisted destinations; otherwise it is optional.
    """


class Flashcall(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    app_name: str
    """
    The name that identifies the application requesting 2fa in the verification
    message.
    """

    default_verification_timeout_secs: int
    """
    For every request that is initiated via this Verify profile, this sets the
    number of seconds before a verification request code expires. Once the
    verification request expires, the user cannot use the code to verify their
    identity.
    """

    whitelisted_destinations: SequenceNotStr[str]
    """Enabled country destinations to send verification codes.

    The elements in the list must be valid ISO 3166-1 alpha-2 country codes. If set
    to `["*"]`, all destinations will be allowed. **Conditionally required:** this
    field must be provided when your organization is configured to require explicit
    whitelisted destinations; otherwise it is optional.
    """


class SMS(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    alpha_sender: Optional[str]
    """
    The alphanumeric sender ID to use when sending to destinations that require an
    alphanumeric sender ID.
    """

    app_name: str
    """
    The name that identifies the application requesting 2fa in the verification
    message.
    """

    code_length: int
    """The length of the verify code to generate."""

    default_verification_timeout_secs: int
    """
    For every request that is initiated via this Verify profile, this sets the
    number of seconds before a verification request code expires. Once the
    verification request expires, the user cannot use the code to verify their
    identity.
    """

    messaging_template_id: str
    """The message template identifier selected from /verify_profiles/templates"""

    whitelisted_destinations: SequenceNotStr[str]
    """Enabled country destinations to send verification codes.

    The elements in the list must be valid ISO 3166-1 alpha-2 country codes. If set
    to `["*"]`, all destinations will be allowed. **Conditionally required:** this
    field must be provided when your organization is configured to require explicit
    whitelisted destinations; otherwise it is optional.
    """


class Whatsapp(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    default_verification_timeout_secs: int
    """
    For every request that is initiated via this Verify profile, this sets the
    number of seconds before a verification request code expires. Once the
    verification request expires, the user cannot use the code to verify their
    identity.
    """

    sender_phone_number: Optional[str]
    """Phone number registered on the customer WABA to send OTPs from"""

    template_id: Optional[str]
    """Customer pre-approved authentication template name registered on Meta"""

    waba_id: Optional[str]
    """Customer Meta WABA ID for Bring-Your-Own-WABA sending"""

    whitelisted_destinations: SequenceNotStr[str]
    """Enabled country destinations to send verification codes.

    The elements in the list must be valid ISO 3166-1 alpha-2 country codes. If set
    to `["*"]`, all destinations will be allowed. **Conditionally required:** this
    field must be provided when your organization is configured to require explicit
    whitelisted destinations; otherwise it is optional.
    """
