# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .action_reply_params import ActionReplyParams as ActionReplyParams
from .label_create_params import LabelCreateParams as LabelCreateParams
from .action_forward_params import ActionForwardParams as ActionForwardParams
from .action_reply_all_params import ActionReplyAllParams as ActionReplyAllParams
from .label_delete_all_params import LabelDeleteAllParams as LabelDeleteAllParams
from .inbox_action_recipient_input_param import InboxActionRecipientInputParam as InboxActionRecipientInputParam
from .inbox_action_email_address_input_param import (
    InboxActionEmailAddressInputParam as InboxActionEmailAddressInputParam,
)

if TYPE_CHECKING:
    from .label_create_response import LabelCreateResponse as LabelCreateResponse
    from .label_delete_all_response import LabelDeleteAllResponse as LabelDeleteAllResponse


def __getattr__(name: str) -> Any:
    if name == "LabelCreateResponse":
        from .label_create_response import LabelCreateResponse

        return LabelCreateResponse
    if name == "LabelDeleteAllResponse":
        from .label_delete_all_response import LabelDeleteAllResponse

        return LabelDeleteAllResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
