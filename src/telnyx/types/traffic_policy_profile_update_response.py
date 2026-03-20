# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .traffic_policy_profile import TrafficPolicyProfile

__all__ = ["TrafficPolicyProfileUpdateResponse"]


class TrafficPolicyProfileUpdateResponse(BaseModel):
    data: Optional[TrafficPolicyProfile] = None
