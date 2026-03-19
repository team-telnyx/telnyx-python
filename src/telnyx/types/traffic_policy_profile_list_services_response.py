# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["TrafficPolicyProfileListServicesResponse"]


class TrafficPolicyProfileListServicesResponse(BaseModel):
    id: Optional[str] = None
    """The service identifier."""

    group: Optional[str] = None
    """The group the service belongs to."""

    name: Optional[str] = None
    """The name of the service."""

    resource_type: Optional[str] = None
