# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.ai.tests.test_framework.v1 import (
    AITestMetric,
    MetricListResponse,
    MetricBulkCreateResponse,
    ScenarioGenerationResponse,
    MetricRetrieveGenerateMetricsProgressResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetrics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        metric = client.ai.tests.test_framework.v1.metrics.create(
            name="Escalates on refund denial",
        )
        assert_matches_type(AITestMetric, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        metric = client.ai.tests.test_framework.v1.metrics.create(
            name="Escalates on refund denial",
            add_to_new_agents=False,
            agents=[1259],
            assistant_id="assistant_id",
            audio_enabled=True,
            description="Returns a score for whether the assistant escalates when the caller's refund is denied.",
            display_order=0,
            enum_values=["string"],
            eval_type="continuous_qualitative",
            observability_enabled=True,
            prompt="Score the assistant's escalation behaviour between 0.0 and 1.0.",
            sampling_enabled=True,
            simulation_enabled=True,
            type="llm_judge",
        )
        assert_matches_type(AITestMetric, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.ai.tests.test_framework.v1.metrics.with_raw_response.create(
            name="Escalates on refund denial",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(AITestMetric, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.ai.tests.test_framework.v1.metrics.with_streaming_response.create(
            name="Escalates on refund denial",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(AITestMetric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        metric = client.ai.tests.test_framework.v1.metrics.retrieve(
            0,
        )
        assert_matches_type(AITestMetric, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.ai.tests.test_framework.v1.metrics.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(AITestMetric, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.ai.tests.test_framework.v1.metrics.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(AITestMetric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        metric = client.ai.tests.test_framework.v1.metrics.update(
            id=0,
        )
        assert_matches_type(AITestMetric, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        metric = client.ai.tests.test_framework.v1.metrics.update(
            id=0,
            add_to_new_agents=True,
            agents=[0],
            audio_enabled=True,
            description="description",
            display_order=0,
            enum_values=["string"],
            eval_type="eval_type",
            name="Escalates on refund denial",
            observability_enabled=True,
            prompt="Score the assistant's escalation behaviour between 0.0 and 1.0, considering tone.",
            sampling_enabled=True,
            simulation_enabled=True,
            type="type",
        )
        assert_matches_type(AITestMetric, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.ai.tests.test_framework.v1.metrics.with_raw_response.update(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(AITestMetric, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.ai.tests.test_framework.v1.metrics.with_streaming_response.update(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(AITestMetric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        metric = client.ai.tests.test_framework.v1.metrics.list()
        assert_matches_type(MetricListResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        metric = client.ai.tests.test_framework.v1.metrics.list(
            agent_id=0,
            assistant_id="assistant_id",
        )
        assert_matches_type(MetricListResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.ai.tests.test_framework.v1.metrics.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(MetricListResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.ai.tests.test_framework.v1.metrics.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(MetricListResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        metric = client.ai.tests.test_framework.v1.metrics.delete(
            0,
        )
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.ai.tests.test_framework.v1.metrics.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.ai.tests.test_framework.v1.metrics.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(object, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_bulk_create(self, client: Telnyx) -> None:
        metric = client.ai.tests.test_framework.v1.metrics.bulk_create(
            body=[{"name": "Greets within 5 seconds"}],
        )
        assert_matches_type(MetricBulkCreateResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_bulk_create(self, client: Telnyx) -> None:
        response = client.ai.tests.test_framework.v1.metrics.with_raw_response.bulk_create(
            body=[{"name": "Greets within 5 seconds"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(MetricBulkCreateResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_bulk_create(self, client: Telnyx) -> None:
        with client.ai.tests.test_framework.v1.metrics.with_streaming_response.bulk_create(
            body=[{"name": "Greets within 5 seconds"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(MetricBulkCreateResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_metrics(self, client: Telnyx) -> None:
        metric = client.ai.tests.test_framework.v1.metrics.generate_metrics(
            agent_id=1259,
            num_metrics=5,
        )
        assert_matches_type(ScenarioGenerationResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_metrics_with_all_params(self, client: Telnyx) -> None:
        metric = client.ai.tests.test_framework.v1.metrics.generate_metrics(
            agent_id=1259,
            num_metrics=5,
            scenarios=[9512],
        )
        assert_matches_type(ScenarioGenerationResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_generate_metrics(self, client: Telnyx) -> None:
        response = client.ai.tests.test_framework.v1.metrics.with_raw_response.generate_metrics(
            agent_id=1259,
            num_metrics=5,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(ScenarioGenerationResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_generate_metrics(self, client: Telnyx) -> None:
        with client.ai.tests.test_framework.v1.metrics.with_streaming_response.generate_metrics(
            agent_id=1259,
            num_metrics=5,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(ScenarioGenerationResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_generate_metrics_progress(self, client: Telnyx) -> None:
        metric = client.ai.tests.test_framework.v1.metrics.retrieve_generate_metrics_progress(
            progress_id="progress_id",
        )
        assert_matches_type(MetricRetrieveGenerateMetricsProgressResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_generate_metrics_progress(self, client: Telnyx) -> None:
        response = client.ai.tests.test_framework.v1.metrics.with_raw_response.retrieve_generate_metrics_progress(
            progress_id="progress_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(MetricRetrieveGenerateMetricsProgressResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_generate_metrics_progress(self, client: Telnyx) -> None:
        with client.ai.tests.test_framework.v1.metrics.with_streaming_response.retrieve_generate_metrics_progress(
            progress_id="progress_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(MetricRetrieveGenerateMetricsProgressResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMetrics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        metric = await async_client.ai.tests.test_framework.v1.metrics.create(
            name="Escalates on refund denial",
        )
        assert_matches_type(AITestMetric, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        metric = await async_client.ai.tests.test_framework.v1.metrics.create(
            name="Escalates on refund denial",
            add_to_new_agents=False,
            agents=[1259],
            assistant_id="assistant_id",
            audio_enabled=True,
            description="Returns a score for whether the assistant escalates when the caller's refund is denied.",
            display_order=0,
            enum_values=["string"],
            eval_type="continuous_qualitative",
            observability_enabled=True,
            prompt="Score the assistant's escalation behaviour between 0.0 and 1.0.",
            sampling_enabled=True,
            simulation_enabled=True,
            type="llm_judge",
        )
        assert_matches_type(AITestMetric, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.tests.test_framework.v1.metrics.with_raw_response.create(
            name="Escalates on refund denial",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(AITestMetric, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.tests.test_framework.v1.metrics.with_streaming_response.create(
            name="Escalates on refund denial",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(AITestMetric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        metric = await async_client.ai.tests.test_framework.v1.metrics.retrieve(
            0,
        )
        assert_matches_type(AITestMetric, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.tests.test_framework.v1.metrics.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(AITestMetric, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.tests.test_framework.v1.metrics.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(AITestMetric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        metric = await async_client.ai.tests.test_framework.v1.metrics.update(
            id=0,
        )
        assert_matches_type(AITestMetric, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        metric = await async_client.ai.tests.test_framework.v1.metrics.update(
            id=0,
            add_to_new_agents=True,
            agents=[0],
            audio_enabled=True,
            description="description",
            display_order=0,
            enum_values=["string"],
            eval_type="eval_type",
            name="Escalates on refund denial",
            observability_enabled=True,
            prompt="Score the assistant's escalation behaviour between 0.0 and 1.0, considering tone.",
            sampling_enabled=True,
            simulation_enabled=True,
            type="type",
        )
        assert_matches_type(AITestMetric, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.tests.test_framework.v1.metrics.with_raw_response.update(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(AITestMetric, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.tests.test_framework.v1.metrics.with_streaming_response.update(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(AITestMetric, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        metric = await async_client.ai.tests.test_framework.v1.metrics.list()
        assert_matches_type(MetricListResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        metric = await async_client.ai.tests.test_framework.v1.metrics.list(
            agent_id=0,
            assistant_id="assistant_id",
        )
        assert_matches_type(MetricListResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.tests.test_framework.v1.metrics.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(MetricListResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.tests.test_framework.v1.metrics.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(MetricListResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        metric = await async_client.ai.tests.test_framework.v1.metrics.delete(
            0,
        )
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.tests.test_framework.v1.metrics.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(object, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.tests.test_framework.v1.metrics.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(object, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_bulk_create(self, async_client: AsyncTelnyx) -> None:
        metric = await async_client.ai.tests.test_framework.v1.metrics.bulk_create(
            body=[{"name": "Greets within 5 seconds"}],
        )
        assert_matches_type(MetricBulkCreateResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_bulk_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.tests.test_framework.v1.metrics.with_raw_response.bulk_create(
            body=[{"name": "Greets within 5 seconds"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(MetricBulkCreateResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_bulk_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.tests.test_framework.v1.metrics.with_streaming_response.bulk_create(
            body=[{"name": "Greets within 5 seconds"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(MetricBulkCreateResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_metrics(self, async_client: AsyncTelnyx) -> None:
        metric = await async_client.ai.tests.test_framework.v1.metrics.generate_metrics(
            agent_id=1259,
            num_metrics=5,
        )
        assert_matches_type(ScenarioGenerationResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_metrics_with_all_params(self, async_client: AsyncTelnyx) -> None:
        metric = await async_client.ai.tests.test_framework.v1.metrics.generate_metrics(
            agent_id=1259,
            num_metrics=5,
            scenarios=[9512],
        )
        assert_matches_type(ScenarioGenerationResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_generate_metrics(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.tests.test_framework.v1.metrics.with_raw_response.generate_metrics(
            agent_id=1259,
            num_metrics=5,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(ScenarioGenerationResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_generate_metrics(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.tests.test_framework.v1.metrics.with_streaming_response.generate_metrics(
            agent_id=1259,
            num_metrics=5,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(ScenarioGenerationResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_generate_metrics_progress(self, async_client: AsyncTelnyx) -> None:
        metric = await async_client.ai.tests.test_framework.v1.metrics.retrieve_generate_metrics_progress(
            progress_id="progress_id",
        )
        assert_matches_type(MetricRetrieveGenerateMetricsProgressResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_generate_metrics_progress(self, async_client: AsyncTelnyx) -> None:
        response = (
            await async_client.ai.tests.test_framework.v1.metrics.with_raw_response.retrieve_generate_metrics_progress(
                progress_id="progress_id",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(MetricRetrieveGenerateMetricsProgressResponse, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_generate_metrics_progress(self, async_client: AsyncTelnyx) -> None:
        async with (
            async_client.ai.tests.test_framework.v1.metrics.with_streaming_response.retrieve_generate_metrics_progress(
                progress_id="progress_id",
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(MetricRetrieveGenerateMetricsProgressResponse, metric, path=["response"])

        assert cast(Any, response.is_closed) is True
