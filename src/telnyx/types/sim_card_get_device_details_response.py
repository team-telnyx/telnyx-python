# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SimCardGetDeviceDetailsResponse", "Data"]


class Data(BaseModel):
    brand_name: Optional[str] = None
    """Brand of the device where the SIM card is being used in."""

    device_type: Optional[str] = None
    """Type of the device where the SIM card is being used in."""

    imei: Optional[str] = None
    """IMEI of the device where the SIM card is being used in."""

    api_model_name: Optional[str] = FieldInfo(alias="model_name", default=None)
    """Brand of the device where the SIM card is being used in."""

    operating_system: Optional[str] = None
    """Operating system of the device where the SIM card is being used in."""

    record_type: Optional[str] = None


class SimCardGetDeviceDetailsResponse(BaseModel):
    data: Optional[Data] = None
