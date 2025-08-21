# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["JobCreateParams", "Hyperparameters"]


class JobCreateParams(TypedDict, total=False):
    model: Required[str]
    """The base model that is being fine-tuned."""

    training_file: Required[str]
    """The storage bucket or object used for training."""

    hyperparameters: Hyperparameters
    """The hyperparameters used for the fine-tuning job."""

    suffix: str
    """Optional suffix to append to the fine tuned model's name."""


class Hyperparameters(TypedDict, total=False):
    n_epochs: int
    """The number of epochs to train the model for.

    An epoch refers to one full cycle through the training dataset. 'auto' decides
    the optimal number of epochs based on the size of the dataset. If setting the
    number manually, we support any number between 1 and 50 epochs.
    """
