# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ClientGetObjectParams"]


class ClientGetObjectParams(TypedDict, total=False):
    bucket_name: Required[Annotated[str, PropertyInfo(alias="bucketName")]]

    upload_id: Annotated[str, PropertyInfo(alias="uploadId")]
