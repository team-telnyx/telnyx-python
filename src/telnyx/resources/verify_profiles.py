# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    verify_profile_list_params,
    verify_profile_create_params,
    verify_profile_update_params,
    verify_profile_create_template_params,
    verify_profile_update_template_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.verify_profile import VerifyProfile
from ..types.message_template import MessageTemplate
from ..types.verify_profile_data import VerifyProfileData
from ..types.verify_profile_retrieve_templates_response import VerifyProfileRetrieveTemplatesResponse

__all__ = ["VerifyProfilesResource", "AsyncVerifyProfilesResource"]


class VerifyProfilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VerifyProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return VerifyProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VerifyProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return VerifyProfilesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        call: verify_profile_create_params.Call | Omit = omit,
        flashcall: verify_profile_create_params.Flashcall | Omit = omit,
        language: str | Omit = omit,
        sms: verify_profile_create_params.SMS | Omit = omit,
        webhook_failover_url: str | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerifyProfileData:
        """
        Creates a new Verify profile to associate verifications with.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/verify_profiles",
            body=maybe_transform(
                {
                    "name": name,
                    "call": call,
                    "flashcall": flashcall,
                    "language": language,
                    "sms": sms,
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                },
                verify_profile_create_params.VerifyProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerifyProfileData,
        )

    def retrieve(
        self,
        verify_profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerifyProfileData:
        """
        Gets a single Verify profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not verify_profile_id:
            raise ValueError(f"Expected a non-empty value for `verify_profile_id` but received {verify_profile_id!r}")
        return self._get(
            f"/verify_profiles/{verify_profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerifyProfileData,
        )

    def update(
        self,
        verify_profile_id: str,
        *,
        call: verify_profile_update_params.Call | Omit = omit,
        flashcall: verify_profile_update_params.Flashcall | Omit = omit,
        language: str | Omit = omit,
        name: str | Omit = omit,
        sms: verify_profile_update_params.SMS | Omit = omit,
        webhook_failover_url: str | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerifyProfileData:
        """
        Update Verify profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not verify_profile_id:
            raise ValueError(f"Expected a non-empty value for `verify_profile_id` but received {verify_profile_id!r}")
        return self._patch(
            f"/verify_profiles/{verify_profile_id}",
            body=maybe_transform(
                {
                    "call": call,
                    "flashcall": flashcall,
                    "language": language,
                    "name": name,
                    "sms": sms,
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                },
                verify_profile_update_params.VerifyProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerifyProfileData,
        )

    def list(
        self,
        *,
        filter: verify_profile_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[VerifyProfile]:
        """
        Gets a paginated list of Verify profiles.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[name]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/verify_profiles",
            page=SyncDefaultFlatPagination[VerifyProfile],
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
                    },
                    verify_profile_list_params.VerifyProfileListParams,
                ),
            ),
            model=VerifyProfile,
        )

    def delete(
        self,
        verify_profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerifyProfileData:
        """
        Delete Verify profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not verify_profile_id:
            raise ValueError(f"Expected a non-empty value for `verify_profile_id` but received {verify_profile_id!r}")
        return self._delete(
            f"/verify_profiles/{verify_profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerifyProfileData,
        )

    def create_template(
        self,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageTemplate:
        """
        Create a new Verify profile message template.

        Args:
          text: The text content of the message template.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/verify_profiles/templates",
            body=maybe_transform(
                {"text": text}, verify_profile_create_template_params.VerifyProfileCreateTemplateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageTemplate,
        )

    def retrieve_templates(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerifyProfileRetrieveTemplatesResponse:
        """List all Verify profile message templates."""
        return self._get(
            "/verify_profiles/templates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerifyProfileRetrieveTemplatesResponse,
        )

    def update_template(
        self,
        template_id: str,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageTemplate:
        """
        Update an existing Verify profile message template.

        Args:
          text: The text content of the message template.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return self._patch(
            f"/verify_profiles/templates/{template_id}",
            body=maybe_transform(
                {"text": text}, verify_profile_update_template_params.VerifyProfileUpdateTemplateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageTemplate,
        )


class AsyncVerifyProfilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVerifyProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVerifyProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVerifyProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncVerifyProfilesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        call: verify_profile_create_params.Call | Omit = omit,
        flashcall: verify_profile_create_params.Flashcall | Omit = omit,
        language: str | Omit = omit,
        sms: verify_profile_create_params.SMS | Omit = omit,
        webhook_failover_url: str | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerifyProfileData:
        """
        Creates a new Verify profile to associate verifications with.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/verify_profiles",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "call": call,
                    "flashcall": flashcall,
                    "language": language,
                    "sms": sms,
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                },
                verify_profile_create_params.VerifyProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerifyProfileData,
        )

    async def retrieve(
        self,
        verify_profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerifyProfileData:
        """
        Gets a single Verify profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not verify_profile_id:
            raise ValueError(f"Expected a non-empty value for `verify_profile_id` but received {verify_profile_id!r}")
        return await self._get(
            f"/verify_profiles/{verify_profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerifyProfileData,
        )

    async def update(
        self,
        verify_profile_id: str,
        *,
        call: verify_profile_update_params.Call | Omit = omit,
        flashcall: verify_profile_update_params.Flashcall | Omit = omit,
        language: str | Omit = omit,
        name: str | Omit = omit,
        sms: verify_profile_update_params.SMS | Omit = omit,
        webhook_failover_url: str | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerifyProfileData:
        """
        Update Verify profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not verify_profile_id:
            raise ValueError(f"Expected a non-empty value for `verify_profile_id` but received {verify_profile_id!r}")
        return await self._patch(
            f"/verify_profiles/{verify_profile_id}",
            body=await async_maybe_transform(
                {
                    "call": call,
                    "flashcall": flashcall,
                    "language": language,
                    "name": name,
                    "sms": sms,
                    "webhook_failover_url": webhook_failover_url,
                    "webhook_url": webhook_url,
                },
                verify_profile_update_params.VerifyProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerifyProfileData,
        )

    def list(
        self,
        *,
        filter: verify_profile_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[VerifyProfile, AsyncDefaultFlatPagination[VerifyProfile]]:
        """
        Gets a paginated list of Verify profiles.

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[name]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/verify_profiles",
            page=AsyncDefaultFlatPagination[VerifyProfile],
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
                    },
                    verify_profile_list_params.VerifyProfileListParams,
                ),
            ),
            model=VerifyProfile,
        )

    async def delete(
        self,
        verify_profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerifyProfileData:
        """
        Delete Verify profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not verify_profile_id:
            raise ValueError(f"Expected a non-empty value for `verify_profile_id` but received {verify_profile_id!r}")
        return await self._delete(
            f"/verify_profiles/{verify_profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerifyProfileData,
        )

    async def create_template(
        self,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageTemplate:
        """
        Create a new Verify profile message template.

        Args:
          text: The text content of the message template.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/verify_profiles/templates",
            body=await async_maybe_transform(
                {"text": text}, verify_profile_create_template_params.VerifyProfileCreateTemplateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageTemplate,
        )

    async def retrieve_templates(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerifyProfileRetrieveTemplatesResponse:
        """List all Verify profile message templates."""
        return await self._get(
            "/verify_profiles/templates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerifyProfileRetrieveTemplatesResponse,
        )

    async def update_template(
        self,
        template_id: str,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageTemplate:
        """
        Update an existing Verify profile message template.

        Args:
          text: The text content of the message template.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return await self._patch(
            f"/verify_profiles/templates/{template_id}",
            body=await async_maybe_transform(
                {"text": text}, verify_profile_update_template_params.VerifyProfileUpdateTemplateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageTemplate,
        )


class VerifyProfilesResourceWithRawResponse:
    def __init__(self, verify_profiles: VerifyProfilesResource) -> None:
        self._verify_profiles = verify_profiles

        self.create = to_raw_response_wrapper(
            verify_profiles.create,
        )
        self.retrieve = to_raw_response_wrapper(
            verify_profiles.retrieve,
        )
        self.update = to_raw_response_wrapper(
            verify_profiles.update,
        )
        self.list = to_raw_response_wrapper(
            verify_profiles.list,
        )
        self.delete = to_raw_response_wrapper(
            verify_profiles.delete,
        )
        self.create_template = to_raw_response_wrapper(
            verify_profiles.create_template,
        )
        self.retrieve_templates = to_raw_response_wrapper(
            verify_profiles.retrieve_templates,
        )
        self.update_template = to_raw_response_wrapper(
            verify_profiles.update_template,
        )


class AsyncVerifyProfilesResourceWithRawResponse:
    def __init__(self, verify_profiles: AsyncVerifyProfilesResource) -> None:
        self._verify_profiles = verify_profiles

        self.create = async_to_raw_response_wrapper(
            verify_profiles.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            verify_profiles.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            verify_profiles.update,
        )
        self.list = async_to_raw_response_wrapper(
            verify_profiles.list,
        )
        self.delete = async_to_raw_response_wrapper(
            verify_profiles.delete,
        )
        self.create_template = async_to_raw_response_wrapper(
            verify_profiles.create_template,
        )
        self.retrieve_templates = async_to_raw_response_wrapper(
            verify_profiles.retrieve_templates,
        )
        self.update_template = async_to_raw_response_wrapper(
            verify_profiles.update_template,
        )


class VerifyProfilesResourceWithStreamingResponse:
    def __init__(self, verify_profiles: VerifyProfilesResource) -> None:
        self._verify_profiles = verify_profiles

        self.create = to_streamed_response_wrapper(
            verify_profiles.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            verify_profiles.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            verify_profiles.update,
        )
        self.list = to_streamed_response_wrapper(
            verify_profiles.list,
        )
        self.delete = to_streamed_response_wrapper(
            verify_profiles.delete,
        )
        self.create_template = to_streamed_response_wrapper(
            verify_profiles.create_template,
        )
        self.retrieve_templates = to_streamed_response_wrapper(
            verify_profiles.retrieve_templates,
        )
        self.update_template = to_streamed_response_wrapper(
            verify_profiles.update_template,
        )


class AsyncVerifyProfilesResourceWithStreamingResponse:
    def __init__(self, verify_profiles: AsyncVerifyProfilesResource) -> None:
        self._verify_profiles = verify_profiles

        self.create = async_to_streamed_response_wrapper(
            verify_profiles.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            verify_profiles.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            verify_profiles.update,
        )
        self.list = async_to_streamed_response_wrapper(
            verify_profiles.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            verify_profiles.delete,
        )
        self.create_template = async_to_streamed_response_wrapper(
            verify_profiles.create_template,
        )
        self.retrieve_templates = async_to_streamed_response_wrapper(
            verify_profiles.retrieve_templates,
        )
        self.update_template = async_to_streamed_response_wrapper(
            verify_profiles.update_template,
        )
