# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.ai import (
    ClusterListResponse,
    ClusterComputeResponse,
    ClusterRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClusters:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        cluster = client.ai.clusters.retrieve(
            task_id="task_id",
        )
        assert_matches_type(ClusterRetrieveResponse, cluster, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Telnyx) -> None:
        cluster = client.ai.clusters.retrieve(
            task_id="task_id",
            show_subclusters=True,
            top_n_nodes=0,
        )
        assert_matches_type(ClusterRetrieveResponse, cluster, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.ai.clusters.with_raw_response.retrieve(
            task_id="task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(ClusterRetrieveResponse, cluster, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.ai.clusters.with_streaming_response.retrieve(
            task_id="task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(ClusterRetrieveResponse, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.ai.clusters.with_raw_response.retrieve(
                task_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        cluster = client.ai.clusters.list()
        assert_matches_type(ClusterListResponse, cluster, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        cluster = client.ai.clusters.list(
            page={
                "number": 0,
                "size": 0,
            },
        )
        assert_matches_type(ClusterListResponse, cluster, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.ai.clusters.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(ClusterListResponse, cluster, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.ai.clusters.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(ClusterListResponse, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        cluster = client.ai.clusters.delete(
            "task_id",
        )
        assert cluster is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.ai.clusters.with_raw_response.delete(
            "task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert cluster is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.ai.clusters.with_streaming_response.delete(
            "task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert cluster is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.ai.clusters.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_compute(self, client: Telnyx) -> None:
        cluster = client.ai.clusters.compute(
            bucket="bucket",
        )
        assert_matches_type(ClusterComputeResponse, cluster, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_compute_with_all_params(self, client: Telnyx) -> None:
        cluster = client.ai.clusters.compute(
            bucket="bucket",
            files=["string"],
            min_cluster_size=0,
            min_subcluster_size=0,
            prefix="prefix",
        )
        assert_matches_type(ClusterComputeResponse, cluster, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_compute(self, client: Telnyx) -> None:
        response = client.ai.clusters.with_raw_response.compute(
            bucket="bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(ClusterComputeResponse, cluster, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_compute(self, client: Telnyx) -> None:
        with client.ai.clusters.with_streaming_response.compute(
            bucket="bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(ClusterComputeResponse, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_fetch_graph(self, client: Telnyx) -> None:
        cluster = client.ai.clusters.fetch_graph(
            task_id="task_id",
        )
        assert_matches_type(object, cluster, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_fetch_graph_with_all_params(self, client: Telnyx) -> None:
        cluster = client.ai.clusters.fetch_graph(
            task_id="task_id",
            cluster_id=0,
        )
        assert_matches_type(object, cluster, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_fetch_graph(self, client: Telnyx) -> None:
        response = client.ai.clusters.with_raw_response.fetch_graph(
            task_id="task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(object, cluster, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_fetch_graph(self, client: Telnyx) -> None:
        with client.ai.clusters.with_streaming_response.fetch_graph(
            task_id="task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(object, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_fetch_graph(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.ai.clusters.with_raw_response.fetch_graph(
                task_id="",
            )


class TestAsyncClusters:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        cluster = await async_client.ai.clusters.retrieve(
            task_id="task_id",
        )
        assert_matches_type(ClusterRetrieveResponse, cluster, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTelnyx) -> None:
        cluster = await async_client.ai.clusters.retrieve(
            task_id="task_id",
            show_subclusters=True,
            top_n_nodes=0,
        )
        assert_matches_type(ClusterRetrieveResponse, cluster, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.clusters.with_raw_response.retrieve(
            task_id="task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(ClusterRetrieveResponse, cluster, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.clusters.with_streaming_response.retrieve(
            task_id="task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(ClusterRetrieveResponse, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.ai.clusters.with_raw_response.retrieve(
                task_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        cluster = await async_client.ai.clusters.list()
        assert_matches_type(ClusterListResponse, cluster, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        cluster = await async_client.ai.clusters.list(
            page={
                "number": 0,
                "size": 0,
            },
        )
        assert_matches_type(ClusterListResponse, cluster, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.clusters.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(ClusterListResponse, cluster, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.clusters.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(ClusterListResponse, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        cluster = await async_client.ai.clusters.delete(
            "task_id",
        )
        assert cluster is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.clusters.with_raw_response.delete(
            "task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert cluster is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.clusters.with_streaming_response.delete(
            "task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert cluster is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.ai.clusters.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_compute(self, async_client: AsyncTelnyx) -> None:
        cluster = await async_client.ai.clusters.compute(
            bucket="bucket",
        )
        assert_matches_type(ClusterComputeResponse, cluster, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_compute_with_all_params(self, async_client: AsyncTelnyx) -> None:
        cluster = await async_client.ai.clusters.compute(
            bucket="bucket",
            files=["string"],
            min_cluster_size=0,
            min_subcluster_size=0,
            prefix="prefix",
        )
        assert_matches_type(ClusterComputeResponse, cluster, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_compute(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.clusters.with_raw_response.compute(
            bucket="bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(ClusterComputeResponse, cluster, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_compute(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.clusters.with_streaming_response.compute(
            bucket="bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(ClusterComputeResponse, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_fetch_graph(self, async_client: AsyncTelnyx) -> None:
        cluster = await async_client.ai.clusters.fetch_graph(
            task_id="task_id",
        )
        assert_matches_type(object, cluster, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_fetch_graph_with_all_params(self, async_client: AsyncTelnyx) -> None:
        cluster = await async_client.ai.clusters.fetch_graph(
            task_id="task_id",
            cluster_id=0,
        )
        assert_matches_type(object, cluster, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_fetch_graph(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.clusters.with_raw_response.fetch_graph(
            task_id="task_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(object, cluster, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_fetch_graph(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.clusters.with_streaming_response.fetch_graph(
            task_id="task_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(object, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_fetch_graph(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.ai.clusters.with_raw_response.fetch_graph(
                task_id="",
            )
