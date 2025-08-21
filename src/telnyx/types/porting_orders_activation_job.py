# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PortingOrdersActivationJob", "ActivationWindow"]


class ActivationWindow(BaseModel):
    end_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the activation window ends"""

    start_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the activation window starts"""


class PortingOrdersActivationJob(BaseModel):
    id: Optional[str] = None
    """Uniquely identifies this activation job"""

    activate_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the activation job should be executed.

    This time should be between some activation window.
    """

    activation_type: Optional[Literal["scheduled", "on-demand"]] = None
    """Specifies the type of this activation job"""

    activation_windows: Optional[List[ActivationWindow]] = None
    """List of allowed activation windows for this activation job"""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    record_type: Optional[str] = None
    """Identifies the type of the resource."""

    status: Optional[Literal["created", "in-process", "completed", "failed"]] = None
    """Specifies the status of this activation job"""

    updated_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""
