# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExternalLlmReqParam"]


class ExternalLlmReqParam(TypedDict, total=False):
    base_url: Required[str]
    """Base URL for the external LLM endpoint."""

    model: Required[str]
    """Model identifier to use with the external LLM endpoint."""

    authentication_method: Literal["token", "certificate"]
    """Authentication method used when connecting to the external LLM endpoint."""

    certificate_ref: str
    """
    Integration secret identifier for the client certificate used with certificate
    authentication.
    """

    forward_metadata: bool
    """
    When `true`, Telnyx forwards the assistant's dynamic variables to the external
    LLM endpoint as a top-level `extra_metadata` object on the chat completion
    request body. Defaults to `false`. Example payload sent to the external
    endpoint:
    `{"extra_metadata": {"customer_name": "Jane", "account_id": "acct_789", "telnyx_agent_target": "+13125550100", "telnyx_end_user_target": "+13125550123"}}`.
    Distinct from OpenAI's native `metadata` field, which has its own size and type
    limits.
    """

    llm_api_key_ref: str
    """Integration secret identifier for the external LLM API key."""

    token_retrieval_url: str
    """
    URL used to retrieve an access token when certificate authentication is enabled.
    """
