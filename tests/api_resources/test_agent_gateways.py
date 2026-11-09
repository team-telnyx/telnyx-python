# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    AgentGateway,
    AgentGatewayResponse,
    AgentGatewayRetrieveModelsResponse,
    AgentGatewayRetrieveSpendLogsResponse,
)
from telnyx._utils import parse_datetime
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgentGateways:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        agent_gateway = client.agent_gateways.create(
            wireguard_interface_id="c788eb40-a4c0-4bf5-8f84-976027960f8e",
        )
        assert_matches_type(AgentGatewayResponse, agent_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        agent_gateway = client.agent_gateways.create(
            wireguard_interface_id="c788eb40-a4c0-4bf5-8f84-976027960f8e",
            name="support-gw",
        )
        assert_matches_type(AgentGatewayResponse, agent_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.agent_gateways.with_raw_response.create(
            wireguard_interface_id="c788eb40-a4c0-4bf5-8f84-976027960f8e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_gateway = response.parse()
        assert_matches_type(AgentGatewayResponse, agent_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.agent_gateways.with_streaming_response.create(
            wireguard_interface_id="c788eb40-a4c0-4bf5-8f84-976027960f8e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_gateway = response.parse()
            assert_matches_type(AgentGatewayResponse, agent_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        agent_gateway = client.agent_gateways.retrieve(
            "ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )
        assert_matches_type(AgentGatewayResponse, agent_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.agent_gateways.with_raw_response.retrieve(
            "ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_gateway = response.parse()
        assert_matches_type(AgentGatewayResponse, agent_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.agent_gateways.with_streaming_response.retrieve(
            "ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_gateway = response.parse()
            assert_matches_type(AgentGatewayResponse, agent_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.agent_gateways.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        agent_gateway = client.agent_gateways.list()
        assert_matches_type(SyncDefaultFlatPagination[AgentGateway], agent_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        agent_gateway = client.agent_gateways.list(
            page_number=1,
            page_size=1,
        )
        assert_matches_type(SyncDefaultFlatPagination[AgentGateway], agent_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.agent_gateways.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_gateway = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[AgentGateway], agent_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.agent_gateways.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_gateway = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[AgentGateway], agent_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        agent_gateway = client.agent_gateways.delete(
            "ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )
        assert_matches_type(AgentGatewayResponse, agent_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.agent_gateways.with_raw_response.delete(
            "ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_gateway = response.parse()
        assert_matches_type(AgentGatewayResponse, agent_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.agent_gateways.with_streaming_response.delete(
            "ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_gateway = response.parse()
            assert_matches_type(AgentGatewayResponse, agent_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.agent_gateways.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_models(self, client: Telnyx) -> None:
        agent_gateway = client.agent_gateways.retrieve_models(
            "32ce035d-3165-4031-b1a7-a7c0c259590a",
        )
        assert_matches_type(AgentGatewayRetrieveModelsResponse, agent_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_models(self, client: Telnyx) -> None:
        response = client.agent_gateways.with_raw_response.retrieve_models(
            "32ce035d-3165-4031-b1a7-a7c0c259590a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_gateway = response.parse()
        assert_matches_type(AgentGatewayRetrieveModelsResponse, agent_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_models(self, client: Telnyx) -> None:
        with client.agent_gateways.with_streaming_response.retrieve_models(
            "32ce035d-3165-4031-b1a7-a7c0c259590a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_gateway = response.parse()
            assert_matches_type(AgentGatewayRetrieveModelsResponse, agent_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_models(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.agent_gateways.with_raw_response.retrieve_models(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_spend_logs(self, client: Telnyx) -> None:
        agent_gateway = client.agent_gateways.retrieve_spend_logs(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )
        assert_matches_type(AgentGatewayRetrieveSpendLogsResponse, agent_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_spend_logs_with_all_params(self, client: Telnyx) -> None:
        agent_gateway = client.agent_gateways.retrieve_spend_logs(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            key_id="ecc2efdd09bd231a9ad9bd2aada37aa7ccc3d38a03cc25beb6c28aa0aaa316be",
            page_number=1,
            page_size=1,
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentGatewayRetrieveSpendLogsResponse, agent_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_spend_logs(self, client: Telnyx) -> None:
        response = client.agent_gateways.with_raw_response.retrieve_spend_logs(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_gateway = response.parse()
        assert_matches_type(AgentGatewayRetrieveSpendLogsResponse, agent_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_spend_logs(self, client: Telnyx) -> None:
        with client.agent_gateways.with_streaming_response.retrieve_spend_logs(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_gateway = response.parse()
            assert_matches_type(AgentGatewayRetrieveSpendLogsResponse, agent_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_spend_logs(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.agent_gateways.with_raw_response.retrieve_spend_logs(
                instance_id="",
            )


class TestAsyncAgentGateways:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        agent_gateway = await async_client.agent_gateways.create(
            wireguard_interface_id="c788eb40-a4c0-4bf5-8f84-976027960f8e",
        )
        assert_matches_type(AgentGatewayResponse, agent_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        agent_gateway = await async_client.agent_gateways.create(
            wireguard_interface_id="c788eb40-a4c0-4bf5-8f84-976027960f8e",
            name="support-gw",
        )
        assert_matches_type(AgentGatewayResponse, agent_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.agent_gateways.with_raw_response.create(
            wireguard_interface_id="c788eb40-a4c0-4bf5-8f84-976027960f8e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_gateway = await response.parse()
        assert_matches_type(AgentGatewayResponse, agent_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.agent_gateways.with_streaming_response.create(
            wireguard_interface_id="c788eb40-a4c0-4bf5-8f84-976027960f8e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_gateway = await response.parse()
            assert_matches_type(AgentGatewayResponse, agent_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        agent_gateway = await async_client.agent_gateways.retrieve(
            "ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )
        assert_matches_type(AgentGatewayResponse, agent_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.agent_gateways.with_raw_response.retrieve(
            "ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_gateway = await response.parse()
        assert_matches_type(AgentGatewayResponse, agent_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.agent_gateways.with_streaming_response.retrieve(
            "ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_gateway = await response.parse()
            assert_matches_type(AgentGatewayResponse, agent_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.agent_gateways.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        agent_gateway = await async_client.agent_gateways.list()
        assert_matches_type(AsyncDefaultFlatPagination[AgentGateway], agent_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        agent_gateway = await async_client.agent_gateways.list(
            page_number=1,
            page_size=1,
        )
        assert_matches_type(AsyncDefaultFlatPagination[AgentGateway], agent_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.agent_gateways.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_gateway = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[AgentGateway], agent_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.agent_gateways.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_gateway = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[AgentGateway], agent_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        agent_gateway = await async_client.agent_gateways.delete(
            "ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )
        assert_matches_type(AgentGatewayResponse, agent_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.agent_gateways.with_raw_response.delete(
            "ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_gateway = await response.parse()
        assert_matches_type(AgentGatewayResponse, agent_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.agent_gateways.with_streaming_response.delete(
            "ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_gateway = await response.parse()
            assert_matches_type(AgentGatewayResponse, agent_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.agent_gateways.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_models(self, async_client: AsyncTelnyx) -> None:
        agent_gateway = await async_client.agent_gateways.retrieve_models(
            "32ce035d-3165-4031-b1a7-a7c0c259590a",
        )
        assert_matches_type(AgentGatewayRetrieveModelsResponse, agent_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_models(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.agent_gateways.with_raw_response.retrieve_models(
            "32ce035d-3165-4031-b1a7-a7c0c259590a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_gateway = await response.parse()
        assert_matches_type(AgentGatewayRetrieveModelsResponse, agent_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_models(self, async_client: AsyncTelnyx) -> None:
        async with async_client.agent_gateways.with_streaming_response.retrieve_models(
            "32ce035d-3165-4031-b1a7-a7c0c259590a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_gateway = await response.parse()
            assert_matches_type(AgentGatewayRetrieveModelsResponse, agent_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_models(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.agent_gateways.with_raw_response.retrieve_models(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_spend_logs(self, async_client: AsyncTelnyx) -> None:
        agent_gateway = await async_client.agent_gateways.retrieve_spend_logs(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )
        assert_matches_type(AgentGatewayRetrieveSpendLogsResponse, agent_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_spend_logs_with_all_params(self, async_client: AsyncTelnyx) -> None:
        agent_gateway = await async_client.agent_gateways.retrieve_spend_logs(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            key_id="ecc2efdd09bd231a9ad9bd2aada37aa7ccc3d38a03cc25beb6c28aa0aaa316be",
            page_number=1,
            page_size=1,
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentGatewayRetrieveSpendLogsResponse, agent_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_spend_logs(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.agent_gateways.with_raw_response.retrieve_spend_logs(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent_gateway = await response.parse()
        assert_matches_type(AgentGatewayRetrieveSpendLogsResponse, agent_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_spend_logs(self, async_client: AsyncTelnyx) -> None:
        async with async_client.agent_gateways.with_streaming_response.retrieve_spend_logs(
            instance_id="ecffdf4b-93ea-4a7b-8295-51dfd2077996",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent_gateway = await response.parse()
            assert_matches_type(AgentGatewayRetrieveSpendLogsResponse, agent_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_spend_logs(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.agent_gateways.with_raw_response.retrieve_spend_logs(
                instance_id="",
            )
