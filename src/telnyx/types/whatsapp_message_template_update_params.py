# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Iterable, ForwardRef
from typing_extensions import Literal, TypeAlias, TypedDict

__all__ = ["WhatsappMessageTemplateUpdateParams", "Component"]


class WhatsappMessageTemplateUpdateParams(TypedDict, total=False):
    category: Literal["MARKETING", "UTILITY", "AUTHENTICATION"]

    components: Iterable[Component]
    """Updated template components. Same structure as the create request."""


if TYPE_CHECKING:
    Component: TypeAlias = Union[
        "WhatsappTemplateHeaderComponentParam",
        "WhatsappTemplateBodyComponentParam",
        "WhatsappTemplateFooterComponentParam",
        "WhatsappTemplateButtonsComponentParam",
        "WhatsappTemplateCarouselComponentParam",
    ]
else:
    Component = Union[
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).WhatsappTemplateHeaderComponentParam"),
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).WhatsappTemplateBodyComponentParam"),
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).WhatsappTemplateFooterComponentParam"),
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).WhatsappTemplateButtonsComponentParam"),
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).WhatsappTemplateCarouselComponentParam"),
    ]

from .whatsapp.whatsapp_template_body_component_param import WhatsappTemplateBodyComponentParam
from .whatsapp.whatsapp_template_footer_component_param import WhatsappTemplateFooterComponentParam
from .whatsapp.whatsapp_template_header_component_param import WhatsappTemplateHeaderComponentParam
from .whatsapp.whatsapp_template_buttons_component_param import WhatsappTemplateButtonsComponentParam
from .whatsapp.whatsapp_template_carousel_component_param import WhatsappTemplateCarouselComponentParam
