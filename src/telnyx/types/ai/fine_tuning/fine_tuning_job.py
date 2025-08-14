# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["FineTuningJob", "Hyperparameters"]


class Hyperparameters(BaseModel):
    n_epochs: int
    """The number of epochs to train the model for.

    An epoch refers to one full cycle through the training dataset.
    """


class FineTuningJob(BaseModel):
    id: str
    """The name of the fine-tuned model that is being created."""

    created_at: int
    """The Unix timestamp (in seconds) for when the fine-tuning job was created."""

    finished_at: Optional[int] = None
    """The Unix timestamp (in seconds) for when the fine-tuning job was finished.

    The value will be null if the fine-tuning job is still running.
    """

    hyperparameters: Hyperparameters
    """The hyperparameters used for the fine-tuning job."""

    model: str
    """The base model that is being fine-tuned."""

    organization_id: str
    """The organization that owns the fine-tuning job."""

    status: Literal["queued", "running", "succeeded", "failed", "cancelled"]
    """The current status of the fine-tuning job."""

    trained_tokens: Optional[int] = None
    """The total number of billable tokens processed by this fine-tuning job.

    The value will be null if the fine-tuning job is still running.
    """

    training_file: str
    """The storage bucket or object used for training."""
