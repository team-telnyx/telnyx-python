# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["UserProfilePatchAllParams"]


class UserProfilePatchAllParams(TypedDict, total=False):
    address_1: Optional[str]
    """First line of the profile address."""

    address_2: Optional[str]
    """Second line of the profile address."""

    business_name: Optional[str]
    """Business name associated with the profile."""

    city: Optional[str]
    """City in the profile address."""

    company_size: str
    """Company size reported by the user."""

    country: Optional[str]
    """Country code in the profile address."""

    data_locality: Literal["USA", "DEU", "AUS", "UAE", "CAN"]
    """
    Data locality: USA (United States), DEU (Germany), AUS (Australia), UAE (United
    Arab Emirates), or CAN (Canada). A change is permitted only if data locality has
    not previously been changed. A successful change sets data_locality_updated_at
    and initializes data_locality_migration_status to not_started.
    """

    default_managed_account_allow_custom_pricing: bool
    """Default custom-pricing setting for managed accounts."""

    default_managed_account_inherit_emergency_terms_of_service: bool
    """
    Default emergency terms-of-service inheritance setting for managed accounts,
    where supported.
    """

    default_managed_account_rollup_billing: bool
    """Default rollup-billing setting for managed accounts."""

    default_notify_manager_account: bool
    """Default setting for notifying the manager account."""

    default_numbers_external_pin: str
    """Default alphanumeric external PIN for phone numbers."""

    first_name: Optional[str]
    """The user's first name."""

    got_free_number_at_signup: bool
    """Whether the user received a free number at signup."""

    last_name: Optional[str]
    """The user's last name."""

    low_balance_notification_frequency: Optional[Literal[2, 4, 12, 24]]
    """Low-balance notification frequency.

    Organization sub-users cannot set a non-null frequency. The resulting profile
    must have both a threshold and frequency, or neither.
    """

    low_balance_threshold_amount: Optional[float]
    """Low-balance notification threshold in the billing currency.

    The resulting profile must have both a threshold and notification frequency, or
    neither.
    """

    notify_on_invoice_available: bool
    """Whether to notify the user when an invoice is available."""

    notify_on_invoice_payment: bool
    """Whether to notify the user when an invoice is paid."""

    npac_user: bool
    """Whether the user is an NPAC user."""

    onboarding_build_method: SequenceNotStr[str]
    """Build methods reported during onboarding."""

    onboarding_industries: SequenceNotStr[str]
    """Industries reported during onboarding."""

    onboarding_monthly_budget: SequenceNotStr[str]
    """Monthly budget ranges reported during onboarding."""

    onboarding_product_interest: SequenceNotStr[str]
    """Products of interest reported during onboarding."""

    onboarding_project_types: SequenceNotStr[str]
    """Onboarding project types."""

    onboarding_reasons_for_consideration: SequenceNotStr[str]
    """Reasons for considering Telnyx."""

    onboarding_referrer: SequenceNotStr[str]
    """Referral sources reported during onboarding."""

    onboarding_use_cases_other: SequenceNotStr[str]
    """Other onboarding use cases."""

    phone_number: Optional[str]
    """Contact phone number associated with the profile."""

    port_out_pin_validation: bool
    """Whether port-out PIN validation is enabled."""

    primary_use_case: str
    """Primary use case for the account."""

    role: str
    """The user's role."""

    state: Optional[str]
    """State or region in the profile address."""

    ui_theme: Literal[0, 1]
    """User interface theme: 0 for dark or 1 for light."""

    use_cases: SequenceNotStr[str]
    """Use cases reported by the user."""

    user_subscription_opt_in: bool
    """Whether the user opts in to subscriptions."""

    zip: Optional[str]
    """Postal code in the profile address."""
