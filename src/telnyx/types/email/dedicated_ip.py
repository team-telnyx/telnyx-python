# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import date, datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DedicatedIP", "Billing", "Provisioning", "ProvisioningChecklist", "Warmup", "WarmupToday"]


class Billing(BaseModel):
    """Monthly recurring charge (MRC) state for the IP's current allocation."""

    charged: Optional[bool] = None
    """True when `status` is `active`, `stopping`, or `stop_failed`.

    An IP carries mail only after its charge has been created.
    """

    status: Optional[
        Literal["not_started", "pending", "in_progress", "active", "stopping", "stopped", "stop_failed", "failed"]
    ] = None
    """`not_started`: no charge recorded for the current allocation.

    `pending`: the charge is queued. `in_progress`: the charge is being created.
    `active`: the MRC is active. `stopping`: release requested; the MRC stop is
    being processed. `stopped`: the MRC has stopped. `stop_failed`: the MRC stop
    failed and the charge remains. `failed`: the charge could not be created.
    """


class ProvisioningChecklist(BaseModel):
    """Informational progress flags for the Telnyx-managed PTR.

    They do not gate `start_warmup`; use `dns_status` to check whether the IP can carry mail.
    """

    forward_confirmed: Optional[bool] = None

    ptr_authored: Optional[bool] = None

    ptr_merged: Optional[bool] = None

    ptr_requested: Optional[bool] = None


class Provisioning(BaseModel):
    """Read-only status of the Telnyx-managed PTR record.

    No customer action is required to complete it.
    """

    checklist: Optional[ProvisioningChecklist] = None
    """Informational progress flags for the Telnyx-managed PTR.

    They do not gate `start_warmup`; use `dns_status` to check whether the IP can
    carry mail.
    """

    dns_status: Optional[Literal["not_applicable", "pending_ptr", "pending_dns", "dns_confirmed", "dns_lost"]] = None
    """`dns_confirmed`: the PTR is forward-confirmed and `dns_confirmed_at` is set.

    `pending_ptr`: the PTR record is not yet in place. `pending_dns`: the PTR record
    is waiting for forward confirmation. `dns_lost`: a previously confirmed PTR no
    longer confirms, or the PTR request was abandoned before it ever confirmed
    (`ptr_request_state` is `abandoned`); the IP carries no mail until DNS is
    confirmed. `not_applicable`: the IP is released or has no PTR record on file.
    """

    ptr_request_pr_url: Optional[str] = None
    """Reference to the Telnyx PTR change request, when one exists. Informational."""

    ptr_request_state: Optional[Literal["pending", "pr_open", "merged", "confirmed", "failed", "abandoned"]] = None
    """
    State of the Telnyx PTR change: `pending`, `pr_open`, `merged`, `confirmed`,
    `failed`, or `abandoned`. Informational.
    """


class WarmupToday(BaseModel):
    """Today's warmup allowance report card (current UTC day).

    Null outside the warmup window (before start_warmup, after release/suspension). `active` IPs report the ramp-complete allowance, except as described for `cap`.
    """

    cap: Optional[int] = None
    """The day's allowance cap.

    Null when the ramp has not opened yet (day 0: the scheduler has not armed a
    stage cap) — distinct from a spent day, which reports the cap with remaining 0.
    `active` IPs report `100000000`, the ramp-complete cap; `complete_warmup`
    applies it to the current day immediately. A day's allowance created before the
    IP became `active` can keep its stored `cap` and `remaining` until the next
    first-attempt send refreshes them.
    """

    day: Optional[date] = None
    """The UTC day this snapshot describes (warmup caps reset at UTC midnight)."""

    granted: Optional[int] = None
    """First-attempt sends released from warmup hold so far today.

    Delivery retries never lease allowance and are not counted.
    """

    remaining: Optional[int] = None
    """Headroom left today.

    A queued send held by the daily cap is explained by remaining == 0; null mirrors
    cap (ramp not open yet). On an `active` IP whose `cap` is below `100000000`,
    remaining == 0 is a stored allowance and does not block the next eligible
    first-attempt send.
    """


