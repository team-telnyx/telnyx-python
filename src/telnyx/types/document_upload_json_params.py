# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypedDict

from .._types import Base64FileInput
from .._utils import PropertyInfo
from .._models import set_pydantic_config

__all__ = ["DocumentUploadJsonParams", "Document"]


class DocumentUploadJsonParams(TypedDict, total=False):
    document: Required[Document]


class Document(TypedDict, total=False):
    customer_reference: str
    """A customer reference string for customer look ups."""

    file: Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]
    """
    Alternatively, instead of the URL you can provide the Base64 encoded contents of
    the file you are uploading.
    """

    filename: str
    """The filename of the document."""

    url: str
    """
    If the file is already hosted publicly, you can provide a URL and have the
    documents service fetch it for you.
    """


set_pydantic_config(Document, {"arbitrary_types_allowed": True})
