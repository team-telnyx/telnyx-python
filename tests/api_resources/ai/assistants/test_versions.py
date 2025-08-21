# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.ai import (
    AssistantsList,
)
from telnyx.types.ai.assistants import (
    VersionUpdateResponse,
    VersionPromoteResponse,
    VersionRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVersions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        version = client.ai.assistants.versions.retrieve(
            version_id="version_id",
            assistant_id="assistant_id",
        )
        assert_matches_type(VersionRetrieveResponse, version, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Telnyx) -> None:
        version = client.ai.assistants.versions.retrieve(
            version_id="version_id",
            assistant_id="assistant_id",
            include_mcp_servers=True,
        )
        assert_matches_type(VersionRetrieveResponse, version, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.ai.assistants.versions.with_raw_response.retrieve(
            version_id="version_id",
            assistant_id="assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(VersionRetrieveResponse, version, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.ai.assistants.versions.with_streaming_response.retrieve(
            version_id="version_id",
            assistant_id="assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(VersionRetrieveResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.ai.assistants.versions.with_raw_response.retrieve(
                version_id="version_id",
                assistant_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            client.ai.assistants.versions.with_raw_response.retrieve(
                version_id="",
                assistant_id="assistant_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        version = client.ai.assistants.versions.update(
            version_id="version_id",
            assistant_id="assistant_id",
        )
        assert_matches_type(VersionUpdateResponse, version, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        version = client.ai.assistants.versions.update(
            version_id="version_id",
            assistant_id="assistant_id",
            description="description",
            dynamic_variables={"foo": "bar"},
            dynamic_variables_webhook_url="dynamic_variables_webhook_url",
            enabled_features=["telephony"],
            greeting="greeting",
            insight_settings={"insight_group_id": "insight_group_id"},
            instructions="instructions",
            llm_api_key_ref="llm_api_key_ref",
            messaging_settings={
                "default_messaging_profile_id": "default_messaging_profile_id",
                "delivery_status_webhook_url": "delivery_status_webhook_url",
            },
            model="model",
            name="name",
            privacy_settings={"data_retention": True},
            telephony_settings={
                "default_texml_app_id": "default_texml_app_id",
                "supports_unauthenticated_web_calls": True,
            },
            tools=[
                {
                    "type": "webhook",
                    "webhook": {
                        "description": "description",
                        "name": "name",
                        "url": "https://example.com/api/v1/function",
                        "body_parameters": {
                            "properties": {
                                "age": "bar",
                                "location": "bar",
                            },
                            "required": ["age", "location"],
                            "type": "object",
                        },
                        "headers": [
                            {
                                "name": "name",
                                "value": "value",
                            }
                        ],
                        "method": "GET",
                        "path_parameters": {
                            "properties": {"id": "bar"},
                            "required": ["id"],
                            "type": "object",
                        },
                        "query_parameters": {
                            "properties": {"page": "bar"},
                            "required": ["page"],
                            "type": "object",
                        },
                    },
                }
            ],
            transcription={
                "language": "language",
                "model": "model",
            },
            voice_settings={
                "voice": "voice",
                "api_key_ref": "api_key_ref",
                "voice_speed": 0,
            },
        )
        assert_matches_type(VersionUpdateResponse, version, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.ai.assistants.versions.with_raw_response.update(
            version_id="version_id",
            assistant_id="assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(VersionUpdateResponse, version, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.ai.assistants.versions.with_streaming_response.update(
            version_id="version_id",
            assistant_id="assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(VersionUpdateResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.ai.assistants.versions.with_raw_response.update(
                version_id="version_id",
                assistant_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            client.ai.assistants.versions.with_raw_response.update(
                version_id="",
                assistant_id="assistant_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        version = client.ai.assistants.versions.list(
            "assistant_id",
        )
        assert_matches_type(AssistantsList, version, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.ai.assistants.versions.with_raw_response.list(
            "assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(AssistantsList, version, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.ai.assistants.versions.with_streaming_response.list(
            "assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(AssistantsList, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.ai.assistants.versions.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        version = client.ai.assistants.versions.delete(
            version_id="version_id",
            assistant_id="assistant_id",
        )
        assert version is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.ai.assistants.versions.with_raw_response.delete(
            version_id="version_id",
            assistant_id="assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert version is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.ai.assistants.versions.with_streaming_response.delete(
            version_id="version_id",
            assistant_id="assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert version is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.ai.assistants.versions.with_raw_response.delete(
                version_id="version_id",
                assistant_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            client.ai.assistants.versions.with_raw_response.delete(
                version_id="",
                assistant_id="assistant_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_promote(self, client: Telnyx) -> None:
        version = client.ai.assistants.versions.promote(
            version_id="version_id",
            assistant_id="assistant_id",
        )
        assert_matches_type(VersionPromoteResponse, version, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_promote(self, client: Telnyx) -> None:
        response = client.ai.assistants.versions.with_raw_response.promote(
            version_id="version_id",
            assistant_id="assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(VersionPromoteResponse, version, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_promote(self, client: Telnyx) -> None:
        with client.ai.assistants.versions.with_streaming_response.promote(
            version_id="version_id",
            assistant_id="assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(VersionPromoteResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_promote(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.ai.assistants.versions.with_raw_response.promote(
                version_id="version_id",
                assistant_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            client.ai.assistants.versions.with_raw_response.promote(
                version_id="",
                assistant_id="assistant_id",
            )


class TestAsyncVersions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        version = await async_client.ai.assistants.versions.retrieve(
            version_id="version_id",
            assistant_id="assistant_id",
        )
        assert_matches_type(VersionRetrieveResponse, version, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTelnyx) -> None:
        version = await async_client.ai.assistants.versions.retrieve(
            version_id="version_id",
            assistant_id="assistant_id",
            include_mcp_servers=True,
        )
        assert_matches_type(VersionRetrieveResponse, version, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.assistants.versions.with_raw_response.retrieve(
            version_id="version_id",
            assistant_id="assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(VersionRetrieveResponse, version, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.assistants.versions.with_streaming_response.retrieve(
            version_id="version_id",
            assistant_id="assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(VersionRetrieveResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            await async_client.ai.assistants.versions.with_raw_response.retrieve(
                version_id="version_id",
                assistant_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            await async_client.ai.assistants.versions.with_raw_response.retrieve(
                version_id="",
                assistant_id="assistant_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        version = await async_client.ai.assistants.versions.update(
            version_id="version_id",
            assistant_id="assistant_id",
        )
        assert_matches_type(VersionUpdateResponse, version, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        version = await async_client.ai.assistants.versions.update(
            version_id="version_id",
            assistant_id="assistant_id",
            description="description",
            dynamic_variables={"foo": "bar"},
            dynamic_variables_webhook_url="dynamic_variables_webhook_url",
            enabled_features=["telephony"],
            greeting="greeting",
            insight_settings={"insight_group_id": "insight_group_id"},
            instructions="instructions",
            llm_api_key_ref="llm_api_key_ref",
            messaging_settings={
                "default_messaging_profile_id": "default_messaging_profile_id",
                "delivery_status_webhook_url": "delivery_status_webhook_url",
            },
            model="model",
            name="name",
            privacy_settings={"data_retention": True},
            telephony_settings={
                "default_texml_app_id": "default_texml_app_id",
                "supports_unauthenticated_web_calls": True,
            },
            tools=[
                {
                    "type": "webhook",
                    "webhook": {
                        "description": "description",
                        "name": "name",
                        "url": "https://example.com/api/v1/function",
                        "body_parameters": {
                            "properties": {
                                "age": "bar",
                                "location": "bar",
                            },
                            "required": ["age", "location"],
                            "type": "object",
                        },
                        "headers": [
                            {
                                "name": "name",
                                "value": "value",
                            }
                        ],
                        "method": "GET",
                        "path_parameters": {
                            "properties": {"id": "bar"},
                            "required": ["id"],
                            "type": "object",
                        },
                        "query_parameters": {
                            "properties": {"page": "bar"},
                            "required": ["page"],
                            "type": "object",
                        },
                    },
                }
            ],
            transcription={
                "language": "language",
                "model": "model",
            },
            voice_settings={
                "voice": "voice",
                "api_key_ref": "api_key_ref",
                "voice_speed": 0,
            },
        )
        assert_matches_type(VersionUpdateResponse, version, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.assistants.versions.with_raw_response.update(
            version_id="version_id",
            assistant_id="assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(VersionUpdateResponse, version, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.assistants.versions.with_streaming_response.update(
            version_id="version_id",
            assistant_id="assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(VersionUpdateResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            await async_client.ai.assistants.versions.with_raw_response.update(
                version_id="version_id",
                assistant_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            await async_client.ai.assistants.versions.with_raw_response.update(
                version_id="",
                assistant_id="assistant_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        version = await async_client.ai.assistants.versions.list(
            "assistant_id",
        )
        assert_matches_type(AssistantsList, version, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.assistants.versions.with_raw_response.list(
            "assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(AssistantsList, version, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.assistants.versions.with_streaming_response.list(
            "assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(AssistantsList, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            await async_client.ai.assistants.versions.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        version = await async_client.ai.assistants.versions.delete(
            version_id="version_id",
            assistant_id="assistant_id",
        )
        assert version is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.assistants.versions.with_raw_response.delete(
            version_id="version_id",
            assistant_id="assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert version is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.assistants.versions.with_streaming_response.delete(
            version_id="version_id",
            assistant_id="assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert version is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            await async_client.ai.assistants.versions.with_raw_response.delete(
                version_id="version_id",
                assistant_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            await async_client.ai.assistants.versions.with_raw_response.delete(
                version_id="",
                assistant_id="assistant_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_promote(self, async_client: AsyncTelnyx) -> None:
        version = await async_client.ai.assistants.versions.promote(
            version_id="version_id",
            assistant_id="assistant_id",
        )
        assert_matches_type(VersionPromoteResponse, version, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_promote(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.assistants.versions.with_raw_response.promote(
            version_id="version_id",
            assistant_id="assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(VersionPromoteResponse, version, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_promote(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.assistants.versions.with_streaming_response.promote(
            version_id="version_id",
            assistant_id="assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(VersionPromoteResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_promote(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            await async_client.ai.assistants.versions.with_raw_response.promote(
                version_id="version_id",
                assistant_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            await async_client.ai.assistants.versions.with_raw_response.promote(
                version_id="",
                assistant_id="assistant_id",
            )
