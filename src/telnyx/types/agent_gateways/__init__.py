# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .key_list_params import KeyListParams as KeyListParams
from .api_create_params import APICreateParams as APICreateParams
from .api_update_params import APIUpdateParams as APIUpdateParams
from .key_create_params import KeyCreateParams as KeyCreateParams
from .key_update_params import KeyUpdateParams as KeyUpdateParams
from .team_create_params import TeamCreateParams as TeamCreateParams
from .team_update_params import TeamUpdateParams as TeamUpdateParams
from .policy_create_params import PolicyCreateParams as PolicyCreateParams
from .policy_update_params import PolicyUpdateParams as PolicyUpdateParams
from .guardrail_create_params import GuardrailCreateParams as GuardrailCreateParams
from .guardrail_update_params import GuardrailUpdateParams as GuardrailUpdateParams
from .mcp_server_create_params import McpServerCreateParams as McpServerCreateParams
from .mcp_server_update_params import McpServerUpdateParams as McpServerUpdateParams
from .agent_gateway_no_auth_param import AgentGatewayNoAuthParam as AgentGatewayNoAuthParam
from .agent_gateway_policy_step_param import AgentGatewayPolicyStepParam as AgentGatewayPolicyStepParam
from .agent_gateway_static_auth_param import AgentGatewayStaticAuthParam as AgentGatewayStaticAuthParam
from .policy_attachment_create_params import PolicyAttachmentCreateParams as PolicyAttachmentCreateParams
from .agent_gateway_aws_sig_v4_auth_param import AgentGatewayAwsSigV4AuthParam as AgentGatewayAwsSigV4AuthParam
from .agent_gateway_policy_pipeline_param import AgentGatewayPolicyPipelineParam as AgentGatewayPolicyPipelineParam
from .agent_gateway_passthrough_auth_param import AgentGatewayPassthroughAuthParam as AgentGatewayPassthroughAuthParam
from .agent_gateway_policy_guardrails_param import (
    AgentGatewayPolicyGuardrailsParam as AgentGatewayPolicyGuardrailsParam,
)
from .agent_gateway_oauth_client_credentials_param import (
    AgentGatewayOAuthClientCredentialsParam as AgentGatewayOAuthClientCredentialsParam,
)

if TYPE_CHECKING:
    from .agent_gateway_api import AgentGatewayAPI as AgentGatewayAPI
    from .agent_gateway_key import AgentGatewayKey as AgentGatewayKey
    from .api_list_response import APIListResponse as APIListResponse
    from .key_list_response import KeyListResponse as KeyListResponse
    from .agent_gateway_team import AgentGatewayTeam as AgentGatewayTeam
    from .team_list_response import TeamListResponse as TeamListResponse
    from .key_create_response import KeyCreateResponse as KeyCreateResponse
    from .agent_gateway_policy import AgentGatewayPolicy as AgentGatewayPolicy
    from .policy_list_response import PolicyListResponse as PolicyListResponse
    from .agent_gateway_guardrail import AgentGatewayGuardrail as AgentGatewayGuardrail
    from .guardrail_list_response import GuardrailListResponse as GuardrailListResponse
    from .agent_gateway_mcp_server import AgentGatewayMcpServer as AgentGatewayMcpServer
    from .agent_gateway_shown_auth import AgentGatewayShownAuth as AgentGatewayShownAuth
    from .mcp_server_list_response import McpServerListResponse as McpServerListResponse
    from .agent_gateway_policy_step import AgentGatewayPolicyStep as AgentGatewayPolicyStep
    from .agent_gateway_api_response import AgentGatewayAPIResponse as AgentGatewayAPIResponse
    from .agent_gateway_key_response import AgentGatewayKeyResponse as AgentGatewayKeyResponse
    from .agent_gateway_team_response import AgentGatewayTeamResponse as AgentGatewayTeamResponse
    from .agent_gateway_policy_pipeline import AgentGatewayPolicyPipeline as AgentGatewayPolicyPipeline
    from .agent_gateway_policy_response import AgentGatewayPolicyResponse as AgentGatewayPolicyResponse
    from .agent_gateway_policy_attachment import AgentGatewayPolicyAttachment as AgentGatewayPolicyAttachment
    from .agent_gateway_policy_guardrails import AgentGatewayPolicyGuardrails as AgentGatewayPolicyGuardrails
    from .policy_attachment_list_response import PolicyAttachmentListResponse as PolicyAttachmentListResponse
    from .agent_gateway_guardrail_response import AgentGatewayGuardrailResponse as AgentGatewayGuardrailResponse
    from .agent_gateway_mcp_server_response import AgentGatewayMcpServerResponse as AgentGatewayMcpServerResponse
    from .agent_gateway_policy_attachment_response import (
        AgentGatewayPolicyAttachmentResponse as AgentGatewayPolicyAttachmentResponse,
    )


