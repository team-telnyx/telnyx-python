# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._models import BaseModel
from .remediation_request import RemediationRequest

__all__ = ["RemediationRequestWrapped"]


class RemediationRequestWrapped(BaseModel):
    data: RemediationRequest
    """Full detail of a remediation request, returned on submit and GET by id."""
