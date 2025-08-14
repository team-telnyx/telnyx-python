# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["ClientPutObjectParams"]


class ClientPutObjectParams(TypedDict, total=False):
    bucket_name: Required[Annotated[str, PropertyInfo(alias="bucketName")]]

    body: Required[FileTypes]

    part_number: Annotated[str, PropertyInfo(alias="partNumber")]

    upload_id: Annotated[str, PropertyInfo(alias="uploadId")]
