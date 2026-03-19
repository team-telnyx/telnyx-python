# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "CreditAccountCreatePaymentQuoteResponse",
    "Data",
    "DataPaymentRequirements",
    "DataPaymentRequirementsAccept",
    "DataPaymentRequirementsAcceptExtra",
    "DataPaymentRequirementsResource",
]


class DataPaymentRequirementsAcceptExtra(BaseModel):
    """
    Additional scheme-specific parameters including EIP-712 domain info and the facilitator URL.
    """

    facilitator_url: Optional[str] = FieldInfo(alias="facilitatorUrl", default=None)

    name: Optional[str] = None
    """EIP-712 domain name (e.g. "USD Coin")."""

    quote_id: Optional[str] = FieldInfo(alias="quoteId", default=None)

    version: Optional[str] = None
    """EIP-712 domain version."""


class DataPaymentRequirementsAccept(BaseModel):
    amount: Optional[str] = None
    """Amount in the token's smallest unit."""

    asset: Optional[str] = None
    """Token contract address (e.g. USDC on Base)."""

    extra: Optional[DataPaymentRequirementsAcceptExtra] = None
    """
    Additional scheme-specific parameters including EIP-712 domain info and the
    facilitator URL.
    """

    max_timeout_seconds: Optional[int] = FieldInfo(alias="maxTimeoutSeconds", default=None)
    """Maximum time in seconds before the payment authorization expires."""

    network: Optional[str] = None
    """Blockchain network identifier in CAIP-2 format (e.g. "eip155:8453" for Base)."""

    pay_to: Optional[str] = FieldInfo(alias="payTo", default=None)
    """Recipient wallet address."""

    scheme: Optional[str] = None
    """Payment scheme (e.g. "exact")."""


class DataPaymentRequirementsResource(BaseModel):
    """The resource being paid for. Included in the payment signature."""

    description: Optional[str] = None
    """Human-readable description of the payment."""

    mime_type: Optional[str] = FieldInfo(alias="mimeType", default=None)
    """MIME type of the resource."""

    url: Optional[str] = None
    """Canonical URL of the payment resource."""


class DataPaymentRequirements(BaseModel):
    """x402 protocol v2 payment requirements.

    Contains all information needed to construct and sign a payment authorization.
    """

    accepts: Optional[List[DataPaymentRequirementsAccept]] = None
    """Accepted payment schemes. Currently only the `exact` EVM scheme is supported."""

    resource: Optional[DataPaymentRequirementsResource] = None
    """The resource being paid for. Included in the payment signature."""

    x402_version: Optional[Literal[2]] = FieldInfo(alias="x402Version", default=None)
    """x402 protocol version. Currently always 2."""


class Data(BaseModel):
    id: Optional[str] = None
    """Unique quote identifier. Use this to settle the payment."""

    amount_crypto: Optional[str] = None
    """The equivalent amount in the payment cryptocurrency's smallest unit (e.g.

    USDC has 6 decimals, so $50.00 = "50000000").
    """

    amount_usd: Optional[str] = None
    """The quoted amount in USD."""

    expires_at: Optional[datetime] = None
    """ISO 8601 timestamp when the quote expires."""

    network: Optional[str] = None
    """The blockchain network for the payment in CAIP-2 format (e.g.

    eip155:8453 for Base).
    """

    payment_requirements: Optional[DataPaymentRequirements] = None
    """x402 protocol v2 payment requirements.

    Contains all information needed to construct and sign a payment authorization.
    """

    record_type: Optional[Literal["quote"]] = None


class CreditAccountCreatePaymentQuoteResponse(BaseModel):
    data: Optional[Data] = None
