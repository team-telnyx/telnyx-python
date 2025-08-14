# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["RcGenerateDeeplinkResponse", "Data"]


class Data(BaseModel):
    url: str
    """The generated deeplink URL"""


class RcGenerateDeeplinkResponse(BaseModel):
    data: Data
