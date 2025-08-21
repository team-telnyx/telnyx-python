# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BrandQualifyByUsecaseResponse"]


class BrandQualifyByUsecaseResponse(BaseModel):
    annual_fee: Optional[float] = FieldInfo(alias="annualFee", default=None)
    """Campaign annual subscription fee"""

    max_sub_usecases: Optional[int] = FieldInfo(alias="maxSubUsecases", default=None)
    """Maximum number of sub-usecases declaration required."""

    min_sub_usecases: Optional[int] = FieldInfo(alias="minSubUsecases", default=None)
    """Minimum number of sub-usecases declaration required."""

    mno_metadata: Optional[Dict[str, object]] = FieldInfo(alias="mnoMetadata", default=None)
    """Map of usecase metadata for each MNO.

    Key is the network ID of the MNO (e.g. 10017), Value is the mno metadata for the
    usecase.
    """

    monthly_fee: Optional[float] = FieldInfo(alias="monthlyFee", default=None)
    """Campaign monthly subscription fee"""

    quarterly_fee: Optional[float] = FieldInfo(alias="quarterlyFee", default=None)
    """Campaign quarterly subscription fee"""

    usecase: Optional[str] = None
    """Campaign usecase"""
