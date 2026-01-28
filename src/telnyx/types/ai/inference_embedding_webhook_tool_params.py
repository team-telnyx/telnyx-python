# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "InferenceEmbeddingWebhookToolParams",
    "Webhook",
    "WebhookBodyParameters",
    "WebhookHeader",
    "WebhookPathParameters",
    "WebhookQueryParameters",
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

    body_parameters: Optional[WebhookBodyParameters] = None
    """The body parameters the webhook tool accepts, described as a JSON Schema object.

    These parameters will be passed to the webhook as the body of the request. See
    the [JSON Schema reference](https://json-schema.org/understanding-json-schema)
    for documentation about the format
    """

    headers: Optional[List[WebhookHeader]] = None
    """The headers to be sent to the external tool."""

    method: Optional[Literal["GET", "POST", "PUT", "DELETE", "PATCH"]] = None
    """The HTTP method to be used when calling the external tool."""

    path_parameters: Optional[WebhookPathParameters] = None
    """The path parameters the webhook tool accepts, described as a JSON Schema object.

    These parameters will be passed to the webhook as the path of the request if the
    URL contains a placeholder for a value. See the
    [JSON Schema reference](https://json-schema.org/understanding-json-schema) for
    documentation about the format
    """

    query_parameters: Optional[WebhookQueryParameters] = None
    """The query parameters the webhook tool accepts, described as a JSON Schema
    object.

    These parameters will be passed to the webhook as the query of the request. See
    the [JSON Schema reference](https://json-schema.org/understanding-json-schema)
    for documentation about the format
    """

    timeout_ms: Optional[int] = None
    """The maximum number of milliseconds to wait for the webhook to respond.

    Only applicable when async is false.
    """


class InferenceEmbeddingWebhookToolParams(BaseModel):
    type: Literal["webhook"]

    webhook: Webhook
