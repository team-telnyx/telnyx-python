# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["NumberLookupRetrieveParams"]


class NumberLookupRetrieveParams(TypedDict, total=False):
    type: Literal["carrier", "caller-name", "caller-identity", "enhanced-caller-name"]
    """Specifies the type of number lookup to be performed.

    May be supplied more than once to request several data sources in a single call
    (for example, `?type=carrier&type=enhanced-caller-name`). Each requested type
    populates the corresponding object in the response.
    """
