# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .brand.brand import (
    BrandResource,
    AsyncBrandResource,
    BrandResourceWithRawResponse,
    AsyncBrandResourceWithRawResponse,
    BrandResourceWithStreamingResponse,
    AsyncBrandResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .campaign.campaign import (
    CampaignResource,
    AsyncCampaignResource,
    CampaignResourceWithRawResponse,
    AsyncCampaignResourceWithRawResponse,
    CampaignResourceWithStreamingResponse,
    AsyncCampaignResourceWithStreamingResponse,
)
from .partner_campaigns import (
    PartnerCampaignsResource,
    AsyncPartnerCampaignsResource,
    PartnerCampaignsResourceWithRawResponse,
    AsyncPartnerCampaignsResourceWithRawResponse,
    PartnerCampaignsResourceWithStreamingResponse,
    AsyncPartnerCampaignsResourceWithStreamingResponse,
)
from .phone_number_campaigns import (
    PhoneNumberCampaignsResource,
    AsyncPhoneNumberCampaignsResource,
    PhoneNumberCampaignsResourceWithRawResponse,
    AsyncPhoneNumberCampaignsResourceWithRawResponse,
    PhoneNumberCampaignsResourceWithStreamingResponse,
    AsyncPhoneNumberCampaignsResourceWithStreamingResponse,
)
from .campaign_builder.campaign_builder import (
    CampaignBuilderResource,
    AsyncCampaignBuilderResource,
    CampaignBuilderResourceWithRawResponse,
    AsyncCampaignBuilderResourceWithRawResponse,
    CampaignBuilderResourceWithStreamingResponse,
    AsyncCampaignBuilderResourceWithStreamingResponse,
)
from .phone_number_assignment_by_profile import (
    PhoneNumberAssignmentByProfileResource,
    AsyncPhoneNumberAssignmentByProfileResource,
    PhoneNumberAssignmentByProfileResourceWithRawResponse,
    AsyncPhoneNumberAssignmentByProfileResourceWithRawResponse,
    PhoneNumberAssignmentByProfileResourceWithStreamingResponse,
    AsyncPhoneNumberAssignmentByProfileResourceWithStreamingResponse,
)
from ...types.messaging_10dlc_get_enum_response import Messaging10dlcGetEnumResponse

__all__ = ["Messaging10dlcResource", "AsyncMessaging10dlcResource"]


