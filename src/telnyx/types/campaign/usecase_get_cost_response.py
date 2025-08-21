# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["UsecaseGetCostResponse"]


class UsecaseGetCostResponse(BaseModel):
    campaign_usecase: str = FieldInfo(alias="campaignUsecase")

    description: str

    monthly_cost: str = FieldInfo(alias="monthlyCost")

    up_front_cost: str = FieldInfo(alias="upFrontCost")
