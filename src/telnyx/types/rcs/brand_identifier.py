# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from .ein_brand_identifier import EinBrandIdentifier
from .stock_symbol_brand_identifier import StockSymbolBrandIdentifier

__all__ = ["BrandIdentifier"]

BrandIdentifier: TypeAlias = Annotated[
    Union[EinBrandIdentifier, StockSymbolBrandIdentifier], PropertyInfo(discriminator="identifier_type")
]
