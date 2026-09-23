# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .function_definition_param import FunctionDefinitionParam as FunctionDefinitionParam
from .chat_create_completion_params import ChatCreateCompletionParams as ChatCreateCompletionParams
from .chat_create_completion_response import ChatCreateCompletionResponse as ChatCreateCompletionResponse
from .embedding_create_embeddings_params import EmbeddingCreateEmbeddingsParams as EmbeddingCreateEmbeddingsParams

if TYPE_CHECKING:
    from .function_definition import FunctionDefinition as FunctionDefinition
    from .embedding_create_embeddings_response import (
        EmbeddingCreateEmbeddingsResponse as EmbeddingCreateEmbeddingsResponse,
    )
    from .embedding_list_embedding_models_response import (
        EmbeddingListEmbeddingModelsResponse as EmbeddingListEmbeddingModelsResponse,
    )


def __getattr__(name: str) -> Any:
    if name == "EmbeddingCreateEmbeddingsResponse":
        from .embedding_create_embeddings_response import EmbeddingCreateEmbeddingsResponse

        return EmbeddingCreateEmbeddingsResponse
    if name == "EmbeddingListEmbeddingModelsResponse":
        from .embedding_list_embedding_models_response import EmbeddingListEmbeddingModelsResponse

        return EmbeddingListEmbeddingModelsResponse
    if name == "FunctionDefinition":
        from .function_definition import FunctionDefinition

        return FunctionDefinition
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
