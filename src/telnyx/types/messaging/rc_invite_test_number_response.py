# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RcInviteTestNumberResponse", "Data"]


class Data(BaseModel):
    agent_id: Optional[str] = None
    """RCS agent ID"""

    phone_number: Optional[str] = None
    """Phone number that was invited for testing"""

    record_type: Optional[Literal["rcs.test_number_invite"]] = None
    """Identifies the type of the resource"""

    status: Optional[str] = None
    """Status of the test number invitation"""


class RcInviteTestNumberResponse(BaseModel):
    data: Data
