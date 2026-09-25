# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["ProfileIngestParams", "Variant0", "Variant1"]


class Variant0(TypedDict, total=False):
    namespace: Required[str]

    body: Required[Dict[str, object]]

    session_id: Optional[str]
    """Names the session.

    Re-ingesting the same session replaces what it held and keeps its `source_id`.
    Omit it to have one derived from the content and returned. No whitespace,
    control characters, or any of / \\  # ? %.
    """


class Variant1(TypedDict, total=False):
    namespace: Required[str]

    body: Required[Union[Iterable[object], str, float, bool]]

    session_id: Optional[str]
    """Names the session.

    Re-ingesting the same session replaces what it held and keeps its `source_id`.
    Omit it to have one derived from the content and returned. No whitespace,
    control characters, or any of / \\  # ? %.
    """


ProfileIngestParams: TypeAlias = Union[Variant0, Variant1]
