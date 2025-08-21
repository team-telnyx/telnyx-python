# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from .jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
)
from .voice import (
    VoiceResource,
    AsyncVoiceResource,
    VoiceResourceWithRawResponse,
    AsyncVoiceResourceWithRawResponse,
    VoiceResourceWithStreamingResponse,
    AsyncVoiceResourceWithStreamingResponse,
)
from ...types import phone_number_list_params, phone_number_update_params, phone_number_slim_list_params
from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .messaging import (
    MessagingResource,
    AsyncMessagingResource,
    MessagingResourceWithRawResponse,
    AsyncMessagingResourceWithRawResponse,
    MessagingResourceWithStreamingResponse,
    AsyncMessagingResourceWithStreamingResponse,
)
from .voicemail import (
    VoicemailResource,
    AsyncVoicemailResource,
    VoicemailResourceWithRawResponse,
    AsyncVoicemailResourceWithRawResponse,
    VoicemailResourceWithStreamingResponse,
    AsyncVoicemailResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .csv_downloads import (
    CsvDownloadsResource,
    AsyncCsvDownloadsResource,
    CsvDownloadsResourceWithRawResponse,
    AsyncCsvDownloadsResourceWithRawResponse,
    CsvDownloadsResourceWithStreamingResponse,
    AsyncCsvDownloadsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.phone_number_list_response import PhoneNumberListResponse
from ...types.phone_number_delete_response import PhoneNumberDeleteResponse
from ...types.phone_number_update_response import PhoneNumberUpdateResponse
from ...types.phone_number_retrieve_response import PhoneNumberRetrieveResponse
from ...types.phone_number_slim_list_response import PhoneNumberSlimListResponse

__all__ = ["PhoneNumbersResource", "AsyncPhoneNumbersResource"]


class PhoneNumbersResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def csv_downloads(self) -> CsvDownloadsResource:
        return CsvDownloadsResource(self._client)

    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

    @cached_property
    def messaging(self) -> MessagingResource:
        return MessagingResource(self._client)

    @cached_property
    def voice(self) -> VoiceResource:
        return VoiceResource(self._client)

    @cached_property
    def voicemail(self) -> VoicemailResource:
        return VoicemailResource(self._client)

    @cached_property
    def with_raw_response(self) -> PhoneNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return PhoneNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhoneNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return PhoneNumbersResourceWithStreamingResponse(self)

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
    ) -> PhoneNumberRetrieveResponse:
        """
        Retrieve a phone number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/phone_numbers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        billing_group_id: str | NotGiven = NOT_GIVEN,
        connection_id: str | NotGiven = NOT_GIVEN,
        customer_reference: str | NotGiven = NOT_GIVEN,
        external_pin: str | NotGiven = NOT_GIVEN,
        hd_voice_enabled: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberUpdateResponse:
        """
        Update a phone number

        Args:
          billing_group_id: Identifies the billing group associated with the phone number.

          connection_id: Identifies the connection associated with the phone number.

          customer_reference: A customer reference string for customer look ups.

          external_pin: If someone attempts to port your phone number away from Telnyx and your phone
              number has an external PIN set, we will attempt to verify that you provided the
              correct external PIN to the winning carrier. Note that not all carriers
              cooperate with this security mechanism.

          hd_voice_enabled: Indicates whether HD voice is enabled for this number.

          tags: A list of user-assigned tags to help organize phone numbers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/phone_numbers/{id}",
            body=maybe_transform(
                {
                    "billing_group_id": billing_group_id,
                    "connection_id": connection_id,
                    "customer_reference": customer_reference,
                    "external_pin": external_pin,
                    "hd_voice_enabled": hd_voice_enabled,
                    "tags": tags,
                },
                phone_number_update_params.PhoneNumberUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberUpdateResponse,
        )

    def list(
        self,
        *,
        filter: phone_number_list_params.Filter | NotGiven = NOT_GIVEN,
        page: phone_number_list_params.Page | NotGiven = NOT_GIVEN,
        sort: Literal["purchased_at", "phone_number", "connection_name", "usage_payment_method"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberListResponse:
        """
        List phone numbers

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[tag],
              filter[phone_number], filter[status], filter[country_iso_alpha2],
              filter[connection_id], filter[voice.connection_name],
              filter[voice.usage_payment_method], filter[billing_group_id],
              filter[emergency_address_id], filter[customer_reference], filter[number_type],
              filter[source]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          sort: Specifies the sort order for results. If not given, results are sorted by
              created_at in descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/phone_numbers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                        "sort": sort,
                    },
                    phone_number_list_params.PhoneNumberListParams,
                ),
            ),
            cast_to=PhoneNumberListResponse,
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
    ) -> PhoneNumberDeleteResponse:
        """
        Delete a phone number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/phone_numbers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberDeleteResponse,
        )

    def slim_list(
        self,
        *,
        filter: phone_number_slim_list_params.Filter | NotGiven = NOT_GIVEN,
        include_connection: bool | NotGiven = NOT_GIVEN,
        include_tags: bool | NotGiven = NOT_GIVEN,
        page: phone_number_slim_list_params.Page | NotGiven = NOT_GIVEN,
        sort: Literal["purchased_at", "phone_number", "connection_name", "usage_payment_method"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberSlimListResponse:
        """
        List phone numbers, This endpoint is a lighter version of the /phone_numbers
        endpoint having higher performance and rate limit.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[tag],
              filter[phone_number], filter[status], filter[country_iso_alpha2],
              filter[connection_id], filter[voice.connection_name],
              filter[voice.usage_payment_method], filter[billing_group_id],
              filter[emergency_address_id], filter[customer_reference], filter[number_type],
              filter[source]

          include_connection: Include the connection associated with the phone number.

          include_tags: Include the tags associated with the phone number.

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          sort: Specifies the sort order for results. If not given, results are sorted by
              created_at in descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/phone_numbers/slim",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "include_connection": include_connection,
                        "include_tags": include_tags,
                        "page": page,
                        "sort": sort,
                    },
                    phone_number_slim_list_params.PhoneNumberSlimListParams,
                ),
            ),
            cast_to=PhoneNumberSlimListResponse,
        )


class AsyncPhoneNumbersResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def csv_downloads(self) -> AsyncCsvDownloadsResource:
        return AsyncCsvDownloadsResource(self._client)

    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

    @cached_property
    def messaging(self) -> AsyncMessagingResource:
        return AsyncMessagingResource(self._client)

    @cached_property
    def voice(self) -> AsyncVoiceResource:
        return AsyncVoiceResource(self._client)

    @cached_property
    def voicemail(self) -> AsyncVoicemailResource:
        return AsyncVoicemailResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPhoneNumbersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPhoneNumbersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhoneNumbersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncPhoneNumbersResourceWithStreamingResponse(self)

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
    ) -> PhoneNumberRetrieveResponse:
        """
        Retrieve a phone number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/phone_numbers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        billing_group_id: str | NotGiven = NOT_GIVEN,
        connection_id: str | NotGiven = NOT_GIVEN,
        customer_reference: str | NotGiven = NOT_GIVEN,
        external_pin: str | NotGiven = NOT_GIVEN,
        hd_voice_enabled: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberUpdateResponse:
        """
        Update a phone number

        Args:
          billing_group_id: Identifies the billing group associated with the phone number.

          connection_id: Identifies the connection associated with the phone number.

          customer_reference: A customer reference string for customer look ups.

          external_pin: If someone attempts to port your phone number away from Telnyx and your phone
              number has an external PIN set, we will attempt to verify that you provided the
              correct external PIN to the winning carrier. Note that not all carriers
              cooperate with this security mechanism.

          hd_voice_enabled: Indicates whether HD voice is enabled for this number.

          tags: A list of user-assigned tags to help organize phone numbers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/phone_numbers/{id}",
            body=await async_maybe_transform(
                {
                    "billing_group_id": billing_group_id,
                    "connection_id": connection_id,
                    "customer_reference": customer_reference,
                    "external_pin": external_pin,
                    "hd_voice_enabled": hd_voice_enabled,
                    "tags": tags,
                },
                phone_number_update_params.PhoneNumberUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberUpdateResponse,
        )

    async def list(
        self,
        *,
        filter: phone_number_list_params.Filter | NotGiven = NOT_GIVEN,
        page: phone_number_list_params.Page | NotGiven = NOT_GIVEN,
        sort: Literal["purchased_at", "phone_number", "connection_name", "usage_payment_method"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberListResponse:
        """
        List phone numbers

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[tag],
              filter[phone_number], filter[status], filter[country_iso_alpha2],
              filter[connection_id], filter[voice.connection_name],
              filter[voice.usage_payment_method], filter[billing_group_id],
              filter[emergency_address_id], filter[customer_reference], filter[number_type],
              filter[source]

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          sort: Specifies the sort order for results. If not given, results are sorted by
              created_at in descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/phone_numbers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                        "sort": sort,
                    },
                    phone_number_list_params.PhoneNumberListParams,
                ),
            ),
            cast_to=PhoneNumberListResponse,
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
    ) -> PhoneNumberDeleteResponse:
        """
        Delete a phone number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/phone_numbers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberDeleteResponse,
        )

    async def slim_list(
        self,
        *,
        filter: phone_number_slim_list_params.Filter | NotGiven = NOT_GIVEN,
        include_connection: bool | NotGiven = NOT_GIVEN,
        include_tags: bool | NotGiven = NOT_GIVEN,
        page: phone_number_slim_list_params.Page | NotGiven = NOT_GIVEN,
        sort: Literal["purchased_at", "phone_number", "connection_name", "usage_payment_method"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberSlimListResponse:
        """
        List phone numbers, This endpoint is a lighter version of the /phone_numbers
        endpoint having higher performance and rate limit.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[tag],
              filter[phone_number], filter[status], filter[country_iso_alpha2],
              filter[connection_id], filter[voice.connection_name],
              filter[voice.usage_payment_method], filter[billing_group_id],
              filter[emergency_address_id], filter[customer_reference], filter[number_type],
              filter[source]

          include_connection: Include the connection associated with the phone number.

          include_tags: Include the tags associated with the phone number.

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          sort: Specifies the sort order for results. If not given, results are sorted by
              created_at in descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/phone_numbers/slim",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "include_connection": include_connection,
                        "include_tags": include_tags,
                        "page": page,
                        "sort": sort,
                    },
                    phone_number_slim_list_params.PhoneNumberSlimListParams,
                ),
            ),
            cast_to=PhoneNumberSlimListResponse,
        )


