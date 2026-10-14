# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ProfilePreviewParams"]


class ProfilePreviewParams(TypedDict, total=False):
    namespace: Required[str]
    """The namespace. `default` exists for every organization."""

    instructions: Optional[str]
    """The candidate note to try.

    `null`, empty, or whitespace-only previews the neutral default -- the summary a
    profile returns to when instructions are cleared. Capped at 2000 characters, the
    same cap `PATCH /settings` applies on save; a longer note is refused with `422`
    before anything is generated.
    """
