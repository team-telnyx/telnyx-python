# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.ai import cluster_list_params, cluster_compute_params, cluster_retrieve_params, cluster_fetch_graph_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.ai.cluster_list_response import ClusterListResponse
from ...types.ai.cluster_compute_response import ClusterComputeResponse
from ...types.ai.cluster_retrieve_response import ClusterRetrieveResponse

__all__ = ["ClustersResource", "AsyncClustersResource"]


class ClustersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClustersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ClustersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClustersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ClustersResourceWithStreamingResponse(self)

    def retrieve(
        self,
        task_id: str,
        *,
        show_subclusters: bool | NotGiven = NOT_GIVEN,
        top_n_nodes: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClusterRetrieveResponse:
        """
        Fetch a cluster

        Args:
          show_subclusters: Whether or not to include subclusters and their nodes in the response.

          top_n_nodes: The number of nodes in the cluster to return in the response. Nodes will be
              sorted by their centrality within the cluster.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._get(
            f"/ai/clusters/{task_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "show_subclusters": show_subclusters,
                        "top_n_nodes": top_n_nodes,
                    },
                    cluster_retrieve_params.ClusterRetrieveParams,
                ),
            ),
            cast_to=ClusterRetrieveResponse,
        )

    def list(
        self,
        *,
        page: cluster_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClusterListResponse:
        """List all clusters

        Args:
          page: Consolidated page parameter (deepObject style).

        Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ai/clusters",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"page": page}, cluster_list_params.ClusterListParams),
            ),
            cast_to=ClusterListResponse,
        )

    def delete(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a cluster

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/ai/clusters/{task_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def compute(
        self,
        *,
        bucket: str,
        files: List[str] | NotGiven = NOT_GIVEN,
        min_cluster_size: int | NotGiven = NOT_GIVEN,
        min_subcluster_size: int | NotGiven = NOT_GIVEN,
        prefix: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClusterComputeResponse:
        """
        Starts a background task to compute how the data in an
        [embedded storage bucket](https://developers.telnyx.com/api/inference/inference-embedding/post-embedding)
        is clustered. This helps identify common themes and patterns in the data.

        Args:
          bucket: The embedded storage bucket to compute the clusters from. The bucket must
              already be
              [embedded](https://developers.telnyx.com/api/inference/inference-embedding/post-embedding).

          files: Array of files to filter which are included.

          min_cluster_size: Smallest number of related text chunks to qualify as a cluster. Top-level
              clusters should be thought of as identifying broad themes in your data.

          min_subcluster_size: Smallest number of related text chunks to qualify as a sub-cluster. Sub-clusters
              should be thought of as identifying more specific topics within a broader theme.

          prefix: Prefix to filter whcih files in the buckets are included.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/clusters",
            body=maybe_transform(
                {
                    "bucket": bucket,
                    "files": files,
                    "min_cluster_size": min_cluster_size,
                    "min_subcluster_size": min_subcluster_size,
                    "prefix": prefix,
                },
                cluster_compute_params.ClusterComputeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClusterComputeResponse,
        )

    def fetch_graph(
        self,
        task_id: str,
        *,
        cluster_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Fetch a cluster visualization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._get(
            f"/ai/clusters/{task_id}/graph",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"cluster_id": cluster_id}, cluster_fetch_graph_params.ClusterFetchGraphParams),
            ),
            cast_to=object,
        )


class AsyncClustersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClustersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClustersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClustersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncClustersResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        task_id: str,
        *,
        show_subclusters: bool | NotGiven = NOT_GIVEN,
        top_n_nodes: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClusterRetrieveResponse:
        """
        Fetch a cluster

        Args:
          show_subclusters: Whether or not to include subclusters and their nodes in the response.

          top_n_nodes: The number of nodes in the cluster to return in the response. Nodes will be
              sorted by their centrality within the cluster.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._get(
            f"/ai/clusters/{task_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "show_subclusters": show_subclusters,
                        "top_n_nodes": top_n_nodes,
                    },
                    cluster_retrieve_params.ClusterRetrieveParams,
                ),
            ),
            cast_to=ClusterRetrieveResponse,
        )

    async def list(
        self,
        *,
        page: cluster_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClusterListResponse:
        """List all clusters

        Args:
          page: Consolidated page parameter (deepObject style).

        Originally: page[number],
              page[size]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ai/clusters",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"page": page}, cluster_list_params.ClusterListParams),
            ),
            cast_to=ClusterListResponse,
        )

    async def delete(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a cluster

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/ai/clusters/{task_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def compute(
        self,
        *,
        bucket: str,
        files: List[str] | NotGiven = NOT_GIVEN,
        min_cluster_size: int | NotGiven = NOT_GIVEN,
        min_subcluster_size: int | NotGiven = NOT_GIVEN,
        prefix: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClusterComputeResponse:
        """
        Starts a background task to compute how the data in an
        [embedded storage bucket](https://developers.telnyx.com/api/inference/inference-embedding/post-embedding)
        is clustered. This helps identify common themes and patterns in the data.

        Args:
          bucket: The embedded storage bucket to compute the clusters from. The bucket must
              already be
              [embedded](https://developers.telnyx.com/api/inference/inference-embedding/post-embedding).

          files: Array of files to filter which are included.

          min_cluster_size: Smallest number of related text chunks to qualify as a cluster. Top-level
              clusters should be thought of as identifying broad themes in your data.

          min_subcluster_size: Smallest number of related text chunks to qualify as a sub-cluster. Sub-clusters
              should be thought of as identifying more specific topics within a broader theme.

          prefix: Prefix to filter whcih files in the buckets are included.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/clusters",
            body=await async_maybe_transform(
                {
                    "bucket": bucket,
                    "files": files,
                    "min_cluster_size": min_cluster_size,
                    "min_subcluster_size": min_subcluster_size,
                    "prefix": prefix,
                },
                cluster_compute_params.ClusterComputeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClusterComputeResponse,
        )

    async def fetch_graph(
        self,
        task_id: str,
        *,
        cluster_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Fetch a cluster visualization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._get(
            f"/ai/clusters/{task_id}/graph",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cluster_id": cluster_id}, cluster_fetch_graph_params.ClusterFetchGraphParams
                ),
            ),
            cast_to=object,
        )


class ClustersResourceWithRawResponse:
    def __init__(self, clusters: ClustersResource) -> None:
        self._clusters = clusters

        self.retrieve = to_raw_response_wrapper(
            clusters.retrieve,
        )
        self.list = to_raw_response_wrapper(
            clusters.list,
        )
        self.delete = to_raw_response_wrapper(
            clusters.delete,
        )
        self.compute = to_raw_response_wrapper(
            clusters.compute,
        )
        self.fetch_graph = to_raw_response_wrapper(
            clusters.fetch_graph,
        )


class AsyncClustersResourceWithRawResponse:
    def __init__(self, clusters: AsyncClustersResource) -> None:
        self._clusters = clusters

        self.retrieve = async_to_raw_response_wrapper(
            clusters.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            clusters.list,
        )
        self.delete = async_to_raw_response_wrapper(
            clusters.delete,
        )
        self.compute = async_to_raw_response_wrapper(
            clusters.compute,
        )
        self.fetch_graph = async_to_raw_response_wrapper(
            clusters.fetch_graph,
        )


class ClustersResourceWithStreamingResponse:
    def __init__(self, clusters: ClustersResource) -> None:
        self._clusters = clusters

        self.retrieve = to_streamed_response_wrapper(
            clusters.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            clusters.list,
        )
        self.delete = to_streamed_response_wrapper(
            clusters.delete,
        )
        self.compute = to_streamed_response_wrapper(
            clusters.compute,
        )
        self.fetch_graph = to_streamed_response_wrapper(
            clusters.fetch_graph,
        )


class AsyncClustersResourceWithStreamingResponse:
    def __init__(self, clusters: AsyncClustersResource) -> None:
        self._clusters = clusters

        self.retrieve = async_to_streamed_response_wrapper(
            clusters.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            clusters.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            clusters.delete,
        )
        self.compute = async_to_streamed_response_wrapper(
            clusters.compute,
        )
        self.fetch_graph = async_to_streamed_response_wrapper(
            clusters.fetch_graph,
        )
