# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["MessagingProfileRetrieveMetricsResponse"]


class MessagingProfileRetrieveMetricsResponse(BaseModel):
    data: Optional[Dict[str, object]] = None
    """Detailed metrics for a messaging profile."""