class Messaging10dlcResource(SyncAPIResource):
    @cached_property
    def brand(self) -> BrandResource:
        """Brand operations"""
        return BrandResource(self._client)

    @cached_property
    def campaign(self) -> CampaignResource:
        """Campaign operations"""
        return CampaignResource(self._client)

    @cached_property
    def campaign_builder(self) -> CampaignBuilderResource:
        """Campaign operations"""
        return CampaignBuilderResource(self._client)

    @cached_property
    def partner_campaigns(self) -> PartnerCampaignsResource:
        return PartnerCampaignsResource(self._client)

    @cached_property
    def phone_number_campaigns(self) -> PhoneNumberCampaignsResource:
        """Phone number campaign assignment"""
        return PhoneNumberCampaignsResource(self._client)

    @cached_property
    def phone_number_assignment_by_profile(self) -> PhoneNumberAssignmentByProfileResource:
        """Phone number campaign bulk assignment"""
        return PhoneNumberAssignmentByProfileResource(self._client)

    @cached_property
    def with_raw_response(self) -> Messaging10dlcResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return Messaging10dlcResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> Messaging10dlcResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return Messaging10dlcResourceWithStreamingResponse(self)

    def get_enum(
        self,
        endpoint: Literal[
            "mno",
            "optionalAttributes",
            "usecase",
            "vertical",
            "altBusinessIdType",
            "brandIdentityStatus",
            "brandRelationship",
            "campaignStatus",
            "entityType",
            "extVettingProvider",
            "vettingStatus",
            "brandStatus",
            "operationStatus",
            "approvedPublicCompany",
            "stockExchange",
            "vettingClass",
        ],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Messaging10dlcGetEnumResponse:
        """
        Get Enum

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not endpoint:
            raise ValueError(f"Expected a non-empty value for `endpoint` but received {endpoint!r}")
        return cast(
            Messaging10dlcGetEnumResponse,
            self._get(
                f"/10dlc/enum/{endpoint}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, Messaging10dlcGetEnumResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncMessaging10dlcResource(AsyncAPIResource):
    @cached_property
    def brand(self) -> AsyncBrandResource:
        """Brand operations"""
        return AsyncBrandResource(self._client)

    @cached_property
    def campaign(self) -> AsyncCampaignResource:
        """Campaign operations"""
        return AsyncCampaignResource(self._client)

    @cached_property
    def campaign_builder(self) -> AsyncCampaignBuilderResource:
        """Campaign operations"""
        return AsyncCampaignBuilderResource(self._client)

    @cached_property
    def partner_campaigns(self) -> AsyncPartnerCampaignsResource:
        return AsyncPartnerCampaignsResource(self._client)

    @cached_property
    def phone_number_campaigns(self) -> AsyncPhoneNumberCampaignsResource:
        """Phone number campaign assignment"""
        return AsyncPhoneNumberCampaignsResource(self._client)

    @cached_property
    def phone_number_assignment_by_profile(self) -> AsyncPhoneNumberAssignmentByProfileResource:
        """Phone number campaign bulk assignment"""
        return AsyncPhoneNumberAssignmentByProfileResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMessaging10dlcResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessaging10dlcResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessaging10dlcResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncMessaging10dlcResourceWithStreamingResponse(self)

    async def get_enum(
        self,
        endpoint: Literal[
            "mno",
            "optionalAttributes",
            "usecase",
            "vertical",
            "altBusinessIdType",
            "brandIdentityStatus",
            "brandRelationship",
            "campaignStatus",
            "entityType",
            "extVettingProvider",
            "vettingStatus",
            "brandStatus",
            "operationStatus",
            "approvedPublicCompany",
            "stockExchange",
            "vettingClass",
        ],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Messaging10dlcGetEnumResponse:
        """
        Get Enum

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not endpoint:
            raise ValueError(f"Expected a non-empty value for `endpoint` but received {endpoint!r}")
        return cast(
            Messaging10dlcGetEnumResponse,
            await self._get(
                f"/10dlc/enum/{endpoint}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, Messaging10dlcGetEnumResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class Messaging10dlcResourceWithRawResponse:
    def __init__(self, messaging_10dlc: Messaging10dlcResource) -> None:
        self._messaging_10dlc = messaging_10dlc

        self.get_enum = to_raw_response_wrapper(
            messaging_10dlc.get_enum,
        )

    @cached_property
    def brand(self) -> BrandResourceWithRawResponse:
        """Brand operations"""
        return BrandResourceWithRawResponse(self._messaging_10dlc.brand)

    @cached_property
    def campaign(self) -> CampaignResourceWithRawResponse:
        """Campaign operations"""
        return CampaignResourceWithRawResponse(self._messaging_10dlc.campaign)

    @cached_property
    def campaign_builder(self) -> CampaignBuilderResourceWithRawResponse:
        """Campaign operations"""
        return CampaignBuilderResourceWithRawResponse(self._messaging_10dlc.campaign_builder)

    @cached_property
    def partner_campaigns(self) -> PartnerCampaignsResourceWithRawResponse:
        return PartnerCampaignsResourceWithRawResponse(self._messaging_10dlc.partner_campaigns)

    @cached_property
    def phone_number_campaigns(self) -> PhoneNumberCampaignsResourceWithRawResponse:
        """Phone number campaign assignment"""
        return PhoneNumberCampaignsResourceWithRawResponse(self._messaging_10dlc.phone_number_campaigns)

    @cached_property
    def phone_number_assignment_by_profile(self) -> PhoneNumberAssignmentByProfileResourceWithRawResponse:
        """Phone number campaign bulk assignment"""
        return PhoneNumberAssignmentByProfileResourceWithRawResponse(
            self._messaging_10dlc.phone_number_assignment_by_profile
        )


class AsyncMessaging10dlcResourceWithRawResponse:
    def __init__(self, messaging_10dlc: AsyncMessaging10dlcResource) -> None:
        self._messaging_10dlc = messaging_10dlc

        self.get_enum = async_to_raw_response_wrapper(
            messaging_10dlc.get_enum,
        )

    @cached_property
    def brand(self) -> AsyncBrandResourceWithRawResponse:
        """Brand operations"""
        return AsyncBrandResourceWithRawResponse(self._messaging_10dlc.brand)

    @cached_property
    def campaign(self) -> AsyncCampaignResourceWithRawResponse:
        """Campaign operations"""
        return AsyncCampaignResourceWithRawResponse(self._messaging_10dlc.campaign)

    @cached_property
    def campaign_builder(self) -> AsyncCampaignBuilderResourceWithRawResponse:
        """Campaign operations"""
        return AsyncCampaignBuilderResourceWithRawResponse(self._messaging_10dlc.campaign_builder)

    @cached_property
    def partner_campaigns(self) -> AsyncPartnerCampaignsResourceWithRawResponse:
        return AsyncPartnerCampaignsResourceWithRawResponse(self._messaging_10dlc.partner_campaigns)

    @cached_property
    def phone_number_campaigns(self) -> AsyncPhoneNumberCampaignsResourceWithRawResponse:
        """Phone number campaign assignment"""
        return AsyncPhoneNumberCampaignsResourceWithRawResponse(self._messaging_10dlc.phone_number_campaigns)

    @cached_property
    def phone_number_assignment_by_profile(self) -> AsyncPhoneNumberAssignmentByProfileResourceWithRawResponse:
        """Phone number campaign bulk assignment"""
        return AsyncPhoneNumberAssignmentByProfileResourceWithRawResponse(
            self._messaging_10dlc.phone_number_assignment_by_profile
        )


class Messaging10dlcResourceWithStreamingResponse:
    def __init__(self, messaging_10dlc: Messaging10dlcResource) -> None:
        self._messaging_10dlc = messaging_10dlc

        self.get_enum = to_streamed_response_wrapper(
            messaging_10dlc.get_enum,
        )

    @cached_property
    def brand(self) -> BrandResourceWithStreamingResponse:
        """Brand operations"""
        return BrandResourceWithStreamingResponse(self._messaging_10dlc.brand)

    @cached_property
    def campaign(self) -> CampaignResourceWithStreamingResponse:
        """Campaign operations"""
        return CampaignResourceWithStreamingResponse(self._messaging_10dlc.campaign)

    @cached_property
    def campaign_builder(self) -> CampaignBuilderResourceWithStreamingResponse:
        """Campaign operations"""
        return CampaignBuilderResourceWithStreamingResponse(self._messaging_10dlc.campaign_builder)

    @cached_property
    def partner_campaigns(self) -> PartnerCampaignsResourceWithStreamingResponse:
        return PartnerCampaignsResourceWithStreamingResponse(self._messaging_10dlc.partner_campaigns)

    @cached_property
    def phone_number_campaigns(self) -> PhoneNumberCampaignsResourceWithStreamingResponse:
        """Phone number campaign assignment"""
        return PhoneNumberCampaignsResourceWithStreamingResponse(self._messaging_10dlc.phone_number_campaigns)

    @cached_property
    def phone_number_assignment_by_profile(self) -> PhoneNumberAssignmentByProfileResourceWithStreamingResponse:
        """Phone number campaign bulk assignment"""
        return PhoneNumberAssignmentByProfileResourceWithStreamingResponse(
            self._messaging_10dlc.phone_number_assignment_by_profile
        )


class AsyncMessaging10dlcResourceWithStreamingResponse:
    def __init__(self, messaging_10dlc: AsyncMessaging10dlcResource) -> None:
        self._messaging_10dlc = messaging_10dlc

        self.get_enum = async_to_streamed_response_wrapper(
            messaging_10dlc.get_enum,
        )

    @cached_property
    def brand(self) -> AsyncBrandResourceWithStreamingResponse:
        """Brand operations"""
        return AsyncBrandResourceWithStreamingResponse(self._messaging_10dlc.brand)

    @cached_property
    def campaign(self) -> AsyncCampaignResourceWithStreamingResponse:
        """Campaign operations"""
        return AsyncCampaignResourceWithStreamingResponse(self._messaging_10dlc.campaign)

    @cached_property
    def campaign_builder(self) -> AsyncCampaignBuilderResourceWithStreamingResponse:
        """Campaign operations"""
        return AsyncCampaignBuilderResourceWithStreamingResponse(self._messaging_10dlc.campaign_builder)

    @cached_property
    def partner_campaigns(self) -> AsyncPartnerCampaignsResourceWithStreamingResponse:
        return AsyncPartnerCampaignsResourceWithStreamingResponse(self._messaging_10dlc.partner_campaigns)

    @cached_property
    def phone_number_campaigns(self) -> AsyncPhoneNumberCampaignsResourceWithStreamingResponse:
        """Phone number campaign assignment"""
        return AsyncPhoneNumberCampaignsResourceWithStreamingResponse(self._messaging_10dlc.phone_number_campaigns)

    @cached_property
    def phone_number_assignment_by_profile(self) -> AsyncPhoneNumberAssignmentByProfileResourceWithStreamingResponse:
        """Phone number campaign bulk assignment"""
        return AsyncPhoneNumberAssignmentByProfileResourceWithStreamingResponse(
            self._messaging_10dlc.phone_number_assignment_by_profile
        )
