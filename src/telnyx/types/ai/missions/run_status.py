# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["RunStatus"]

RunStatus: TypeAlias = Literal["pending", "running", "paused", "succeeded", "failed", "cancelled"]
