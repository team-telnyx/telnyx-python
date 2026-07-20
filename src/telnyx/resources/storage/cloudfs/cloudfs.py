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
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.storage import cloudf_list_params, cloudf_create_params, cloudf_update_params
from ....types.storage.cloudf_list_response import CloudfListResponse
from ....types.storage.cloudfs_filesystem_response_wrapper import CloudfsFilesystemResponseWrapper
from ....types.storage.cloudfs_filesystem_detail_response_wrapper import CloudfsFilesystemDetailResponseWrapper

__all__ = ["CloudfsResource", "AsyncCloudfsResource"]


class CloudfsResource(SyncAPIResource):
    """
    Manage CloudFS filesystems — JuiceFS-compatible filesystems backed by Telnyx Cloud Storage
    """

    @cached_property
    def actions(self) -> ActionsResource:
        """
        Manage CloudFS filesystems — JuiceFS-compatible filesystems backed by Telnyx Cloud Storage
        """
        return ActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CloudfsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return CloudfsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CloudfsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return CloudfsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        region: Literal["us-central-1", "us-east-1", "us-west-1"],
        idempotency_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CloudfsFilesystemResponseWrapper:
        """Creates a CloudFS filesystem.

        Provisioning is synchronous — typically a few
        seconds, up to a few minutes — and the filesystem is returned with status
        `ready`, together with its S3 bucket and metadata connection details. This
        response is the only time the filesystem's `meta_token` — and the
        credential-bearing `meta_url` — are returned; store them securely. If the token
        is lost, issue a new one with the rotate-meta-token action. Names are unique
        within your organization: creating with an existing name returns a `422`.
        Requests are idempotent: retrying with the same `Idempotency-Key` within 24
        hours replays the original response instead of creating another filesystem.

        Args:
          name: Filesystem name, unique within your organization. Names are trimmed and
              lowercased; after normalization they may contain lowercase letters, numbers,
              `.`, `_`, and `-` only.

          region: Region where the filesystem's storage and metadata are provisioned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or {})}
        return self._post(
            "/storage/cloudfs",
            body=maybe_transform(
                {
                    "name": name,
                    "region": region,
                },
                cloudf_create_params.CloudfCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CloudfsFilesystemResponseWrapper,
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
    ) -> CloudfsFilesystemDetailResponseWrapper:
        """Retrieves a CloudFS filesystem by its ID.

        The returned `meta_url` omits the
        credential — the metadata token is only ever returned by create and
        rotate-meta-token. A filesystem whose last lifecycle action failed includes a
        customer-safe `error` message.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/storage/cloudfs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CloudfsFilesystemDetailResponseWrapper,
        )

    def update(
        self,
        id: str,
        *,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CloudfsFilesystemDetailResponseWrapper:
        """Updates a CloudFS filesystem.

        Only `name` can be changed; other fields are
        immutable and unknown fields are rejected with a `400`. Renaming to a name that
        already exists in your organization returns a `422`.

        Args:
          name: New filesystem name, unique within your organization. Names are trimmed and
              lowercased; after normalization they may contain lowercase letters, numbers,
              `.`, `_`, and `-` only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/storage/cloudfs/{id}", id=id),
            body=maybe_transform({"name": name}, cloudf_update_params.CloudfUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CloudfsFilesystemDetailResponseWrapper,
        )

    def list(
        self,
        *,
        filter_name: str | Omit = omit,
        filter_region: str | Omit = omit,
        filter_status: Literal["provisioning", "ready", "needs_format", "deleting", "failed"] | Omit = omit,
        page_after: str | Omit = omit,
        page_before: str | Omit = omit,
        page_limit: int | Omit = omit,
        sort: Literal["created_at", "-created_at", "updated_at", "-updated_at", "name", "-name"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CloudfListResponse:
        """Lists the CloudFS filesystems for the authenticated user's organization.

        Results
        use cursor-based pagination: fetch the next page by passing `meta.cursors.after`
        as `page[after]`, or follow the `meta.next` URL.

        Args:
          filter_name: Return only the filesystem whose name matches exactly.

          filter_region: Return only filesystems in this region.

          filter_status: Return only filesystems with this status. Unrecognized values are ignored.

          page_after: Opaque cursor from a previous response's `meta.cursors.after`; returns the page
              after it. Mutually exclusive with `page[before]`.

          page_before: Opaque cursor from a previous response's `meta.cursors.before`; returns the page
              before it. Mutually exclusive with `page[after]`.

          page_limit: The number of filesystems to return per page. Values above 250 are treated
              as 250.

          sort: Sort order for the results: a field name for ascending, or the field name
              prefixed with `-` for descending.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/storage/cloudfs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_name": filter_name,
                        "filter_region": filter_region,
                        "filter_status": filter_status,
                        "page_after": page_after,
                        "page_before": page_before,
                        "page_limit": page_limit,
                        "sort": sort,
                    },
                    cloudf_list_params.CloudfListParams,
                ),
            ),
            cast_to=CloudfListResponse,
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
    ) -> CloudfsFilesystemDetailResponseWrapper:
        """
        Permanently deletes a CloudFS filesystem, removing its S3 bucket and its
        metadata database. Deletion is synchronous: the response returns the
        filesystem's final state with status `deleted`. There is no restore. A
        filesystem that is still `provisioning` returns a `409`. If the filesystem still
        contains data, the request may be rejected with a `409` — drain the bucket and
        retry.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/storage/cloudfs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CloudfsFilesystemDetailResponseWrapper,
        )


class AsyncCloudfsResource(AsyncAPIResource):
    """
    Manage CloudFS filesystems — JuiceFS-compatible filesystems backed by Telnyx Cloud Storage
    """

    @cached_property
    def actions(self) -> AsyncActionsResource:
        """
        Manage CloudFS filesystems — JuiceFS-compatible filesystems backed by Telnyx Cloud Storage
        """
        return AsyncActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCloudfsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCloudfsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCloudfsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncCloudfsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        region: Literal["us-central-1", "us-east-1", "us-west-1"],
        idempotency_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CloudfsFilesystemResponseWrapper:
        """Creates a CloudFS filesystem.

        Provisioning is synchronous — typically a few
        seconds, up to a few minutes — and the filesystem is returned with status
        `ready`, together with its S3 bucket and metadata connection details. This
        response is the only time the filesystem's `meta_token` — and the
        credential-bearing `meta_url` — are returned; store them securely. If the token
        is lost, issue a new one with the rotate-meta-token action. Names are unique
        within your organization: creating with an existing name returns a `422`.
        Requests are idempotent: retrying with the same `Idempotency-Key` within 24
        hours replays the original response instead of creating another filesystem.

        Args:
          name: Filesystem name, unique within your organization. Names are trimmed and
              lowercased; after normalization they may contain lowercase letters, numbers,
              `.`, `_`, and `-` only.

          region: Region where the filesystem's storage and metadata are provisioned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or {})}
        return await self._post(
            "/storage/cloudfs",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "region": region,
                },
                cloudf_create_params.CloudfCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CloudfsFilesystemResponseWrapper,
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
    ) -> CloudfsFilesystemDetailResponseWrapper:
        """Retrieves a CloudFS filesystem by its ID.

        The returned `meta_url` omits the
        credential — the metadata token is only ever returned by create and
        rotate-meta-token. A filesystem whose last lifecycle action failed includes a
        customer-safe `error` message.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/storage/cloudfs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CloudfsFilesystemDetailResponseWrapper,
        )

    async def update(
        self,
        id: str,
        *,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CloudfsFilesystemDetailResponseWrapper:
        """Updates a CloudFS filesystem.

        Only `name` can be changed; other fields are
        immutable and unknown fields are rejected with a `400`. Renaming to a name that
        already exists in your organization returns a `422`.

        Args:
          name: New filesystem name, unique within your organization. Names are trimmed and
              lowercased; after normalization they may contain lowercase letters, numbers,
              `.`, `_`, and `-` only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/storage/cloudfs/{id}", id=id),
            body=await async_maybe_transform({"name": name}, cloudf_update_params.CloudfUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CloudfsFilesystemDetailResponseWrapper,
        )

    async def list(
        self,
        *,
        filter_name: str | Omit = omit,
        filter_region: str | Omit = omit,
        filter_status: Literal["provisioning", "ready", "needs_format", "deleting", "failed"] | Omit = omit,
        page_after: str | Omit = omit,
        page_before: str | Omit = omit,
        page_limit: int | Omit = omit,
        sort: Literal["created_at", "-created_at", "updated_at", "-updated_at", "name", "-name"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CloudfListResponse:
        """Lists the CloudFS filesystems for the authenticated user's organization.

        Results
        use cursor-based pagination: fetch the next page by passing `meta.cursors.after`
        as `page[after]`, or follow the `meta.next` URL.

        Args:
          filter_name: Return only the filesystem whose name matches exactly.

          filter_region: Return only filesystems in this region.

          filter_status: Return only filesystems with this status. Unrecognized values are ignored.

          page_after: Opaque cursor from a previous response's `meta.cursors.after`; returns the page
              after it. Mutually exclusive with `page[before]`.

          page_before: Opaque cursor from a previous response's `meta.cursors.before`; returns the page
              before it. Mutually exclusive with `page[after]`.

          page_limit: The number of filesystems to return per page. Values above 250 are treated
              as 250.

          sort: Sort order for the results: a field name for ascending, or the field name
              prefixed with `-` for descending.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/storage/cloudfs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter_name": filter_name,
                        "filter_region": filter_region,
                        "filter_status": filter_status,
                        "page_after": page_after,
                        "page_before": page_before,
                        "page_limit": page_limit,
                        "sort": sort,
                    },
                    cloudf_list_params.CloudfListParams,
                ),
            ),
            cast_to=CloudfListResponse,
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
    ) -> CloudfsFilesystemDetailResponseWrapper:
        """
        Permanently deletes a CloudFS filesystem, removing its S3 bucket and its
        metadata database. Deletion is synchronous: the response returns the
        filesystem's final state with status `deleted`. There is no restore. A
        filesystem that is still `provisioning` returns a `409`. If the filesystem still
        contains data, the request may be rejected with a `409` — drain the bucket and
        retry.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/storage/cloudfs/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CloudfsFilesystemDetailResponseWrapper,
        )


class CloudfsResourceWithRawResponse:
    def __init__(self, cloudfs: CloudfsResource) -> None:
        self._cloudfs = cloudfs

        self.create = to_raw_response_wrapper(
            cloudfs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            cloudfs.retrieve,
        )
        self.update = to_raw_response_wrapper(
            cloudfs.update,
        )
        self.list = to_raw_response_wrapper(
            cloudfs.list,
        )
        self.delete = to_raw_response_wrapper(
            cloudfs.delete,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        """
        Manage CloudFS filesystems — JuiceFS-compatible filesystems backed by Telnyx Cloud Storage
        """
        return ActionsResourceWithRawResponse(self._cloudfs.actions)


class AsyncCloudfsResourceWithRawResponse:
    def __init__(self, cloudfs: AsyncCloudfsResource) -> None:
        self._cloudfs = cloudfs

        self.create = async_to_raw_response_wrapper(
            cloudfs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            cloudfs.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            cloudfs.update,
        )
        self.list = async_to_raw_response_wrapper(
            cloudfs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            cloudfs.delete,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        """
        Manage CloudFS filesystems — JuiceFS-compatible filesystems backed by Telnyx Cloud Storage
        """
        return AsyncActionsResourceWithRawResponse(self._cloudfs.actions)


class CloudfsResourceWithStreamingResponse:
    def __init__(self, cloudfs: CloudfsResource) -> None:
        self._cloudfs = cloudfs

        self.create = to_streamed_response_wrapper(
            cloudfs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            cloudfs.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            cloudfs.update,
        )
        self.list = to_streamed_response_wrapper(
            cloudfs.list,
        )
        self.delete = to_streamed_response_wrapper(
            cloudfs.delete,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        """
        Manage CloudFS filesystems — JuiceFS-compatible filesystems backed by Telnyx Cloud Storage
        """
        return ActionsResourceWithStreamingResponse(self._cloudfs.actions)


class AsyncCloudfsResourceWithStreamingResponse:
    def __init__(self, cloudfs: AsyncCloudfsResource) -> None:
        self._cloudfs = cloudfs

        self.create = async_to_streamed_response_wrapper(
            cloudfs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            cloudfs.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            cloudfs.update,
        )
        self.list = async_to_streamed_response_wrapper(
            cloudfs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            cloudfs.delete,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        """
        Manage CloudFS filesystems — JuiceFS-compatible filesystems backed by Telnyx Cloud Storage
        """
        return AsyncActionsResourceWithStreamingResponse(self._cloudfs.actions)
