# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "DetailRecordListResponse",
    "Data",
    "DataMessageDetailRecord",
    "DataConferenceDetailRecord",
    "DataConferenceParticipantDetailRecord",
    "DataAmdDetailRecord",
    "DataVerifyDetailRecord",
    "DataSimCardUsageDetailRecord",
    "DataMediaStorageDetailRecord",
    "Meta",
]


class DataMessageDetailRecord(BaseModel):
    record_type: str
    """Identifies the record schema"""

    carrier: Optional[str] = None
    """Country-specific carrier used to send or receive the message"""

    carrier_fee: Optional[str] = None
    """Fee charged by certain carriers in order to deliver certain message types.

    Telnyx passes this fee on to the customer according to our pricing table
    """

    cld: Optional[str] = None
    """The recipient of the message (to parameter in the Messaging API)"""

    cli: Optional[str] = None
    """The sender of the message (from parameter in the Messaging API).

    For Alphanumeric ID messages, this is the sender ID value
    """

    completed_at: Optional[datetime] = None
    """Message completion time"""

    cost: Optional[str] = None
    """Amount, in the user currency, for the Telnyx billing cost"""

    country_code: Optional[str] = None
    """
    Two-letter representation of the country of the cld property using the ISO
    3166-1 alpha-2 format
    """

    created_at: Optional[datetime] = None
    """Message creation time"""

    currency: Optional[str] = None
    """
    Telnyx account currency used to describe monetary values, including billing cost
    """

    delivery_status: Optional[str] = None
    """Final webhook delivery status"""

    delivery_status_failover_url: Optional[str] = None
    """Failover customer-provided URL which Telnyx posts delivery status webhooks to"""

    delivery_status_webhook_url: Optional[str] = None
    """Primary customer-provided URL which Telnyx posts delivery status webhooks to"""

    direction: Optional[Literal["inbound", "outbound"]] = None
    """Logical direction of the message from the Telnyx customer's perspective.

    It's inbound when the Telnyx customer receives the message, or outbound
    otherwise
    """

    errors: Optional[List[str]] = None
    """Telnyx API error codes returned by the Telnyx gateway"""

    fteu: Optional[bool] = None
    """Indicates whether this is a Free-To-End-User (FTEU) short code message"""

    mcc: Optional[str] = None
    """Mobile country code.

    Only available for certain products, such as Global Outbound-Only from
    Alphanumeric Sender ID
    """

    message_type: Optional[Literal["SMS", "MMS", "RCS"]] = None
    """Describes the Messaging service used to send the message.

    Available services are: Short Message Service (SMS), Multimedia Messaging
    Service (MMS), and Rich Communication Services (RCS)
    """

    mnc: Optional[str] = None
    """Mobile network code.

    Only available for certain products, such as Global Outbound-Only from
    Alphanumeric Sender ID
    """

    on_net: Optional[bool] = None
    """Indicates whether both sender and recipient numbers are Telnyx-managed"""

    parts: Optional[int] = None
    """Number of message parts.

    The message is broken down in multiple parts when its length surpasses the limit
    of 160 characters
    """

    profile_id: Optional[str] = None
    """Unique identifier of the Messaging Profile used to send or receive the message"""

    profile_name: Optional[str] = None
    """Name of the Messaging Profile used to send or receive the message"""

    rate: Optional[str] = None
    """Currency amount per billing unit used to calculate the Telnyx billing cost"""

    sent_at: Optional[datetime] = None
    """Time when the message was sent"""

    source_country_code: Optional[str] = None
    """
    Two-letter representation of the country of the cli property using the ISO
    3166-1 alpha-2 format
    """

    status: Optional[
        Literal["gw_timeout", "delivered", "dlr_unconfirmed", "dlr_timeout", "received", "gw_reject", "failed"]
    ] = None
    """Final status of the message after the delivery attempt"""

    tags: Optional[str] = None
    """Comma-separated tags assigned to the Telnyx number associated with the message"""

    updated_at: Optional[datetime] = None
    """Message updated time"""

    user_id: Optional[str] = None
    """Identifier of the Telnyx account who owns the message"""

    uuid: Optional[str] = None
    """Unique identifier of the message"""


