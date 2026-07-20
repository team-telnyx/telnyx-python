# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .insight_list_params import InsightListParams as InsightListParams
from .message_list_params import MessageListParams as MessageListParams
from .insight_create_params import InsightCreateParams as InsightCreateParams
from .insight_update_params import InsightUpdateParams as InsightUpdateParams
from .insight_group_update_params import InsightGroupUpdateParams as InsightGroupUpdateParams
from .insight_group_insight_groups_params import InsightGroupInsightGroupsParams as InsightGroupInsightGroupsParams
from .insight_group_retrieve_insight_groups_params import (
    InsightGroupRetrieveInsightGroupsParams as InsightGroupRetrieveInsightGroupsParams,
)
from .conversation_insight_retrieve_aggregates_params import (
    ConversationInsightRetrieveAggregatesParams as ConversationInsightRetrieveAggregatesParams,
)

if TYPE_CHECKING:
    from .insight_template import InsightTemplate as InsightTemplate
    from .message_list_response import MessageListResponse as MessageListResponse
    from .insight_template_group import InsightTemplateGroup as InsightTemplateGroup
    from .insight_template_detail import InsightTemplateDetail as InsightTemplateDetail
    from .insight_template_group_detail import InsightTemplateGroupDetail as InsightTemplateGroupDetail
    from .conversation_insight_retrieve_aggregates_response import (
        ConversationInsightRetrieveAggregatesResponse as ConversationInsightRetrieveAggregatesResponse,
    )


def __getattr__(name: str) -> Any:
    if name == "InsightTemplateGroup":
        from .insight_template_group import InsightTemplateGroup

        return InsightTemplateGroup
    if name == "InsightTemplateGroupDetail":
        from .insight_template_group_detail import InsightTemplateGroupDetail

        return InsightTemplateGroupDetail
    if name == "InsightTemplate":
        from .insight_template import InsightTemplate

        return InsightTemplate
    if name == "InsightTemplateDetail":
        from .insight_template_detail import InsightTemplateDetail

        return InsightTemplateDetail
    if name == "MessageListResponse":
        from .message_list_response import MessageListResponse

        return MessageListResponse
    if name == "ConversationInsightRetrieveAggregatesResponse":
        from .conversation_insight_retrieve_aggregates_response import ConversationInsightRetrieveAggregatesResponse

        return ConversationInsightRetrieveAggregatesResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