class Warmup(BaseModel):
    """Warmup ramp state for a dedicated IP."""

    daily_cap: Optional[int] = None
    """Daily cap of the current ramp stage.

    Null until the scheduler arms the first stage, and cleared when the ramp
    completes, automatically or through `complete_warmup`. On an `active` IP this
    value is informational and can keep an earlier stage cap after a suspension is
    lifted; it does not limit sending.
    """

    paused: Optional[bool] = None
    """True while the ramp is paused."""

    paused_at: Optional[datetime] = None
    """When the ramp was paused. Null when not paused."""

    progress: Optional[int] = None
    """Ramp progress (0-100): the share of the 28 send-day schedule completed.

    Only UTC days on which the IP sent mail count. Set to 100 when the ramp
    completes, automatically or through `complete_warmup`. On an `active` IP this
    value is informational and can keep an earlier value after a suspension is
    lifted.
    """

    started_at: Optional[datetime] = None
    """When `start_warmup` was called. Null before warm-up starts and after release."""

    today: Optional[WarmupToday] = None
    """Today's warmup allowance report card (current UTC day).

    Null outside the warmup window (before start_warmup, after release/suspension).
    `active` IPs report the ramp-complete allowance, except as described for `cap`.
    """


class DedicatedIP(BaseModel):
    """A dedicated sending IP address owned by the account."""

    id: Optional[str] = None

    billing: Optional[Billing] = None
    """Monthly recurring charge (MRC) state for the IP's current allocation."""

    created_at: Optional[datetime] = None

    dns_confirmed_at: Optional[datetime] = None
    """
    When the PTR hostname was forward-confirmed (PTR → hostname → A record → this
    IP). The IP carries mail only while this is set.
    """

    ip_address: Optional[str] = None
    """The allocated IPv4/IPv6 address."""

    ip_version: Optional[Literal["ipv4", "ipv6"]] = None

    pool_id: Optional[str] = None

    provisioning: Optional[Provisioning] = None
    """Read-only status of the Telnyx-managed PTR record.

    No customer action is required to complete it.
    """

    provisioning_status: Optional[
        Literal["not_applicable", "pending_ptr", "pending_dns", "dns_confirmed", "dns_lost"]
    ] = None
    """Same value as `provisioning.dns_status`."""

    ptr_hostname: Optional[str] = None
    """
    Telnyx-managed reverse DNS (PTR) hostname of the IP, in the form
    `mta-<a-b-c-d>.msgtelnyx.com`. Also used as the EHLO hostname when sending from
    the IP. Managed by Telnyx and cannot be changed through the API.
    """

    quarantine_until: Optional[datetime] = None
    """Set on release to 30 days after `released_at`.

    The address is not returned to stock before this time.
    """

    record_type: Optional[Literal["dedicated_ip"]] = None

    region: Optional[str] = None
    """Region label of the allocated IP (for example, `ewr-nj1`)."""

    released_at: Optional[datetime] = None
    """When the IP was released. Null until release."""

    status: Optional[Literal["provisioning", "warming_up", "active", "suspended", "released"]] = None
    """Lifecycle status.

    `provisioning`: purchased and billed, carries no mail until `start_warmup`.
    `warming_up`: warm-up ramp in progress. `active`: ramp complete. `suspended`:
    suspended by Telnyx; carries no mail and is still billed. `released`: returned
    to Telnyx; carries no mail.
    """

    suspension_reason: Optional[str] = None
    """Reason Telnyx recorded when suspending the IP.

    Null unless `status` is `suspended`.
    """

    updated_at: Optional[datetime] = None

    warmup: Optional[Warmup] = None
    """Warmup ramp state for a dedicated IP."""
