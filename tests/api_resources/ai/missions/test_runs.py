# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from telnyx.types.ai.missions import (
    MissionRunData,
    RunCreateResponse,
    RunUpdateResponse,
    RunPauseRunResponse,
    RunRetrieveResponse,
    RunCancelRunResponse,
    RunResumeRunResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        run = client.ai.missions.runs.create(
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        run = client.ai.missions.runs.create(
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            input={"foo": "bar"},
            metadata={"foo": "bar"},
        )
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.ai.missions.runs.with_raw_response.create(
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.ai.missions.runs.with_streaming_response.create(
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunCreateResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.runs.with_raw_response.create(
                mission_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        run = client.ai.missions.runs.retrieve(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunRetrieveResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.ai.missions.runs.with_raw_response.retrieve(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunRetrieveResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.ai.missions.runs.with_streaming_response.retrieve(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunRetrieveResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.runs.with_raw_response.retrieve(
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.ai.missions.runs.with_raw_response.retrieve(
                run_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        run = client.ai.missions.runs.update(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunUpdateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        run = client.ai.missions.runs.update(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            error="error",
            metadata={"foo": "bar"},
            result_payload={"foo": "bar"},
            result_summary="result_summary",
            status="pending",
        )
        assert_matches_type(RunUpdateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.ai.missions.runs.with_raw_response.update(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunUpdateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.ai.missions.runs.with_streaming_response.update(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunUpdateResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.runs.with_raw_response.update(
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.ai.missions.runs.with_raw_response.update(
                run_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        run = client.ai.missions.runs.list(
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncDefaultFlatPagination[MissionRunData], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        run = client.ai.missions.runs.list(
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_number=1,
            page_size=1,
            status="status",
        )
        assert_matches_type(SyncDefaultFlatPagination[MissionRunData], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.ai.missions.runs.with_raw_response.list(
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[MissionRunData], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.ai.missions.runs.with_streaming_response.list(
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[MissionRunData], run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.runs.with_raw_response.list(
                mission_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel_run(self, client: Telnyx) -> None:
        run = client.ai.missions.runs.cancel_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunCancelRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel_run(self, client: Telnyx) -> None:
        response = client.ai.missions.runs.with_raw_response.cancel_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunCancelRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel_run(self, client: Telnyx) -> None:
        with client.ai.missions.runs.with_streaming_response.cancel_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunCancelRunResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel_run(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.runs.with_raw_response.cancel_run(
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.ai.missions.runs.with_raw_response.cancel_run(
                run_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_runs(self, client: Telnyx) -> None:
        run = client.ai.missions.runs.list_runs()
        assert_matches_type(SyncDefaultFlatPagination[MissionRunData], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_runs_with_all_params(self, client: Telnyx) -> None:
        run = client.ai.missions.runs.list_runs(
            page_number=1,
            page_size=1,
            status="status",
        )
        assert_matches_type(SyncDefaultFlatPagination[MissionRunData], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_runs(self, client: Telnyx) -> None:
        response = client.ai.missions.runs.with_raw_response.list_runs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[MissionRunData], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_runs(self, client: Telnyx) -> None:
        with client.ai.missions.runs.with_streaming_response.list_runs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[MissionRunData], run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_pause_run(self, client: Telnyx) -> None:
        run = client.ai.missions.runs.pause_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunPauseRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_pause_run(self, client: Telnyx) -> None:
        response = client.ai.missions.runs.with_raw_response.pause_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunPauseRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_pause_run(self, client: Telnyx) -> None:
        with client.ai.missions.runs.with_streaming_response.pause_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunPauseRunResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_pause_run(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.runs.with_raw_response.pause_run(
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.ai.missions.runs.with_raw_response.pause_run(
                run_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_resume_run(self, client: Telnyx) -> None:
        run = client.ai.missions.runs.resume_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunResumeRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_resume_run(self, client: Telnyx) -> None:
        response = client.ai.missions.runs.with_raw_response.resume_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunResumeRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_resume_run(self, client: Telnyx) -> None:
        with client.ai.missions.runs.with_streaming_response.resume_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunResumeRunResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_resume_run(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.runs.with_raw_response.resume_run(
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.ai.missions.runs.with_raw_response.resume_run(
                run_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncRuns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        run = await async_client.ai.missions.runs.create(
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        run = await async_client.ai.missions.runs.create(
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            input={"foo": "bar"},
            metadata={"foo": "bar"},
        )
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.runs.with_raw_response.create(
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.runs.with_streaming_response.create(
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunCreateResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.runs.with_raw_response.create(
                mission_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        run = await async_client.ai.missions.runs.retrieve(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunRetrieveResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.runs.with_raw_response.retrieve(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunRetrieveResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.runs.with_streaming_response.retrieve(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunRetrieveResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.runs.with_raw_response.retrieve(
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.ai.missions.runs.with_raw_response.retrieve(
                run_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        run = await async_client.ai.missions.runs.update(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunUpdateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        run = await async_client.ai.missions.runs.update(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            error="error",
            metadata={"foo": "bar"},
            result_payload={"foo": "bar"},
            result_summary="result_summary",
            status="pending",
        )
        assert_matches_type(RunUpdateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.runs.with_raw_response.update(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunUpdateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.runs.with_streaming_response.update(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunUpdateResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.runs.with_raw_response.update(
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.ai.missions.runs.with_raw_response.update(
                run_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        run = await async_client.ai.missions.runs.list(
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncDefaultFlatPagination[MissionRunData], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        run = await async_client.ai.missions.runs.list(
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_number=1,
            page_size=1,
            status="status",
        )
        assert_matches_type(AsyncDefaultFlatPagination[MissionRunData], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.runs.with_raw_response.list(
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[MissionRunData], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.runs.with_streaming_response.list(
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[MissionRunData], run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.runs.with_raw_response.list(
                mission_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel_run(self, async_client: AsyncTelnyx) -> None:
        run = await async_client.ai.missions.runs.cancel_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunCancelRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel_run(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.runs.with_raw_response.cancel_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunCancelRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel_run(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.runs.with_streaming_response.cancel_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunCancelRunResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel_run(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.runs.with_raw_response.cancel_run(
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.ai.missions.runs.with_raw_response.cancel_run(
                run_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_runs(self, async_client: AsyncTelnyx) -> None:
        run = await async_client.ai.missions.runs.list_runs()
        assert_matches_type(AsyncDefaultFlatPagination[MissionRunData], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_runs_with_all_params(self, async_client: AsyncTelnyx) -> None:
        run = await async_client.ai.missions.runs.list_runs(
            page_number=1,
            page_size=1,
            status="status",
        )
        assert_matches_type(AsyncDefaultFlatPagination[MissionRunData], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_runs(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.runs.with_raw_response.list_runs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[MissionRunData], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_runs(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.runs.with_streaming_response.list_runs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[MissionRunData], run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_pause_run(self, async_client: AsyncTelnyx) -> None:
        run = await async_client.ai.missions.runs.pause_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunPauseRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_pause_run(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.runs.with_raw_response.pause_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunPauseRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_pause_run(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.runs.with_streaming_response.pause_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunPauseRunResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_pause_run(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.runs.with_raw_response.pause_run(
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.ai.missions.runs.with_raw_response.pause_run(
                run_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_resume_run(self, async_client: AsyncTelnyx) -> None:
        run = await async_client.ai.missions.runs.resume_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunResumeRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_resume_run(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.runs.with_raw_response.resume_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunResumeRunResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_resume_run(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.runs.with_streaming_response.resume_run(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunResumeRunResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_resume_run(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.runs.with_raw_response.resume_run(
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.ai.missions.runs.with_raw_response.resume_run(
                run_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
