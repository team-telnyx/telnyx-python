# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["WirelessBlocklistValueListResponse", "DataCountry", "DataMcc", "DataPlmn"]


class DataCountry(BaseModel):
    code: str
    """ISO 3166-1 Alpha-2 Country Code."""

    name: str
    """The name of the country."""


class DataMcc(BaseModel):
    code: str
    """Mobile Country Code."""

    name: str
    """The name of the country."""


class DataPlmn(BaseModel):
    code: str
    """Public land mobile network code (MCC + MNC)."""

    name: str
    """The name of the network."""


class WirelessBlocklistValueListResponse(BaseModel):
    data: Union[List[DataCountry], List[DataMcc], List[DataPlmn], None] = None

    meta: Optional[PaginationMeta] = None