def __getattr__(name: str) -> Any:
    if name == "AgentGatewayAPI":
        from .agent_gateway_api import AgentGatewayAPI

        return AgentGatewayAPI
    if name == "AgentGatewayAPIResponse":
        from .agent_gateway_api_response import AgentGatewayAPIResponse

        return AgentGatewayAPIResponse
    if name == "AgentGatewayShownAuth":
        from .agent_gateway_shown_auth import AgentGatewayShownAuth

        return AgentGatewayShownAuth
    if name == "APIListResponse":
        from .api_list_response import APIListResponse

        return APIListResponse
    if name == "AgentGatewayGuardrail":
        from .agent_gateway_guardrail import AgentGatewayGuardrail

        return AgentGatewayGuardrail
    if name == "AgentGatewayGuardrailResponse":
        from .agent_gateway_guardrail_response import AgentGatewayGuardrailResponse

        return AgentGatewayGuardrailResponse
    if name == "GuardrailListResponse":
        from .guardrail_list_response import GuardrailListResponse

        return GuardrailListResponse
    if name == "AgentGatewayKey":
        from .agent_gateway_key import AgentGatewayKey

        return AgentGatewayKey
    if name == "AgentGatewayKeyResponse":
        from .agent_gateway_key_response import AgentGatewayKeyResponse

        return AgentGatewayKeyResponse
    if name == "KeyCreateResponse":
        from .key_create_response import KeyCreateResponse

        return KeyCreateResponse
    if name == "KeyListResponse":
        from .key_list_response import KeyListResponse

        return KeyListResponse
    if name == "AgentGatewayMcpServer":
        from .agent_gateway_mcp_server import AgentGatewayMcpServer

        return AgentGatewayMcpServer
    if name == "AgentGatewayMcpServerResponse":
        from .agent_gateway_mcp_server_response import AgentGatewayMcpServerResponse

        return AgentGatewayMcpServerResponse
    if name == "McpServerListResponse":
        from .mcp_server_list_response import McpServerListResponse

        return McpServerListResponse
    if name == "AgentGatewayPolicy":
        from .agent_gateway_policy import AgentGatewayPolicy

        return AgentGatewayPolicy
    if name == "AgentGatewayPolicyGuardrails":
        from .agent_gateway_policy_guardrails import AgentGatewayPolicyGuardrails

        return AgentGatewayPolicyGuardrails
    if name == "AgentGatewayPolicyPipeline":
        from .agent_gateway_policy_pipeline import AgentGatewayPolicyPipeline

        return AgentGatewayPolicyPipeline
    if name == "AgentGatewayPolicyResponse":
        from .agent_gateway_policy_response import AgentGatewayPolicyResponse

        return AgentGatewayPolicyResponse
    if name == "AgentGatewayPolicyStep":
        from .agent_gateway_policy_step import AgentGatewayPolicyStep

        return AgentGatewayPolicyStep
    if name == "PolicyListResponse":
        from .policy_list_response import PolicyListResponse

        return PolicyListResponse
    if name == "AgentGatewayPolicyAttachment":
        from .agent_gateway_policy_attachment import AgentGatewayPolicyAttachment

        return AgentGatewayPolicyAttachment
    if name == "AgentGatewayPolicyAttachmentResponse":
        from .agent_gateway_policy_attachment_response import AgentGatewayPolicyAttachmentResponse

        return AgentGatewayPolicyAttachmentResponse
    if name == "PolicyAttachmentListResponse":
        from .policy_attachment_list_response import PolicyAttachmentListResponse

        return PolicyAttachmentListResponse
    if name == "AgentGatewayTeam":
        from .agent_gateway_team import AgentGatewayTeam

        return AgentGatewayTeam
    if name == "AgentGatewayTeamResponse":
        from .agent_gateway_team_response import AgentGatewayTeamResponse

        return AgentGatewayTeamResponse
    if name == "TeamListResponse":
        from .team_list_response import TeamListResponse

        return TeamListResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
