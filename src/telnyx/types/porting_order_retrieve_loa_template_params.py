# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PortingOrderRetrieveLoaTemplateParams"]


class PortingOrderRetrieveLoaTemplateParams(TypedDict, total=False):
    loa_configuration_id: str
    """The identifier of the LOA configuration to use for the template.

    If not provided, the default LOA configuration will be used.
    """
