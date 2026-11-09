# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.agent_gateways import APIListResponse, AgentGatewayAPIResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPIs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        api = client.agent_gateways.apis.create(
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            name="petstore",
            spec_url="https://petstore3.swagger.io/api/v3/openapi.json",
        )
        assert_matches_type(AgentGatewayAPIResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        api = client.agent_gateways.apis.create(
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            name="petstore",
            spec_url="https://petstore3.swagger.io/api/v3/openapi.json",
            auth={"type": "none"},
            base_url="https://petstore3.swagger.io/api/v3",
            forwarded_headers=["string"],
            open_to_every_key=True,
            static_headers={"foo": "string"},
            tools=["string"],
        )
        assert_matches_type(AgentGatewayAPIResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.agent_gateways.apis.with_raw_response.create(
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            name="petstore",
            spec_url="https://petstore3.swagger.io/api/v3/openapi.json",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = response.parse()
        assert_matches_type(AgentGatewayAPIResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.agent_gateways.apis.with_streaming_response.create(
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            name="petstore",
            spec_url="https://petstore3.swagger.io/api/v3/openapi.json",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = response.parse()
            assert_matches_type(AgentGatewayAPIResponse, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.agent_gateways.apis.with_raw_response.create(
                instance_id="",
                name="petstore",
                spec_url="https://petstore3.swagger.io/api/v3/openapi.json",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        api = client.agent_gateways.apis.update(
            api_id="dbe53cc0-bf7e-4f7a-8d84-752d19890eb3",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        )
        assert_matches_type(AgentGatewayAPIResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        api = client.agent_gateways.apis.update(
            api_id="dbe53cc0-bf7e-4f7a-8d84-752d19890eb3",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            auth={"type": "none"},
            base_url="base_url",
            forwarded_headers=["string"],
            name="name",
            open_to_every_key=True,
            spec_url="spec_url",
            static_headers={"foo": "string"},
            tools=["findpetsbystatus", "getpetbyid"],
        )
        assert_matches_type(AgentGatewayAPIResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.agent_gateways.apis.with_raw_response.update(
            api_id="dbe53cc0-bf7e-4f7a-8d84-752d19890eb3",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = response.parse()
        assert_matches_type(AgentGatewayAPIResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.agent_gateways.apis.with_streaming_response.update(
            api_id="dbe53cc0-bf7e-4f7a-8d84-752d19890eb3",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = response.parse()
            assert_matches_type(AgentGatewayAPIResponse, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.agent_gateways.apis.with_raw_response.update(
                api_id="dbe53cc0-bf7e-4f7a-8d84-752d19890eb3",
                instance_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_id` but received ''"):
            client.agent_gateways.apis.with_raw_response.update(
                api_id="",
                instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        api = client.agent_gateways.apis.list(
            "32ce035d-3165-4031-b1a7-a7c0c259590a",
        )
        assert_matches_type(APIListResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.agent_gateways.apis.with_raw_response.list(
            "32ce035d-3165-4031-b1a7-a7c0c259590a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = response.parse()
        assert_matches_type(APIListResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.agent_gateways.apis.with_streaming_response.list(
            "32ce035d-3165-4031-b1a7-a7c0c259590a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = response.parse()
            assert_matches_type(APIListResponse, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.agent_gateways.apis.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        api = client.agent_gateways.apis.delete(
            api_id="dbe53cc0-bf7e-4f7a-8d84-752d19890eb3",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        )
        assert_matches_type(AgentGatewayAPIResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.agent_gateways.apis.with_raw_response.delete(
            api_id="dbe53cc0-bf7e-4f7a-8d84-752d19890eb3",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = response.parse()
        assert_matches_type(AgentGatewayAPIResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.agent_gateways.apis.with_streaming_response.delete(
            api_id="dbe53cc0-bf7e-4f7a-8d84-752d19890eb3",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = response.parse()
            assert_matches_type(AgentGatewayAPIResponse, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.agent_gateways.apis.with_raw_response.delete(
                api_id="dbe53cc0-bf7e-4f7a-8d84-752d19890eb3",
                instance_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_id` but received ''"):
            client.agent_gateways.apis.with_raw_response.delete(
                api_id="",
                instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            )


class TestAsyncAPIs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        api = await async_client.agent_gateways.apis.create(
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            name="petstore",
            spec_url="https://petstore3.swagger.io/api/v3/openapi.json",
        )
        assert_matches_type(AgentGatewayAPIResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        api = await async_client.agent_gateways.apis.create(
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            name="petstore",
            spec_url="https://petstore3.swagger.io/api/v3/openapi.json",
            auth={"type": "none"},
            base_url="https://petstore3.swagger.io/api/v3",
            forwarded_headers=["string"],
            open_to_every_key=True,
            static_headers={"foo": "string"},
            tools=["string"],
        )
        assert_matches_type(AgentGatewayAPIResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.agent_gateways.apis.with_raw_response.create(
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            name="petstore",
            spec_url="https://petstore3.swagger.io/api/v3/openapi.json",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = await response.parse()
        assert_matches_type(AgentGatewayAPIResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.agent_gateways.apis.with_streaming_response.create(
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            name="petstore",
            spec_url="https://petstore3.swagger.io/api/v3/openapi.json",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = await response.parse()
            assert_matches_type(AgentGatewayAPIResponse, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.agent_gateways.apis.with_raw_response.create(
                instance_id="",
                name="petstore",
                spec_url="https://petstore3.swagger.io/api/v3/openapi.json",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        api = await async_client.agent_gateways.apis.update(
            api_id="dbe53cc0-bf7e-4f7a-8d84-752d19890eb3",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        )
        assert_matches_type(AgentGatewayAPIResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        api = await async_client.agent_gateways.apis.update(
            api_id="dbe53cc0-bf7e-4f7a-8d84-752d19890eb3",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            auth={"type": "none"},
            base_url="base_url",
            forwarded_headers=["string"],
            name="name",
            open_to_every_key=True,
            spec_url="spec_url",
            static_headers={"foo": "string"},
            tools=["findpetsbystatus", "getpetbyid"],
        )
        assert_matches_type(AgentGatewayAPIResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.agent_gateways.apis.with_raw_response.update(
            api_id="dbe53cc0-bf7e-4f7a-8d84-752d19890eb3",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = await response.parse()
        assert_matches_type(AgentGatewayAPIResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.agent_gateways.apis.with_streaming_response.update(
            api_id="dbe53cc0-bf7e-4f7a-8d84-752d19890eb3",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = await response.parse()
            assert_matches_type(AgentGatewayAPIResponse, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.agent_gateways.apis.with_raw_response.update(
                api_id="dbe53cc0-bf7e-4f7a-8d84-752d19890eb3",
                instance_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_id` but received ''"):
            await async_client.agent_gateways.apis.with_raw_response.update(
                api_id="",
                instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        api = await async_client.agent_gateways.apis.list(
            "32ce035d-3165-4031-b1a7-a7c0c259590a",
        )
        assert_matches_type(APIListResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.agent_gateways.apis.with_raw_response.list(
            "32ce035d-3165-4031-b1a7-a7c0c259590a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = await response.parse()
        assert_matches_type(APIListResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.agent_gateways.apis.with_streaming_response.list(
            "32ce035d-3165-4031-b1a7-a7c0c259590a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = await response.parse()
            assert_matches_type(APIListResponse, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.agent_gateways.apis.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        api = await async_client.agent_gateways.apis.delete(
            api_id="dbe53cc0-bf7e-4f7a-8d84-752d19890eb3",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        )
        assert_matches_type(AgentGatewayAPIResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.agent_gateways.apis.with_raw_response.delete(
            api_id="dbe53cc0-bf7e-4f7a-8d84-752d19890eb3",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = await response.parse()
        assert_matches_type(AgentGatewayAPIResponse, api, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.agent_gateways.apis.with_streaming_response.delete(
            api_id="dbe53cc0-bf7e-4f7a-8d84-752d19890eb3",
            instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = await response.parse()
            assert_matches_type(AgentGatewayAPIResponse, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.agent_gateways.apis.with_raw_response.delete(
                api_id="dbe53cc0-bf7e-4f7a-8d84-752d19890eb3",
                instance_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_id` but received ''"):
            await async_client.agent_gateways.apis.with_raw_response.delete(
                api_id="",
                instance_id="32ce035d-3165-4031-b1a7-a7c0c259590a",
            )
