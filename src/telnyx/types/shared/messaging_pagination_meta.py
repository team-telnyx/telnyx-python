# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["MessagingPaginationMeta"]


class MessagingPaginationMeta(BaseModel):
    page_number: int

    page_size: int

    total_pages: int

    total_results: int
