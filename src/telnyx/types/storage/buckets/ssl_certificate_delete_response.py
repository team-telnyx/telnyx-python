# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from .ssl_certificate import SslCertificate

__all__ = ["SslCertificateDeleteResponse"]


class SslCertificateDeleteResponse(BaseModel):
    data: Optional[SslCertificate] = None