class PhoneNumbersResourceWithRawResponse:
    def __init__(self, phone_numbers: PhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.retrieve = to_raw_response_wrapper(
            phone_numbers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            phone_numbers.update,
        )
        self.list = to_raw_response_wrapper(
            phone_numbers.list,
        )
        self.delete = to_raw_response_wrapper(
            phone_numbers.delete,
        )
        self.slim_list = to_raw_response_wrapper(
            phone_numbers.slim_list,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._phone_numbers.actions)

    @cached_property
    def csv_downloads(self) -> CsvDownloadsResourceWithRawResponse:
        return CsvDownloadsResourceWithRawResponse(self._phone_numbers.csv_downloads)

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._phone_numbers.jobs)

    @cached_property
    def messaging(self) -> MessagingResourceWithRawResponse:
        return MessagingResourceWithRawResponse(self._phone_numbers.messaging)

    @cached_property
    def voice(self) -> VoiceResourceWithRawResponse:
        return VoiceResourceWithRawResponse(self._phone_numbers.voice)

    @cached_property
    def voicemail(self) -> VoicemailResourceWithRawResponse:
        return VoicemailResourceWithRawResponse(self._phone_numbers.voicemail)


class AsyncPhoneNumbersResourceWithRawResponse:
    def __init__(self, phone_numbers: AsyncPhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.retrieve = async_to_raw_response_wrapper(
            phone_numbers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            phone_numbers.update,
        )
        self.list = async_to_raw_response_wrapper(
            phone_numbers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            phone_numbers.delete,
        )
        self.slim_list = async_to_raw_response_wrapper(
            phone_numbers.slim_list,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._phone_numbers.actions)

    @cached_property
    def csv_downloads(self) -> AsyncCsvDownloadsResourceWithRawResponse:
        return AsyncCsvDownloadsResourceWithRawResponse(self._phone_numbers.csv_downloads)

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._phone_numbers.jobs)

    @cached_property
    def messaging(self) -> AsyncMessagingResourceWithRawResponse:
        return AsyncMessagingResourceWithRawResponse(self._phone_numbers.messaging)

    @cached_property
    def voice(self) -> AsyncVoiceResourceWithRawResponse:
        return AsyncVoiceResourceWithRawResponse(self._phone_numbers.voice)

    @cached_property
    def voicemail(self) -> AsyncVoicemailResourceWithRawResponse:
        return AsyncVoicemailResourceWithRawResponse(self._phone_numbers.voicemail)


