# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .brand_address import BrandAddress
from .brand_contact import BrandContact
from .brand_identifier import BrandIdentifier
from .capabilities_response import CapabilitiesResponse

__all__ = ["BrandResponse"]


class BrandResponse(BaseModel):
    addresses: Dict[str, BrandAddress]

    brand_id: str

    capabilities: CapabilitiesResponse

    contacts: Dict[str, BrandContact]

    display_name: str

    identifiers: Dict[str, BrandIdentifier]

    legal_entity_type: str

    legal_name: str

    organization_type: str

    profile_id: Optional[str] = None

    status: Literal["CREATED", "CONFIGURED", "SUBMITTED", "REVIEWING", "VETTING", "VERIFIED", "REJECTED", "FAILED"]

    website_url: str
