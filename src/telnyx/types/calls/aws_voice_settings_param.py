# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["AwsVoiceSettingsParam"]


class AwsVoiceSettingsParamTyped(TypedDict, total=False):
    type: Required[Literal["aws"]]
    """Voice settings provider type"""


AwsVoiceSettingsParam: TypeAlias = Union[AwsVoiceSettingsParamTyped, Dict[str, object]]
