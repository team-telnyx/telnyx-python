# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .verified_number import VerifiedNumber
from .ai.assistants.tests.test_suites.meta import Meta

__all__ = ["VerifiedNumberListResponse"]


class VerifiedNumberListResponse(BaseModel):
    data: List[VerifiedNumber]

    meta: Meta
