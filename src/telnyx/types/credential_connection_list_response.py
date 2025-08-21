# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .credential_connection import CredentialConnection
from .shared.connections_pagination_meta import ConnectionsPaginationMeta

__all__ = ["CredentialConnectionListResponse"]


class CredentialConnectionListResponse(BaseModel):
    data: Optional[List[CredentialConnection]] = None

    meta: Optional[ConnectionsPaginationMeta] = None
