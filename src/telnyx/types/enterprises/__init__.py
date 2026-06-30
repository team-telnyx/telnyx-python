# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .dir_list_params import DirListParams as DirListParams
from .dir_create_params import DirCreateParams as DirCreateParams
from .reputation_enable_params import ReputationEnableParams as ReputationEnableParams
from .reputation_check_frequency import ReputationCheckFrequency as ReputationCheckFrequency
from .reputation_update_frequency_params import ReputationUpdateFrequencyParams as ReputationUpdateFrequencyParams

if TYPE_CHECKING:
    from .enterprise_reputation_public import EnterpriseReputationPublic as EnterpriseReputationPublic
    from .enterprise_reputation_public_wrapped import (
        EnterpriseReputationPublicWrapped as EnterpriseReputationPublicWrapped,
    )


def __getattr__(name: str) -> Any:
    if name == "EnterpriseReputationPublic":
        from .enterprise_reputation_public import EnterpriseReputationPublic

        return EnterpriseReputationPublic
    if name == "EnterpriseReputationPublicWrapped":
        from .enterprise_reputation_public_wrapped import EnterpriseReputationPublicWrapped

        return EnterpriseReputationPublicWrapped
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
