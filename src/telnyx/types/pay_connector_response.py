# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .pay_connector import PayConnector

__all__ = ["PayConnectorResponse"]


class PayConnectorResponse(BaseModel):
    data: Optional[PayConnector] = None
    """Organization-owned connector.

    Examples and config properties here describe generic connectors; listing is not
    restricted to that type unless filter[type]=generic is supplied. Passwords and
    bearer tokens are omitted, not masked. Defaults for auth_type and timeout need
    not appear in stored config.
    """
