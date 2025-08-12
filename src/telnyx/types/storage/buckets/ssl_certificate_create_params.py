# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ...._types import FileTypes

__all__ = ["SslCertificateCreateParams"]


class SslCertificateCreateParams(TypedDict, total=False):
    certificate: FileTypes
    """The SSL certificate file"""

    private_key: FileTypes
    """The private key file"""
