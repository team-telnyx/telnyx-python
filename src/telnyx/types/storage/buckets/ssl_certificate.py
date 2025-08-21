# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["SslCertificate", "IssuedBy", "IssuedTo"]


class IssuedBy(BaseModel):
    common_name: Optional[str] = None
    """The common name of the entity the certificate was issued by"""

    organization: Optional[str] = None
    """The organization the certificate was issued by"""

    organization_unit: Optional[str] = None
    """The organizational unit the certificate was issued by"""


class IssuedTo(BaseModel):
    common_name: Optional[str] = None
    """The common name of the entity the certificate was issued to"""

    organization: Optional[str] = None
    """The organization the certificate was issued to"""

    organization_unit: Optional[str] = None
    """The organizational unit the certificate was issued to"""


class SslCertificate(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the SSL certificate"""

    created_at: Optional[datetime] = None
    """Time when SSL certificate was uploaded"""

    issued_by: Optional[IssuedBy] = None

    issued_to: Optional[IssuedTo] = None

    valid_from: Optional[datetime] = None
    """The time the certificate is valid from"""

    valid_to: Optional[datetime] = None
    """The time the certificate is valid to"""
