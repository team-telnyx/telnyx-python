# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

from ..._models import BaseModel
from .authentication_method import AuthenticationMethod

__all__ = ["ExternalLlm"]


class ExternalLlm(BaseModel):
    base_url: str
    """Base URL for the external LLM endpoint."""

    model: str
    """Model identifier to use with the external LLM endpoint."""

    authentication_method: Optional[AuthenticationMethod] = None
    """Authentication method used when connecting to the external LLM endpoint."""

    certificate_ref: Optional[str] = None
    """
    Integration secret identifier for the client certificate used with certificate
    authentication.
    """

    extra_headers: Optional[Dict[str, str]] = None
    """
    Custom HTTP headers Telnyx sets on every request to the external LLM endpoint,
    in addition to the authentication header. Keys are header names, values are
    static strings. At most 32 headers. Reserved names are rejected:
    accept-encoding, authorization, connection, content-encoding, content-length,
    content-type, cookie, expect, host, keep-alive, proxy-authenticate,
    proxy-authorization, proxy-connection, set-cookie, te, trailer,
    transfer-encoding, upgrade, x-host-rewrite, x-request-id, x-trace-id, and any
    x-telnyx-_ or x-stainless-_ header; '\\__' counts as '-' when names are compared.
    Names must be valid HTTP header names (RFC 7230 token, at most 128 characters)
    and must not repeat (case-insensitive). Values must be printable ASCII, at most
    4096 characters, with no leading or trailing whitespace. Values are stored as
    plain text and returned when the assistant is retrieved.
    """

    forward_metadata: Optional[bool] = None
    """
    When `true`, Telnyx forwards the assistant's dynamic variables to the external
    LLM endpoint as a top-level `extra_metadata` object on the chat completion
    request body. Defaults to `false`. Example payload sent to the external
    endpoint:
    `{"extra_metadata": {"customer_name": "Jane", "account_id": "acct_789", "telnyx_agent_target": "+13125550100", "telnyx_end_user_target": "+13125550123"}}`.
    Distinct from OpenAI's native `metadata` field, which has its own size and type
    limits.
    """

    llm_api_key_ref: Optional[str] = None
    """Integration secret identifier for the external LLM API key."""

    token_retrieval_url: Optional[str] = None
    """
    URL used to retrieve an access token when certificate authentication is enabled.
    """
