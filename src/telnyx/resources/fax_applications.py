# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import (
    AnchorsiteOverride,
    fax_application_list_params,
    fax_application_create_params,
    fax_application_update_params,
)
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
from ..pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.fax_application import FaxApplication
from ..types.anchorsite_override import AnchorsiteOverride
from ..types.fax_application_create_response import FaxApplicationCreateResponse
from ..types.fax_application_delete_response import FaxApplicationDeleteResponse
from ..types.fax_application_update_response import FaxApplicationUpdateResponse
from ..types.fax_application_retrieve_response import FaxApplicationRetrieveResponse

__all__ = ["FaxApplicationsResource", "AsyncFaxApplicationsResource"]


class FaxApplicationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FaxApplicationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return FaxApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FaxApplicationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return FaxApplicationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        application_name: str,
        webhook_event_url: str,
        active: bool | Omit = omit,
        anchorsite_override: AnchorsiteOverride | Omit = omit,
        inbound: fax_application_create_params.Inbound | Omit = omit,
        outbound: fax_application_create_params.Outbound | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        webhook_event_failover_url: Optional[str] | Omit = omit,
        webhook_timeout_secs: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FaxApplicationCreateResponse:
        """Creates a new Fax Application based on the parameters sent in the request.

        The
        application name and webhook URL are required. Once created, you can assign
        phone numbers to your application using the `/phone_numbers` endpoint.

        Args:
          application_name: A user-assigned name to help manage the application.

          webhook_event_url: The URL where webhooks related to this connection will be sent. Must include a
              scheme, such as 'https'.

          active: Specifies whether the connection can be used.

          anchorsite_override: `Latency` directs Telnyx to route media through the site with the lowest
              round-trip time to the user's connection. Telnyx calculates this time using ICMP
              ping messages. This can be disabled by specifying a site to handle all media.

          tags: Tags associated with the Fax Application.

          webhook_event_failover_url: The failover URL where webhooks related to this connection will be sent if
              sending to the primary URL fails. Must include a scheme, such as 'https'.

          webhook_timeout_secs: Specifies how many seconds to wait before timing out a webhook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/fax_applications",
            body=maybe_transform(
                {
                    "application_name": application_name,
                    "webhook_event_url": webhook_event_url,
                    "active": active,
                    "anchorsite_override": anchorsite_override,
                    "inbound": inbound,
                    "outbound": outbound,
                    "tags": tags,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                fax_application_create_params.FaxApplicationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FaxApplicationCreateResponse,
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
    ) -> FaxApplicationRetrieveResponse:
        """
        Return the details of an existing Fax Application inside the 'data' attribute of
        the response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/fax_applications/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FaxApplicationRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        application_name: str,
        webhook_event_url: str,
        active: bool | Omit = omit,
        anchorsite_override: AnchorsiteOverride | Omit = omit,
        fax_email_recipient: Optional[str] | Omit = omit,
        inbound: fax_application_update_params.Inbound | Omit = omit,
        outbound: fax_application_update_params.Outbound | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        webhook_event_failover_url: Optional[str] | Omit = omit,
        webhook_timeout_secs: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FaxApplicationUpdateResponse:
        """
        Updates settings of an existing Fax Application based on the parameters of the
        request.

        Args:
          application_name: A user-assigned name to help manage the application.

          webhook_event_url: The URL where webhooks related to this connection will be sent. Must include a
              scheme, such as 'https'.

          active: Specifies whether the connection can be used.

          anchorsite_override: `Latency` directs Telnyx to route media through the site with the lowest
              round-trip time to the user's connection. Telnyx calculates this time using ICMP
              ping messages. This can be disabled by specifying a site to handle all media.

          fax_email_recipient: Specifies an email address where faxes sent to this application will be
              forwarded to (as pdf or tiff attachments)

          tags: Tags associated with the Fax Application.

          webhook_event_failover_url: The failover URL where webhooks related to this connection will be sent if
              sending to the primary URL fails. Must include a scheme, such as 'https'.

          webhook_timeout_secs: Specifies how many seconds to wait before timing out a webhook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/fax_applications/{id}",
            body=maybe_transform(
                {
                    "application_name": application_name,
                    "webhook_event_url": webhook_event_url,
                    "active": active,
                    "anchorsite_override": anchorsite_override,
                    "fax_email_recipient": fax_email_recipient,
                    "inbound": inbound,
                    "outbound": outbound,
                    "tags": tags,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                fax_application_update_params.FaxApplicationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FaxApplicationUpdateResponse,
        )

    def list(
        self,
        *,
        filter: fax_application_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal["created_at", "application_name", "active"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[FaxApplication]:
        """
        This endpoint returns a list of your Fax Applications inside the 'data'
        attribute of the response. You can adjust which applications are listed by using
        filters. Fax Applications are used to configure how you send and receive faxes
        using the Programmable Fax API with Telnyx.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[application_name][contains], filter[outbound_voice_profile_id]

          sort: Specifies the sort order for results. By default sorting direction is ascending.
              To have the results sorted in descending order add the <code> -</code>
              prefix.<br/><br/> That is: <ul>

                <li>
                  <code>application_name</code>: sorts the result by the
                  <code>application_name</code> field in ascending order.
                </li>

                <li>
                  <code>-application_name</code>: sorts the result by the
                  <code>application_name</code> field in descending order.
                </li>
              </ul> <br/> If not given, results are sorted by <code>created_at</code> in descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/fax_applications",
            page=SyncDefaultFlatPagination[FaxApplication],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    fax_application_list_params.FaxApplicationListParams,
                ),
            ),
            model=FaxApplication,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FaxApplicationDeleteResponse:
        """Permanently deletes a Fax Application.

        Deletion may be prevented if the
        application is in use by phone numbers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/fax_applications/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FaxApplicationDeleteResponse,
        )


class AsyncFaxApplicationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFaxApplicationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFaxApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFaxApplicationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncFaxApplicationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        application_name: str,
        webhook_event_url: str,
        active: bool | Omit = omit,
        anchorsite_override: AnchorsiteOverride | Omit = omit,
        inbound: fax_application_create_params.Inbound | Omit = omit,
        outbound: fax_application_create_params.Outbound | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        webhook_event_failover_url: Optional[str] | Omit = omit,
        webhook_timeout_secs: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FaxApplicationCreateResponse:
        """Creates a new Fax Application based on the parameters sent in the request.

        The
        application name and webhook URL are required. Once created, you can assign
        phone numbers to your application using the `/phone_numbers` endpoint.

        Args:
          application_name: A user-assigned name to help manage the application.

          webhook_event_url: The URL where webhooks related to this connection will be sent. Must include a
              scheme, such as 'https'.

          active: Specifies whether the connection can be used.

          anchorsite_override: `Latency` directs Telnyx to route media through the site with the lowest
              round-trip time to the user's connection. Telnyx calculates this time using ICMP
              ping messages. This can be disabled by specifying a site to handle all media.

          tags: Tags associated with the Fax Application.

          webhook_event_failover_url: The failover URL where webhooks related to this connection will be sent if
              sending to the primary URL fails. Must include a scheme, such as 'https'.

          webhook_timeout_secs: Specifies how many seconds to wait before timing out a webhook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/fax_applications",
            body=await async_maybe_transform(
                {
                    "application_name": application_name,
                    "webhook_event_url": webhook_event_url,
                    "active": active,
                    "anchorsite_override": anchorsite_override,
                    "inbound": inbound,
                    "outbound": outbound,
                    "tags": tags,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                fax_application_create_params.FaxApplicationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FaxApplicationCreateResponse,
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
    ) -> FaxApplicationRetrieveResponse:
        """
        Return the details of an existing Fax Application inside the 'data' attribute of
        the response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/fax_applications/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FaxApplicationRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        application_name: str,
        webhook_event_url: str,
        active: bool | Omit = omit,
        anchorsite_override: AnchorsiteOverride | Omit = omit,
        fax_email_recipient: Optional[str] | Omit = omit,
        inbound: fax_application_update_params.Inbound | Omit = omit,
        outbound: fax_application_update_params.Outbound | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        webhook_event_failover_url: Optional[str] | Omit = omit,
        webhook_timeout_secs: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FaxApplicationUpdateResponse:
        """
        Updates settings of an existing Fax Application based on the parameters of the
        request.

        Args:
          application_name: A user-assigned name to help manage the application.

          webhook_event_url: The URL where webhooks related to this connection will be sent. Must include a
              scheme, such as 'https'.

          active: Specifies whether the connection can be used.

          anchorsite_override: `Latency` directs Telnyx to route media through the site with the lowest
              round-trip time to the user's connection. Telnyx calculates this time using ICMP
              ping messages. This can be disabled by specifying a site to handle all media.

          fax_email_recipient: Specifies an email address where faxes sent to this application will be
              forwarded to (as pdf or tiff attachments)

          tags: Tags associated with the Fax Application.

          webhook_event_failover_url: The failover URL where webhooks related to this connection will be sent if
              sending to the primary URL fails. Must include a scheme, such as 'https'.

          webhook_timeout_secs: Specifies how many seconds to wait before timing out a webhook.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/fax_applications/{id}",
            body=await async_maybe_transform(
                {
                    "application_name": application_name,
                    "webhook_event_url": webhook_event_url,
                    "active": active,
                    "anchorsite_override": anchorsite_override,
                    "fax_email_recipient": fax_email_recipient,
                    "inbound": inbound,
                    "outbound": outbound,
                    "tags": tags,
                    "webhook_event_failover_url": webhook_event_failover_url,
                    "webhook_timeout_secs": webhook_timeout_secs,
                },
                fax_application_update_params.FaxApplicationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FaxApplicationUpdateResponse,
        )

    def list(
        self,
        *,
        filter: fax_application_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal["created_at", "application_name", "active"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[FaxApplication, AsyncDefaultFlatPagination[FaxApplication]]:
        """
        This endpoint returns a list of your Fax Applications inside the 'data'
        attribute of the response. You can adjust which applications are listed by using
        filters. Fax Applications are used to configure how you send and receive faxes
        using the Programmable Fax API with Telnyx.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[application_name][contains], filter[outbound_voice_profile_id]

          sort: Specifies the sort order for results. By default sorting direction is ascending.
              To have the results sorted in descending order add the <code> -</code>
              prefix.<br/><br/> That is: <ul>

                <li>
                  <code>application_name</code>: sorts the result by the
                  <code>application_name</code> field in ascending order.
                </li>

                <li>
                  <code>-application_name</code>: sorts the result by the
                  <code>application_name</code> field in descending order.
                </li>
              </ul> <br/> If not given, results are sorted by <code>created_at</code> in descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/fax_applications",
            page=AsyncDefaultFlatPagination[FaxApplication],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    fax_application_list_params.FaxApplicationListParams,
                ),
            ),
            model=FaxApplication,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FaxApplicationDeleteResponse:
        """Permanently deletes a Fax Application.

        Deletion may be prevented if the
        application is in use by phone numbers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/fax_applications/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FaxApplicationDeleteResponse,
        )


class FaxApplicationsResourceWithRawResponse:
    def __init__(self, fax_applications: FaxApplicationsResource) -> None:
        self._fax_applications = fax_applications

        self.create = to_raw_response_wrapper(
            fax_applications.create,
        )
        self.retrieve = to_raw_response_wrapper(
            fax_applications.retrieve,
        )
        self.update = to_raw_response_wrapper(
            fax_applications.update,
        )
        self.list = to_raw_response_wrapper(
            fax_applications.list,
        )
        self.delete = to_raw_response_wrapper(
            fax_applications.delete,
        )


class AsyncFaxApplicationsResourceWithRawResponse:
    def __init__(self, fax_applications: AsyncFaxApplicationsResource) -> None:
        self._fax_applications = fax_applications

        self.create = async_to_raw_response_wrapper(
            fax_applications.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            fax_applications.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            fax_applications.update,
        )
        self.list = async_to_raw_response_wrapper(
            fax_applications.list,
        )
        self.delete = async_to_raw_response_wrapper(
            fax_applications.delete,
        )


class FaxApplicationsResourceWithStreamingResponse:
    def __init__(self, fax_applications: FaxApplicationsResource) -> None:
        self._fax_applications = fax_applications

        self.create = to_streamed_response_wrapper(
            fax_applications.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            fax_applications.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            fax_applications.update,
        )
        self.list = to_streamed_response_wrapper(
            fax_applications.list,
        )
        self.delete = to_streamed_response_wrapper(
            fax_applications.delete,
        )


class AsyncFaxApplicationsResourceWithStreamingResponse:
    def __init__(self, fax_applications: AsyncFaxApplicationsResource) -> None:
        self._fax_applications = fax_applications

        self.create = async_to_streamed_response_wrapper(
            fax_applications.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            fax_applications.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            fax_applications.update,
        )
        self.list = async_to_streamed_response_wrapper(
            fax_applications.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            fax_applications.delete,
        )
