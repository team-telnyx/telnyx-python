# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["VerifyProfile", "Call", "Flashcall", "SMS"]


class Call(BaseModel):
    app_name: Optional[str] = None
    """
    The name that identifies the application requesting 2fa in the verification
    message.
    """

    code_length: Optional[int] = None
    """The length of the verify code to generate."""

    default_verification_timeout_secs: Optional[int] = None
    """
    For every request that is initiated via this Verify profile, this sets the
    number of seconds before a verification request code expires. Once the
    verification request expires, the user cannot use the code to verify their
    identity.
    """

    messaging_template_id: Optional[str] = None
    """The message template identifier selected from /verify_profiles/templates"""

    whitelisted_destinations: Optional[List[str]] = None
    """Enabled country destinations to send verification codes.

    The elements in the list must be valid ISO 3166-1 alpha-2 country codes. If set
    to `["*"]`, all destinations will be allowed.
    """

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class Flashcall(BaseModel):
    default_verification_timeout_secs: Optional[int] = None
    """
    For every request that is initiated via this Verify profile, this sets the
    number of seconds before a verification request code expires. Once the
    verification request expires, the user cannot use the code to verify their
    identity.
    """

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class SMS(BaseModel):
    alpha_sender: Optional[str] = None
    """
    The alphanumeric sender ID to use when sending to destinations that require an
    alphanumeric sender ID.
    """

    app_name: Optional[str] = None
    """
    The name that identifies the application requesting 2fa in the verification
    message.
    """

    code_length: Optional[int] = None
    """The length of the verify code to generate."""

    default_verification_timeout_secs: Optional[int] = None
    """
    For every request that is initiated via this Verify profile, this sets the
    number of seconds before a verification request code expires. Once the
    verification request expires, the user cannot use the code to verify their
    identity.
    """

    messaging_template_id: Optional[str] = None
    """The message template identifier selected from /verify_profiles/templates"""

    whitelisted_destinations: Optional[List[str]] = None
    """Enabled country destinations to send verification codes.

    The elements in the list must be valid ISO 3166-1 alpha-2 country codes. If set
    to `["*"]`, all destinations will be allowed.
    """

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class VerifyProfile(BaseModel):
    id: Optional[str] = None

    call: Optional[Call] = None

    created_at: Optional[str] = None

    flashcall: Optional[Flashcall] = None

    language: Optional[str] = None

    name: Optional[str] = None

    record_type: Optional[Literal["verification_profile"]] = None
    """The possible verification profile record types."""

    sms: Optional[SMS] = None

    updated_at: Optional[str] = None

    webhook_failover_url: Optional[str] = None

    webhook_url: Optional[str] = None
