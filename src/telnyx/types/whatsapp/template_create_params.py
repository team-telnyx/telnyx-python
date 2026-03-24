# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "TemplateCreateParams",
    "Component",
    "ComponentHeader",
    "ComponentHeaderExample",
    "ComponentBody",
    "ComponentBodyExample",
    "ComponentFooter",
    "ComponentButtons",
    "ComponentButtonsButton",
    "ComponentCarousel",
    "ComponentCarouselCard",
]


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


class ComponentHeaderExample(TypedDict, total=False):
    """Sample values for header variables."""

    header_handle: SequenceNotStr[str]
    """Media handle for IMAGE, VIDEO, or DOCUMENT headers."""

    header_text: SequenceNotStr[str]
    """Sample values for text header variables."""


class ComponentHeader(TypedDict, total=False):
    """Optional header displayed at the top of the message."""

    format: Required[Literal["TEXT", "IMAGE", "VIDEO", "DOCUMENT", "LOCATION"]]
    """
    Header format type: TEXT (supports one variable), IMAGE, VIDEO, DOCUMENT, or
    LOCATION.
    """

    type: Required[Literal["HEADER"]]

    example: ComponentHeaderExample
    """Sample values for header variables."""

    text: str
    """Header text.

    Required when format is TEXT. Supports one variable ({{1}}). Variables cannot be
    at the start or end.
    """


class ComponentBodyExample(TypedDict, total=False):
    """Sample values for body variables. Required when body text contains parameters."""

    body_text: Iterable[SequenceNotStr[str]]
    """Array containing one array of sample values, one per variable in order."""


class ComponentBody(TypedDict, total=False):
    """The main text content of the message.

    Supports multiple variable parameters ({{1}}, {{2}}, etc.). Variables cannot be at the start or end. Maximum 1024 characters.
    """

    type: Required[Literal["BODY"]]

    example: ComponentBodyExample
    """Sample values for body variables. Required when body text contains parameters."""

    text: str
    """Body text content.

    Use {{1}}, {{2}}, etc. for variable placeholders. Required for MARKETING and
    UTILITY templates. Optional for AUTHENTICATION templates where Meta provides the
    built-in OTP body.
    """


class ComponentFooter(TypedDict, total=False):
    """Optional footer displayed at the bottom of the message.

    Does not support variables.
    """

    type: Required[Literal["FOOTER"]]

    code_expiration_minutes: int
    """OTP code expiration time in minutes.

    Used in AUTHENTICATION template footers instead of free-form text.
    """

    text: str
    """Footer text. Maximum 60 characters. For non-authentication templates."""


class ComponentButtonsButton(TypedDict, total=False):
    type: Required[Literal["URL", "PHONE_NUMBER", "QUICK_REPLY", "OTP", "COPY_CODE", "FLOW"]]

    autofill_text: str
    """Custom autofill button text for ONE_TAP OTP buttons."""

    example: SequenceNotStr[str]
    """Sample values for URL variable."""

    flow_action: Literal["navigate", "data_exchange"]
    """Flow action type for FLOW-type buttons."""

    flow_id: str
    """Flow ID for FLOW-type buttons."""

    navigate_screen: str
    """Target screen name for FLOW buttons with navigate action."""

    otp_type: Literal["COPY_CODE", "ONE_TAP"]

    package_name: str
    """Android package name. Required for ONE_TAP OTP buttons."""

    phone_number: str
    """Phone number in E.164 format."""

    signature_hash: str
    """Android app signing key hash. Required for ONE_TAP OTP buttons."""

    text: str
    """Button label text.

    Maximum 25 characters. Required for URL, PHONE_NUMBER, and QUICK_REPLY buttons.
    Not required for OTP buttons (Meta supplies the label).
    """

    url: str
    """URL for URL-type buttons. Supports one variable ({{1}})."""

    zero_tap_terms_accepted: bool
    """Whether zero-tap terms have been accepted."""


class ComponentButtons(TypedDict, total=False):
    """Optional interactive buttons. Maximum 3 buttons per template."""

    buttons: Required[Iterable[ComponentButtonsButton]]
    """Array of button objects. Meta supports various combinations of button types."""

    type: Required[Literal["BUTTONS"]]


class ComponentCarouselCard(TypedDict, total=False):
    components: Iterable[Dict[str, object]]


class ComponentCarousel(TypedDict, total=False):
    """Carousel component for multi-card templates.

    Each card can contain its own header, body, and buttons.
    """

    cards: Required[Iterable[ComponentCarouselCard]]
    """Array of card objects, each with its own components."""

    type: Required[Literal["CAROUSEL"]]


Component: TypeAlias = Union[ComponentHeader, ComponentBody, ComponentFooter, ComponentButtons, ComponentCarousel]
