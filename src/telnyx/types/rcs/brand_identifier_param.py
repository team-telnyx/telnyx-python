# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .ein_brand_identifier_param import EinBrandIdentifierParam
from .stock_symbol_brand_identifier_param import StockSymbolBrandIdentifierParam

__all__ = ["BrandIdentifierParam"]

BrandIdentifierParam: TypeAlias = Union[EinBrandIdentifierParam, StockSymbolBrandIdentifierParam]
