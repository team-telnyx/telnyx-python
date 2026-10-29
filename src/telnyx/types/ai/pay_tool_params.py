# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "PayToolParams",
    "Prompts",
    "PromptsBankAccountNumberUnionMember1",
    "PromptsBankRoutingNumberUnionMember1",
    "PromptsExpirationDateUnionMember1",
    "PromptsPaymentCardNumberUnionMember1",
    "PromptsPostalCodeUnionMember1",
    "PromptsSecurityCodeUnionMember1",
]


class PromptsBankAccountNumberUnionMember1(BaseModel):
    """
    A text-to-speech prompt with optional matching qualifiers, mirroring the Voice API PayPrompt schema.
    """

    text: str
    """Text spoken for the payment collection step."""

    attempt: Optional[str] = None
    """Space-separated 1-based attempt numbers (1-9 followed by digits only, e.g.

    `"2 3"`) for which this prompt applies. A prompt qualified with an attempt
    number above `max_attempts` (default 3) is rejected at write time — it could
    never play.
    """

    card_type: Optional[
        Literal["visa", "mastercard", "amex", "optima", "discover", "diners-club", "jcb", "maestro", "enroute"]
    ] = None
    """Lowercase, case-sensitive detected card type for which this prompt applies."""

    error_type: Optional[
        Literal[
            "timeout",
            "invalid-card-number",
            "invalid-card-type",
            "invalid-date",
            "invalid-security-code",
            "invalid-postal-code",
            "invalid-bank-routing-number",
            "invalid-bank-account-number",
            "input-matching-failed",
        ]
    ] = None
    """Step error for which this prompt applies."""


class PromptsBankRoutingNumberUnionMember1(BaseModel):
    """
    A text-to-speech prompt with optional matching qualifiers, mirroring the Voice API PayPrompt schema.
    """

    text: str
    """Text spoken for the payment collection step."""

    attempt: Optional[str] = None
    """Space-separated 1-based attempt numbers (1-9 followed by digits only, e.g.

    `"2 3"`) for which this prompt applies. A prompt qualified with an attempt
    number above `max_attempts` (default 3) is rejected at write time — it could
    never play.
    """

    card_type: Optional[
        Literal["visa", "mastercard", "amex", "optima", "discover", "diners-club", "jcb", "maestro", "enroute"]
    ] = None
    """Lowercase, case-sensitive detected card type for which this prompt applies."""

    error_type: Optional[
        Literal[
            "timeout",
            "invalid-card-number",
            "invalid-card-type",
            "invalid-date",
            "invalid-security-code",
            "invalid-postal-code",
            "invalid-bank-routing-number",
            "invalid-bank-account-number",
            "input-matching-failed",
        ]
    ] = None
    """Step error for which this prompt applies."""


class PromptsExpirationDateUnionMember1(BaseModel):
    """
    A text-to-speech prompt with optional matching qualifiers, mirroring the Voice API PayPrompt schema.
    """

    text: str
    """Text spoken for the payment collection step."""

    attempt: Optional[str] = None
    """Space-separated 1-based attempt numbers (1-9 followed by digits only, e.g.

    `"2 3"`) for which this prompt applies. A prompt qualified with an attempt
    number above `max_attempts` (default 3) is rejected at write time — it could
    never play.
    """

    card_type: Optional[
        Literal["visa", "mastercard", "amex", "optima", "discover", "diners-club", "jcb", "maestro", "enroute"]
    ] = None
    """Lowercase, case-sensitive detected card type for which this prompt applies."""

    error_type: Optional[
        Literal[
            "timeout",
            "invalid-card-number",
            "invalid-card-type",
            "invalid-date",
            "invalid-security-code",
            "invalid-postal-code",
            "invalid-bank-routing-number",
            "invalid-bank-account-number",
            "input-matching-failed",
        ]
    ] = None
    """Step error for which this prompt applies."""


class PromptsPaymentCardNumberUnionMember1(BaseModel):
    """
    A text-to-speech prompt with optional matching qualifiers, mirroring the Voice API PayPrompt schema.
    """

    text: str
    """Text spoken for the payment collection step."""

    attempt: Optional[str] = None
    """Space-separated 1-based attempt numbers (1-9 followed by digits only, e.g.

    `"2 3"`) for which this prompt applies. A prompt qualified with an attempt
    number above `max_attempts` (default 3) is rejected at write time — it could
    never play.
    """

    card_type: Optional[
        Literal["visa", "mastercard", "amex", "optima", "discover", "diners-club", "jcb", "maestro", "enroute"]
    ] = None
    """Lowercase, case-sensitive detected card type for which this prompt applies."""

    error_type: Optional[
        Literal[
            "timeout",
            "invalid-card-number",
            "invalid-card-type",
            "invalid-date",
            "invalid-security-code",
            "invalid-postal-code",
            "invalid-bank-routing-number",
            "invalid-bank-account-number",
            "input-matching-failed",
        ]
    ] = None
    """Step error for which this prompt applies."""


class PromptsPostalCodeUnionMember1(BaseModel):
    """
    A text-to-speech prompt with optional matching qualifiers, mirroring the Voice API PayPrompt schema.
    """

    text: str
    """Text spoken for the payment collection step."""

    attempt: Optional[str] = None
    """Space-separated 1-based attempt numbers (1-9 followed by digits only, e.g.

    `"2 3"`) for which this prompt applies. A prompt qualified with an attempt
    number above `max_attempts` (default 3) is rejected at write time — it could
    never play.
    """

    card_type: Optional[
        Literal["visa", "mastercard", "amex", "optima", "discover", "diners-club", "jcb", "maestro", "enroute"]
    ] = None
    """Lowercase, case-sensitive detected card type for which this prompt applies."""

    error_type: Optional[
        Literal[
            "timeout",
            "invalid-card-number",
            "invalid-card-type",
            "invalid-date",
            "invalid-security-code",
            "invalid-postal-code",
            "invalid-bank-routing-number",
            "invalid-bank-account-number",
            "input-matching-failed",
        ]
    ] = None
    """Step error for which this prompt applies."""


