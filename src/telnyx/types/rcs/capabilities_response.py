# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel

__all__ = ["CapabilitiesResponse"]


class CapabilitiesResponse(BaseModel):
    brand_entity: bool

    brand_verification: bool

    campaigns: bool

    distinct_launch_phase: bool

    invite_test_devices: bool

    per_carrier_approval: bool

    submission_sections: bool

    templates: bool

    vendor_webhooks: bool
