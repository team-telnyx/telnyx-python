# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..verification import Verification
from ..ai.assistants.tests.test_suites.meta import Meta

__all__ = ["ByPhoneNumberListResponse"]


class ByPhoneNumberListResponse(BaseModel):
    data: List[Verification]

    meta: Meta
