# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import is_given, maybe_transform, strip_not_given, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ...._base_client import AsyncPaginator, make_request_options
from ....types.organizations import user_list_params, user_retrieve_params
from ....types.organizations.user_list_response import UserListResponse
from ....types.organizations.user_retrieve_response import UserRetrieveResponse
from ....types.organizations.user_get_groups_report_response import UserGetGroupsReportResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        include_groups: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveResponse:
        """
        Returns a user in your organization.

        Args:
          include_groups: When set to true, includes the groups array for each user in the response. The
              groups array contains objects with id and name for each group the user belongs
              to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/organizations/users/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"include_groups": include_groups}, user_retrieve_params.UserRetrieveParams),
            ),
            cast_to=UserRetrieveResponse,
        )

    def list(
        self,
        *,
        filter_email: str | Omit = omit,
        filter_user_status: Literal["enabled", "disabled", "blocked"] | Omit = omit,
        include_groups: bool | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[UserListResponse]:
        """
        Returns a list of the users in your organization.

        Args:
          filter_email: Filter by email address (partial match)

          filter_user_status: Filter by user status

          include_groups: When set to true, includes the groups array for each user in the response. The
              groups array contains objects with id and name for each group the user belongs
              to.

          page_number: The page number to load

          page_size: The size of the page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/organizations/users",
            page=SyncDefaultFlatPagination[UserListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_email": filter_email,
                        "filter_user_status": filter_user_status,
                        "include_groups": include_groups,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            model=UserListResponse,
        )

    def get_groups_report(
        self,
        *,
        accept: Literal["application/json", "text/csv"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserGetGroupsReportResponse:
        """
        Returns a report of all users in your organization with their group memberships.
        This endpoint returns all users without pagination and always includes group
        information. The report can be retrieved in JSON or CSV format by sending
        specific content-type headers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"Accept": str(accept) if is_given(accept) else not_given}),
            **(extra_headers or {}),
        }
        return self._get(
            "/organizations/users/users_groups_report",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserGetGroupsReportResponse,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        include_groups: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveResponse:
        """
        Returns a user in your organization.

        Args:
          include_groups: When set to true, includes the groups array for each user in the response. The
              groups array contains objects with id and name for each group the user belongs
              to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/organizations/users/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_groups": include_groups}, user_retrieve_params.UserRetrieveParams
                ),
            ),
            cast_to=UserRetrieveResponse,
        )

    def list(
        self,
        *,
        filter_email: str | Omit = omit,
        filter_user_status: Literal["enabled", "disabled", "blocked"] | Omit = omit,
        include_groups: bool | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[UserListResponse, AsyncDefaultFlatPagination[UserListResponse]]:
        """
        Returns a list of the users in your organization.

        Args:
          filter_email: Filter by email address (partial match)

          filter_user_status: Filter by user status

          include_groups: When set to true, includes the groups array for each user in the response. The
              groups array contains objects with id and name for each group the user belongs
              to.

          page_number: The page number to load

          page_size: The size of the page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/organizations/users",
            page=AsyncDefaultFlatPagination[UserListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_email": filter_email,
                        "filter_user_status": filter_user_status,
                        "include_groups": include_groups,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            model=UserListResponse,
        )

    async def get_groups_report(
        self,
        *,
        accept: Literal["application/json", "text/csv"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserGetGroupsReportResponse:
        """
        Returns a report of all users in your organization with their group memberships.
        This endpoint returns all users without pagination and always includes group
        information. The report can be retrieved in JSON or CSV format by sending
        specific content-type headers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"Accept": str(accept) if is_given(accept) else not_given}),
            **(extra_headers or {}),
        }
        return await self._get(
            "/organizations/users/users_groups_report",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserGetGroupsReportResponse,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.retrieve = to_raw_response_wrapper(
            users.retrieve,
        )
        self.list = to_raw_response_wrapper(
            users.list,
        )
        self.get_groups_report = to_raw_response_wrapper(
            users.get_groups_report,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._users.actions)


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.retrieve = async_to_raw_response_wrapper(
            users.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            users.list,
        )
        self.get_groups_report = async_to_raw_response_wrapper(
            users.get_groups_report,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._users.actions)


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.retrieve = to_streamed_response_wrapper(
            users.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            users.list,
        )
        self.get_groups_report = to_streamed_response_wrapper(
            users.get_groups_report,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._users.actions)


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.retrieve = async_to_streamed_response_wrapper(
            users.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            users.list,
        )
        self.get_groups_report = async_to_streamed_response_wrapper(
            users.get_groups_report,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._users.actions)
