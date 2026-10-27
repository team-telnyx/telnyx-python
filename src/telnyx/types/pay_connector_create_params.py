# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PayConnectorCreateParams"]


class PayConnectorCreateParams(TypedDict, total=False):
    config: Required["GenericPayConnectorConfigParam"]
    """Configuration for a generic connector.

    A config update replaces the complete object, not individual keys. Unknown
    config keys are discarded. Authentication credentials must be nonblank strings
    when required by the selected auth_type.
    """

    name: Required[str]
    """Unique within the authenticated organization.

    Used in resource paths and as connector_name in the Call Control Pay request.
    Cannot be renamed by update.
    """

    mode: Literal["test", "live"]
    """Defaults to test on creation.

    Test restricts collected card numbers but still contacts the configured
    processor; use a processor sandbox URL and sandbox credentials. Live removes the
    test-card restriction. Neither mode locks API updates.
    """

    type: Literal["generic"]
    """Connector type covered by this reference."""


from .generic_pay_connector_config_param import GenericPayConnectorConfigParam
