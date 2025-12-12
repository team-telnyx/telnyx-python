# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Messaging10dlcGetEnumResponse", "EnumPaginatedResponse"]


class EnumPaginatedResponse(BaseModel):
    page: int

    records: List[Dict[str, object]]

    total_records: int = FieldInfo(alias="totalRecords")


Messaging10dlcGetEnumResponse: TypeAlias = Union[
    List[str], List[Dict[str, object]], Dict[str, object], Dict[str, object], EnumPaginatedResponse
]
