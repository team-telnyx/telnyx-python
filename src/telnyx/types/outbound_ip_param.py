# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["OutboundIPParam"]


class OutboundIPParam(TypedDict, total=False):
    ani_override: str
    """
    Set a phone number as the ani_override value to override caller id number on
    outbound calls.
    """

    ani_override_type: Literal["always", "normal", "emergency"]
    """Specifies when we apply your ani_override setting.

    Only applies when ani_override is not blank.
    """

    call_parking_enabled: Optional[bool]
    """
    Forces all SIP calls originated on this connection to be "parked" instead of
    "bridged" to the destination specified on the URI. Parked calls will return
    ringback to the caller and will await for a Call Control command to define which
    action will be taken next.
    """

    channel_limit: int
    """
    When set, this will limit the total number of outbound calls to phone numbers
    associated with this connection.
    """

    generate_ringback_tone: bool
    """Generate ringback tone through 183 session progress message with early media."""

    instant_ringback_enabled: bool
    """
    When set, ringback will not wait for indication before sending ringback tone to
    calling party.
    """

    ip_authentication_method: Literal["tech-prefixp-charge-info", "token"]

    ip_authentication_token: str

    localization: str
    """
    A 2-character country code specifying the country whose national dialing rules
    should be used. For example, if set to `US` then any US number can be dialed
    without preprending +1 to the number. When left blank, Telnyx will try US and GB
    dialing rules, in that order, by default.
    """

    outbound_voice_profile_id: str
    """Identifies the associated outbound voice profile."""

    t38_reinvite_source: Literal["telnyx", "customer", "disabled", "passthru", "caller-passthru", "callee-passthru"]
    """This setting only affects connections with Fax-type Outbound Voice Profiles.

    The setting dictates whether or not Telnyx sends a t.38 reinvite.<br/><br/> By
    default, Telnyx will send the re-invite. If set to `customer`, the caller is
    expected to send the t.38 reinvite.
    """

    tech_prefix: str
    """Numerical chars only, exactly 4 characters."""
