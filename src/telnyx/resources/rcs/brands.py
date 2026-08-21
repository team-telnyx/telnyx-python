# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.rcs import BrandLegalEntityType, BrandOrganizationType, brand_create_params, brand_update_params
from ..._base_client import make_request_options
from ...types.rcs.brand_response import BrandResponse
from ...types.rcs.brand_address_param import BrandAddressParam
from ...types.rcs.brand_list_response import BrandListResponse
from ...types.rcs.brand_legal_entity_type import BrandLegalEntityType
from ...types.rcs.brand_organization_type import BrandOrganizationType

__all__ = ["BrandsResource", "AsyncBrandsResource"]


class BrandsResource(SyncAPIResource):
    """Manage the legal business entities that operate RCS agents."""

    @cached_property
    def with_raw_response(self) -> BrandsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return BrandsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrandsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return BrandsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        addresses: Dict[str, BrandAddressParam],
        contacts: brand_create_params.Contacts,
        display_name: str,
        identifiers: brand_create_params.Identifiers,
        legal_entity_type: BrandLegalEntityType,
        legal_name: str,
        organization_type: BrandOrganizationType,
        website_url: str,
        profile_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandResponse:
        """Creates an editable RCS brand draft.

        Creating the draft does not begin external
        review.

        Args:
          contacts: Named business contacts. Use the `brand` key for the required BRAND contact.

          identifiers: Named business identifiers. Use the `ein` key for the required EIN and
              `stock_symbol` for a public-profit brand's stock symbol.

          profile_id: A Messaging Profile owned by the authenticated organization. Agents inherit this
              value when they do not provide their own profile.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/rcs/brands",
            body=maybe_transform(
                {
                    "addresses": addresses,
                    "contacts": contacts,
                    "display_name": display_name,
                    "identifiers": identifiers,
                    "legal_entity_type": legal_entity_type,
                    "legal_name": legal_name,
                    "organization_type": organization_type,
                    "website_url": website_url,
                    "profile_id": profile_id,
                },
                brand_create_params.BrandCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandResponse:
        """
        Retrieves an RCS brand and its current lifecycle status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/rcs/brands/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandResponse,
        )

    def update(
        self,
        id: str,
        *,
        addresses: Dict[str, BrandAddressParam] | Omit = omit,
        contacts: brand_update_params.Contacts | Omit = omit,
        display_name: str | Omit = omit,
        identifiers: brand_update_params.Identifiers | Omit = omit,
        legal_entity_type: BrandLegalEntityType | Omit = omit,
        legal_name: str | Omit = omit,
        organization_type: BrandOrganizationType | Omit = omit,
        profile_id: str | Omit = omit,
        website_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandResponse:
        """Updates one or more fields on a brand while its status is `CREATED`.

        Submitted
        brands cannot be changed.

        Args:
          contacts: Named business contacts. Use the `brand` key for the required BRAND contact.

          identifiers: Named business identifiers. Use the `ein` key for the required EIN and
              `stock_symbol` for a public-profit brand's stock symbol.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/rcs/brands/{id}", id=id),
            body=maybe_transform(
                {
                    "addresses": addresses,
                    "contacts": contacts,
                    "display_name": display_name,
                    "identifiers": identifiers,
                    "legal_entity_type": legal_entity_type,
                    "legal_name": legal_name,
                    "organization_type": organization_type,
                    "profile_id": profile_id,
                    "website_url": website_url,
                },
                brand_update_params.BrandUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandListResponse:
        """Lists RCS brands owned by the authenticated organization."""
        return self._get(
            "/rcs/brands",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandListResponse,
        )

    def submit(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandResponse:
        """
        Starts asynchronous provider provisioning and external review for a brand.
        Repeating this request for an in-progress brand returns its current state
        without creating new work.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/rcs/brands/{id}/submit", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandResponse,
        )