class DataConferenceDetailRecord(BaseModel):
    record_type: str

    id: Optional[str] = None
    """Conference id"""

    call_leg_id: Optional[str] = None
    """Telnyx UUID that identifies the conference call leg"""

    call_sec: Optional[int] = None
    """Duration of the conference call in seconds"""

    call_session_id: Optional[str] = None
    """Telnyx UUID that identifies with conference call session"""

    connection_id: Optional[str] = None
    """Connection id"""

    ended_at: Optional[datetime] = None
    """Conference end time"""

    expires_at: Optional[datetime] = None
    """Conference expiry time"""

    is_telnyx_billable: Optional[bool] = None
    """Indicates whether Telnyx billing charges might be applicable"""

    name: Optional[str] = None
    """Conference name"""

    participant_call_sec: Optional[int] = None
    """Sum of the conference call duration for all participants in seconds"""

    participant_count: Optional[int] = None
    """Number of participants that joined the conference call"""

    region: Optional[str] = None
    """Region where the conference is hosted"""

    started_at: Optional[datetime] = None
    """Conference start time"""

    user_id: Optional[str] = None
    """User id"""


class DataConferenceParticipantDetailRecord(BaseModel):
    record_type: str

    id: Optional[str] = None
    """Participant id"""

    billed_sec: Optional[int] = None
    """Duration of the conference call for billing purposes"""

    call_leg_id: Optional[str] = None
    """Telnyx UUID that identifies the conference call leg"""

    call_sec: Optional[int] = None
    """Duration of the conference call in seconds"""

    call_session_id: Optional[str] = None
    """Telnyx UUID that identifies with conference call session"""

    conference_id: Optional[str] = None
    """Conference id"""

    cost: Optional[str] = None
    """Currency amount for Telnyx billing cost"""

    currency: Optional[str] = None
    """
    Telnyx account currency used to describe monetary values, including billing cost
    """

    destination_number: Optional[str] = None
    """Number called by the participant to join the conference"""

    is_telnyx_billable: Optional[bool] = None
    """Indicates whether Telnyx billing charges might be applicable"""

    joined_at: Optional[datetime] = None
    """Participant join time"""

    left_at: Optional[datetime] = None
    """Participant leave time"""

    originating_number: Optional[str] = None
    """Participant origin number used in the conference call"""

    rate: Optional[str] = None
    """Currency amount per billing unit used to calculate the Telnyx billing cost"""

    rate_measured_in: Optional[str] = None
    """Billing unit used to calculate the Telnyx billing cost"""

    user_id: Optional[str] = None
    """User id"""


class DataAmdDetailRecord(BaseModel):
    record_type: str

    id: Optional[str] = None
    """Feature invocation id"""

    billing_group_id: Optional[str] = None
    """Billing Group id"""

    billing_group_name: Optional[str] = None
    """Name of the Billing Group specified in billing_group_id"""

    call_leg_id: Optional[str] = None
    """Telnyx UUID that identifies the related call leg"""

    call_session_id: Optional[str] = None
    """Telnyx UUID that identifies the related call session"""

    connection_id: Optional[str] = None
    """Connection id"""

    connection_name: Optional[str] = None
    """Connection name"""

    cost: Optional[str] = None
    """Currency amount for Telnyx billing cost"""

    currency: Optional[str] = None
    """
    Telnyx account currency used to describe monetary values, including billing cost
    """

    feature: Optional[Literal["PREMIUM"]] = None
    """Feature name"""

    invoked_at: Optional[datetime] = None
    """Feature invocation time"""

    is_telnyx_billable: Optional[bool] = None
    """Indicates whether Telnyx billing charges might be applicable"""

    rate: Optional[str] = None
    """Currency amount per billing unit used to calculate the Telnyx billing cost"""

    rate_measured_in: Optional[str] = None
    """Billing unit used to calculate the Telnyx billing cost"""

    tags: Optional[str] = None
    """User-provided tags"""


