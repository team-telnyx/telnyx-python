# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .porting_order_misc_param import PortingOrderMiscParam
from .porting_order_end_user_param import PortingOrderEndUserParam
from .porting_order_documents_param import PortingOrderDocumentsParam
from .porting_order_user_feedback_param import PortingOrderUserFeedbackParam
from .porting_order_phone_number_configuration_param import PortingOrderPhoneNumberConfigurationParam

__all__ = ["PortingOrderUpdateParams", "ActivationSettings", "Messaging", "Requirement"]


class PortingOrderUpdateParams(TypedDict, total=False):
    activation_settings: ActivationSettings

    customer_reference: str

    documents: PortingOrderDocumentsParam
    """Can be specified directly or via the `requirement_group_id` parameter."""

    end_user: PortingOrderEndUserParam

    messaging: Messaging

    misc: PortingOrderMiscParam

    phone_number_configuration: PortingOrderPhoneNumberConfigurationParam

    requirement_group_id: str
    """
    If present, we will read the current values from the specified Requirement Group
    into the Documents and Requirements for this Porting Order. Note that any future
    changes in the Requirement Group would have no impact on this Porting Order. We
    will return an error if a specified Requirement Group conflicts with documents
    or requirements in the same request.
    """

    requirements: Iterable[Requirement]
    """List of requirements for porting numbers."""

    user_feedback: PortingOrderUserFeedbackParam

    webhook_url: str


class ActivationSettings(TypedDict, total=False):
    foc_datetime_requested: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """ISO 8601 formatted Date/Time requested for the FOC date"""


class Messaging(TypedDict, total=False):
    enable_messaging: bool
    """
    Indicates whether Telnyx will port messaging capabilities from the losing
    carrier. If false, any messaging capabilities will stay with their current
    provider.
    """


class Requirement(TypedDict, total=False):
    field_value: Required[str]
    """
    identifies the document or provides the text value that satisfies this
    requirement
    """

    requirement_type_id: Required[str]
    """Identifies the requirement type that the `field_value` fulfills"""
