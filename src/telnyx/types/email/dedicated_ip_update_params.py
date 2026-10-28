# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DedicatedIPUpdateParams", "Warmup"]


class DedicatedIPUpdateParams(TypedDict, total=False):
    drain: bool
    """Set together with `force: true` to move the last IP out of its current pool.

    Acknowledges that mail routed to the emptied pool is held. Used only with
    `pool_id`.
    """

    force: bool
    """Set together with `drain: true` to move the last IP out of its current pool.

    Used only with `pool_id`.
    """

    pool_id: str
    """Move the IP to this pool, replacing its current membership.

    Use the IP's current pool to change only its weight. To take an IP out of a
    pool, use `DELETE /email/ip_pools/{id}/ips/{ip_id}`.
    """

    warmup: Warmup
    """Alias for `warmup_paused`."""

    warmup_paused: bool
    """
    Pause (`true`) or resume (`false`) the warm-up ramp; equivalent to the
    `pause_warmup` and `resume_warmup` actions. A Boolean value takes precedence
    over `warmup.paused`. When a pause field is present and `pool_id` is absent,
    supplying neither pause field as a Boolean invokes resume.
    """

    weight: int
    """Routing weight in the target pool. Used only with `pool_id`."""


class Warmup(TypedDict, total=False):
    """Alias for `warmup_paused`."""

    paused: bool
    """Pause (`true`) or resume (`false`) the warm-up ramp.

    Used only when `warmup_paused` is not a Boolean.
    """
