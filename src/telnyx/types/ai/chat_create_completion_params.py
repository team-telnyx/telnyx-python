# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .inference_embedding_bucket_ids_param import InferenceEmbeddingBucketIDsParam

__all__ = [
    "ChatCreateCompletionParams",
    "Message",
    "MessageContentTextAndImageArray",
    "ResponseFormat",
    "Tool",
    "ToolChatCompletionToolParam",
    "ToolChatCompletionToolParamFunction",
    "ToolRetrieval",
]


class ChatCreateCompletionParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]
    """A list of the previous chat messages for context."""

    api_key_ref: str
    """
    If you are using an external inference provider like xAI or OpenAI, this field
    allows you to pass along a reference to your API key. After creating an
    [integration secret](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
    for you API key, pass the secret's `identifier` in this field.
    """

    best_of: int
    """
    This is used with `use_beam_search` to determine how many candidate beams to
    explore.
    """

    early_stopping: bool
    """This is used with `use_beam_search`.

    If `true`, generation stops as soon as there are `best_of` complete candidates;
    if `false`, a heuristic is applied and the generation stops when is it very
    unlikely to find better candidates.
    """

    frequency_penalty: float
    """Higher values will penalize the model from repeating the same output tokens."""

    guided_choice: List[str]
    """If specified, the output will be exactly one of the choices."""

    guided_json: Dict[str, object]
    """Must be a valid JSON schema.

    If specified, the output will follow the JSON schema.
    """

    guided_regex: str
    """If specified, the output will follow the regex pattern."""

    length_penalty: float
    """This is used with `use_beam_search` to prefer shorter or longer completions."""

    logprobs: bool
    """Whether to return log probabilities of the output tokens or not.

    If true, returns the log probabilities of each output token returned in the
    `content` of `message`.
    """

    max_tokens: int
    """Maximum number of completion tokens the model should generate."""

    min_p: float
    """
    This is an alternative to `top_p` that
    [many prefer](https://github.com/huggingface/transformers/issues/27670). Must be
    in [0, 1].
    """

    model: str
    """The language model to chat with.

    If you are optimizing for speed + price, try
    `meta-llama/Meta-Llama-3.1-8B-Instruct`. For quality, try
    `meta-llama/Meta-Llama-3.1-70B-Instruct`. Or explore our
    [LLM Library](https://telnyx.com/products/llm-library).
    """

    n: float
    """This will return multiple choices for you instead of a single chat completion."""

    presence_penalty: float
    """Higher values will penalize the model from repeating the same output tokens."""

    response_format: ResponseFormat
    """Use this is you want to guarantee a JSON output without defining a schema.

    For control over the schema, use `guided_json`.
    """

    stream: bool
    """Whether or not to stream data-only server-sent events as they become available."""

    temperature: float
    """Adjusts the "creativity" of the model.

    Lower values make the model more deterministic and repetitive, while higher
    values make the model more random and creative.
    """

    tool_choice: Literal["none", "auto", "required"]

    tools: Iterable[Tool]
    """
    The `function` tool type follows the same schema as the
    [OpenAI Chat Completions API](https://platform.openai.com/docs/api-reference/chat).
    The `retrieval` tool type is unique to Telnyx. You may pass a list of
    [embedded storage buckets](https://developers.telnyx.com/api/inference/inference-embedding/post-embedding)
    for retrieval-augmented generation.
    """

    top_logprobs: int
    """This is used with `logprobs`.

    An integer between 0 and 20 specifying the number of most likely tokens to
    return at each token position, each with an associated log probability.
    """

    top_p: float
    """An alternative or complement to `temperature`.

    This adjusts how many of the top possibilities to consider.
    """

    use_beam_search: bool
    """
    Setting this to `true` will allow the model to
    [explore more completion options](https://huggingface.co/blog/how-to-generate#beam-search).
    This is not supported by OpenAI.
    """


class MessageContentTextAndImageArray(TypedDict, total=False):
    type: Required[Literal["text", "image_url"]]

    image_url: str

    text: str


class Message(TypedDict, total=False):
    content: Required[Union[str, Iterable[MessageContentTextAndImageArray]]]

    role: Required[Literal["system", "user", "assistant", "tool"]]


class ResponseFormat(TypedDict, total=False):
    type: Required[Literal["text", "json_object"]]


class ToolChatCompletionToolParamFunction(TypedDict, total=False):
    name: Required[str]

    description: str

    parameters: Dict[str, object]


class ToolChatCompletionToolParam(TypedDict, total=False):
    function: Required[ToolChatCompletionToolParamFunction]

    type: Required[Literal["function"]]


class ToolRetrieval(TypedDict, total=False):
    retrieval: Required[InferenceEmbeddingBucketIDsParam]

    type: Required[Literal["retrieval"]]


Tool: TypeAlias = Union[ToolChatCompletionToolParam, ToolRetrieval]
