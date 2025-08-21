# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .custom_storage_configuration import CustomStorageConfiguration

__all__ = ["CustomStorageCredentialUpdateResponse"]


class CustomStorageCredentialUpdateResponse(BaseModel):
    connection_id: str
    """
    Uniquely identifies a Telnyx application (Call Control, TeXML) or Sip connection
    resource.
    """

    data: CustomStorageConfiguration

    record_type: Literal["custom_storage_credentials"]
    """Identifies record type."""
