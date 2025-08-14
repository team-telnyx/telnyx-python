# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .url import URL
from .volume import Volume
from ...._models import BaseModel
from .tf_phone_number import TfPhoneNumber
from .use_case_categories import UseCaseCategories
from .tf_verification_status import TfVerificationStatus

__all__ = ["VerificationRequestStatus"]


class VerificationRequestStatus(BaseModel):
    id: str

    additional_information: str = FieldInfo(alias="additionalInformation")

    business_addr1: str = FieldInfo(alias="businessAddr1")

    business_city: str = FieldInfo(alias="businessCity")

    business_contact_email: str = FieldInfo(alias="businessContactEmail")

    business_contact_first_name: str = FieldInfo(alias="businessContactFirstName")

    business_contact_last_name: str = FieldInfo(alias="businessContactLastName")

    business_contact_phone: str = FieldInfo(alias="businessContactPhone")

    business_name: str = FieldInfo(alias="businessName")

    business_state: str = FieldInfo(alias="businessState")

    business_zip: str = FieldInfo(alias="businessZip")

    corporate_website: str = FieldInfo(alias="corporateWebsite")

    isv_reseller: str = FieldInfo(alias="isvReseller")

    message_volume: Volume = FieldInfo(alias="messageVolume")
    """Message Volume Enums"""

    opt_in_workflow: str = FieldInfo(alias="optInWorkflow")

    opt_in_workflow_image_urls: List[URL] = FieldInfo(alias="optInWorkflowImageURLs")

    phone_numbers: List[TfPhoneNumber] = FieldInfo(alias="phoneNumbers")

    production_message_content: str = FieldInfo(alias="productionMessageContent")

    use_case: UseCaseCategories = FieldInfo(alias="useCase")
    """Tollfree usecase categories"""

    use_case_summary: str = FieldInfo(alias="useCaseSummary")

    verification_status: TfVerificationStatus = FieldInfo(alias="verificationStatus")
    """Tollfree verification status"""

    business_addr2: Optional[str] = FieldInfo(alias="businessAddr2", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    reason: Optional[str] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    webhook_url: Optional[str] = FieldInfo(alias="webhookUrl", default=None)