class PromptsSecurityCodeUnionMember1(BaseModel):
    """
    A text-to-speech prompt with optional matching qualifiers, mirroring the Voice API PayPrompt schema.
    """

    text: str
    """Text spoken for the payment collection step."""

    attempt: Optional[str] = None
    """Space-separated 1-based attempt numbers (1-9 followed by digits only, e.g.

    `"2 3"`) for which this prompt applies. A prompt qualified with an attempt
    number above `max_attempts` (default 3) is rejected at write time — it could
    never play.
    """

    card_type: Optional[
        Literal["visa", "mastercard", "amex", "optima", "discover", "diners-club", "jcb", "maestro", "enroute"]
    ] = None
    """Lowercase, case-sensitive detected card type for which this prompt applies."""

    error_type: Optional[
        Literal[
            "timeout",
            "invalid-card-number",
            "invalid-card-type",
            "invalid-date",
            "invalid-security-code",
            "invalid-postal-code",
            "invalid-bank-routing-number",
            "invalid-bank-account-number",
            "input-matching-failed",
        ]
    ] = None
    """Step error for which this prompt applies."""


class Prompts(BaseModel):
    """Custom text-to-speech prompts keyed by payment collection step.

    The AI assistant merges its own card-number prompt into this map, matching on the same step keys.
    """

    bank_account_number: Union[str, List[PromptsBankAccountNumberUnionMember1], None] = FieldInfo(
        alias="bank-account-number", default=None
    )
    """A default prompt string or an ordered list of qualified prompts."""

    bank_routing_number: Union[str, List[PromptsBankRoutingNumberUnionMember1], None] = FieldInfo(
        alias="bank-routing-number", default=None
    )
    """A default prompt string or an ordered list of qualified prompts."""

    expiration_date: Union[str, List[PromptsExpirationDateUnionMember1], None] = FieldInfo(
        alias="expiration-date", default=None
    )
    """A default prompt string or an ordered list of qualified prompts."""

    payment_card_number: Union[str, List[PromptsPaymentCardNumberUnionMember1], None] = FieldInfo(
        alias="payment-card-number", default=None
    )
    """A default prompt string or an ordered list of qualified prompts."""

    postal_code: Union[str, List[PromptsPostalCodeUnionMember1], None] = FieldInfo(alias="postal-code", default=None)
    """A default prompt string or an ordered list of qualified prompts."""

    security_code: Union[str, List[PromptsSecurityCodeUnionMember1], None] = FieldInfo(
        alias="security-code", default=None
    )
    """A default prompt string or an ordered list of qualified prompts."""


class PayToolParams(BaseModel):
    connector_name: str
    """The name of the pay connector configured in the Telnyx API.

    Must reference an existing pay connector for this organization.
    """

    connector_parameters: Optional[Dict[str, object]] = None
    """
    Custom key/value parameters forwarded to the pay connector as `parameters` in
    the processor request. String values may use `{{dynamic_variable}}` templating,
    resolved per call.
    """

    currency: Optional[str] = None
    """Default currency for payments processed by this tool."""

    description: Optional[str] = None
    """
    Description of the pay tool shown to the assistant so it knows when to call the
    tool. Not sent to the payment connector — the per-call `description` argument
    the assistant passes is what reaches the processor.
    """

    inter_digit_timeout_millis: Optional[int] = None
    """Time in milliseconds to wait between consecutive DTMF digits.

    Omitted means the platform default (5000) applies.
    """

    max_attempts: Optional[int] = None
    """Maximum number of attempts for each payment collection step.

    Omitted means the platform default (3) applies.
    """

    min_postal_code_length: Optional[int] = None
    """
    Minimum number of digits the caller must enter when collecting a credit-card
    billing postal code. Applies only when `postal_code` prompts the caller. Omitted
    means the platform default (1) applies. The maximum number of digits collected
    is the greater of 10 and this value. This does not validate the length of a
    postal code supplied directly in `postal_code`.
    """

    payment_method: Optional[str] = None
    """Default payment method for payments processed by this tool."""

    postal_code: Union[str, bool, None] = None
    """Controls billing postal code collection for credit-card payments.

    Set to `false` to skip the postal code prompt without supplying a postal code to
    the payment connector (non-US cards, e.g. Irish Eircodes). Set to `true` to
    prompt the caller. Supply a non-empty string, such as `"90210"`, to use that
    postal code without prompting. This option does not affect ACH debit payments or
    payments using an existing token.
    """

    prompts: Optional[Prompts] = None
    """Custom text-to-speech prompts keyed by payment collection step.

    The AI assistant merges its own card-number prompt into this map, matching on
    the same step keys.
    """

    timeout_millis: Optional[int] = None
    """Time in milliseconds to wait for DTMF input for each collection step.

    Omitted means the platform default (5000) applies. Increase this for slower
    entry, e.g. a 16-digit card number.
    """

    valid_card_types: Optional[
        List[Literal["visa", "mastercard", "amex", "maestro", "discover", "optima", "jcb", "diners-club", "enroute"]]
    ] = None
    """Restricts accepted card numbers to the listed card types.

    When the caller enters a card number that does not match one of the listed
    types, Pay treats the input as invalid and re-prompts for the card number.
    """
