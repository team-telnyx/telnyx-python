# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["TaskStatus"]

TaskStatus: TypeAlias = Literal["pending", "starting", "running", "completed", "failed"]
