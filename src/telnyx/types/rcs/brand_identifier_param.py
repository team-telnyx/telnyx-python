# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, ForwardRef
from typing_extensions import TypeAlias

__all__ = ["BrandIdentifierParam"]

if TYPE_CHECKING:
    BrandIdentifierParam: TypeAlias = Union["EinBrandIdentifierParam", "StockSymbolBrandIdentifierParam"]
else:
    BrandIdentifierParam = Union[
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).EinBrandIdentifierParam"),
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).StockSymbolBrandIdentifierParam"),
    ]

from .ein_brand_identifier_param import EinBrandIdentifierParam
from .stock_symbol_brand_identifier_param import StockSymbolBrandIdentifierParam
