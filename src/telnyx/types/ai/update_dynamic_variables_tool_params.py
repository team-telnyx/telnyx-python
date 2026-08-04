# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["UpdateDynamicVariablesToolParams", "UpdatableVariable"]


class UpdatableVariable(BaseModel):
    name: str
    """The dynamic-variable key to update.

    Must match `^[a-zA-Z0-9._-]+$` and may not start with the reserved `telnyx_`
    prefix (reserved for system variables). The `pattern` encodes both rules via a
    negative lookahead.
    """

    description: Optional[str] = None
    """
    Optional description of the variable, guiding the assistant on what value to
    capture.
    """

    type: Optional[str] = None
    """Optional hint for the variable's value type (e.g. `string`)."""


class UpdateDynamicVariablesToolParams(BaseModel):
    """Configuration for an update_dynamic_variables tool."""

    description: str
    """
    Description of the tool passed to the assistant, guiding when to call it and
    which variables to update.
    """

    name: str
    """The function name surfaced to the LLM.

    Must match the OpenAI function-name pattern `^[a-zA-Z0-9_-]+$` and be unique
    across the assistant's function, webhook, and client_side tools.
    """

    updatable_variables: List[UpdatableVariable]
    """The dynamic variables the assistant is allowed to write.

    At least one is required.
    """
