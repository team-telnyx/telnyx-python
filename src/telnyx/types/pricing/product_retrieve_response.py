# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional

from ..._models import BaseModel
from .pricing_tier import PricingTier

__all__ = ["ProductRetrieveResponse"]


class ProductRetrieveResponse(BaseModel):
    """A single pricing entry.

    Standard products include rate, unit, currency, type, country_iso, direction, and tiers. Inference products include model, input_rate, output_rate, cached_input_rate, and their respective tier arrays. Rate-deck products include pricing_type and note fields with null rate and empty tiers.
    """

    cached_input_rate: Optional[str] = None
    """Cached input token rate. Present only on inference product entries."""

    cached_input_tiers: Optional[List[PricingTier]] = None
    """Cached input token tiered pricing. Present only on inference product entries."""

    country_iso: Optional[str] = None
    """ISO country code. Null for non-geographic products."""

    currency: Optional[str] = None
    """ISO currency code (e.g., USD)."""

    direction: Optional[str] = None
    """Direction (e.g., termination). Null for non-directional products."""

    input_rate: Optional[str] = None
    """Input token rate. Present only on inference product entries."""

    input_tiers: Optional[List[PricingTier]] = None
    """Input token tiered pricing. Present only on inference product entries."""

    model: Optional[str] = None
    """Model identifier. Present only on inference product entries."""

    name: Optional[str] = None
    """Human-readable name describing the pricing entry."""

    note: Optional[str] = None
    """
    Additional note for rate-deck products (e.g., "Pricing is determined by the
    WhatsApp rate deck.").
    """

    output_rate: Optional[str] = None
    """Output token rate. Present only on inference product entries."""

    output_tiers: Optional[List[PricingTier]] = None
    """Output token tiered pricing. Present only on inference product entries."""

    pricing_type: Optional[str] = None
    """Pricing type for non-standard products (e.g., rate_deck).

    Absent on standard products.
    """

    rate: Union[float, str, None] = None
    """Per-unit rate.

    Numeric for standard products, string for inference products. Null for rate-deck
    products.
    """

    tiers: Optional[List[PricingTier]] = None
    """Volume-based tiered pricing. Empty for rate-deck products."""

    type: Optional[str] = None
    """Pricing type (e.g., usage)."""

    unit: Optional[str] = None
    """Unit of measurement (e.g., part, message, GB, per_1k_tokens)."""