class PhoneNumbersResourceWithStreamingResponse:
    def __init__(self, phone_numbers: PhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.retrieve = to_streamed_response_wrapper(
            phone_numbers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            phone_numbers.update,
        )
        self.list = to_streamed_response_wrapper(
            phone_numbers.list,
        )
        self.delete = to_streamed_response_wrapper(
            phone_numbers.delete,
        )
        self.slim_list = to_streamed_response_wrapper(
            phone_numbers.slim_list,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._phone_numbers.actions)

    @cached_property
    def csv_downloads(self) -> CsvDownloadsResourceWithStreamingResponse:
        return CsvDownloadsResourceWithStreamingResponse(self._phone_numbers.csv_downloads)

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._phone_numbers.jobs)

    @cached_property
    def messaging(self) -> MessagingResourceWithStreamingResponse:
        return MessagingResourceWithStreamingResponse(self._phone_numbers.messaging)

    @cached_property
    def voice(self) -> VoiceResourceWithStreamingResponse:
        return VoiceResourceWithStreamingResponse(self._phone_numbers.voice)

    @cached_property
    def voicemail(self) -> VoicemailResourceWithStreamingResponse:
        return VoicemailResourceWithStreamingResponse(self._phone_numbers.voicemail)


class AsyncPhoneNumbersResourceWithStreamingResponse:
    def __init__(self, phone_numbers: AsyncPhoneNumbersResource) -> None:
        self._phone_numbers = phone_numbers

        self.retrieve = async_to_streamed_response_wrapper(
            phone_numbers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            phone_numbers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            phone_numbers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            phone_numbers.delete,
        )
        self.slim_list = async_to_streamed_response_wrapper(
            phone_numbers.slim_list,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._phone_numbers.actions)

    @cached_property
    def csv_downloads(self) -> AsyncCsvDownloadsResourceWithStreamingResponse:
        return AsyncCsvDownloadsResourceWithStreamingResponse(self._phone_numbers.csv_downloads)

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._phone_numbers.jobs)

    @cached_property
    def messaging(self) -> AsyncMessagingResourceWithStreamingResponse:
        return AsyncMessagingResourceWithStreamingResponse(self._phone_numbers.messaging)

    @cached_property
    def voice(self) -> AsyncVoiceResourceWithStreamingResponse:
        return AsyncVoiceResourceWithStreamingResponse(self._phone_numbers.voice)

    @cached_property
    def voicemail(self) -> AsyncVoicemailResourceWithStreamingResponse:
        return AsyncVoicemailResourceWithStreamingResponse(self._phone_numbers.voicemail)
