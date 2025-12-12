# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BrandTriggerSMSOtpResponse"]


class BrandTriggerSMSOtpResponse(BaseModel):
    """Response after successfully triggering a Brand SMS OTP"""

    brand_id: str = FieldInfo(alias="brandId")
    """The Brand ID for which the OTP was triggered"""

    reference_id: str = FieldInfo(alias="referenceId")
    """The reference ID that can be used to check OTP status"""
