# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ...._types import SequenceNotStr
from ..bucket_ids_param import BucketIDsParam

__all__ = [
    "ChatCreateCompletionParams",
    "Message",
    "MessageContentTextAndImageArray",
    "ResponseFormat",
    "ResponseFormatResponseFormatText",
    "ResponseFormatResponseFormatJsonObject",
    "ResponseFormatResponseFormatJsonSchemaParam",
    "ResponseFormatResponseFormatJsonSchemaParamJsonSchema",
    "Tool",
    "ToolFunction",
    "ToolFunctionFunction",
    "ToolRetrieval",
]


class ChatCreateCompletionParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]
    """A list of the previous chat messages for context."""

    api_key_ref: str
    """
    If you are using an external inference provider like xAI or OpenAI, this field
    allows you to pass along a reference to your API key. After creating an
    [integration secret](https://developers.telnyx.com/api-reference/integration-secrets/create-a-secret)
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

    enable_thinking: bool
    """
    Whether to enable the thinking/reasoning phase for models that support it (e.g.,
    QwQ, Qwen3). When set to false, the model will skip the internal reasoning step
    and respond directly, which can reduce latency. Defaults to true.
    """

    frequency_penalty: float
    """Higher values will penalize the model from repeating the same output tokens."""

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

    mode: Literal["preferred", "strict"]
    """How strictly `region` is applied.

    `preferred` (the default when `region` is set) tries that region first and falls
    back to another when the model cannot be served there, so a request that would
    have succeeded still succeeds. `strict` pins the request: it is served from that
    region or it fails with a 422, never redirected to another region. Requires
    `region`.
    """

    model: str
    """The language model to chat with."""

    n: float
    """This will return multiple choices for you instead of a single chat completion."""

    presence_penalty: float
    """Higher values will penalize the model from repeating the same output tokens."""

    reasoning_effort: Literal["none", "minimal", "low", "medium", "high", "xhigh", "max"]
    """Controls the reasoning effort for models that support it.

    When set, the model spends more or less compute on internal reasoning before
    generating its response. Supported values: none, minimal, low, medium, high,
    xhigh, max. Not all models support all values; unsupported values are rejected
    with a 400 error. When omitted, reasoning models use their default effort level.
    """

    region: Literal["USA", "EU", "AUS", "UAE"]
    """
    Optional data-residency region the request should be served from, using the same
    vocabulary as your account's Data Locality setting. Behavior depends on `mode`.
    Supported for Telnyx-hosted models only: a request routed to an external
    provider never passes through Telnyx model routing, so a region cannot be
    enforced for it. Omit for today's latency-based routing.
    """

    response_format: ResponseFormat
    """Controls the format of the model output.

    `json_object` guarantees valid JSON output without defining a schema;
    `json_schema` constrains the output to the JSON schema you supply via the
    `json_schema` property and is the supported way to get guaranteed structured
    output on Telnyx-hosted models.
    """

    seed: int
    """
    If specified, the system will make a best effort to sample deterministically,
    such that repeated requests with the same `seed` and parameters should return
    the same result.
    """

    service_tier: str
    """The service tier to use for this request.

    Supported values vary by model; use `GET /v2/ai/openai/models` and inspect the
    model's `service_tiers` field. If omitted, Telnyx-hosted models use `default`.
    """

    stop: Union[str, SequenceNotStr[str]]
    """Up to 4 sequences where the API will stop generating further tokens.

    The returned text will not contain the stop sequence.
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
    [embedded storage buckets](https://developers.telnyx.com/api-reference/embeddings/embed-documents)
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


class ResponseFormatResponseFormatText(TypedDict, total=False):
    """Plain text output."""

    type: Required[Literal["text"]]


class ResponseFormatResponseFormatJsonObject(TypedDict, total=False):
    """JSON mode: the model output is valid JSON, without a schema."""

    type: Required[Literal["json_object"]]


class ResponseFormatResponseFormatJsonSchemaParamJsonSchema(TypedDict, total=False):
    """The JSON schema configuration, required when `type` is `json_schema`.

    Matches the [OpenAI structured outputs](https://platform.openai.com/docs/guides/structured-outputs) `json_schema` response format.
    """

    name: Required[str]
    """The name of the response format. Used for clarity only."""

    description: str
    """
    A description of what the response format is for, typically used to guide the
    model.
    """

    schema: Dict[str, object]
    """The JSON schema the model output must conform to.

    A valid [JSON Schema](https://json-schema.org) object, e.g. a Pydantic
    `model_json_schema()` export.
    """

    strict: bool
    """Enables strict schema adherence when supported by the model.

    If the generated output does not match the provided schema, the request fails
    instead of returning non-conformant output.
    """


class ResponseFormatResponseFormatJsonSchemaParam(TypedDict, total=False):
    """
    Structured output: the model output is constrained to the JSON schema supplied in `json_schema`.
    """

    json_schema: Required[ResponseFormatResponseFormatJsonSchemaParamJsonSchema]
    """The JSON schema configuration, required when `type` is `json_schema`.

    Matches the
    [OpenAI structured outputs](https://platform.openai.com/docs/guides/structured-outputs)
    `json_schema` response format.
    """

    type: Required[Literal["json_schema"]]


ResponseFormat: TypeAlias = Union[
    ResponseFormatResponseFormatText,
    ResponseFormatResponseFormatJsonObject,
    ResponseFormatResponseFormatJsonSchemaParam,
]


class ToolFunctionFunction(TypedDict, total=False):
    name: Required[str]

    description: str

    parameters: Dict[str, object]


class ToolFunction(TypedDict, total=False):
    function: Required[ToolFunctionFunction]

    type: Required[Literal["function"]]


class ToolRetrieval(TypedDict, total=False):
    retrieval: Required[BucketIDsParam]

    type: Required[Literal["retrieval"]]


Tool: TypeAlias = Union[ToolFunction, ToolRetrieval]
