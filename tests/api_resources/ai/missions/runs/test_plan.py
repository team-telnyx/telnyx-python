# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.ai.missions.runs import (
    PlanCreateResponse,
    PlanRetrieveResponse,
    PlanUpdateStepResponse,
    PlanAddStepsToPlanResponse,
    PlanGetStepDetailsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPlan:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        plan = client.ai.missions.runs.plan.create(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            steps=[
                {
                    "description": "description",
                    "sequence": 0,
                    "step_id": "step_id",
                }
            ],
        )
        assert_matches_type(PlanCreateResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.ai.missions.runs.plan.with_raw_response.create(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            steps=[
                {
                    "description": "description",
                    "sequence": 0,
                    "step_id": "step_id",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(PlanCreateResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.ai.missions.runs.plan.with_streaming_response.create(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            steps=[
                {
                    "description": "description",
                    "sequence": 0,
                    "step_id": "step_id",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(PlanCreateResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.runs.plan.with_raw_response.create(
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                mission_id="",
                steps=[
                    {
                        "description": "description",
                        "sequence": 0,
                        "step_id": "step_id",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.ai.missions.runs.plan.with_raw_response.create(
                run_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                steps=[
                    {
                        "description": "description",
                        "sequence": 0,
                        "step_id": "step_id",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        plan = client.ai.missions.runs.plan.retrieve(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PlanRetrieveResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.ai.missions.runs.plan.with_raw_response.retrieve(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(PlanRetrieveResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.ai.missions.runs.plan.with_streaming_response.retrieve(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(PlanRetrieveResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.runs.plan.with_raw_response.retrieve(
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.ai.missions.runs.plan.with_raw_response.retrieve(
                run_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_steps_to_plan(self, client: Telnyx) -> None:
        plan = client.ai.missions.runs.plan.add_steps_to_plan(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            steps=[
                {
                    "description": "description",
                    "sequence": 0,
                    "step_id": "step_id",
                }
            ],
        )
        assert_matches_type(PlanAddStepsToPlanResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add_steps_to_plan(self, client: Telnyx) -> None:
        response = client.ai.missions.runs.plan.with_raw_response.add_steps_to_plan(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            steps=[
                {
                    "description": "description",
                    "sequence": 0,
                    "step_id": "step_id",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(PlanAddStepsToPlanResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add_steps_to_plan(self, client: Telnyx) -> None:
        with client.ai.missions.runs.plan.with_streaming_response.add_steps_to_plan(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            steps=[
                {
                    "description": "description",
                    "sequence": 0,
                    "step_id": "step_id",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(PlanAddStepsToPlanResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_add_steps_to_plan(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.runs.plan.with_raw_response.add_steps_to_plan(
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                mission_id="",
                steps=[
                    {
                        "description": "description",
                        "sequence": 0,
                        "step_id": "step_id",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.ai.missions.runs.plan.with_raw_response.add_steps_to_plan(
                run_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                steps=[
                    {
                        "description": "description",
                        "sequence": 0,
                        "step_id": "step_id",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_step_details(self, client: Telnyx) -> None:
        plan = client.ai.missions.runs.plan.get_step_details(
            step_id="step_id",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PlanGetStepDetailsResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_step_details(self, client: Telnyx) -> None:
        response = client.ai.missions.runs.plan.with_raw_response.get_step_details(
            step_id="step_id",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(PlanGetStepDetailsResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_step_details(self, client: Telnyx) -> None:
        with client.ai.missions.runs.plan.with_streaming_response.get_step_details(
            step_id="step_id",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(PlanGetStepDetailsResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_step_details(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.runs.plan.with_raw_response.get_step_details(
                step_id="step_id",
                mission_id="",
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.ai.missions.runs.plan.with_raw_response.get_step_details(
                step_id="step_id",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                run_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            client.ai.missions.runs.plan.with_raw_response.get_step_details(
                step_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_step(self, client: Telnyx) -> None:
        plan = client.ai.missions.runs.plan.update_step(
            step_id="step_id",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PlanUpdateStepResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_step_with_all_params(self, client: Telnyx) -> None:
        plan = client.ai.missions.runs.plan.update_step(
            step_id="step_id",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={"foo": "bar"},
            status="pending",
        )
        assert_matches_type(PlanUpdateStepResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_step(self, client: Telnyx) -> None:
        response = client.ai.missions.runs.plan.with_raw_response.update_step(
            step_id="step_id",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(PlanUpdateStepResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_step(self, client: Telnyx) -> None:
        with client.ai.missions.runs.plan.with_streaming_response.update_step(
            step_id="step_id",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(PlanUpdateStepResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_step(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.runs.plan.with_raw_response.update_step(
                step_id="step_id",
                mission_id="",
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.ai.missions.runs.plan.with_raw_response.update_step(
                step_id="step_id",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                run_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            client.ai.missions.runs.plan.with_raw_response.update_step(
                step_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncPlan:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        plan = await async_client.ai.missions.runs.plan.create(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            steps=[
                {
                    "description": "description",
                    "sequence": 0,
                    "step_id": "step_id",
                }
            ],
        )
        assert_matches_type(PlanCreateResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.runs.plan.with_raw_response.create(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            steps=[
                {
                    "description": "description",
                    "sequence": 0,
                    "step_id": "step_id",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(PlanCreateResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.runs.plan.with_streaming_response.create(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            steps=[
                {
                    "description": "description",
                    "sequence": 0,
                    "step_id": "step_id",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(PlanCreateResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.runs.plan.with_raw_response.create(
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                mission_id="",
                steps=[
                    {
                        "description": "description",
                        "sequence": 0,
                        "step_id": "step_id",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.ai.missions.runs.plan.with_raw_response.create(
                run_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                steps=[
                    {
                        "description": "description",
                        "sequence": 0,
                        "step_id": "step_id",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        plan = await async_client.ai.missions.runs.plan.retrieve(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PlanRetrieveResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.runs.plan.with_raw_response.retrieve(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(PlanRetrieveResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.runs.plan.with_streaming_response.retrieve(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(PlanRetrieveResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.runs.plan.with_raw_response.retrieve(
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.ai.missions.runs.plan.with_raw_response.retrieve(
                run_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_steps_to_plan(self, async_client: AsyncTelnyx) -> None:
        plan = await async_client.ai.missions.runs.plan.add_steps_to_plan(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            steps=[
                {
                    "description": "description",
                    "sequence": 0,
                    "step_id": "step_id",
                }
            ],
        )
        assert_matches_type(PlanAddStepsToPlanResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add_steps_to_plan(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.runs.plan.with_raw_response.add_steps_to_plan(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            steps=[
                {
                    "description": "description",
                    "sequence": 0,
                    "step_id": "step_id",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(PlanAddStepsToPlanResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add_steps_to_plan(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.runs.plan.with_streaming_response.add_steps_to_plan(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            steps=[
                {
                    "description": "description",
                    "sequence": 0,
                    "step_id": "step_id",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(PlanAddStepsToPlanResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_add_steps_to_plan(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.runs.plan.with_raw_response.add_steps_to_plan(
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                mission_id="",
                steps=[
                    {
                        "description": "description",
                        "sequence": 0,
                        "step_id": "step_id",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.ai.missions.runs.plan.with_raw_response.add_steps_to_plan(
                run_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                steps=[
                    {
                        "description": "description",
                        "sequence": 0,
                        "step_id": "step_id",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_step_details(self, async_client: AsyncTelnyx) -> None:
        plan = await async_client.ai.missions.runs.plan.get_step_details(
            step_id="step_id",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PlanGetStepDetailsResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_step_details(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.runs.plan.with_raw_response.get_step_details(
            step_id="step_id",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(PlanGetStepDetailsResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_step_details(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.runs.plan.with_streaming_response.get_step_details(
            step_id="step_id",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(PlanGetStepDetailsResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_step_details(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.runs.plan.with_raw_response.get_step_details(
                step_id="step_id",
                mission_id="",
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.ai.missions.runs.plan.with_raw_response.get_step_details(
                step_id="step_id",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                run_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            await async_client.ai.missions.runs.plan.with_raw_response.get_step_details(
                step_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_step(self, async_client: AsyncTelnyx) -> None:
        plan = await async_client.ai.missions.runs.plan.update_step(
            step_id="step_id",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PlanUpdateStepResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_step_with_all_params(self, async_client: AsyncTelnyx) -> None:
        plan = await async_client.ai.missions.runs.plan.update_step(
            step_id="step_id",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={"foo": "bar"},
            status="pending",
        )
        assert_matches_type(PlanUpdateStepResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_step(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.runs.plan.with_raw_response.update_step(
            step_id="step_id",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(PlanUpdateStepResponse, plan, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_step(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.runs.plan.with_streaming_response.update_step(
            step_id="step_id",
            mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(PlanUpdateStepResponse, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_step(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.runs.plan.with_raw_response.update_step(
                step_id="step_id",
                mission_id="",
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.ai.missions.runs.plan.with_raw_response.update_step(
                step_id="step_id",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                run_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            await async_client.ai.missions.runs.plan.with_raw_response.update_step(
                step_id="",
                mission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
