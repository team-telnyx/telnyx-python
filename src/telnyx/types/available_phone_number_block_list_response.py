# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.feature import Feature
from .shared.cost_information import CostInformation
from .shared.region_information import RegionInformation
from .shared.available_phone_numbers_metadata import AvailablePhoneNumbersMetadata

__all__ = ["AvailablePhoneNumberBlockListResponse", "Data"]


class Data(BaseModel):
    cost_information: Optional[CostInformation] = None

    features: Optional[List[Feature]] = None

    phone_number: Optional[str] = None

    range: Optional[int] = None

    record_type: Optional[Literal["available_phone_number_block"]] = None

    region_information: Optional[List[RegionInformation]] = None


class AvailablePhoneNumberBlockListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[AvailablePhoneNumbersMetadata] = None
