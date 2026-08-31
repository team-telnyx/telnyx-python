# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "InferenceEmbeddingWebhookToolParams",
    "Webhook",
    "WebhookBodyParameters",
    "WebhookHeader",
    "WebhookMessage",
    "WebhookMessageWebhookToolRequestStartMessage",
    "WebhookMessageWebhookToolRequestResponseDelayedMessage",
    "WebhookPathParameters",
    "WebhookQueryParameters",
    "WebhookStoreFieldsAsVariable",
]


class WebhookBodyParameters(BaseModel):
    """The body parameters the webhook tool accepts, described as a JSON Schema object.

    These parameters will be passed to the webhook as the body of the request. See the [JSON Schema reference](https://json-schema.org/understanding-json-schema) for documentation about the format
    """

    properties: Optional[Dict[str, object]] = None
    """The properties of the body parameters."""

    required: Optional[List[str]] = None
    """The required properties of the body parameters."""

    type: Optional[Literal["object"]] = None


class WebhookHeader(BaseModel):
    name: Optional[str] = None

    value: Optional[str] = None
    """The value of the header.

    Note that we support mustache templating for the value. For example you can use
    `Bearer {{#integration_secret}}test-secret{{/integration_secret}}` to pass the
    value of the integration secret as the bearer token.
    [Telnyx signature headers](https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-webhooks)
    will be automatically added to the request.
    """


class WebhookMessageWebhookToolRequestStartMessage(BaseModel):
    content: str
    """The text the assistant speaks."""

    type: Literal["request_start"]
    """Speak the filler message immediately when the webhook request begins."""

    timing_ms: Optional[int] = None
    """An optional delay value. This value is ignored for `request_start` messages."""


class WebhookMessageWebhookToolRequestResponseDelayedMessage(BaseModel):
    content: str
    """The text the assistant speaks."""

    timing_ms: int
    """The delay in milliseconds from the start of the webhook request."""

    type: Literal["request_response_delayed"]
    """
    Speak the filler message after the configured delay if the webhook response is
    still pending.
    """


WebhookMessage: TypeAlias = Union[
    WebhookMessageWebhookToolRequestStartMessage, WebhookMessageWebhookToolRequestResponseDelayedMessage
]


class WebhookPathParameters(BaseModel):
    """The path parameters the webhook tool accepts, described as a JSON Schema object.

    These parameters will be passed to the webhook as the path of the request if the URL contains a placeholder for a value. See the [JSON Schema reference](https://json-schema.org/understanding-json-schema) for documentation about the format
    """

    properties: Optional[Dict[str, object]] = None
    """The properties of the path parameters."""

    required: Optional[List[str]] = None
    """The required properties of the path parameters."""

    type: Optional[Literal["object"]] = None


class WebhookQueryParameters(BaseModel):
    """The query parameters the webhook tool accepts, described as a JSON Schema object.

    These parameters will be passed to the webhook as the query of the request. See the [JSON Schema reference](https://json-schema.org/understanding-json-schema) for documentation about the format
    """

    properties: Optional[Dict[str, object]] = None
    """The properties of the query parameters."""

    required: Optional[List[str]] = None
    """The required properties of the query parameters."""

    type: Optional[Literal["object"]] = None


class WebhookStoreFieldsAsVariable(BaseModel):
    name: str
    """The name of the dynamic variable to store the extracted value in."""

    value_path: str
    """A dot-notation path to the value in the webhook response body (e.g.

    'customer.name' or 'id').
    """


class Webhook(BaseModel):
    description: str
    """The description of the tool."""

    name: str
    """The name of the tool."""

    url: str
    """The URL of the external tool to be called.

    This URL is going to be used by the assistant. The URL can be templated like:
    `https://example.com/api/v1/{id}`, where `{id}` is a placeholder for a value
    that will be provided by the assistant if `path_parameters` are provided with
    the `id` attribute.
    """

    async_: Optional[bool] = FieldInfo(alias="async", default=None)
    """
    If async, the assistant will move forward without waiting for your server to
    respond.
    """

    async_timeout_ms: Optional[int] = None
    """
    Maximum time in milliseconds that the conversation worker waits for an async
    webhook response before returning "Submitted" to the LLM. If unset, the platform
    default (currently 300ms) is used.
    """

    body_parameters: Optional[WebhookBodyParameters] = None
    """The body parameters the webhook tool accepts, described as a JSON Schema object.

    These parameters will be passed to the webhook as the body of the request. See
    the [JSON Schema reference](https://json-schema.org/understanding-json-schema)
    for documentation about the format
    """

    headers: Optional[List[WebhookHeader]] = None
    """The headers to be sent to the external tool."""

    messages: Optional[List[WebhookMessage]] = None
    """Filler messages spoken while a synchronous webhook request is in progress.

    `request_start` messages are spoken immediately when the request begins.
    `request_response_delayed` messages are spoken after `timing_ms` has elapsed
    only if the webhook response is still pending. Filler messages are not used for
    asynchronous webhooks.
    """

    method: Optional[Literal["GET", "POST", "PUT", "DELETE", "PATCH"]] = None
    """The HTTP method to be used when calling the external tool."""

    path_parameters: Optional[WebhookPathParameters] = None
    """The path parameters the webhook tool accepts, described as a JSON Schema object.

    These parameters will be passed to the webhook as the path of the request if the
    URL contains a placeholder for a value. See the
    [JSON Schema reference](https://json-schema.org/understanding-json-schema) for
    documentation about the format
    """

    preset_body_fields: Optional[Dict[str, object]] = None
    """Body fields supplied by the assistant configuration rather than by the model.

    They are never advertised in the tool definition, so the LLM can neither see nor
    set them, and they take precedence over a `body_parameters` value of the same
    name. Values support mustache templating, so they can hold dynamic variables
    (`{{customer_id}}`) and integration secrets
    (`{{#integration_secret}}my-secret{{/integration_secret}}`). Not sent on `GET`
    requests, which carry no body.
    """

    preset_query_params: Optional[Dict[str, object]] = None
    """
    Query string parameters supplied by the assistant configuration rather than by
    the model. They are never advertised in the tool definition, so the LLM can
    neither see nor set them, and they take precedence over a `query_parameters`
    value of the same name. Values support mustache templating, so they can hold
    dynamic variables (`{{telnyx_end_user_target}}`) and integration secrets
    (`{{#integration_secret}}my-secret{{/integration_secret}}`). Unlike values
    templated directly into the `url`, these are percent-encoded, so a value such as
    `+15551234567` survives the round trip.
    """

    query_parameters: Optional[WebhookQueryParameters] = None
    """The query parameters the webhook tool accepts, described as a JSON Schema
    object.

    These parameters will be passed to the webhook as the query of the request. See
    the [JSON Schema reference](https://json-schema.org/understanding-json-schema)
    for documentation about the format
    """

    store_fields_as_variables: Optional[List[WebhookStoreFieldsAsVariable]] = None
    """
    A list of mappings that extract values from the webhook response and store them
    as dynamic variables. Each mapping specifies a dynamic variable name and a
    dot-notation path to the value in the response body.
    """

    timeout_ms: Optional[int] = None
    """The maximum number of milliseconds to wait for the webhook to respond.

    Only applicable when async is false.
    """


class InferenceEmbeddingWebhookToolParams(BaseModel):
    type: Literal["webhook"]

    webhook: Webhook
