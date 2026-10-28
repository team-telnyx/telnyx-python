# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.ai.tests.schedules.v1 import (
    ScheduledTestJob,
    CronJobRetrieveCronJobsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCronJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        cron_job = client.ai.tests.schedules.v1.cron_jobs.retrieve(
            0,
        )
        assert_matches_type(ScheduledTestJob, cron_job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.ai.tests.schedules.v1.cron_jobs.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cron_job = response.parse()
        assert_matches_type(ScheduledTestJob, cron_job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.ai.tests.schedules.v1.cron_jobs.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cron_job = response.parse()
            assert_matches_type(ScheduledTestJob, cron_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        cron_job = client.ai.tests.schedules.v1.cron_jobs.update(
            id=0,
        )
        assert_matches_type(ScheduledTestJob, cron_job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        cron_job = client.ai.tests.schedules.v1.cron_jobs.update(
            id=0,
            agent=0,
            crontab_expression="0 4 * * *",
            execution_mode="execution_mode",
            frequency=0,
            is_active=True,
            name="Nightly regression - updated",
            notify_on="both",
            personalities=[0],
            run_as_text=True,
            scenarios=[0],
            tags=["string"],
            timezone="timezone",
        )
        assert_matches_type(ScheduledTestJob, cron_job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.ai.tests.schedules.v1.cron_jobs.with_raw_response.update(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cron_job = response.parse()
        assert_matches_type(ScheduledTestJob, cron_job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.ai.tests.schedules.v1.cron_jobs.with_streaming_response.update(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cron_job = response.parse()
            assert_matches_type(ScheduledTestJob, cron_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        cron_job = client.ai.tests.schedules.v1.cron_jobs.delete(
            0,
        )
        assert_matches_type(object, cron_job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.ai.tests.schedules.v1.cron_jobs.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cron_job = response.parse()
        assert_matches_type(object, cron_job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.ai.tests.schedules.v1.cron_jobs.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cron_job = response.parse()
            assert_matches_type(object, cron_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cron_jobs(self, client: Telnyx) -> None:
        cron_job = client.ai.tests.schedules.v1.cron_jobs.cron_jobs(
            crontab_expression="0 3 * * *",
        )
        assert_matches_type(ScheduledTestJob, cron_job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cron_jobs_with_all_params(self, client: Telnyx) -> None:
        cron_job = client.ai.tests.schedules.v1.cron_jobs.cron_jobs(
            crontab_expression="0 3 * * *",
            agent=1259,
            execution_mode="voice",
            frequency=0,
            is_active=True,
            name="Nightly regression",
            notify_on="failure",
            personalities=[0],
            run_as_text=True,
            scenarios=[9512],
            tags=["string"],
            timezone="America/Chicago",
        )
        assert_matches_type(ScheduledTestJob, cron_job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cron_jobs(self, client: Telnyx) -> None:
        response = client.ai.tests.schedules.v1.cron_jobs.with_raw_response.cron_jobs(
            crontab_expression="0 3 * * *",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cron_job = response.parse()
        assert_matches_type(ScheduledTestJob, cron_job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cron_jobs(self, client: Telnyx) -> None:
        with client.ai.tests.schedules.v1.cron_jobs.with_streaming_response.cron_jobs(
            crontab_expression="0 3 * * *",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cron_job = response.parse()
            assert_matches_type(ScheduledTestJob, cron_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_cron_jobs(self, client: Telnyx) -> None:
        cron_job = client.ai.tests.schedules.v1.cron_jobs.retrieve_cron_jobs()
        assert_matches_type(CronJobRetrieveCronJobsResponse, cron_job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_cron_jobs_with_all_params(self, client: Telnyx) -> None:
        cron_job = client.ai.tests.schedules.v1.cron_jobs.retrieve_cron_jobs(
            agent_id=0,
        )
        assert_matches_type(CronJobRetrieveCronJobsResponse, cron_job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_cron_jobs(self, client: Telnyx) -> None:
        response = client.ai.tests.schedules.v1.cron_jobs.with_raw_response.retrieve_cron_jobs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cron_job = response.parse()
        assert_matches_type(CronJobRetrieveCronJobsResponse, cron_job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_cron_jobs(self, client: Telnyx) -> None:
        with client.ai.tests.schedules.v1.cron_jobs.with_streaming_response.retrieve_cron_jobs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cron_job = response.parse()
            assert_matches_type(CronJobRetrieveCronJobsResponse, cron_job, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCronJobs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        cron_job = await async_client.ai.tests.schedules.v1.cron_jobs.retrieve(
            0,
        )
        assert_matches_type(ScheduledTestJob, cron_job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.tests.schedules.v1.cron_jobs.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cron_job = await response.parse()
        assert_matches_type(ScheduledTestJob, cron_job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.tests.schedules.v1.cron_jobs.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cron_job = await response.parse()
            assert_matches_type(ScheduledTestJob, cron_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        cron_job = await async_client.ai.tests.schedules.v1.cron_jobs.update(
            id=0,
        )
        assert_matches_type(ScheduledTestJob, cron_job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        cron_job = await async_client.ai.tests.schedules.v1.cron_jobs.update(
            id=0,
            agent=0,
            crontab_expression="0 4 * * *",
            execution_mode="execution_mode",
            frequency=0,
            is_active=True,
            name="Nightly regression - updated",
            notify_on="both",
            personalities=[0],
            run_as_text=True,
            scenarios=[0],
            tags=["string"],
            timezone="timezone",
        )
        assert_matches_type(ScheduledTestJob, cron_job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.tests.schedules.v1.cron_jobs.with_raw_response.update(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cron_job = await response.parse()
        assert_matches_type(ScheduledTestJob, cron_job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.tests.schedules.v1.cron_jobs.with_streaming_response.update(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cron_job = await response.parse()
            assert_matches_type(ScheduledTestJob, cron_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        cron_job = await async_client.ai.tests.schedules.v1.cron_jobs.delete(
            0,
        )
        assert_matches_type(object, cron_job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.tests.schedules.v1.cron_jobs.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cron_job = await response.parse()
        assert_matches_type(object, cron_job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.tests.schedules.v1.cron_jobs.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cron_job = await response.parse()
            assert_matches_type(object, cron_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cron_jobs(self, async_client: AsyncTelnyx) -> None:
        cron_job = await async_client.ai.tests.schedules.v1.cron_jobs.cron_jobs(
            crontab_expression="0 3 * * *",
        )
        assert_matches_type(ScheduledTestJob, cron_job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cron_jobs_with_all_params(self, async_client: AsyncTelnyx) -> None:
        cron_job = await async_client.ai.tests.schedules.v1.cron_jobs.cron_jobs(
            crontab_expression="0 3 * * *",
            agent=1259,
            execution_mode="voice",
            frequency=0,
            is_active=True,
            name="Nightly regression",
            notify_on="failure",
            personalities=[0],
            run_as_text=True,
            scenarios=[9512],
            tags=["string"],
            timezone="America/Chicago",
        )
        assert_matches_type(ScheduledTestJob, cron_job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cron_jobs(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.tests.schedules.v1.cron_jobs.with_raw_response.cron_jobs(
            crontab_expression="0 3 * * *",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cron_job = await response.parse()
        assert_matches_type(ScheduledTestJob, cron_job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cron_jobs(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.tests.schedules.v1.cron_jobs.with_streaming_response.cron_jobs(
            crontab_expression="0 3 * * *",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cron_job = await response.parse()
            assert_matches_type(ScheduledTestJob, cron_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_cron_jobs(self, async_client: AsyncTelnyx) -> None:
        cron_job = await async_client.ai.tests.schedules.v1.cron_jobs.retrieve_cron_jobs()
        assert_matches_type(CronJobRetrieveCronJobsResponse, cron_job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_cron_jobs_with_all_params(self, async_client: AsyncTelnyx) -> None:
        cron_job = await async_client.ai.tests.schedules.v1.cron_jobs.retrieve_cron_jobs(
            agent_id=0,
        )
        assert_matches_type(CronJobRetrieveCronJobsResponse, cron_job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_cron_jobs(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.tests.schedules.v1.cron_jobs.with_raw_response.retrieve_cron_jobs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cron_job = await response.parse()
        assert_matches_type(CronJobRetrieveCronJobsResponse, cron_job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_cron_jobs(self, async_client: AsyncTelnyx) -> None:
        async with (
            async_client.ai.tests.schedules.v1.cron_jobs.with_streaming_response.retrieve_cron_jobs()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cron_job = await response.parse()
            assert_matches_type(CronJobRetrieveCronJobsResponse, cron_job, path=["response"])

        assert cast(Any, response.is_closed) is True
