# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .spend_group_by import SpendGroupBy as SpendGroupBy
from .budget_duration import BudgetDuration as BudgetDuration
from .spend_group_by_param import SpendGroupByParam as SpendGroupByParam
from .token_key_list_params import TokenKeyListParams as TokenKeyListParams
from .token_group_list_params import TokenGroupListParams as TokenGroupListParams
from .token_key_create_params import TokenKeyCreateParams as TokenKeyCreateParams
from .token_key_update_params import TokenKeyUpdateParams as TokenKeyUpdateParams
from .token_group_create_params import TokenGroupCreateParams as TokenGroupCreateParams
from .token_group_update_params import TokenGroupUpdateParams as TokenGroupUpdateParams
from .spend_retrieve_events_params import SpendRetrieveEventsParams as SpendRetrieveEventsParams
from .usage_retrieve_export_params import UsageRetrieveExportParams as UsageRetrieveExportParams
from .spend_retrieve_summary_params import SpendRetrieveSummaryParams as SpendRetrieveSummaryParams
from .usage_retrieve_summary_params import UsageRetrieveSummaryParams as UsageRetrieveSummaryParams

if TYPE_CHECKING:
    from .token_key import TokenKey as TokenKey
    from .token_group import TokenGroup as TokenGroup
    from .guardrail_finding import GuardrailFinding as GuardrailFinding
    from .token_key_response import TokenKeyResponse as TokenKeyResponse
    from .token_group_response import TokenGroupResponse as TokenGroupResponse
    from .ai_gateway_resources_page_meta import AIGatewayResourcesPageMeta as AIGatewayResourcesPageMeta
    from .spend_retrieve_events_response import SpendRetrieveEventsResponse as SpendRetrieveEventsResponse
    from .usage_retrieve_export_response import UsageRetrieveExportResponse as UsageRetrieveExportResponse
    from .spend_retrieve_summary_response import SpendRetrieveSummaryResponse as SpendRetrieveSummaryResponse
    from .usage_retrieve_summary_response import UsageRetrieveSummaryResponse as UsageRetrieveSummaryResponse


def __getattr__(name: str) -> Any:
    if name == "GuardrailFinding":
        from .guardrail_finding import GuardrailFinding

        return GuardrailFinding
    if name == "UsageRetrieveExportResponse":
        from .usage_retrieve_export_response import UsageRetrieveExportResponse

        return UsageRetrieveExportResponse
    if name == "UsageRetrieveSummaryResponse":
        from .usage_retrieve_summary_response import UsageRetrieveSummaryResponse

        return UsageRetrieveSummaryResponse
    if name == "SpendRetrieveEventsResponse":
        from .spend_retrieve_events_response import SpendRetrieveEventsResponse

        return SpendRetrieveEventsResponse
    if name == "SpendRetrieveSummaryResponse":
        from .spend_retrieve_summary_response import SpendRetrieveSummaryResponse

        return SpendRetrieveSummaryResponse
    if name == "AIGatewayResourcesPageMeta":
        from .ai_gateway_resources_page_meta import AIGatewayResourcesPageMeta

        return AIGatewayResourcesPageMeta
    if name == "TokenGroup":
        from .token_group import TokenGroup

        return TokenGroup
    if name == "TokenGroupResponse":
        from .token_group_response import TokenGroupResponse

        return TokenGroupResponse
    if name == "TokenKey":
        from .token_key import TokenKey

        return TokenKey
    if name == "TokenKeyResponse":
        from .token_key_response import TokenKeyResponse

        return TokenKeyResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
