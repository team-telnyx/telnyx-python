# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import user_profile_patch_all_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.user_profile_list_response import UserProfileListResponse
from ..types.user_profile_patch_all_response import UserProfilePatchAllResponse

__all__ = ["UserProfileResource", "AsyncUserProfileResource"]


class UserProfileResource(SyncAPIResource):
    """Read and update the authenticated user's profile and data locality."""

    @cached_property
    def with_raw_response(self) -> UserProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return UserProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return UserProfileResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserProfileListResponse:
        """
        Retrieve the authenticated user's profile, including data locality and migration
        status.

        **Beta:** this API should be considered a beta integration target because it may
        change if user account settings require changes
        """
        return self._get(
            "/user_profile",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserProfileListResponse,
        )

    def patch_all(
        self,
        *,
        address_1: Optional[str] | Omit = omit,
        address_2: Optional[str] | Omit = omit,
        business_name: Optional[str] | Omit = omit,
        city: Optional[str] | Omit = omit,
        company_size: str | Omit = omit,
        country: Optional[str] | Omit = omit,
        data_locality: Literal["USA", "DEU", "AUS", "UAE", "CAN"] | Omit = omit,
        default_managed_account_allow_custom_pricing: bool | Omit = omit,
        default_managed_account_inherit_emergency_terms_of_service: bool | Omit = omit,
        default_managed_account_rollup_billing: bool | Omit = omit,
        default_notify_manager_account: bool | Omit = omit,
        default_numbers_external_pin: str | Omit = omit,
        first_name: Optional[str] | Omit = omit,
        got_free_number_at_signup: bool | Omit = omit,
        last_name: Optional[str] | Omit = omit,
        low_balance_notification_frequency: Optional[Literal[2, 4, 12, 24]] | Omit = omit,
        low_balance_threshold_amount: Optional[float] | Omit = omit,
        notify_on_invoice_available: bool | Omit = omit,
        notify_on_invoice_payment: bool | Omit = omit,
        npac_user: bool | Omit = omit,
        onboarding_build_method: SequenceNotStr[str] | Omit = omit,
        onboarding_industries: SequenceNotStr[str] | Omit = omit,
        onboarding_monthly_budget: SequenceNotStr[str] | Omit = omit,
        onboarding_product_interest: SequenceNotStr[str] | Omit = omit,
        onboarding_project_types: SequenceNotStr[str] | Omit = omit,
        onboarding_reasons_for_consideration: SequenceNotStr[str] | Omit = omit,
        onboarding_referrer: SequenceNotStr[str] | Omit = omit,
        onboarding_use_cases_other: SequenceNotStr[str] | Omit = omit,
        phone_number: Optional[str] | Omit = omit,
        port_out_pin_validation: bool | Omit = omit,
        primary_use_case: str | Omit = omit,
        role: str | Omit = omit,
        state: Optional[str] | Omit = omit,
        ui_theme: Literal[0, 1] | Omit = omit,
        use_cases: SequenceNotStr[str] | Omit = omit,
        user_subscription_opt_in: bool | Omit = omit,
        zip: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserProfilePatchAllResponse:
        """Update the authenticated user's profile using top-level JSON fields.

        Returns the
        updated profile.

        **Beta:** this API should be considered a beta integration target because it may
        change if user account settings require changes

        Args:
          address_1: First line of the profile address.

          address_2: Second line of the profile address.

          business_name: Business name associated with the profile.

          city: City in the profile address.

          company_size: Company size reported by the user.

          country: Country code in the profile address.

          data_locality: Data locality: USA (United States), DEU (Germany), AUS (Australia), UAE (United
              Arab Emirates), or CAN (Canada). A change is permitted only if data locality has
              not previously been changed. A successful change sets data_locality_updated_at
              and initializes data_locality_migration_status to not_started.

          default_managed_account_allow_custom_pricing: Default custom-pricing setting for managed accounts.

          default_managed_account_inherit_emergency_terms_of_service: Default emergency terms-of-service inheritance setting for managed accounts,
              where supported.

          default_managed_account_rollup_billing: Default rollup-billing setting for managed accounts.

          default_notify_manager_account: Default setting for notifying the manager account.

          default_numbers_external_pin: Default alphanumeric external PIN for phone numbers.

          first_name: The user's first name.

          got_free_number_at_signup: Whether the user received a free number at signup.

          last_name: The user's last name.

          low_balance_notification_frequency: Low-balance notification frequency. Organization sub-users cannot set a non-null
              frequency. The resulting profile must have both a threshold and frequency, or
              neither.

          low_balance_threshold_amount: Low-balance notification threshold in the billing currency. The resulting
              profile must have both a threshold and notification frequency, or neither.

          notify_on_invoice_available: Whether to notify the user when an invoice is available.

          notify_on_invoice_payment: Whether to notify the user when an invoice is paid.

          npac_user: Whether the user is an NPAC user.

          onboarding_build_method: Build methods reported during onboarding.

          onboarding_industries: Industries reported during onboarding.

          onboarding_monthly_budget: Monthly budget ranges reported during onboarding.

          onboarding_product_interest: Products of interest reported during onboarding.

          onboarding_project_types: Onboarding project types.

          onboarding_reasons_for_consideration: Reasons for considering Telnyx.

          onboarding_referrer: Referral sources reported during onboarding.

          onboarding_use_cases_other: Other onboarding use cases.

          phone_number: Contact phone number associated with the profile.

          port_out_pin_validation: Whether port-out PIN validation is enabled.

          primary_use_case: Primary use case for the account.

          role: The user's role.

          state: State or region in the profile address.

          ui_theme: User interface theme: 0 for dark or 1 for light.

          use_cases: Use cases reported by the user.

          user_subscription_opt_in: Whether the user opts in to subscriptions.

          zip: Postal code in the profile address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/user_profile",
            body=maybe_transform(
                {
                    "address_1": address_1,
                    "address_2": address_2,
                    "business_name": business_name,
                    "city": city,
                    "company_size": company_size,
                    "country": country,
                    "data_locality": data_locality,
                    "default_managed_account_allow_custom_pricing": default_managed_account_allow_custom_pricing,
                    "default_managed_account_inherit_emergency_terms_of_service": default_managed_account_inherit_emergency_terms_of_service,
                    "default_managed_account_rollup_billing": default_managed_account_rollup_billing,
                    "default_notify_manager_account": default_notify_manager_account,
                    "default_numbers_external_pin": default_numbers_external_pin,
                    "first_name": first_name,
                    "got_free_number_at_signup": got_free_number_at_signup,
                    "last_name": last_name,
                    "low_balance_notification_frequency": low_balance_notification_frequency,
                    "low_balance_threshold_amount": low_balance_threshold_amount,
                    "notify_on_invoice_available": notify_on_invoice_available,
                    "notify_on_invoice_payment": notify_on_invoice_payment,
                    "npac_user": npac_user,
                    "onboarding_build_method": onboarding_build_method,
                    "onboarding_industries": onboarding_industries,
                    "onboarding_monthly_budget": onboarding_monthly_budget,
                    "onboarding_product_interest": onboarding_product_interest,
                    "onboarding_project_types": onboarding_project_types,
                    "onboarding_reasons_for_consideration": onboarding_reasons_for_consideration,
                    "onboarding_referrer": onboarding_referrer,
                    "onboarding_use_cases_other": onboarding_use_cases_other,
                    "phone_number": phone_number,
                    "port_out_pin_validation": port_out_pin_validation,
                    "primary_use_case": primary_use_case,
                    "role": role,
                    "state": state,
                    "ui_theme": ui_theme,
                    "use_cases": use_cases,
                    "user_subscription_opt_in": user_subscription_opt_in,
                    "zip": zip,
                },
                user_profile_patch_all_params.UserProfilePatchAllParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserProfilePatchAllResponse,
        )


class AsyncUserProfileResource(AsyncAPIResource):
    """Read and update the authenticated user's profile and data locality."""

    @cached_property
    def with_raw_response(self) -> AsyncUserProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUserProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncUserProfileResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserProfileListResponse:
        """
        Retrieve the authenticated user's profile, including data locality and migration
        status.

        **Beta:** this API should be considered a beta integration target because it may
        change if user account settings require changes
        """
        return await self._get(
            "/user_profile",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserProfileListResponse,
        )

    async def patch_all(
        self,
        *,
        address_1: Optional[str] | Omit = omit,
        address_2: Optional[str] | Omit = omit,
        business_name: Optional[str] | Omit = omit,
        city: Optional[str] | Omit = omit,
        company_size: str | Omit = omit,
        country: Optional[str] | Omit = omit,
        data_locality: Literal["USA", "DEU", "AUS", "UAE", "CAN"] | Omit = omit,
        default_managed_account_allow_custom_pricing: bool | Omit = omit,
        default_managed_account_inherit_emergency_terms_of_service: bool | Omit = omit,
        default_managed_account_rollup_billing: bool | Omit = omit,
        default_notify_manager_account: bool | Omit = omit,
        default_numbers_external_pin: str | Omit = omit,
        first_name: Optional[str] | Omit = omit,
        got_free_number_at_signup: bool | Omit = omit,
        last_name: Optional[str] | Omit = omit,
        low_balance_notification_frequency: Optional[Literal[2, 4, 12, 24]] | Omit = omit,
        low_balance_threshold_amount: Optional[float] | Omit = omit,
        notify_on_invoice_available: bool | Omit = omit,
        notify_on_invoice_payment: bool | Omit = omit,
        npac_user: bool | Omit = omit,
        onboarding_build_method: SequenceNotStr[str] | Omit = omit,
        onboarding_industries: SequenceNotStr[str] | Omit = omit,
        onboarding_monthly_budget: SequenceNotStr[str] | Omit = omit,
        onboarding_product_interest: SequenceNotStr[str] | Omit = omit,
        onboarding_project_types: SequenceNotStr[str] | Omit = omit,
        onboarding_reasons_for_consideration: SequenceNotStr[str] | Omit = omit,
        onboarding_referrer: SequenceNotStr[str] | Omit = omit,
        onboarding_use_cases_other: SequenceNotStr[str] | Omit = omit,
        phone_number: Optional[str] | Omit = omit,
        port_out_pin_validation: bool | Omit = omit,
        primary_use_case: str | Omit = omit,
        role: str | Omit = omit,
        state: Optional[str] | Omit = omit,
        ui_theme: Literal[0, 1] | Omit = omit,
        use_cases: SequenceNotStr[str] | Omit = omit,
        user_subscription_opt_in: bool | Omit = omit,
        zip: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserProfilePatchAllResponse:
        """Update the authenticated user's profile using top-level JSON fields.

        Returns the
        updated profile.

        **Beta:** this API should be considered a beta integration target because it may
        change if user account settings require changes

        Args:
          address_1: First line of the profile address.

          address_2: Second line of the profile address.

          business_name: Business name associated with the profile.

          city: City in the profile address.

          company_size: Company size reported by the user.

          country: Country code in the profile address.

          data_locality: Data locality: USA (United States), DEU (Germany), AUS (Australia), UAE (United
              Arab Emirates), or CAN (Canada). A change is permitted only if data locality has
              not previously been changed. A successful change sets data_locality_updated_at
              and initializes data_locality_migration_status to not_started.

          default_managed_account_allow_custom_pricing: Default custom-pricing setting for managed accounts.

          default_managed_account_inherit_emergency_terms_of_service: Default emergency terms-of-service inheritance setting for managed accounts,
              where supported.

          default_managed_account_rollup_billing: Default rollup-billing setting for managed accounts.

          default_notify_manager_account: Default setting for notifying the manager account.

          default_numbers_external_pin: Default alphanumeric external PIN for phone numbers.

          first_name: The user's first name.

          got_free_number_at_signup: Whether the user received a free number at signup.

          last_name: The user's last name.

          low_balance_notification_frequency: Low-balance notification frequency. Organization sub-users cannot set a non-null
              frequency. The resulting profile must have both a threshold and frequency, or
              neither.

          low_balance_threshold_amount: Low-balance notification threshold in the billing currency. The resulting
              profile must have both a threshold and notification frequency, or neither.

          notify_on_invoice_available: Whether to notify the user when an invoice is available.

          notify_on_invoice_payment: Whether to notify the user when an invoice is paid.

          npac_user: Whether the user is an NPAC user.

          onboarding_build_method: Build methods reported during onboarding.

          onboarding_industries: Industries reported during onboarding.

          onboarding_monthly_budget: Monthly budget ranges reported during onboarding.

          onboarding_product_interest: Products of interest reported during onboarding.

          onboarding_project_types: Onboarding project types.

          onboarding_reasons_for_consideration: Reasons for considering Telnyx.

          onboarding_referrer: Referral sources reported during onboarding.

          onboarding_use_cases_other: Other onboarding use cases.

          phone_number: Contact phone number associated with the profile.

          port_out_pin_validation: Whether port-out PIN validation is enabled.

          primary_use_case: Primary use case for the account.

          role: The user's role.

          state: State or region in the profile address.

          ui_theme: User interface theme: 0 for dark or 1 for light.

          use_cases: Use cases reported by the user.

          user_subscription_opt_in: Whether the user opts in to subscriptions.

          zip: Postal code in the profile address.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/user_profile",
            body=await async_maybe_transform(
                {
                    "address_1": address_1,
                    "address_2": address_2,
                    "business_name": business_name,
                    "city": city,
                    "company_size": company_size,
                    "country": country,
                    "data_locality": data_locality,
                    "default_managed_account_allow_custom_pricing": default_managed_account_allow_custom_pricing,
                    "default_managed_account_inherit_emergency_terms_of_service": default_managed_account_inherit_emergency_terms_of_service,
                    "default_managed_account_rollup_billing": default_managed_account_rollup_billing,
                    "default_notify_manager_account": default_notify_manager_account,
                    "default_numbers_external_pin": default_numbers_external_pin,
                    "first_name": first_name,
                    "got_free_number_at_signup": got_free_number_at_signup,
                    "last_name": last_name,
                    "low_balance_notification_frequency": low_balance_notification_frequency,
                    "low_balance_threshold_amount": low_balance_threshold_amount,
                    "notify_on_invoice_available": notify_on_invoice_available,
                    "notify_on_invoice_payment": notify_on_invoice_payment,
                    "npac_user": npac_user,
                    "onboarding_build_method": onboarding_build_method,
                    "onboarding_industries": onboarding_industries,
                    "onboarding_monthly_budget": onboarding_monthly_budget,
                    "onboarding_product_interest": onboarding_product_interest,
                    "onboarding_project_types": onboarding_project_types,
                    "onboarding_reasons_for_consideration": onboarding_reasons_for_consideration,
                    "onboarding_referrer": onboarding_referrer,
                    "onboarding_use_cases_other": onboarding_use_cases_other,
                    "phone_number": phone_number,
                    "port_out_pin_validation": port_out_pin_validation,
                    "primary_use_case": primary_use_case,
                    "role": role,
                    "state": state,
                    "ui_theme": ui_theme,
                    "use_cases": use_cases,
                    "user_subscription_opt_in": user_subscription_opt_in,
                    "zip": zip,
                },
                user_profile_patch_all_params.UserProfilePatchAllParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserProfilePatchAllResponse,
        )


class UserProfileResourceWithRawResponse:
    def __init__(self, user_profile: UserProfileResource) -> None:
        self._user_profile = user_profile

        self.list = to_raw_response_wrapper(
            user_profile.list,
        )
        self.patch_all = to_raw_response_wrapper(
            user_profile.patch_all,
        )


class AsyncUserProfileResourceWithRawResponse:
    def __init__(self, user_profile: AsyncUserProfileResource) -> None:
        self._user_profile = user_profile

        self.list = async_to_raw_response_wrapper(
            user_profile.list,
        )
        self.patch_all = async_to_raw_response_wrapper(
            user_profile.patch_all,
        )


class UserProfileResourceWithStreamingResponse:
    def __init__(self, user_profile: UserProfileResource) -> None:
        self._user_profile = user_profile

        self.list = to_streamed_response_wrapper(
            user_profile.list,
        )
        self.patch_all = to_streamed_response_wrapper(
            user_profile.patch_all,
        )


class AsyncUserProfileResourceWithStreamingResponse:
    def __init__(self, user_profile: AsyncUserProfileResource) -> None:
        self._user_profile = user_profile

        self.list = async_to_streamed_response_wrapper(
            user_profile.list,
        )
        self.patch_all = async_to_streamed_response_wrapper(
            user_profile.patch_all,
        )
