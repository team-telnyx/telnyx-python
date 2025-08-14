# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .verify_profile import VerifyProfile
from .ai.assistants.tests.test_suites.meta import Meta

__all__ = ["VerifyProfileListResponse"]


class VerifyProfileListResponse(BaseModel):
    data: List[VerifyProfile]

    meta: Meta
