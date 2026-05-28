# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["VoiceSDKCallReportLogEntry"]


class VoiceSDKCallReportLogEntry(BaseModel):
    """A raw Voice SDK log entry. Additional SDK-specific fields may be present."""

    context: Optional[Dict[str, object]] = None
    """Raw structured context attached to the log entry."""

    level: Optional[Literal["debug", "info", "warn", "error"]] = None
    """Log level emitted by the SDK."""

    message: Optional[str] = None
    """Log message."""

    timestamp: Optional[datetime] = None
    """Time when the log entry was emitted."""

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
