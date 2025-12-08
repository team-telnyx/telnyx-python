# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.api_error import APIError

__all__ = ["ActionValidateResponse", "Data", "DataSuggested"]


class DataSuggested(BaseModel):
    """Provides normalized address when available."""

    administrative_area: Optional[str] = None
    """The locality of the address.

    For US addresses, this corresponds to the state of the address.
    """

    country_code: Optional[str] = None
    """The two-character (ISO 3166-1 alpha-2) country code of the address."""

    extended_address: Optional[str] = None
    """
    Additional street address information about the address such as, but not limited
    to, unit number or apartment number.
    """

    locality: Optional[str] = None
    """The locality of the address.

    For US addresses, this corresponds to the city of the address.
    """

    postal_code: Optional[str] = None
    """The postal code of the address."""

    street_address: Optional[str] = None
    """The primary street address information about the address."""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class Data(BaseModel):
    result: Literal["valid", "invalid"]
    """Indicates whether an address is valid or invalid."""

    suggested: DataSuggested
    """Provides normalized address when available."""

    errors: Optional[List[APIError]] = None

    record_type: Optional[str] = None
    """Identifies the type of the resource."""


class ActionValidateResponse(BaseModel):
    data: Optional[Data] = None
