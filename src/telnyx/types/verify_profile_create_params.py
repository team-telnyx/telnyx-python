# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["VerifyProfileCreateParams", "Call", "Flashcall", "SMS"]


class VerifyProfileCreateParams(TypedDict, total=False):
    name: Required[str]

    call: Call

    flashcall: Flashcall

    language: str

    sms: SMS

    webhook_failover_url: str

    webhook_url: str


class CallTyped(TypedDict, total=False):
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

    whitelisted_destinations: List[str]
    """Enabled country destinations to send verification codes.

    The elements in the list must be valid ISO 3166-1 alpha-2 country codes. If set
    to `["*"]`, all destinations will be allowed.
    """


Call: TypeAlias = Union[CallTyped, Dict[str, object]]


class FlashcallTyped(TypedDict, total=False):
    default_verification_timeout_secs: int
    """
    For every request that is initiated via this Verify profile, this sets the
    number of seconds before a verification request code expires. Once the
    verification request expires, the user cannot use the code to verify their
    identity.
    """

    whitelisted_destinations: List[str]
    """Enabled country destinations to send verification codes.

    The elements in the list must be valid ISO 3166-1 alpha-2 country codes. If set
    to `["*"]`, all destinations will be allowed.
    """


Flashcall: TypeAlias = Union[FlashcallTyped, Dict[str, object]]


class SMSTyped(TypedDict, total=False):
    whitelisted_destinations: Required[List[str]]
    """Enabled country destinations to send verification codes.

    The elements in the list must be valid ISO 3166-1 alpha-2 country codes. If set
    to `["*"]`, all destinations will be allowed.
    """

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


SMS: TypeAlias = Union[SMSTyped, Dict[str, object]]
