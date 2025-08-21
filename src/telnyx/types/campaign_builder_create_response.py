# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .telnyx_campaign_csp import TelnyxCampaignCsp

__all__ = ["CampaignBuilderCreateResponse"]

CampaignBuilderCreateResponse: TypeAlias = Union[TelnyxCampaignCsp, object]
