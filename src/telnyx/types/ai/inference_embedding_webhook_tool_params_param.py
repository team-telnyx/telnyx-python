# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "InferenceEmbeddingWebhookToolParamsParam",
    "Webhook",
    "WebhookBodyParameters",
    "WebhookHeader",
    "WebhookPathParameters",
    "WebhookQueryParameters",
]


class WebhookBodyParameters(TypedDict, total=False):
    """The body parameters the webhook tool accepts, described as a JSON Schema object.

    These parameters will be passed to the webhook as the body of the request. See the [JSON Schema reference](https://json-schema.org/understanding-json-schema) for documentation about the format
    """

    properties: Dict[str, object]
    """The properties of the body parameters."""

    required: SequenceNotStr[str]
    """The required properties of the body parameters."""

    type: Literal["object"]


class WebhookHeader(TypedDict, total=False):
    name: str

    value: str
    """The value of the header.

    Note that we support mustache templating for the value. For example you can use
    `Bearer {{#integration_secret}}test-secret{{/integration_secret}}` to pass the
    value of the integration secret as the bearer token.
    [Telnyx signature headers](https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-webhooks)
    will be automatically added to the request.
    """


class WebhookPathParameters(TypedDict, total=False):
    """The path parameters the webhook tool accepts, described as a JSON Schema object.

    These parameters will be passed to the webhook as the path of the request if the URL contains a placeholder for a value. See the [JSON Schema reference](https://json-schema.org/understanding-json-schema) for documentation about the format
    """

    properties: Dict[str, object]
    """The properties of the path parameters."""

    required: SequenceNotStr[str]
    """The required properties of the path parameters."""

    type: Literal["object"]


class WebhookQueryParameters(TypedDict, total=False):
    """The query parameters the webhook tool accepts, described as a JSON Schema object.

    These parameters will be passed to the webhook as the query of the request. See the [JSON Schema reference](https://json-schema.org/understanding-json-schema) for documentation about the format
    """

    properties: Dict[str, object]
    """The properties of the query parameters."""

    required: SequenceNotStr[str]
    """The required properties of the query parameters."""

    type: Literal["object"]


_WebhookReservedKeywords = TypedDict(
    "_WebhookReservedKeywords",
    {
        "async": bool,
    },
    total=False,
)


class Webhook(_WebhookReservedKeywords, total=False):
    description: Required[str]
    """The description of the tool."""

    name: Required[str]
    """The name of the tool."""

    url: Required[str]
    """The URL of the external tool to be called.

    This URL is going to be used by the assistant. The URL can be templated like:
    `https://example.com/api/v1/{id}`, where `{id}` is a placeholder for a value
    that will be provided by the assistant if `path_parameters` are provided with
    the `id` attribute.
    """

    body_parameters: WebhookBodyParameters
    """The body parameters the webhook tool accepts, described as a JSON Schema object.

    These parameters will be passed to the webhook as the body of the request. See
    the [JSON Schema reference](https://json-schema.org/understanding-json-schema)
    for documentation about the format
    """

    headers: Iterable[WebhookHeader]
    """The headers to be sent to the external tool."""

    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH"]
    """The HTTP method to be used when calling the external tool."""

    path_parameters: WebhookPathParameters
    """The path parameters the webhook tool accepts, described as a JSON Schema object.

    These parameters will be passed to the webhook as the path of the request if the
    URL contains a placeholder for a value. See the
    [JSON Schema reference](https://json-schema.org/understanding-json-schema) for
    documentation about the format
    """

    query_parameters: WebhookQueryParameters
    """The query parameters the webhook tool accepts, described as a JSON Schema
    object.

    These parameters will be passed to the webhook as the query of the request. See
    the [JSON Schema reference](https://json-schema.org/understanding-json-schema)
    for documentation about the format
    """

    timeout_ms: int
    """The maximum number of milliseconds to wait for the webhook to respond.

    Only applicable when async is false.
    """


class InferenceEmbeddingWebhookToolParamsParam(TypedDict, total=False):
    type: Required[Literal["webhook"]]

    webhook: Required[Webhook]
