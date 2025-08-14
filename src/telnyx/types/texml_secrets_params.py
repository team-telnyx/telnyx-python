# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TexmlSecretsParams"]


class TexmlSecretsParams(TypedDict, total=False):
    name: Required[str]
    """
    Name used as a reference for the secret, if the name already exists within the
    account its value will be replaced
    """

    value: Required[str]
    """Secret value which will be used when rendering the TeXML template"""
