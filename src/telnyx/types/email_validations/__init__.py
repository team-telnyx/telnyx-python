# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .batch_create_params import BatchCreateParams as BatchCreateParams
from .email_validation_batch_status import EmailValidationBatchStatus as EmailValidationBatchStatus

if TYPE_CHECKING:
    from .batch_create_response import BatchCreateResponse as BatchCreateResponse
    from .batch_retrieve_response import BatchRetrieveResponse as BatchRetrieveResponse


def __getattr__(name: str) -> Any:
    if name == "BatchCreateResponse":
        from .batch_create_response import BatchCreateResponse

        return BatchCreateResponse
    if name == "BatchRetrieveResponse":
        from .batch_retrieve_response import BatchRetrieveResponse

        return BatchRetrieveResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
