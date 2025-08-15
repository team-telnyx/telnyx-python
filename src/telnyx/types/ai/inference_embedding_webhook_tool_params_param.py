# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["InferenceEmbeddingWebhookToolParamsParam", "BodyParameters", "Header", "PathParameters", "QueryParameters"]


class BodyParameters(TypedDict, total=False):
    properties: Dict[str, object]
    """The properties of the body parameters."""

    required: List[str]
    """The required properties of the body parameters."""

    type: Literal["object"]


class Header(TypedDict, total=False):
    name: str

    value: str
    """The value of the header.

    Note that we support mustache templating for the value. For example you can use
    `Bearer {{#integration_secret}}test-secret{{/integration_secret}}` to pass the
    value of the integration secret as the bearer token.
    """


class PathParameters(TypedDict, total=False):
    properties: Dict[str, object]
    """The properties of the path parameters."""

    required: List[str]
    """The required properties of the path parameters."""

    type: Literal["object"]


class QueryParameters(TypedDict, total=False):
    properties: Dict[str, object]
    """The properties of the query parameters."""

    required: List[str]
    """The required properties of the query parameters."""

    type: Literal["object"]


class InferenceEmbeddingWebhookToolParamsParam(TypedDict, total=False):
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

    body_parameters: BodyParameters
    """The body parameters the webhook tool accepts, described as a JSON Schema object.

    These parameters will be passed to the webhook as the body of the request. See
    the [JSON Schema reference](https://json-schema.org/understanding-json-schema)
    for documentation about the format
    """

    headers: Iterable[Header]
    """The headers to be sent to the external tool."""

    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH"]
    """The HTTP method to be used when calling the external tool."""

    path_parameters: PathParameters
    """The path parameters the webhook tool accepts, described as a JSON Schema object.

    These parameters will be passed to the webhook as the path of the request if the
    URL contains a placeholder for a value. See the
    [JSON Schema reference](https://json-schema.org/understanding-json-schema) for
    documentation about the format
    """

    query_parameters: QueryParameters
    """The query parameters the webhook tool accepts, described as a JSON Schema
    object.

    These parameters will be passed to the webhook as the query of the request. See
    the [JSON Schema reference](https://json-schema.org/understanding-json-schema)
    for documentation about the format
    """
