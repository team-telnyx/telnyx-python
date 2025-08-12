# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .encrypted_media import EncryptedMedia

__all__ = ["OutboundFqdn"]


class OutboundFqdn(BaseModel):
    ani_override: Optional[str] = None
    """
    Set a phone number as the ani_override value to override caller id number on
    outbound calls.
    """

    ani_override_type: Optional[Literal["always", "normal", "emergency"]] = None
    """Specifies when we should apply your ani_override setting.

    Only applies when ani_override is not blank.
    """

    call_parking_enabled: Optional[bool] = None
    """
    Forces all SIP calls originated on this connection to be \"parked\" instead of
    \"bridged\" to the destination specified on the URI. Parked calls will return
    ringback to the caller and will await for a Call Control command to define which
    action will be taken next.
    """

    channel_limit: Optional[int] = None
    """
    When set, this will limit the total number of inbound calls to phone numbers
    associated with this connection.
    """

    encrypted_media: Optional[EncryptedMedia] = None
    """Enable use of SRTP for encryption.

    Cannot be set if the transport_portocol is TLS.
    """

    generate_ringback_tone: Optional[bool] = None
    """Generate ringback tone through 183 session progress message with early media."""

    instant_ringback_enabled: Optional[bool] = None
    """
    When set, ringback will not wait for indication before sending ringback tone to
    calling party.
    """

    ip_authentication_method: Optional[Literal["credential-authentication", "ip-authentication"]] = None

    ip_authentication_token: Optional[str] = None

    localization: Optional[str] = None
    """
    A 2-character country code specifying the country whose national dialing rules
    should be used. For example, if set to `US` then any US number can be dialed
    without preprending +1 to the number. When left blank, Telnyx will try US and GB
    dialing rules, in that order, by default.",
    """

    outbound_voice_profile_id: Optional[str] = None
    """Identifies the associated outbound voice profile."""

    t38_reinvite_source: Optional[
        Literal["telnyx", "customer", "disabled", "passthru", "caller-passthru", "callee-passthru"]
    ] = None
    """This setting only affects connections with Fax-type Outbound Voice Profiles.

    The setting dictates whether or not Telnyx sends a t.38 reinvite. By default,
    Telnyx will send the re-invite. If set to `customer`, the caller is expected to
    send the t.38 reinvite.
    """

    tech_prefix: Optional[str] = None
    """Numerical chars only, exactly 4 characters."""

    timeout_1xx_secs: Optional[int] = None
    """Time(sec) before aborting if connection is not made."""

    timeout_2xx_secs: Optional[int] = None
    """Time(sec) before aborting if call is unanswered (min: 1, max: 600)."""
