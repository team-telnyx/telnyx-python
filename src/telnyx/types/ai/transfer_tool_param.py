# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .inference_embedding_transfer_tool_params_param import InferenceEmbeddingTransferToolParamsParam

__all__ = ["TransferToolParam"]


class TransferToolParam(TypedDict, total=False):
    transfer: Required[InferenceEmbeddingTransferToolParamsParam]

    type: Required[Literal["transfer"]]
