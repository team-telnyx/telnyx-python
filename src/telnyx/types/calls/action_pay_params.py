# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo
from .pay_prompt_value_param import PayPromptValueParam

__all__ = ["ActionPayParams", "Prompts"]


class ActionPayParams(TypedDict, total=False):
    amount: float
    """Amount to charge. Required when `transaction_type` is `charge`."""

    client_state: str
    """Base64-encoded state included in subsequent webhooks."""

    command_id: str
    """Idempotency key for the command.

    Telnyx ignores a duplicate command with the same `command_id` for the same
    `call_control_id`.
    """

    connector_name: str
    """Name of the Pay connector used to process the transaction."""

    currency: Literal["USD", "usd"]
    """Currency used for the transaction. Pay currently supports USD only."""

    description: str
    """Optional description forwarded with the payment transaction."""

    inter_digit_timeout_millis: int
    """Time in milliseconds to wait between consecutive DTMF digits."""

    language: str
    """Language used for payment prompts."""

    max_attempts: int
    """Maximum number of attempts for each payment collection step."""

    metadata: Dict[str, object]
    """Metadata forwarded to the Pay connector."""

    parameters: Dict[str, object]
    """Additional parameters forwarded to the Pay connector."""

    payment_method: Literal["credit-card", "ach-debit"]
    """Payment method to collect."""

    payment_token: str
    """Existing payment token. When supplied, payment-detail collection is skipped."""

    prompts: Prompts
    """Custom text-to-speech prompts keyed by payment collection step."""

    service_level: str
    """Speech synthesis service level used for payment prompts.

    Pay defaults to `premium`.
    """

    timeout_millis: int
    """Time in milliseconds to wait for DTMF input for each collection step."""

    transaction_type: Literal["charge", "tokenize"]
    """Transaction to perform.

    If omitted, Pay infers `tokenize` when `amount` is absent or zero and `charge`
    when `amount` is positive.
    """

    valid_card_types: List[
        Literal["visa", "mastercard", "amex", "maestro", "discover", "optima", "jcb", "diners-club", "enroute"]
    ]
    """Restricts accepted card numbers to the listed card types.

    When the caller enters a card number that does not match one of the listed
    types, Pay treats the input as invalid and re-prompts for the card number.
    Cannot be used together with `payment_token`.
    """

    voice: str
    """Voice used for payment prompts.

    Accepts `male`, `female`, or a provider voice in `<Provider>.<Model>.<VoiceId>`
    format, for example `AWS.Polly.Joanna` or `Telnyx.KokoroTTS.af`.
    """


class Prompts(TypedDict, total=False):
    """Custom text-to-speech prompts keyed by payment collection step."""

    bank_account_number: Annotated[PayPromptValueParam, PropertyInfo(alias="bank-account-number")]
    """A default prompt string or an ordered list of qualified prompts."""

    bank_routing_number: Annotated[PayPromptValueParam, PropertyInfo(alias="bank-routing-number")]
    """A default prompt string or an ordered list of qualified prompts."""

    expiration_date: Annotated[PayPromptValueParam, PropertyInfo(alias="expiration-date")]
    """A default prompt string or an ordered list of qualified prompts."""

    payment_card_number: Annotated[PayPromptValueParam, PropertyInfo(alias="payment-card-number")]
    """A default prompt string or an ordered list of qualified prompts."""

    postal_code: Annotated[PayPromptValueParam, PropertyInfo(alias="postal-code")]
    """A default prompt string or an ordered list of qualified prompts."""

    security_code: Annotated[PayPromptValueParam, PropertyInfo(alias="security-code")]
    """A default prompt string or an ordered list of qualified prompts."""
