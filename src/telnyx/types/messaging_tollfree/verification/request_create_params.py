# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .volume import Volume
from ...._utils import PropertyInfo
from .url_param import URLParam
from .use_case_categories import UseCaseCategories
from .tf_phone_number_param import TfPhoneNumberParam

__all__ = ["RequestCreateParams"]


class RequestCreateParams(TypedDict, total=False):
    additional_information: Required[Annotated[str, PropertyInfo(alias="additionalInformation")]]
    """Any additional information"""

    business_addr1: Required[Annotated[str, PropertyInfo(alias="businessAddr1")]]
    """Line 1 of the business address"""

    business_city: Required[Annotated[str, PropertyInfo(alias="businessCity")]]
    """The city of the business address; the first letter should be capitalized"""

    business_contact_email: Required[Annotated[str, PropertyInfo(alias="businessContactEmail")]]
    """The email address of the business contact"""

    business_contact_first_name: Required[Annotated[str, PropertyInfo(alias="businessContactFirstName")]]
    """
    First name of the business contact; there are no specific requirements on
    formatting
    """

    business_contact_last_name: Required[Annotated[str, PropertyInfo(alias="businessContactLastName")]]
    """
    Last name of the business contact; there are no specific requirements on
    formatting
    """

    business_contact_phone: Required[Annotated[str, PropertyInfo(alias="businessContactPhone")]]
    """The phone number of the business contact in E.164 format"""

    business_name: Required[Annotated[str, PropertyInfo(alias="businessName")]]
    """Name of the business; there are no specific formatting requirements"""

    business_state: Required[Annotated[str, PropertyInfo(alias="businessState")]]
    """
    The full name of the state (not the 2 letter code) of the business address; the
    first letter should be capitalized
    """

    business_zip: Required[Annotated[str, PropertyInfo(alias="businessZip")]]
    """The ZIP code of the business address"""

    corporate_website: Required[Annotated[str, PropertyInfo(alias="corporateWebsite")]]
    """A URL, including the scheme, pointing to the corporate website"""

    isv_reseller: Required[Annotated[str, PropertyInfo(alias="isvReseller")]]
    """ISV name"""

    message_volume: Required[Annotated[Volume, PropertyInfo(alias="messageVolume")]]
    """Message Volume Enums"""

    opt_in_workflow: Required[Annotated[str, PropertyInfo(alias="optInWorkflow")]]
    """
    Human-readable description of how end users will opt into receiving messages
    from the given phone numbers
    """

    opt_in_workflow_image_urls: Required[Annotated[Iterable[URLParam], PropertyInfo(alias="optInWorkflowImageURLs")]]
    """Images showing the opt-in workflow"""

    phone_numbers: Required[Annotated[Iterable[TfPhoneNumberParam], PropertyInfo(alias="phoneNumbers")]]
    """The phone numbers to request the verification of"""

    production_message_content: Required[Annotated[str, PropertyInfo(alias="productionMessageContent")]]
    """An example of a message that will be sent from the given phone numbers"""

    use_case: Required[Annotated[UseCaseCategories, PropertyInfo(alias="useCase")]]
    """Tollfree usecase categories"""

    use_case_summary: Required[Annotated[str, PropertyInfo(alias="useCaseSummary")]]
    """Human-readable summary of the desired use-case"""

    business_addr2: Annotated[str, PropertyInfo(alias="businessAddr2")]
    """Line 2 of the business address"""

    webhook_url: Annotated[str, PropertyInfo(alias="webhookUrl")]
    """URL that should receive webhooks relating to this verification request"""
