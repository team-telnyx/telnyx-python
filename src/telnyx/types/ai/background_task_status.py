# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["BackgroundTaskStatus"]

BackgroundTaskStatus: TypeAlias = Literal["queued", "processing", "success", "failure", "partial_success"]
