# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .sim_card_group import SimCardGroup

__all__ = ["SimCardGroupRetrieveResponse"]


class SimCardGroupRetrieveResponse(BaseModel):
    data: Optional[SimCardGroup] = None
