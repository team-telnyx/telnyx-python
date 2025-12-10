# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.ai.assistants.tests.test_suites import (
    RunTriggerResponse,
    PaginatedTestRunList,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        run = client.ai.assistants.tests.test_suites.runs.list(
            suite_name="suite_name",
        )
        assert_matches_type(PaginatedTestRunList, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        run = client.ai.assistants.tests.test_suites.runs.list(
            suite_name="suite_name",
            page={
                "number": 1,
                "size": 1,
            },
            status="status",
            test_suite_run_id="test_suite_run_id",
        )
        assert_matches_type(PaginatedTestRunList, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.ai.assistants.tests.test_suites.runs.with_raw_response.list(
            suite_name="suite_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(PaginatedTestRunList, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.ai.assistants.tests.test_suites.runs.with_streaming_response.list(
            suite_name="suite_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(PaginatedTestRunList, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `suite_name` but received ''"):
            client.ai.assistants.tests.test_suites.runs.with_raw_response.list(
                suite_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_trigger(self, client: Telnyx) -> None:
        run = client.ai.assistants.tests.test_suites.runs.trigger(
            suite_name="suite_name",
        )
        assert_matches_type(RunTriggerResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_trigger_with_all_params(self, client: Telnyx) -> None:
        run = client.ai.assistants.tests.test_suites.runs.trigger(
            suite_name="suite_name",
            destination_version_id="123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(RunTriggerResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_trigger(self, client: Telnyx) -> None:
        response = client.ai.assistants.tests.test_suites.runs.with_raw_response.trigger(
            suite_name="suite_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunTriggerResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_trigger(self, client: Telnyx) -> None:
        with client.ai.assistants.tests.test_suites.runs.with_streaming_response.trigger(
            suite_name="suite_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunTriggerResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_trigger(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `suite_name` but received ''"):
            client.ai.assistants.tests.test_suites.runs.with_raw_response.trigger(
                suite_name="",
            )


class TestAsyncRuns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        run = await async_client.ai.assistants.tests.test_suites.runs.list(
            suite_name="suite_name",
        )
        assert_matches_type(PaginatedTestRunList, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        run = await async_client.ai.assistants.tests.test_suites.runs.list(
            suite_name="suite_name",
            page={
                "number": 1,
                "size": 1,
            },
            status="status",
            test_suite_run_id="test_suite_run_id",
        )
        assert_matches_type(PaginatedTestRunList, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.assistants.tests.test_suites.runs.with_raw_response.list(
            suite_name="suite_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(PaginatedTestRunList, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.assistants.tests.test_suites.runs.with_streaming_response.list(
            suite_name="suite_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(PaginatedTestRunList, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `suite_name` but received ''"):
            await async_client.ai.assistants.tests.test_suites.runs.with_raw_response.list(
                suite_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_trigger(self, async_client: AsyncTelnyx) -> None:
        run = await async_client.ai.assistants.tests.test_suites.runs.trigger(
            suite_name="suite_name",
        )
        assert_matches_type(RunTriggerResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_trigger_with_all_params(self, async_client: AsyncTelnyx) -> None:
        run = await async_client.ai.assistants.tests.test_suites.runs.trigger(
            suite_name="suite_name",
            destination_version_id="123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(RunTriggerResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_trigger(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.assistants.tests.test_suites.runs.with_raw_response.trigger(
            suite_name="suite_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunTriggerResponse, run, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_trigger(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.assistants.tests.test_suites.runs.with_streaming_response.trigger(
            suite_name="suite_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunTriggerResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_trigger(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `suite_name` but received ''"):
            await async_client.ai.assistants.tests.test_suites.runs.with_raw_response.trigger(
                suite_name="",
            )
