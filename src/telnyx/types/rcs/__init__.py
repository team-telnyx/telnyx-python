# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .agent_use_case import AgentUseCase as AgentUseCase
from .agent_list_params import AgentListParams as AgentListParams
from .agent_create_params import AgentCreateParams as AgentCreateParams
from .agent_launch_params import AgentLaunchParams as AgentLaunchParams
from .agent_list_response import AgentListResponse as AgentListResponse
from .agent_update_params import AgentUpdateParams as AgentUpdateParams
from .brand_contact_param import BrandContactParam as BrandContactParam
from .brand_create_params import BrandCreateParams as BrandCreateParams
from .brand_list_response import BrandListResponse as BrandListResponse
from .brand_update_params import BrandUpdateParams as BrandUpdateParams
from .agent_interaction_param import AgentInteractionParam as AgentInteractionParam
from .agent_submission_status import AgentSubmissionStatus as AgentSubmissionStatus
from .brand_legal_entity_type import BrandLegalEntityType as BrandLegalEntityType
from .brand_organization_type import BrandOrganizationType as BrandOrganizationType
from .agent_configuration_param import AgentConfigurationParam as AgentConfigurationParam
from .agent_email_contact_param import AgentEmailContactParam as AgentEmailContactParam
from .agent_phone_contact_param import AgentPhoneContactParam as AgentPhoneContactParam
from .ein_brand_identifier_param import EinBrandIdentifierParam as EinBrandIdentifierParam
from .agent_website_contact_param import AgentWebsiteContactParam as AgentWebsiteContactParam
from .agent_consent_configuration_param import AgentConsentConfigurationParam as AgentConsentConfigurationParam
from .agent_testing_configuration_param import AgentTestingConfigurationParam as AgentTestingConfigurationParam
from .agent_campaign_configuration_param import AgentCampaignConfigurationParam as AgentCampaignConfigurationParam
from .stock_symbol_brand_identifier_param import StockSymbolBrandIdentifierParam as StockSymbolBrandIdentifierParam
from .agent_retrieve_carrier_approvals_response import (
    AgentRetrieveCarrierApprovalsResponse as AgentRetrieveCarrierApprovalsResponse,
)

if TYPE_CHECKING:
    from .rcs_agent import RcsAgent as RcsAgent
    from .brand_contact import BrandContact as BrandContact
    from .agent_response import AgentResponse as AgentResponse
    from .brand_response import BrandResponse as BrandResponse
    from .agent_interaction import AgentInteraction as AgentInteraction
    from .rcs_agent_response import RcsAgentResponse as RcsAgentResponse
    from .agent_configuration import AgentConfiguration as AgentConfiguration
    from .agent_email_contact import AgentEmailContact as AgentEmailContact
    from .agent_phone_contact import AgentPhoneContact as AgentPhoneContact
    from .ein_brand_identifier import EinBrandIdentifier as EinBrandIdentifier
    from .agent_website_contact import AgentWebsiteContact as AgentWebsiteContact
    from .capabilities_response import CapabilitiesResponse as CapabilitiesResponse
    from .carrier_approval_response import CarrierApprovalResponse as CarrierApprovalResponse
    from .agent_consent_configuration import AgentConsentConfiguration as AgentConsentConfiguration
    from .agent_testing_configuration import AgentTestingConfiguration as AgentTestingConfiguration
    from .agent_campaign_configuration import AgentCampaignConfiguration as AgentCampaignConfiguration
    from .stock_symbol_brand_identifier import StockSymbolBrandIdentifier as StockSymbolBrandIdentifier


def __getattr__(name: str) -> Any:
    if name == "AgentCampaignConfiguration":
        from .agent_campaign_configuration import AgentCampaignConfiguration

        return AgentCampaignConfiguration
    if name == "AgentConfiguration":
        from .agent_configuration import AgentConfiguration

        return AgentConfiguration
    if name == "AgentConsentConfiguration":
        from .agent_consent_configuration import AgentConsentConfiguration

        return AgentConsentConfiguration
    if name == "AgentEmailContact":
        from .agent_email_contact import AgentEmailContact

        return AgentEmailContact
    if name == "AgentInteraction":
        from .agent_interaction import AgentInteraction

        return AgentInteraction
    if name == "AgentPhoneContact":
        from .agent_phone_contact import AgentPhoneContact

        return AgentPhoneContact
    if name == "AgentResponse":
        from .agent_response import AgentResponse

        return AgentResponse
    if name == "AgentTestingConfiguration":
        from .agent_testing_configuration import AgentTestingConfiguration

        return AgentTestingConfiguration
    if name == "AgentWebsiteContact":
        from .agent_website_contact import AgentWebsiteContact

        return AgentWebsiteContact
    if name == "CapabilitiesResponse":
        from .capabilities_response import CapabilitiesResponse

        return CapabilitiesResponse
    if name == "CarrierApprovalResponse":
        from .carrier_approval_response import CarrierApprovalResponse

        return CarrierApprovalResponse
    if name == "RcsAgent":
        from .rcs_agent import RcsAgent

        return RcsAgent
    if name == "RcsAgentResponse":
        from .rcs_agent_response import RcsAgentResponse

        return RcsAgentResponse
    if name == "BrandContact":
        from .brand_contact import BrandContact

        return BrandContact
    if name == "BrandResponse":
        from .brand_response import BrandResponse

        return BrandResponse
    if name == "EinBrandIdentifier":
        from .ein_brand_identifier import EinBrandIdentifier

        return EinBrandIdentifier
    if name == "StockSymbolBrandIdentifier":
        from .stock_symbol_brand_identifier import StockSymbolBrandIdentifier

        return StockSymbolBrandIdentifier
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
