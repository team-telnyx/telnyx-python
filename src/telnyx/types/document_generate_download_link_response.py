# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["DocumentGenerateDownloadLinkResponse", "Data"]


class Data(BaseModel):
    url: str
    """Pre-signed temporary URL for downloading the document"""


class DocumentGenerateDownloadLinkResponse(BaseModel):
    data: Data
