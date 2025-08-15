# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import (
    Vertical,
    EntityType,
    StockExchange,
    AltBusinessIDType,
    BrandIdentityStatus,
    brand_list_params,
    brand_create_params,
    brand_update_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.vertical import Vertical
from .external_vetting import (
    ExternalVettingResource,
    AsyncExternalVettingResource,
    ExternalVettingResourceWithRawResponse,
    AsyncExternalVettingResourceWithRawResponse,
    ExternalVettingResourceWithStreamingResponse,
    AsyncExternalVettingResourceWithStreamingResponse,
)
from ...types.entity_type import EntityType
from ...types.telnyx_brand import TelnyxBrand
from ...types.stock_exchange import StockExchange
from ...types.brand_list_response import BrandListResponse
from ...types.alt_business_id_type import AltBusinessIDType
from ...types.brand_identity_status import BrandIdentityStatus
from ...types.brand_retrieve_response import BrandRetrieveResponse
from ...types.brand_get_feedback_response import BrandGetFeedbackResponse

__all__ = ["BrandResource", "AsyncBrandResource"]


class BrandResource(SyncAPIResource):
    @cached_property
    def external_vetting(self) -> ExternalVettingResource:
        return ExternalVettingResource(self._client)

    @cached_property
    def with_raw_response(self) -> BrandResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return BrandResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrandResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return BrandResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        country: str,
        display_name: str,
        email: str,
        entity_type: EntityType,
        vertical: Vertical,
        business_contact_email: str | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        company_name: str | NotGiven = NOT_GIVEN,
        ein: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        ip_address: str | NotGiven = NOT_GIVEN,
        is_reseller: bool | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        mobile_phone: str | NotGiven = NOT_GIVEN,
        mock: bool | NotGiven = NOT_GIVEN,
        phone: str | NotGiven = NOT_GIVEN,
        postal_code: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        stock_exchange: StockExchange | NotGiven = NOT_GIVEN,
        stock_symbol: str | NotGiven = NOT_GIVEN,
        street: str | NotGiven = NOT_GIVEN,
        webhook_failover_url: str | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        website: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TelnyxBrand:
        """This endpoint is used to create a new brand.

        A brand is an entity created by The
        Campaign Registry (TCR) that represents an organization or a company. It is this
        entity that TCR created campaigns will be associated with. Each brand creation
        will entail an upfront, non-refundable $4 expense.

        Args:
          country: ISO2 2 characters country code. Example: US - United States

          display_name: Display name, marketing name, or DBA name of the brand.

          email: Valid email address of brand support contact.

          entity_type: Entity type behind the brand. This is the form of business establishment.

          vertical: Vertical or industry segment of the brand or campaign.

          business_contact_email: Business contact email.

              Required if `entityType` is `PUBLIC_PROFIT`.

          city: City name

          company_name: (Required for Non-profit/private/public) Legal company name.

          ein: (Required for Non-profit) Government assigned corporate tax ID. EIN is 9-digits
              in U.S.

          first_name: First name of business contact.

          ip_address: IP address of the browser requesting to create brand identity.

          last_name: Last name of business contact.

          mobile_phone: Valid mobile phone number in e.164 international format.

          mock: Mock brand for testing purposes. Defaults to false.

          phone: Valid phone number in e.164 international format.

          postal_code: Postal codes. Use 5 digit zipcode for United States

          state: State. Must be 2 letters code for United States.

          stock_exchange: (Required for public company) stock exchange.

          stock_symbol: (Required for public company) stock symbol.

          street: Street number and name.

          webhook_failover_url: Webhook failover URL for brand status updates.

          webhook_url: Webhook URL for brand status updates.

          website: Brand website URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/brand",
            body=maybe_transform(
                {
                    "country": country,
                    "display_name": display_name,
                    "email": email,
                    "entity_type": entity_type,
                    "vertical": vertical,
                    "business_contact_email": business_contact_email,
                    "city": city,
                    "company_name": company_name,
                    "ein": ein,
                    "first_name": first_name,
                    "ip_address": ip_address,
                    "is_reseller": is_reseller,
                    "last_name": last_name,
                    "mobile_phone": mobile_phone,
                    "mock": mock,
                    "phone": phone,
                    "postal_code": postal_code,
                    "state": state,
                    "stock_exchange": stock_exchange,
                    "stock_symbol": stock_symbol,
                    "street": street,
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                    "website": website,
                },
                brand_create_params.BrandCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelnyxBrand,
        )

    def retrieve(
        self,
        brand_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandRetrieveResponse:
        """
        Retrieve a brand by `brandId`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return self._get(
            f"/brand/{brand_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandRetrieveResponse,
        )

    def update(
        self,
        brand_id: str,
        *,
        country: str,
        display_name: str,
        email: str,
        entity_type: EntityType,
        vertical: Vertical,
        alt_business_id: str | NotGiven = NOT_GIVEN,
        alt_business_id_type: AltBusinessIDType | NotGiven = NOT_GIVEN,
        business_contact_email: str | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        company_name: str | NotGiven = NOT_GIVEN,
        ein: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        identity_status: BrandIdentityStatus | NotGiven = NOT_GIVEN,
        ip_address: str | NotGiven = NOT_GIVEN,
        is_reseller: bool | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        phone: str | NotGiven = NOT_GIVEN,
        postal_code: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        stock_exchange: StockExchange | NotGiven = NOT_GIVEN,
        stock_symbol: str | NotGiven = NOT_GIVEN,
        street: str | NotGiven = NOT_GIVEN,
        webhook_failover_url: str | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        website: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TelnyxBrand:
        """
        Update a brand's attributes by `brandId`.

        Args:
          country: ISO2 2 characters country code. Example: US - United States

          display_name: Display or marketing name of the brand.

          email: Valid email address of brand support contact.

          entity_type: Entity type behind the brand. This is the form of business establishment.

          vertical: Vertical or industry segment of the brand or campaign.

          alt_business_id: Alternate business identifier such as DUNS, LEI, or GIIN

          alt_business_id_type: An enumeration.

          business_contact_email: Business contact email.

              Required if `entityType` will be changed to `PUBLIC_PROFIT`.

          city: City name

          company_name: (Required for Non-profit/private/public) Legal company name.

          ein: (Required for Non-profit) Government assigned corporate tax ID. EIN is 9-digits
              in U.S.

          first_name: First name of business contact.

          identity_status: The verification status of an active brand

          ip_address: IP address of the browser requesting to create brand identity.

          last_name: Last name of business contact.

          phone: Valid phone number in e.164 international format.

          postal_code: Postal codes. Use 5 digit zipcode for United States

          state: State. Must be 2 letters code for United States.

          stock_exchange: (Required for public company) stock exchange.

          stock_symbol: (Required for public company) stock symbol.

          street: Street number and name.

          webhook_failover_url: Webhook failover URL for brand status updates.

          webhook_url: Webhook URL for brand status updates.

          website: Brand website URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return self._put(
            f"/brand/{brand_id}",
            body=maybe_transform(
                {
                    "country": country,
                    "display_name": display_name,
                    "email": email,
                    "entity_type": entity_type,
                    "vertical": vertical,
                    "alt_business_id": alt_business_id,
                    "alt_business_id_type": alt_business_id_type,
                    "business_contact_email": business_contact_email,
                    "city": city,
                    "company_name": company_name,
                    "ein": ein,
                    "first_name": first_name,
                    "identity_status": identity_status,
                    "ip_address": ip_address,
                    "is_reseller": is_reseller,
                    "last_name": last_name,
                    "phone": phone,
                    "postal_code": postal_code,
                    "state": state,
                    "stock_exchange": stock_exchange,
                    "stock_symbol": stock_symbol,
                    "street": street,
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                    "website": website,
                },
                brand_update_params.BrandUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelnyxBrand,
        )

    def list(
        self,
        *,
        brand_id: str | NotGiven = NOT_GIVEN,
        country: str | NotGiven = NOT_GIVEN,
        display_name: str | NotGiven = NOT_GIVEN,
        entity_type: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        records_per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal[
            "assignedCampaignsCount",
            "-assignedCampaignsCount",
            "brandId",
            "-brandId",
            "createdAt",
            "-createdAt",
            "displayName",
            "-displayName",
            "identityStatus",
            "-identityStatus",
            "status",
            "-status",
            "tcrBrandId",
            "-tcrBrandId",
        ]
        | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        tcr_brand_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandListResponse:
        """
        This endpoint is used to list all brands associated with your organization.

        Args:
          brand_id: Filter results by the Telnyx Brand id

          records_per_page: number of records per page. maximum of 500

          sort: Specifies the sort order for results. If not given, results are sorted by
              createdAt in descending order.

          tcr_brand_id: Filter results by the TCR Brand id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/brand",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "brand_id": brand_id,
                        "country": country,
                        "display_name": display_name,
                        "entity_type": entity_type,
                        "page": page,
                        "records_per_page": records_per_page,
                        "sort": sort,
                        "state": state,
                        "tcr_brand_id": tcr_brand_id,
                    },
                    brand_list_params.BrandListParams,
                ),
            ),
            cast_to=BrandListResponse,
        )

    def delete(
        self,
        brand_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Delete Brand.

        This endpoint is used to delete a brand. Note the brand cannot be
        deleted if it contains one or more active campaigns, the campaigns need to be
        inactive and at least 3 months old due to billing purposes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return self._delete(
            f"/brand/{brand_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def get_feedback(
        self,
        brand_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandGetFeedbackResponse:
        """Get feedback about a brand by ID.

        This endpoint can be used after creating or
        revetting a brand.

        Possible values for `.category[].id`:

        - `TAX_ID` - Data mismatch related to tax id and its associated properties.
        - `STOCK_SYMBOL` - Non public entity registered as a public for profit entity or
          the stock information mismatch.
        - `GOVERNMENT_ENTITY` - Non government entity registered as a government entity.
          Must be a U.S. government entity.
        - `NONPROFIT` - Not a recognized non-profit entity. No IRS tax-exempt status
          found.
        - `OTHERS` - Details of the data misrepresentation if any.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return self._get(
            f"/brand/feedback/{brand_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandGetFeedbackResponse,
        )

    def resend_2fa_email(
        self,
        brand_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Resend brand 2FA email

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/brand/{brand_id}/2faEmail",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def revet(
        self,
        brand_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """This operation allows you to revet the brand.

        However, revetting is allowed once
        after the successful brand registration and thereafter limited to once every 3
        months.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return self._put(
            f"/brand/{brand_id}/revet",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncBrandResource(AsyncAPIResource):
    @cached_property
    def external_vetting(self) -> AsyncExternalVettingResource:
        return AsyncExternalVettingResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBrandResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBrandResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrandResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncBrandResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        country: str,
        display_name: str,
        email: str,
        entity_type: EntityType,
        vertical: Vertical,
        business_contact_email: str | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        company_name: str | NotGiven = NOT_GIVEN,
        ein: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        ip_address: str | NotGiven = NOT_GIVEN,
        is_reseller: bool | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        mobile_phone: str | NotGiven = NOT_GIVEN,
        mock: bool | NotGiven = NOT_GIVEN,
        phone: str | NotGiven = NOT_GIVEN,
        postal_code: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        stock_exchange: StockExchange | NotGiven = NOT_GIVEN,
        stock_symbol: str | NotGiven = NOT_GIVEN,
        street: str | NotGiven = NOT_GIVEN,
        webhook_failover_url: str | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        website: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TelnyxBrand:
        """This endpoint is used to create a new brand.

        A brand is an entity created by The
        Campaign Registry (TCR) that represents an organization or a company. It is this
        entity that TCR created campaigns will be associated with. Each brand creation
        will entail an upfront, non-refundable $4 expense.

        Args:
          country: ISO2 2 characters country code. Example: US - United States

          display_name: Display name, marketing name, or DBA name of the brand.

          email: Valid email address of brand support contact.

          entity_type: Entity type behind the brand. This is the form of business establishment.

          vertical: Vertical or industry segment of the brand or campaign.

          business_contact_email: Business contact email.

              Required if `entityType` is `PUBLIC_PROFIT`.

          city: City name

          company_name: (Required for Non-profit/private/public) Legal company name.

          ein: (Required for Non-profit) Government assigned corporate tax ID. EIN is 9-digits
              in U.S.

          first_name: First name of business contact.

          ip_address: IP address of the browser requesting to create brand identity.

          last_name: Last name of business contact.

          mobile_phone: Valid mobile phone number in e.164 international format.

          mock: Mock brand for testing purposes. Defaults to false.

          phone: Valid phone number in e.164 international format.

          postal_code: Postal codes. Use 5 digit zipcode for United States

          state: State. Must be 2 letters code for United States.

          stock_exchange: (Required for public company) stock exchange.

          stock_symbol: (Required for public company) stock symbol.

          street: Street number and name.

          webhook_failover_url: Webhook failover URL for brand status updates.

          webhook_url: Webhook URL for brand status updates.

          website: Brand website URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/brand",
            body=await async_maybe_transform(
                {
                    "country": country,
                    "display_name": display_name,
                    "email": email,
                    "entity_type": entity_type,
                    "vertical": vertical,
                    "business_contact_email": business_contact_email,
                    "city": city,
                    "company_name": company_name,
                    "ein": ein,
                    "first_name": first_name,
                    "ip_address": ip_address,
                    "is_reseller": is_reseller,
                    "last_name": last_name,
                    "mobile_phone": mobile_phone,
                    "mock": mock,
                    "phone": phone,
                    "postal_code": postal_code,
                    "state": state,
                    "stock_exchange": stock_exchange,
                    "stock_symbol": stock_symbol,
                    "street": street,
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                    "website": website,
                },
                brand_create_params.BrandCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelnyxBrand,
        )

    async def retrieve(
        self,
        brand_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandRetrieveResponse:
        """
        Retrieve a brand by `brandId`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return await self._get(
            f"/brand/{brand_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandRetrieveResponse,
        )

    async def update(
        self,
        brand_id: str,
        *,
        country: str,
        display_name: str,
        email: str,
        entity_type: EntityType,
        vertical: Vertical,
        alt_business_id: str | NotGiven = NOT_GIVEN,
        alt_business_id_type: AltBusinessIDType | NotGiven = NOT_GIVEN,
        business_contact_email: str | NotGiven = NOT_GIVEN,
        city: str | NotGiven = NOT_GIVEN,
        company_name: str | NotGiven = NOT_GIVEN,
        ein: str | NotGiven = NOT_GIVEN,
        first_name: str | NotGiven = NOT_GIVEN,
        identity_status: BrandIdentityStatus | NotGiven = NOT_GIVEN,
        ip_address: str | NotGiven = NOT_GIVEN,
        is_reseller: bool | NotGiven = NOT_GIVEN,
        last_name: str | NotGiven = NOT_GIVEN,
        phone: str | NotGiven = NOT_GIVEN,
        postal_code: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        stock_exchange: StockExchange | NotGiven = NOT_GIVEN,
        stock_symbol: str | NotGiven = NOT_GIVEN,
        street: str | NotGiven = NOT_GIVEN,
        webhook_failover_url: str | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        website: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TelnyxBrand:
        """
        Update a brand's attributes by `brandId`.

        Args:
          country: ISO2 2 characters country code. Example: US - United States

          display_name: Display or marketing name of the brand.

          email: Valid email address of brand support contact.

          entity_type: Entity type behind the brand. This is the form of business establishment.

          vertical: Vertical or industry segment of the brand or campaign.

          alt_business_id: Alternate business identifier such as DUNS, LEI, or GIIN

          alt_business_id_type: An enumeration.

          business_contact_email: Business contact email.

              Required if `entityType` will be changed to `PUBLIC_PROFIT`.

          city: City name

          company_name: (Required for Non-profit/private/public) Legal company name.

          ein: (Required for Non-profit) Government assigned corporate tax ID. EIN is 9-digits
              in U.S.

          first_name: First name of business contact.

          identity_status: The verification status of an active brand

          ip_address: IP address of the browser requesting to create brand identity.

          last_name: Last name of business contact.

          phone: Valid phone number in e.164 international format.

          postal_code: Postal codes. Use 5 digit zipcode for United States

          state: State. Must be 2 letters code for United States.

          stock_exchange: (Required for public company) stock exchange.

          stock_symbol: (Required for public company) stock symbol.

          street: Street number and name.

          webhook_failover_url: Webhook failover URL for brand status updates.

          webhook_url: Webhook URL for brand status updates.

          website: Brand website URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return await self._put(
            f"/brand/{brand_id}",
            body=await async_maybe_transform(
                {
                    "country": country,
                    "display_name": display_name,
                    "email": email,
                    "entity_type": entity_type,
                    "vertical": vertical,
                    "alt_business_id": alt_business_id,
                    "alt_business_id_type": alt_business_id_type,
                    "business_contact_email": business_contact_email,
                    "city": city,
                    "company_name": company_name,
                    "ein": ein,
                    "first_name": first_name,
                    "identity_status": identity_status,
                    "ip_address": ip_address,
                    "is_reseller": is_reseller,
                    "last_name": last_name,
                    "phone": phone,
                    "postal_code": postal_code,
                    "state": state,
                    "stock_exchange": stock_exchange,
                    "stock_symbol": stock_symbol,
                    "street": street,
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                    "website": website,
                },
                brand_update_params.BrandUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelnyxBrand,
        )

    async def list(
        self,
        *,
        brand_id: str | NotGiven = NOT_GIVEN,
        country: str | NotGiven = NOT_GIVEN,
        display_name: str | NotGiven = NOT_GIVEN,
        entity_type: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        records_per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal[
            "assignedCampaignsCount",
            "-assignedCampaignsCount",
            "brandId",
            "-brandId",
            "createdAt",
            "-createdAt",
            "displayName",
            "-displayName",
            "identityStatus",
            "-identityStatus",
            "status",
            "-status",
            "tcrBrandId",
            "-tcrBrandId",
        ]
        | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        tcr_brand_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandListResponse:
        """
        This endpoint is used to list all brands associated with your organization.

        Args:
          brand_id: Filter results by the Telnyx Brand id

          records_per_page: number of records per page. maximum of 500

          sort: Specifies the sort order for results. If not given, results are sorted by
              createdAt in descending order.

          tcr_brand_id: Filter results by the TCR Brand id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/brand",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "brand_id": brand_id,
                        "country": country,
                        "display_name": display_name,
                        "entity_type": entity_type,
                        "page": page,
                        "records_per_page": records_per_page,
                        "sort": sort,
                        "state": state,
                        "tcr_brand_id": tcr_brand_id,
                    },
                    brand_list_params.BrandListParams,
                ),
            ),
            cast_to=BrandListResponse,
        )

    async def delete(
        self,
        brand_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Delete Brand.

        This endpoint is used to delete a brand. Note the brand cannot be
        deleted if it contains one or more active campaigns, the campaigns need to be
        inactive and at least 3 months old due to billing purposes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return await self._delete(
            f"/brand/{brand_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def get_feedback(
        self,
        brand_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandGetFeedbackResponse:
        """Get feedback about a brand by ID.

        This endpoint can be used after creating or
        revetting a brand.

        Possible values for `.category[].id`:

        - `TAX_ID` - Data mismatch related to tax id and its associated properties.
        - `STOCK_SYMBOL` - Non public entity registered as a public for profit entity or
          the stock information mismatch.
        - `GOVERNMENT_ENTITY` - Non government entity registered as a government entity.
          Must be a U.S. government entity.
        - `NONPROFIT` - Not a recognized non-profit entity. No IRS tax-exempt status
          found.
        - `OTHERS` - Details of the data misrepresentation if any.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return await self._get(
            f"/brand/feedback/{brand_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandGetFeedbackResponse,
        )

    async def resend_2fa_email(
        self,
        brand_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Resend brand 2FA email

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/brand/{brand_id}/2faEmail",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def revet(
        self,
        brand_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """This operation allows you to revet the brand.

        However, revetting is allowed once
        after the successful brand registration and thereafter limited to once every 3
        months.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not brand_id:
            raise ValueError(f"Expected a non-empty value for `brand_id` but received {brand_id!r}")
        return await self._put(
            f"/brand/{brand_id}/revet",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class BrandResourceWithRawResponse:
    def __init__(self, brand: BrandResource) -> None:
        self._brand = brand

        self.create = to_raw_response_wrapper(
            brand.create,
        )
        self.retrieve = to_raw_response_wrapper(
            brand.retrieve,
        )
        self.update = to_raw_response_wrapper(
            brand.update,
        )
        self.list = to_raw_response_wrapper(
            brand.list,
        )
        self.delete = to_raw_response_wrapper(
            brand.delete,
        )
        self.get_feedback = to_raw_response_wrapper(
            brand.get_feedback,
        )
        self.resend_2fa_email = to_raw_response_wrapper(
            brand.resend_2fa_email,
        )
        self.revet = to_raw_response_wrapper(
            brand.revet,
        )

    @cached_property
    def external_vetting(self) -> ExternalVettingResourceWithRawResponse:
        return ExternalVettingResourceWithRawResponse(self._brand.external_vetting)


class AsyncBrandResourceWithRawResponse:
    def __init__(self, brand: AsyncBrandResource) -> None:
        self._brand = brand

        self.create = async_to_raw_response_wrapper(
            brand.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            brand.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            brand.update,
        )
        self.list = async_to_raw_response_wrapper(
            brand.list,
        )
        self.delete = async_to_raw_response_wrapper(
            brand.delete,
        )
        self.get_feedback = async_to_raw_response_wrapper(
            brand.get_feedback,
        )
        self.resend_2fa_email = async_to_raw_response_wrapper(
            brand.resend_2fa_email,
        )
        self.revet = async_to_raw_response_wrapper(
            brand.revet,
        )

    @cached_property
    def external_vetting(self) -> AsyncExternalVettingResourceWithRawResponse:
        return AsyncExternalVettingResourceWithRawResponse(self._brand.external_vetting)


class BrandResourceWithStreamingResponse:
    def __init__(self, brand: BrandResource) -> None:
        self._brand = brand

        self.create = to_streamed_response_wrapper(
            brand.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            brand.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            brand.update,
        )
        self.list = to_streamed_response_wrapper(
            brand.list,
        )
        self.delete = to_streamed_response_wrapper(
            brand.delete,
        )
        self.get_feedback = to_streamed_response_wrapper(
            brand.get_feedback,
        )
        self.resend_2fa_email = to_streamed_response_wrapper(
            brand.resend_2fa_email,
        )
        self.revet = to_streamed_response_wrapper(
            brand.revet,
        )

    @cached_property
    def external_vetting(self) -> ExternalVettingResourceWithStreamingResponse:
        return ExternalVettingResourceWithStreamingResponse(self._brand.external_vetting)


class AsyncBrandResourceWithStreamingResponse:
    def __init__(self, brand: AsyncBrandResource) -> None:
        self._brand = brand

        self.create = async_to_streamed_response_wrapper(
            brand.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            brand.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            brand.update,
        )
        self.list = async_to_streamed_response_wrapper(
            brand.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            brand.delete,
        )
        self.get_feedback = async_to_streamed_response_wrapper(
            brand.get_feedback,
        )
        self.resend_2fa_email = async_to_streamed_response_wrapper(
            brand.resend_2fa_email,
        )
        self.revet = async_to_streamed_response_wrapper(
            brand.revet,
        )

    @cached_property
    def external_vetting(self) -> AsyncExternalVettingResourceWithStreamingResponse:
        return AsyncExternalVettingResourceWithStreamingResponse(self._brand.external_vetting)
