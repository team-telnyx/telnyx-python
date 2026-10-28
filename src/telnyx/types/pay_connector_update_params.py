# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PayConnectorUpdateParams"]


class PayConnectorUpdateParams(TypedDict, total=False):
    config: "GenericPayConnectorConfigParam"
    """Configuration for a generic connector.

    A config update replaces the complete object, not individual keys. Unknown
    config keys are discarded. Authentication credentials must be nonblank strings
    when required by the selected auth_type.
    """

    mode: Literal["test", "live"]
    """Omit to preserve the existing mode. Use an explicit test or live value."""

    type: Literal["generic"]
    """Generic connector type. Omit to preserve the existing value."""


from .generic_pay_connector_config_param import GenericPayConnectorConfigParam