class AsyncBrandsResource(AsyncAPIResource):
    """Manage the legal business entities that operate RCS agents."""

    @cached_property
    def with_raw_response(self) -> AsyncBrandsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBrandsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrandsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncBrandsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        addresses: Dict[str, BrandAddressParam],
        contacts: brand_create_params.Contacts,
        display_name: str,
        identifiers: brand_create_params.Identifiers,
        legal_entity_type: BrandLegalEntityType,
        legal_name: str,
        organization_type: BrandOrganizationType,
        website_url: str,
        profile_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandResponse:
        """Creates an editable RCS brand draft.

        Creating the draft does not begin external
        review.

        Args:
          contacts: Named business contacts. Use the `brand` key for the required BRAND contact.

          identifiers: Named business identifiers. Use the `ein` key for the required EIN and
              `stock_symbol` for a public-profit brand's stock symbol.

          profile_id: A Messaging Profile owned by the authenticated organization. Agents inherit this
              value when they do not provide their own profile.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/rcs/brands",
            body=await async_maybe_transform(
                {
                    "addresses": addresses,
                    "contacts": contacts,
                    "display_name": display_name,
                    "identifiers": identifiers,
                    "legal_entity_type": legal_entity_type,
                    "legal_name": legal_name,
                    "organization_type": organization_type,
                    "website_url": website_url,
                    "profile_id": profile_id,
                },
                brand_create_params.BrandCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandResponse:
        """
        Retrieves an RCS brand and its current lifecycle status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/rcs/brands/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandResponse,
        )

    async def update(
        self,
        id: str,
        *,
        addresses: Dict[str, BrandAddressParam] | Omit = omit,
        contacts: brand_update_params.Contacts | Omit = omit,
        display_name: str | Omit = omit,
        identifiers: brand_update_params.Identifiers | Omit = omit,
        legal_entity_type: BrandLegalEntityType | Omit = omit,
        legal_name: str | Omit = omit,
        organization_type: BrandOrganizationType | Omit = omit,
        profile_id: str | Omit = omit,
        website_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandResponse:
        """Updates one or more fields on a brand while its status is `CREATED`.

        Submitted
        brands cannot be changed.

        Args:
          contacts: Named business contacts. Use the `brand` key for the required BRAND contact.

          identifiers: Named business identifiers. Use the `ein` key for the required EIN and
              `stock_symbol` for a public-profit brand's stock symbol.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/rcs/brands/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "addresses": addresses,
                    "contacts": contacts,
                    "display_name": display_name,
                    "identifiers": identifiers,
                    "legal_entity_type": legal_entity_type,
                    "legal_name": legal_name,
                    "organization_type": organization_type,
                    "profile_id": profile_id,
                    "website_url": website_url,
                },
                brand_update_params.BrandUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandListResponse:
        """Lists RCS brands owned by the authenticated organization."""
        return await self._get(
            "/rcs/brands",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandListResponse,
        )

    async def submit(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandResponse:
        """
        Starts asynchronous provider provisioning and external review for a brand.
        Repeating this request for an in-progress brand returns its current state
        without creating new work.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/rcs/brands/{id}/submit", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandResponse,
        )


class BrandsResourceWithRawResponse:
    def __init__(self, brands: BrandsResource) -> None:
        self._brands = brands

        self.create = to_raw_response_wrapper(
            brands.create,
        )
        self.retrieve = to_raw_response_wrapper(
            brands.retrieve,
        )
        self.update = to_raw_response_wrapper(
            brands.update,
        )
        self.list = to_raw_response_wrapper(
            brands.list,
        )
        self.submit = to_raw_response_wrapper(
            brands.submit,
        )


class AsyncBrandsResourceWithRawResponse:
    def __init__(self, brands: AsyncBrandsResource) -> None:
        self._brands = brands

        self.create = async_to_raw_response_wrapper(
            brands.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            brands.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            brands.update,
        )
        self.list = async_to_raw_response_wrapper(
            brands.list,
        )
        self.submit = async_to_raw_response_wrapper(
            brands.submit,
        )


class BrandsResourceWithStreamingResponse:
    def __init__(self, brands: BrandsResource) -> None:
        self._brands = brands

        self.create = to_streamed_response_wrapper(
            brands.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            brands.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            brands.update,
        )
        self.list = to_streamed_response_wrapper(
            brands.list,
        )
        self.submit = to_streamed_response_wrapper(
            brands.submit,
        )


class AsyncBrandsResourceWithStreamingResponse:
    def __init__(self, brands: AsyncBrandsResource) -> None:
        self._brands = brands

        self.create = async_to_streamed_response_wrapper(
            brands.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            brands.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            brands.update,
        )
        self.list = async_to_streamed_response_wrapper(
            brands.list,
        )
        self.submit = async_to_streamed_response_wrapper(
            brands.submit,
        )
