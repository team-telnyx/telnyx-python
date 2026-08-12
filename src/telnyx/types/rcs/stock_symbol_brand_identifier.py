# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["StockSymbolBrandIdentifier"]


class StockSymbolBrandIdentifier(BaseModel):
    identifier_type: Literal["STOCK_SYMBOL"]

    value: str
    """A stock symbol using EXCHANGE:SYMBOL."""
