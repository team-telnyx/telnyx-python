# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UploadPendingCountResponse", "Data"]


class Data(BaseModel):
    pending_numbers_count: Optional[int] = None
    """
    The count of phone numbers that are pending assignment to the external
    connection.
    """

    pending_orders_count: Optional[int] = None
    """The count of number uploads that have not yet been uploaded to Microsoft."""


class UploadPendingCountResponse(BaseModel):
    data: Optional[Data] = None
