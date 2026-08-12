# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["StockSymbolBrandIdentifierParam"]


class StockSymbolBrandIdentifierParam(TypedDict, total=False):
    identifier_type: Required[Literal["STOCK_SYMBOL"]]

    value: Required[str]
    """A stock symbol using EXCHANGE:SYMBOL."""
