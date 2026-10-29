# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "PayToolParamsParam",
    "Prompts",
    "PromptsBankAccountNumberUnionMember1",
    "PromptsBankRoutingNumberUnionMember1",
    "PromptsExpirationDateUnionMember1",
    "PromptsPaymentCardNumberUnionMember1",
    "PromptsPostalCodeUnionMember1",
    "PromptsSecurityCodeUnionMember1",
]


class PromptsBankAccountNumberUnionMember1(TypedDict, total=False):
    """
    A text-to-speech prompt with optional matching qualifiers, mirroring the Voice API PayPrompt schema.
    """

    text: Required[str]
    """Text spoken for the payment collection step."""

    attempt: str
    """Space-separated 1-based attempt numbers (1-9 followed by digits only, e.g.

    `"2 3"`) for which this prompt applies. A prompt qualified with an attempt
    number above `max_attempts` (default 3) is rejected at write time — it could
    never play.
    """

    card_type: Literal["visa", "mastercard", "amex", "optima", "discover", "diners-club", "jcb", "maestro", "enroute"]
    """Lowercase, case-sensitive detected card type for which this prompt applies."""

    error_type: Literal[
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
    """Step error for which this prompt applies."""


class PromptsBankRoutingNumberUnionMember1(TypedDict, total=False):
    """
    A text-to-speech prompt with optional matching qualifiers, mirroring the Voice API PayPrompt schema.
    """

    text: Required[str]
    """Text spoken for the payment collection step."""

    attempt: str
    """Space-separated 1-based attempt numbers (1-9 followed by digits only, e.g.

    `"2 3"`) for which this prompt applies. A prompt qualified with an attempt
    number above `max_attempts` (default 3) is rejected at write time — it could
    never play.
    """

    card_type: Literal["visa", "mastercard", "amex", "optima", "discover", "diners-club", "jcb", "maestro", "enroute"]
    """Lowercase, case-sensitive detected card type for which this prompt applies."""

    error_type: Literal[
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
    """Step error for which this prompt applies."""


class PromptsExpirationDateUnionMember1(TypedDict, total=False):
    """
    A text-to-speech prompt with optional matching qualifiers, mirroring the Voice API PayPrompt schema.
    """

    text: Required[str]
    """Text spoken for the payment collection step."""

    attempt: str
    """Space-separated 1-based attempt numbers (1-9 followed by digits only, e.g.

    `"2 3"`) for which this prompt applies. A prompt qualified with an attempt
    number above `max_attempts` (default 3) is rejected at write time — it could
    never play.
    """

    card_type: Literal["visa", "mastercard", "amex", "optima", "discover", "diners-club", "jcb", "maestro", "enroute"]
    """Lowercase, case-sensitive detected card type for which this prompt applies."""

    error_type: Literal[
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
    """Step error for which this prompt applies."""


class PromptsPaymentCardNumberUnionMember1(TypedDict, total=False):
    """
    A text-to-speech prompt with optional matching qualifiers, mirroring the Voice API PayPrompt schema.
    """

    text: Required[str]
    """Text spoken for the payment collection step."""

    attempt: str
    """Space-separated 1-based attempt numbers (1-9 followed by digits only, e.g.

    `"2 3"`) for which this prompt applies. A prompt qualified with an attempt
    number above `max_attempts` (default 3) is rejected at write time — it could
    never play.
    """

    card_type: Literal["visa", "mastercard", "amex", "optima", "discover", "diners-club", "jcb", "maestro", "enroute"]
    """Lowercase, case-sensitive detected card type for which this prompt applies."""

    error_type: Literal[
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
    """Step error for which this prompt applies."""


class PromptsPostalCodeUnionMember1(TypedDict, total=False):
    """
    A text-to-speech prompt with optional matching qualifiers, mirroring the Voice API PayPrompt schema.
    """

    text: Required[str]
    """Text spoken for the payment collection step."""

    attempt: str
    """Space-separated 1-based attempt numbers (1-9 followed by digits only, e.g.

    `"2 3"`) for which this prompt applies. A prompt qualified with an attempt
    number above `max_attempts` (default 3) is rejected at write time — it could
    never play.
    """

    card_type: Literal["visa", "mastercard", "amex", "optima", "discover", "diners-club", "jcb", "maestro", "enroute"]
    """Lowercase, case-sensitive detected card type for which this prompt applies."""

    error_type: Literal[
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
    """Step error for which this prompt applies."""


class PromptsSecurityCodeUnionMember1(TypedDict, total=False):
    """
    A text-to-speech prompt with optional matching qualifiers, mirroring the Voice API PayPrompt schema.
    """

    text: Required[str]
    """Text spoken for the payment collection step."""

    attempt: str
    """Space-separated 1-based attempt numbers (1-9 followed by digits only, e.g.

    `"2 3"`) for which this prompt applies. A prompt qualified with an attempt
    number above `max_attempts` (default 3) is rejected at write time — it could
    never play.
    """

    card_type: Literal["visa", "mastercard", "amex", "optima", "discover", "diners-club", "jcb", "maestro", "enroute"]
    """Lowercase, case-sensitive detected card type for which this prompt applies."""

    error_type: Literal[
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
    """Step error for which this prompt applies."""


class Prompts(TypedDict, total=False):
    """Custom text-to-speech prompts keyed by payment collection step.

    The AI assistant merges its own card-number prompt into this map, matching on the same step keys.
    """

    bank_account_number: Annotated[
        Union[str, Iterable[PromptsBankAccountNumberUnionMember1]], PropertyInfo(alias="bank-account-number")
    ]
    """A default prompt string or an ordered list of qualified prompts."""

    bank_routing_number: Annotated[
        Union[str, Iterable[PromptsBankRoutingNumberUnionMember1]], PropertyInfo(alias="bank-routing-number")
    ]
    """A default prompt string or an ordered list of qualified prompts."""

    expiration_date: Annotated[
        Union[str, Iterable[PromptsExpirationDateUnionMember1]], PropertyInfo(alias="expiration-date")
    ]
    """A default prompt string or an ordered list of qualified prompts."""

    payment_card_number: Annotated[
        Union[str, Iterable[PromptsPaymentCardNumberUnionMember1]], PropertyInfo(alias="payment-card-number")
    ]
    """A default prompt string or an ordered list of qualified prompts."""

    postal_code: Annotated[Union[str, Iterable[PromptsPostalCodeUnionMember1]], PropertyInfo(alias="postal-code")]
    """A default prompt string or an ordered list of qualified prompts."""

    security_code: Annotated[Union[str, Iterable[PromptsSecurityCodeUnionMember1]], PropertyInfo(alias="security-code")]
    """A default prompt string or an ordered list of qualified prompts."""


class PayToolParamsParam(TypedDict, total=False):
    connector_name: Required[str]
    """The name of the pay connector configured in the Telnyx API.

    Must reference an existing pay connector for this organization.
    """

    connector_parameters: Dict[str, object]
    """
    Custom key/value parameters forwarded to the pay connector as `parameters` in
    the processor request. String values may use `{{dynamic_variable}}` templating,
    resolved per call.
    """

    currency: str
    """Default currency for payments processed by this tool."""

    description: Optional[str]
    """
    Description of the pay tool shown to the assistant so it knows when to call the
    tool. Not sent to the payment connector — the per-call `description` argument
    the assistant passes is what reaches the processor.
    """

    inter_digit_timeout_millis: int
    """Time in milliseconds to wait between consecutive DTMF digits.

    Omitted means the platform default (5000) applies.
    """

    max_attempts: int
    """Maximum number of attempts for each payment collection step.

    Omitted means the platform default (3) applies.
    """

    min_postal_code_length: int
    """
    Minimum number of digits the caller must enter when collecting a credit-card
    billing postal code. Applies only when `postal_code` prompts the caller. Omitted
    means the platform default (1) applies. The maximum number of digits collected
    is the greater of 10 and this value. This does not validate the length of a
    postal code supplied directly in `postal_code`.
    """

    payment_method: str
    """Default payment method for payments processed by this tool."""

    postal_code: Union[str, bool]
    """Controls billing postal code collection for credit-card payments.

    Set to `false` to skip the postal code prompt without supplying a postal code to
    the payment connector (non-US cards, e.g. Irish Eircodes). Set to `true` to
    prompt the caller. Supply a non-empty string, such as `"90210"`, to use that
    postal code without prompting. This option does not affect ACH debit payments or
    payments using an existing token.
    """

    prompts: Prompts
    """Custom text-to-speech prompts keyed by payment collection step.

    The AI assistant merges its own card-number prompt into this map, matching on
    the same step keys.
    """

    timeout_millis: int
    """Time in milliseconds to wait for DTMF input for each collection step.

    Omitted means the platform default (5000) applies. Increase this for slower
    entry, e.g. a 16-digit card number.
    """

    valid_card_types: List[
        Literal["visa", "mastercard", "amex", "maestro", "discover", "optima", "jcb", "diners-club", "enroute"]
    ]
    """Restricts accepted card numbers to the listed card types.

    When the caller enters a card number that does not match one of the listed
    types, Pay treats the input as invalid and re-prompts for the card number.
    """
