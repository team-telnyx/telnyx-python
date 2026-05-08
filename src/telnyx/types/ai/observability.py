# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Observability"]


class Observability(BaseModel):
    host: Optional[str] = None

    prompt_label: Optional[str] = None

    prompt_name: Optional[str] = None

    prompt_sync: Optional[Literal["enabled", "disabled"]] = None
    """Whether to auto-publish the assistant's instructions as a Langfuse prompt.

    When ENABLED + prompt_name set, every assistant create/update pushes
    `instructions` to Langfuse via create_prompt and stores the returned version in
    prompt_version.
    """

    prompt_version: Optional[int] = None

    public_key_ref: Optional[str] = None

    secret_key_ref: Optional[str] = None

    status: Optional[Literal["enabled", "disabled"]] = None
