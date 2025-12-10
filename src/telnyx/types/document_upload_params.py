# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._types import Base64FileInput
from .._utils import PropertyInfo

__all__ = ["DocumentUploadParams", "DocServiceDocumentUploadURL", "DocServiceDocumentUploadInline"]


class DocServiceDocumentUploadURL(TypedDict, total=False):
    url: Required[str]
    """
    If the file is already hosted publicly, you can provide a URL and have the
    documents service fetch it for you.
    """

    customer_reference: str
    """Optional reference string for customer tracking."""

    filename: str
    """The filename of the document."""


class DocServiceDocumentUploadInline(TypedDict, total=False):
    file: Required[Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]]
    """The Base64 encoded contents of the file you are uploading."""

    customer_reference: str
    """A customer reference string for customer look ups."""

    filename: str
    """The filename of the document."""


DocumentUploadParams: TypeAlias = Union[DocServiceDocumentUploadURL, DocServiceDocumentUploadInline]
