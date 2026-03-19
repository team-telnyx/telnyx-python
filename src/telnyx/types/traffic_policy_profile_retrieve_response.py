# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .traffic_policy_profile import TrafficPolicyProfile

__all__ = ["TrafficPolicyProfileRetrieveResponse"]


class TrafficPolicyProfileRetrieveResponse(BaseModel):
    data: Optional[TrafficPolicyProfile] = None
