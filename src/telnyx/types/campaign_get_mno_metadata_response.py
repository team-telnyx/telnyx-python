# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CampaignGetMnoMetadataResponse", "_10999"]


class _10999(BaseModel):
    min_msg_samples: int = FieldInfo(alias="minMsgSamples")

    mno: str

    mno_review: bool = FieldInfo(alias="mnoReview")

    mno_support: bool = FieldInfo(alias="mnoSupport")

    no_embedded_link: bool = FieldInfo(alias="noEmbeddedLink")

    no_embedded_phone: bool = FieldInfo(alias="noEmbeddedPhone")

    qualify: bool

    req_subscriber_help: bool = FieldInfo(alias="reqSubscriberHelp")

    req_subscriber_optin: bool = FieldInfo(alias="reqSubscriberOptin")

    req_subscriber_optout: bool = FieldInfo(alias="reqSubscriberOptout")


class CampaignGetMnoMetadataResponse(BaseModel):
    api_10999: Optional[_10999] = FieldInfo(alias="10999", default=None)
