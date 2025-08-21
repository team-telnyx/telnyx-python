# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ...types.messaging_profiles import (
    autoresp_config_list_params,
    autoresp_config_create_params,
    autoresp_config_update_params,
)
from ...types.messaging_profiles.auto_resp_config_response import AutoRespConfigResponse
from ...types.messaging_profiles.autoresp_config_list_response import AutorespConfigListResponse

__all__ = ["AutorespConfigsResource", "AsyncAutorespConfigsResource"]


class AutorespConfigsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AutorespConfigsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AutorespConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutorespConfigsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AutorespConfigsResourceWithStreamingResponse(self)

    def create(
        self,
        profile_id: str,
        *,
        country_code: str,
        keywords: List[str],
        op: Literal["start", "stop", "info"],
        resp_text: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AutoRespConfigResponse:
        """
        Create Auto-Reponse Setting

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return self._post(
            f"/messaging_profiles/{profile_id}/autoresp_configs",
            body=maybe_transform(
                {
                    "country_code": country_code,
                    "keywords": keywords,
                    "op": op,
                    "resp_text": resp_text,
                },
                autoresp_config_create_params.AutorespConfigCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoRespConfigResponse,
        )

    def retrieve(
        self,
        autoresp_cfg_id: str,
        *,
        profile_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AutoRespConfigResponse:
        """
        Get Auto-Response Setting

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        if not autoresp_cfg_id:
            raise ValueError(f"Expected a non-empty value for `autoresp_cfg_id` but received {autoresp_cfg_id!r}")
        return self._get(
            f"/messaging_profiles/{profile_id}/autoresp_configs/{autoresp_cfg_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoRespConfigResponse,
        )

    def update(
        self,
        autoresp_cfg_id: str,
        *,
        profile_id: str,
        country_code: str,
        keywords: List[str],
        op: Literal["start", "stop", "info"],
        resp_text: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AutoRespConfigResponse:
        """
        Update Auto-Response Setting

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        if not autoresp_cfg_id:
            raise ValueError(f"Expected a non-empty value for `autoresp_cfg_id` but received {autoresp_cfg_id!r}")
        return self._put(
            f"/messaging_profiles/{profile_id}/autoresp_configs/{autoresp_cfg_id}",
            body=maybe_transform(
                {
                    "country_code": country_code,
                    "keywords": keywords,
                    "op": op,
                    "resp_text": resp_text,
                },
                autoresp_config_update_params.AutorespConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoRespConfigResponse,
        )

    def list(
        self,
        profile_id: str,
        *,
        country_code: str | NotGiven = NOT_GIVEN,
        created_at: autoresp_config_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        updated_at: autoresp_config_list_params.UpdatedAt | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AutorespConfigListResponse:
        """
        List Auto-Response Settings

        Args:
          created_at:
              Consolidated created_at parameter (deepObject style). Originally:
              created_at[gte], created_at[lte]

          updated_at:
              Consolidated updated_at parameter (deepObject style). Originally:
              updated_at[gte], updated_at[lte]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return self._get(
            f"/messaging_profiles/{profile_id}/autoresp_configs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "country_code": country_code,
                        "created_at": created_at,
                        "updated_at": updated_at,
                    },
                    autoresp_config_list_params.AutorespConfigListParams,
                ),
            ),
            cast_to=AutorespConfigListResponse,
        )

    def delete(
        self,
        autoresp_cfg_id: str,
        *,
        profile_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete Auto-Response Setting

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        if not autoresp_cfg_id:
            raise ValueError(f"Expected a non-empty value for `autoresp_cfg_id` but received {autoresp_cfg_id!r}")
        return self._delete(
            f"/messaging_profiles/{profile_id}/autoresp_configs/{autoresp_cfg_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncAutorespConfigsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAutorespConfigsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAutorespConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutorespConfigsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncAutorespConfigsResourceWithStreamingResponse(self)

    async def create(
        self,
        profile_id: str,
        *,
        country_code: str,
        keywords: List[str],
        op: Literal["start", "stop", "info"],
        resp_text: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AutoRespConfigResponse:
        """
        Create Auto-Reponse Setting

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return await self._post(
            f"/messaging_profiles/{profile_id}/autoresp_configs",
            body=await async_maybe_transform(
                {
                    "country_code": country_code,
                    "keywords": keywords,
                    "op": op,
                    "resp_text": resp_text,
                },
                autoresp_config_create_params.AutorespConfigCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoRespConfigResponse,
        )

    async def retrieve(
        self,
        autoresp_cfg_id: str,
        *,
        profile_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AutoRespConfigResponse:
        """
        Get Auto-Response Setting

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        if not autoresp_cfg_id:
            raise ValueError(f"Expected a non-empty value for `autoresp_cfg_id` but received {autoresp_cfg_id!r}")
        return await self._get(
            f"/messaging_profiles/{profile_id}/autoresp_configs/{autoresp_cfg_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoRespConfigResponse,
        )

    async def update(
        self,
        autoresp_cfg_id: str,
        *,
        profile_id: str,
        country_code: str,
        keywords: List[str],
        op: Literal["start", "stop", "info"],
        resp_text: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AutoRespConfigResponse:
        """
        Update Auto-Response Setting

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        if not autoresp_cfg_id:
            raise ValueError(f"Expected a non-empty value for `autoresp_cfg_id` but received {autoresp_cfg_id!r}")
        return await self._put(
            f"/messaging_profiles/{profile_id}/autoresp_configs/{autoresp_cfg_id}",
            body=await async_maybe_transform(
                {
                    "country_code": country_code,
                    "keywords": keywords,
                    "op": op,
                    "resp_text": resp_text,
                },
                autoresp_config_update_params.AutorespConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutoRespConfigResponse,
        )

    async def list(
        self,
        profile_id: str,
        *,
        country_code: str | NotGiven = NOT_GIVEN,
        created_at: autoresp_config_list_params.CreatedAt | NotGiven = NOT_GIVEN,
        updated_at: autoresp_config_list_params.UpdatedAt | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AutorespConfigListResponse:
        """
        List Auto-Response Settings

        Args:
          created_at:
              Consolidated created_at parameter (deepObject style). Originally:
              created_at[gte], created_at[lte]

          updated_at:
              Consolidated updated_at parameter (deepObject style). Originally:
              updated_at[gte], updated_at[lte]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return await self._get(
            f"/messaging_profiles/{profile_id}/autoresp_configs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "country_code": country_code,
                        "created_at": created_at,
                        "updated_at": updated_at,
                    },
                    autoresp_config_list_params.AutorespConfigListParams,
                ),
            ),
            cast_to=AutorespConfigListResponse,
        )

    async def delete(
        self,
        autoresp_cfg_id: str,
        *,
        profile_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete Auto-Response Setting

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        if not autoresp_cfg_id:
            raise ValueError(f"Expected a non-empty value for `autoresp_cfg_id` but received {autoresp_cfg_id!r}")
        return await self._delete(
            f"/messaging_profiles/{profile_id}/autoresp_configs/{autoresp_cfg_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AutorespConfigsResourceWithRawResponse:
    def __init__(self, autoresp_configs: AutorespConfigsResource) -> None:
        self._autoresp_configs = autoresp_configs

        self.create = to_raw_response_wrapper(
            autoresp_configs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            autoresp_configs.retrieve,
        )
        self.update = to_raw_response_wrapper(
            autoresp_configs.update,
        )
        self.list = to_raw_response_wrapper(
            autoresp_configs.list,
        )
        self.delete = to_raw_response_wrapper(
            autoresp_configs.delete,
        )


class AsyncAutorespConfigsResourceWithRawResponse:
    def __init__(self, autoresp_configs: AsyncAutorespConfigsResource) -> None:
        self._autoresp_configs = autoresp_configs

        self.create = async_to_raw_response_wrapper(
            autoresp_configs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            autoresp_configs.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            autoresp_configs.update,
        )
        self.list = async_to_raw_response_wrapper(
            autoresp_configs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            autoresp_configs.delete,
        )


class AutorespConfigsResourceWithStreamingResponse:
    def __init__(self, autoresp_configs: AutorespConfigsResource) -> None:
        self._autoresp_configs = autoresp_configs

        self.create = to_streamed_response_wrapper(
            autoresp_configs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            autoresp_configs.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            autoresp_configs.update,
        )
        self.list = to_streamed_response_wrapper(
            autoresp_configs.list,
        )
        self.delete = to_streamed_response_wrapper(
            autoresp_configs.delete,
        )


class AsyncAutorespConfigsResourceWithStreamingResponse:
    def __init__(self, autoresp_configs: AsyncAutorespConfigsResource) -> None:
        self._autoresp_configs = autoresp_configs

        self.create = async_to_streamed_response_wrapper(
            autoresp_configs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            autoresp_configs.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            autoresp_configs.update,
        )
        self.list = async_to_streamed_response_wrapper(
            autoresp_configs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            autoresp_configs.delete,
        )
