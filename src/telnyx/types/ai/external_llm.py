# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ExternalLlm"]


class ExternalLlm(BaseModel):
    base_url: str
    """Base URL for the external LLM endpoint."""

    model: str
    """Model identifier to use with the external LLM endpoint."""

    authentication_method: Optional[Literal["token", "certificate"]] = None
    """Authentication method used when connecting to the external LLM endpoint."""

    certificate_ref: Optional[str] = None
    """
    Integration secret identifier for the client certificate used with certificate
    authentication.
    """

    forward_metadata: Optional[bool] = None
    """
    When enabled, Telnyx forwards the assistant's dynamic variables to the external
    LLM endpoint. Defaults to false. The chat completion request includes a
    top-level `extra_metadata` object when dynamic variables are available. For
    example:
    `{"extra_metadata":{"customer_name":"Jane","account_id":"acct_789","telnyx_agent_target":"+13125550100","telnyx_end_user_target":"+13125550123"}}`.
    """

    llm_api_key_ref: Optional[str] = None
    """Integration secret identifier for the external LLM API key."""

    token_retrieval_url: Optional[str] = None
    """
    URL used to retrieve an access token when certificate authentication is enabled.
    """
