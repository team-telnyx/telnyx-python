# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union

from .._models import BaseModel

__all__ = ["WirelessBlocklistValueListResponse", "DataCountry", "DataMcc", "DataPlmn"]


class DataCountry(BaseModel):
    country_code: str
    """ISO 3166-1 Alpha-2 Country Code."""


class DataMcc(BaseModel):
    mcc: str
    """Mobile Country Code."""


class DataPlmn(BaseModel):
    plmn: str
    """Public land mobile network code (MCC + MNC)."""


class WirelessBlocklistValueListResponse(BaseModel):
    data: Union[List[DataCountry], List[DataMcc], List[DataPlmn]]
