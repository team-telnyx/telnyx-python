# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PortingOrderRetrieveSubRequestResponse", "Data"]


class Data(BaseModel):
    port_request_id: Optional[str] = None
    """Identifies the Port Request associated with the Porting Order"""

    sub_request_id: Optional[str] = None
    """Identifies the Sub Request associated with the Porting Order"""


class PortingOrderRetrieveSubRequestResponse(BaseModel):
    data: Optional[Data] = None
