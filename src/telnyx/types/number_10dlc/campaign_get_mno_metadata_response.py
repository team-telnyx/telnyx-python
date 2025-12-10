# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CampaignGetMnoMetadataResponse", "MnoMetadataItem10999"]


class MnoMetadataItem10999(BaseModel):
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
    mno_metadata_item_10999: Optional[MnoMetadataItem10999] = FieldInfo(alias="10999", default=None)

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]
