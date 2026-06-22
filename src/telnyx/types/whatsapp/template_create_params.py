# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .whatsapp_template_body_component_param import WhatsappTemplateBodyComponentParam
from .whatsapp_template_footer_component_param import WhatsappTemplateFooterComponentParam
from .whatsapp_template_header_component_param import WhatsappTemplateHeaderComponentParam
from .whatsapp_template_buttons_component_param import WhatsappTemplateButtonsComponentParam
from .whatsapp_template_carousel_component_param import WhatsappTemplateCarouselComponentParam

__all__ = ["TemplateCreateParams", "Component"]


class TemplateCreateParams(TypedDict, total=False):
    category: Required[Literal["MARKETING", "UTILITY", "AUTHENTICATION"]]
    """Template category: AUTHENTICATION, UTILITY, or MARKETING."""

    components: Required[Iterable[Component]]
    """Template components defining message structure.

    Passed through to Meta Graph API. Templates with variables must include example
    values. Supports HEADER, BODY, FOOTER, BUTTONS, CAROUSEL and any future Meta
    component types.
    """

    language: Required[str]
    """Template language code (e.g. en_US, es, pt_BR)."""

    name: Required[str]
    """Template name. Lowercase letters, numbers, and underscores only."""

    waba_id: Required[str]
    """The WhatsApp Business Account ID."""


Component: TypeAlias = Union[
    WhatsappTemplateHeaderComponentParam,
    WhatsappTemplateBodyComponentParam,
    WhatsappTemplateFooterComponentParam,
    WhatsappTemplateButtonsComponentParam,
    WhatsappTemplateCarouselComponentParam,
]
