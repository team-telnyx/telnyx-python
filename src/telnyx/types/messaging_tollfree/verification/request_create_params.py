# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .volume import Volume
from ...._utils import PropertyInfo
from .url_param import URLParam
from .use_case_categories import UseCaseCategories
from .tf_phone_number_param import TfPhoneNumberParam
from .toll_free_verification_entity_type import TollFreeVerificationEntityType

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

    age_gated_content: Annotated[bool, PropertyInfo(alias="ageGatedContent")]
    """Indicates if messaging content requires age gating (e.g., 18+).

    Defaults to false if not provided.
    """

    business_addr2: Annotated[str, PropertyInfo(alias="businessAddr2")]
    """Line 2 of the business address"""

    business_registration_country: Annotated[Optional[str], PropertyInfo(alias="businessRegistrationCountry")]
    """ISO 3166-1 alpha-2 country code of the issuing business authority.

    Must be exactly 2 letters. Automatically converted to uppercase. Required from
    January 2026.
    """

    business_registration_number: Annotated[Optional[str], PropertyInfo(alias="businessRegistrationNumber")]
    """
    Official business registration number (e.g., Employer Identification Number
    (EIN) in the U.S.). Required from January 2026.
    """

    business_registration_type: Annotated[Optional[str], PropertyInfo(alias="businessRegistrationType")]
    """Type of business registration being provided. Required from January 2026."""

    campaign_verify_authorization_token: Annotated[
        Optional[str], PropertyInfo(alias="campaignVerifyAuthorizationToken")
    ]
    """
    Campaign Verify Authorization Token required for Political use case submissions
    starting February 17, 2026. This token is validated by Zipwhip and must be
    provided for all Political use case verifications after the deadline.
    """

    doing_business_as: Annotated[Optional[str], PropertyInfo(alias="doingBusinessAs")]
    """Doing Business As (DBA) name if different from legal name"""

    entity_type: Annotated[Optional[TollFreeVerificationEntityType], PropertyInfo(alias="entityType")]
    """Business entity classification"""

    help_message_response: Annotated[Optional[str], PropertyInfo(alias="helpMessageResponse")]
    """The message returned when users text 'HELP'"""

    opt_in_confirmation_response: Annotated[Optional[str], PropertyInfo(alias="optInConfirmationResponse")]
    """Message sent to users confirming their opt-in to receive messages"""

    opt_in_keywords: Annotated[Optional[str], PropertyInfo(alias="optInKeywords")]
    """Keywords used to collect and process consumer opt-ins"""

    privacy_policy_url: Annotated[Optional[str], PropertyInfo(alias="privacyPolicyURL")]
    """URL pointing to the business's privacy policy.

    Plain string, no URL format validation.
    """

    terms_and_condition_url: Annotated[Optional[str], PropertyInfo(alias="termsAndConditionURL")]
    """URL pointing to the business's terms and conditions.

    Plain string, no URL format validation.
    """

    webhook_url: Annotated[str, PropertyInfo(alias="webhookUrl")]
    """URL that should receive webhooks relating to this verification request"""
