# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel
from .spend_limit_block import SpendLimitBlock
from .spend_limit_period import SpendLimitPeriod

__all__ = ["SpendLimit", "Limit", "CredentialLimit", "CredentialLimitLimit", "Evaluation"]


class Limit(BaseModel):
    """The limit set on the account for the product and period, whoever set it.

    `null` when none is set.
    """

    amount: Optional[str] = None
    """Limit in USD, as a decimal string. `null` when `unlimited` is true."""

    origin: Literal["self_service", "operator"]
    """
    `self_service` when a user of the account set it, `operator` when Telnyx support
    did.
    """

    unlimited: bool
    """True when the limit was set to explicitly no cap."""

    updated_at: datetime
    """When the limit was last set or changed."""


class CredentialLimitLimit(BaseModel):
    """The limit of one API key.

    It always has an amount. `null` for an API key that is still blocked after its limit was removed.
    """

    amount: str
    """Limit in USD, as a decimal string."""

    origin: Literal["self_service", "operator"]
    """
    `self_service` when a user of the account set it, `operator` when Telnyx support
    did.
    """

    updated_at: datetime
    """When the limit was last set or changed."""


class CredentialLimit(BaseModel):
    """The limit, spend and block state of one API key in the product and period."""

    block: Optional[SpendLimitBlock] = None
    """The active block of the period. `null` when the period is not blocked."""

    blocked: bool
    """This API key is blocked for the period."""

    credential_id: str
    """Identifier of the API key as recorded on usage. Never the key's secret."""

    limit: Optional[CredentialLimitLimit] = None
    """The limit of one API key.

    It always has an amount. `null` for an API key that is still blocked after its
    limit was removed.
    """

    spend_error: Optional[str] = None
    """Set when `spend_usd` is `null`."""

    spend_usd: Optional[str] = None
    """Spend in USD in the period made with exactly this API key, as a decimal string.

    Usage without an API key identifier, or with another one, counts only toward the
    total. `null` when it could not be read.
    """

    exceeds_total: Optional[bool] = None
    """The API key's limit is above the period's total limit.

    Only a change by Telnyx support can cause it; the total limit still applies to
    the whole account. Lower the API key limit or raise the total.
    """


class Evaluation(BaseModel):
    """What a create, update or delete did to the period at once.

    Only present in write responses.
    """

    blocked_now: bool
    """The change blocked the product: the spend was already above the new limit."""

    evaluation_deferred: bool
    """The spend could not be checked now.

    The change is saved and applied within a few minutes.
    """

    released: bool
    """The change lifted a block of this period."""

    spend_usd: Optional[str] = None
    """Spend in USD used for the check, as a decimal string.

    `null` when the spend was not checked.
    """

    still_blocked_other_period: bool
    """
    The other period has an active block, so the product stays blocked whatever this
    period's result. For an API key write, the API key's limit in the other period.
    """

    still_over_limit: bool
    """A block of this period remains because the spend is still above the new limit."""

    account_blocked: Optional[bool] = None
    """
    API key writes only: the account itself remains blocked for the product under a
    total limit. Absent for total limit writes.
    """

    note: Optional[str] = None
    """Additional information about the result, when there is any."""


class SpendLimit(BaseModel):
    """The spend limit, spend and block state of one product and period.

    The top-level fields describe the total limit of the account; API key limits are nested in `credential_limits`.
    """

    block: Optional[SpendLimitBlock] = None
    """The active block of the period. `null` when the period is not blocked."""

    blocked: bool
    """The product is blocked for the whole account in this period (total limit).

    An API key's own block appears only in `credential_limits`. Always `false` in
    write responses; list the limits to read the block state.
    """

    effective_limit_usd: Optional[str] = None
    """The limit in USD that is enforced, as a decimal string. `null` means unlimited."""

    limit: Optional[Limit] = None
    """The limit set on the account for the product and period, whoever set it.

    `null` when none is set.
    """

    period: SpendLimitPeriod
    """`daily` is the current UTC day; `monthly` is the current UTC calendar month."""

    period_end: date
    """Exclusive end of the current period, a UTC date."""

    period_start: date
    """First UTC day of the current period."""

    product: str
    """Product the entry applies to."""

    product_name: str
    """Display name of the product."""

    record_type: str
    """Identifies the type of the resource."""

    spend_error: Optional[str] = None
    """Set when `spend_usd` is `null`."""

    spend_usd: Optional[str] = None
    """Spend in USD so far in the period, as a decimal string.

    It can lag actual usage by about a minute. `null` when it could not be read.
    """

    credential_id: Optional[str] = None
    """In write responses, the API key the write was about; `null` for the total limit.

    Always `null` in list entries, which describe the total limit.
    """

    credential_limits: Optional[List[CredentialLimit]] = None
    """List responses only.

    One item per API key limit of the product and period, sorted by `credential_id`,
    plus every API key that is still blocked. `[]` when there are none.
    """

    evaluation: Optional[Evaluation] = None
    """What a create, update or delete did to the period at once.

    Only present in write responses.
    """
