# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.porting import (
    loa_configuration_list_params,
    loa_configuration_create_params,
    loa_configuration_update_params,
    loa_configuration_preview_0_params,
)
from ...types.porting.loa_configuration_list_response import LoaConfigurationListResponse
from ...types.porting.loa_configuration_create_response import LoaConfigurationCreateResponse
from ...types.porting.loa_configuration_update_response import LoaConfigurationUpdateResponse
from ...types.porting.loa_configuration_retrieve_response import LoaConfigurationRetrieveResponse

__all__ = ["LoaConfigurationsResource", "AsyncLoaConfigurationsResource"]


class LoaConfigurationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LoaConfigurationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return LoaConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LoaConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return LoaConfigurationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        address: loa_configuration_create_params.Address,
        company_name: str,
        contact: loa_configuration_create_params.Contact,
        logo: loa_configuration_create_params.Logo,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoaConfigurationCreateResponse:
        """
        Create a LOA configuration.

        Args:
          address: The address of the company.

          company_name: The name of the company

          contact: The contact information of the company.

          logo: The logo of the LOA configuration

          name: The name of the LOA configuration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/porting/loa_configurations",
            body=maybe_transform(
                {
                    "address": address,
                    "company_name": company_name,
                    "contact": contact,
                    "logo": logo,
                    "name": name,
                },
                loa_configuration_create_params.LoaConfigurationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoaConfigurationCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoaConfigurationRetrieveResponse:
        """
        Retrieve a specific LOA configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/porting/loa_configurations/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoaConfigurationRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        address: loa_configuration_update_params.Address,
        company_name: str,
        contact: loa_configuration_update_params.Contact,
        logo: loa_configuration_update_params.Logo,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoaConfigurationUpdateResponse:
        """
        Update a specific LOA configuration.

        Args:
          address: The address of the company.

          company_name: The name of the company

          contact: The contact information of the company.

          logo: The logo of the LOA configuration

          name: The name of the LOA configuration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/porting/loa_configurations/{id}",
            body=maybe_transform(
                {
                    "address": address,
                    "company_name": company_name,
                    "contact": contact,
                    "logo": logo,
                    "name": name,
                },
                loa_configuration_update_params.LoaConfigurationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoaConfigurationUpdateResponse,
        )

    def list(
        self,
        *,
        page: loa_configuration_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoaConfigurationListResponse:
        """
        List the LOA configurations.

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/porting/loa_configurations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"page": page}, loa_configuration_list_params.LoaConfigurationListParams),
            ),
            cast_to=LoaConfigurationListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a specific LOA configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/porting/loa_configurations/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def preview_0(
        self,
        *,
        address: loa_configuration_preview_0_params.Address,
        company_name: str,
        contact: loa_configuration_preview_0_params.Contact,
        logo: loa_configuration_preview_0_params.Logo,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Preview the LOA template that would be generated without need to create LOA
        configuration.

        Args:
          address: The address of the company.

          company_name: The name of the company

          contact: The contact information of the company.

          logo: The logo of the LOA configuration

          name: The name of the LOA configuration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/pdf", **(extra_headers or {})}
        return self._post(
            "/porting/loa_configuration/preview",
            body=maybe_transform(
                {
                    "address": address,
                    "company_name": company_name,
                    "contact": contact,
                    "logo": logo,
                    "name": name,
                },
                loa_configuration_preview_0_params.LoaConfigurationPreview0Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def preview_1(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Preview a specific LOA configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/pdf", **(extra_headers or {})}
        return self._get(
            f"/porting/loa_configurations/{id}/preview",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncLoaConfigurationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLoaConfigurationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLoaConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLoaConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncLoaConfigurationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        address: loa_configuration_create_params.Address,
        company_name: str,
        contact: loa_configuration_create_params.Contact,
        logo: loa_configuration_create_params.Logo,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoaConfigurationCreateResponse:
        """
        Create a LOA configuration.

        Args:
          address: The address of the company.

          company_name: The name of the company

          contact: The contact information of the company.

          logo: The logo of the LOA configuration

          name: The name of the LOA configuration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/porting/loa_configurations",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "company_name": company_name,
                    "contact": contact,
                    "logo": logo,
                    "name": name,
                },
                loa_configuration_create_params.LoaConfigurationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoaConfigurationCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoaConfigurationRetrieveResponse:
        """
        Retrieve a specific LOA configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/porting/loa_configurations/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoaConfigurationRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        address: loa_configuration_update_params.Address,
        company_name: str,
        contact: loa_configuration_update_params.Contact,
        logo: loa_configuration_update_params.Logo,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoaConfigurationUpdateResponse:
        """
        Update a specific LOA configuration.

        Args:
          address: The address of the company.

          company_name: The name of the company

          contact: The contact information of the company.

          logo: The logo of the LOA configuration

          name: The name of the LOA configuration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/porting/loa_configurations/{id}",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "company_name": company_name,
                    "contact": contact,
                    "logo": logo,
                    "name": name,
                },
                loa_configuration_update_params.LoaConfigurationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoaConfigurationUpdateResponse,
        )

    async def list(
        self,
        *,
        page: loa_configuration_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoaConfigurationListResponse:
        """
        List the LOA configurations.

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/porting/loa_configurations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"page": page}, loa_configuration_list_params.LoaConfigurationListParams
                ),
            ),
            cast_to=LoaConfigurationListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a specific LOA configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/porting/loa_configurations/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def preview_0(
        self,
        *,
        address: loa_configuration_preview_0_params.Address,
        company_name: str,
        contact: loa_configuration_preview_0_params.Contact,
        logo: loa_configuration_preview_0_params.Logo,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Preview the LOA template that would be generated without need to create LOA
        configuration.

        Args:
          address: The address of the company.

          company_name: The name of the company

          contact: The contact information of the company.

          logo: The logo of the LOA configuration

          name: The name of the LOA configuration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/pdf", **(extra_headers or {})}
        return await self._post(
            "/porting/loa_configuration/preview",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "company_name": company_name,
                    "contact": contact,
                    "logo": logo,
                    "name": name,
                },
                loa_configuration_preview_0_params.LoaConfigurationPreview0Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def preview_1(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Preview a specific LOA configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/pdf", **(extra_headers or {})}
        return await self._get(
            f"/porting/loa_configurations/{id}/preview",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class LoaConfigurationsResourceWithRawResponse:
    def __init__(self, loa_configurations: LoaConfigurationsResource) -> None:
        self._loa_configurations = loa_configurations

        self.create = to_raw_response_wrapper(
            loa_configurations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            loa_configurations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            loa_configurations.update,
        )
        self.list = to_raw_response_wrapper(
            loa_configurations.list,
        )
        self.delete = to_raw_response_wrapper(
            loa_configurations.delete,
        )
        self.preview_0 = to_custom_raw_response_wrapper(
            loa_configurations.preview_0,
            BinaryAPIResponse,
        )
        self.preview_1 = to_custom_raw_response_wrapper(
            loa_configurations.preview_1,
            BinaryAPIResponse,
        )


class AsyncLoaConfigurationsResourceWithRawResponse:
    def __init__(self, loa_configurations: AsyncLoaConfigurationsResource) -> None:
        self._loa_configurations = loa_configurations

        self.create = async_to_raw_response_wrapper(
            loa_configurations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            loa_configurations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            loa_configurations.update,
        )
        self.list = async_to_raw_response_wrapper(
            loa_configurations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            loa_configurations.delete,
        )
        self.preview_0 = async_to_custom_raw_response_wrapper(
            loa_configurations.preview_0,
            AsyncBinaryAPIResponse,
        )
        self.preview_1 = async_to_custom_raw_response_wrapper(
            loa_configurations.preview_1,
            AsyncBinaryAPIResponse,
        )


class LoaConfigurationsResourceWithStreamingResponse:
    def __init__(self, loa_configurations: LoaConfigurationsResource) -> None:
        self._loa_configurations = loa_configurations

        self.create = to_streamed_response_wrapper(
            loa_configurations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            loa_configurations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            loa_configurations.update,
        )
        self.list = to_streamed_response_wrapper(
            loa_configurations.list,
        )
        self.delete = to_streamed_response_wrapper(
            loa_configurations.delete,
        )
        self.preview_0 = to_custom_streamed_response_wrapper(
            loa_configurations.preview_0,
            StreamedBinaryAPIResponse,
        )
        self.preview_1 = to_custom_streamed_response_wrapper(
            loa_configurations.preview_1,
            StreamedBinaryAPIResponse,
        )


class AsyncLoaConfigurationsResourceWithStreamingResponse:
    def __init__(self, loa_configurations: AsyncLoaConfigurationsResource) -> None:
        self._loa_configurations = loa_configurations

        self.create = async_to_streamed_response_wrapper(
            loa_configurations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            loa_configurations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            loa_configurations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            loa_configurations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            loa_configurations.delete,
        )
        self.preview_0 = async_to_custom_streamed_response_wrapper(
            loa_configurations.preview_0,
            AsyncStreamedBinaryAPIResponse,
        )
        self.preview_1 = async_to_custom_streamed_response_wrapper(
            loa_configurations.preview_1,
            AsyncStreamedBinaryAPIResponse,
        )
