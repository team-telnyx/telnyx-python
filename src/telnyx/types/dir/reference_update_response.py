# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .reference import Reference

__all__ = ["ReferenceUpdateResponse"]


class ReferenceUpdateResponse(BaseModel):
    data: Reference
    """A reference (business or financial) on a DIR, in the customer-facing shape.

    No internal identifiers are exposed.
    """