class DataVerifyDetailRecord(BaseModel):
    record_type: str

    id: Optional[str] = None
    """Unique ID of the verification"""

    created_at: Optional[datetime] = None

    currency: Optional[str] = None
    """
    Telnyx account currency used to describe monetary values, including billing
    costs
    """

    delivery_status: Optional[str] = None

    destination_phone_number: Optional[str] = None
    """E.164 formatted phone number"""

    rate: Optional[str] = None
    """Currency amount per billing unit used to calculate the Telnyx billing costs"""

    rate_measured_in: Optional[str] = None
    """Billing unit used to calculate the Telnyx billing costs"""

    updated_at: Optional[datetime] = None

    verification_status: Optional[str] = None

    verify_channel_id: Optional[str] = None

    verify_channel_type: Optional[Literal["sms", "psd2", "call", "flashcall"]] = None
    """
    Depending on the type of verification, the `verify_channel_id` points to one of
    the following channel ids;

    ---

    | verify_channel_type | verify_channel_id |
    | ------------------- | ----------------- |
    | sms, psd2           | messaging_id      |
    | call, flashcall     | call_control_id   |

    ---
    """

    verify_profile_id: Optional[str] = None

    verify_usage_fee: Optional[str] = None
    """Currency amount for Verify Usage Fee"""


class DataSimCardUsageDetailRecord(BaseModel):
    record_type: str

    id: Optional[str] = None
    """Unique identifier for this SIM Card Usage"""

    closed_at: Optional[datetime] = None
    """Event close time"""

    created_at: Optional[datetime] = None
    """Event creation time"""

    currency: Optional[str] = None
    """
    Telnyx account currency used to describe monetary values, including billing cost
    """

    data_cost: Optional[float] = None
    """Data cost"""

    data_rate: Optional[str] = None
    """Currency amount per billing unit used to calculate the Telnyx billing cost"""

    data_unit: Optional[str] = None
    """Unit of wireless link consumption"""

    downlink_data: Optional[float] = None
    """Number of megabytes downloaded"""

    imsi: Optional[str] = None
    """International Mobile Subscriber Identity"""

    ip_address: Optional[str] = None
    """Ip address that generated the event"""

    mcc: Optional[str] = None
    """Mobile country code"""

    mnc: Optional[str] = None
    """Mobile network code"""

    phone_number: Optional[str] = None
    """Telephone number associated to SIM card"""

    sim_card_id: Optional[str] = None
    """Unique identifier for SIM card"""

    sim_card_tags: Optional[str] = None
    """User-provided tags"""

    sim_group_id: Optional[str] = None
    """Unique identifier for SIM group"""

    sim_group_name: Optional[str] = None
    """Sim group name for sim card"""

    uplink_data: Optional[float] = None
    """Number of megabytes uploaded"""


class DataMediaStorageDetailRecord(BaseModel):
    record_type: str

    id: Optional[str] = None
    """Unique identifier for the Media Storage Event"""

    action_type: Optional[str] = None
    """Type of action performed against the Media Storage API"""

    asset_id: Optional[str] = None
    """Asset id"""

    cost: Optional[str] = None
    """Currency amount for Telnyx billing cost"""

    created_at: Optional[datetime] = None
    """Event creation time"""

    currency: Optional[str] = None
    """
    Telnyx account currency used to describe monetary values, including billing cost
    """

    link_channel_id: Optional[str] = None
    """Link channel id"""

    link_channel_type: Optional[str] = None
    """Link channel type"""

    org_id: Optional[str] = None
    """Organization owner id"""

    rate: Optional[str] = None
    """Currency amount per billing unit used to calculate the Telnyx billing cost"""

    rate_measured_in: Optional[str] = None
    """Billing unit used to calculate the Telnyx billing cost"""

    status: Optional[str] = None
    """Request status"""

    user_id: Optional[str] = None
    """User id"""

    webhook_id: Optional[str] = None
    """Webhook id"""


Data: TypeAlias = Annotated[
    Union[
        DataMessageDetailRecord,
        DataConferenceDetailRecord,
        DataConferenceParticipantDetailRecord,
        DataAmdDetailRecord,
        DataVerifyDetailRecord,
        DataSimCardUsageDetailRecord,
        DataMediaStorageDetailRecord,
    ],
    PropertyInfo(discriminator="record_type"),
]


class Meta(BaseModel):
    page_number: Optional[int] = None

    page_size: Optional[int] = None

    total_pages: Optional[int] = None

    total_results: Optional[int] = None


class DetailRecordListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[Meta] = None
