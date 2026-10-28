# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.browser_sessions import ActionCreateResponse, ActionRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Telnyx) -> None:
        action = client.browser_sessions.actions.create(
            id="id",
            type="navigate",
            url="https://example.com",
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Telnyx) -> None:
        action = client.browser_sessions.actions.create(
            id="id",
            type="navigate",
            url="https://example.com",
            wait_seconds=0,
            idempotency_key="x",
            include_observation=True,
            wait_until="load",
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Telnyx) -> None:
        response = client.browser_sessions.actions.with_raw_response.create(
            id="id",
            type="navigate",
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Telnyx) -> None:
        with client.browser_sessions.actions.with_streaming_response.create(
            id="id",
            type="navigate",
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionCreateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_1(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browser_sessions.actions.with_raw_response.create(
                id="",
                type="navigate",
                url="https://example.com",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Telnyx) -> None:
        action = client.browser_sessions.actions.create(
            id="id",
            type="observe",
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Telnyx) -> None:
        action = client.browser_sessions.actions.create(
            id="id",
            type="observe",
            wait_seconds=0,
            idempotency_key="x",
            include_observation=True,
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Telnyx) -> None:
        response = client.browser_sessions.actions.with_raw_response.create(
            id="id",
            type="observe",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Telnyx) -> None:
        with client.browser_sessions.actions.with_streaming_response.create(
            id="id",
            type="observe",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionCreateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_2(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browser_sessions.actions.with_raw_response.create(
                id="",
                type="observe",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_3(self, client: Telnyx) -> None:
        action = client.browser_sessions.actions.create(
            id="id",
            observation_id="x",
            ref="x",
            type="click",
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Telnyx) -> None:
        action = client.browser_sessions.actions.create(
            id="id",
            observation_id="x",
            ref="x",
            type="click",
            wait_seconds=0,
            idempotency_key="x",
            include_observation=True,
            timeout_ms=100,
            wait="no_wait",
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_3(self, client: Telnyx) -> None:
        response = client.browser_sessions.actions.with_raw_response.create(
            id="id",
            observation_id="x",
            ref="x",
            type="click",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_3(self, client: Telnyx) -> None:
        with client.browser_sessions.actions.with_streaming_response.create(
            id="id",
            observation_id="x",
            ref="x",
            type="click",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionCreateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_3(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browser_sessions.actions.with_raw_response.create(
                id="",
                observation_id="x",
                ref="x",
                type="click",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_4(self, client: Telnyx) -> None:
        action = client.browser_sessions.actions.create(
            id="id",
            observation_id="x",
            ref="x",
            type="fill",
            value="value",
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_4(self, client: Telnyx) -> None:
        action = client.browser_sessions.actions.create(
            id="id",
            observation_id="x",
            ref="x",
            type="fill",
            value="value",
            wait_seconds=0,
            idempotency_key="x",
            include_observation=True,
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_4(self, client: Telnyx) -> None:
        response = client.browser_sessions.actions.with_raw_response.create(
            id="id",
            observation_id="x",
            ref="x",
            type="fill",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_4(self, client: Telnyx) -> None:
        with client.browser_sessions.actions.with_streaming_response.create(
            id="id",
            observation_id="x",
            ref="x",
            type="fill",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionCreateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_4(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browser_sessions.actions.with_raw_response.create(
                id="",
                observation_id="x",
                ref="x",
                type="fill",
                value="value",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_5(self, client: Telnyx) -> None:
        action = client.browser_sessions.actions.create(
            id="id",
            observation_id="x",
            ref="x",
            type="select",
            value="value",
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_5(self, client: Telnyx) -> None:
        action = client.browser_sessions.actions.create(
            id="id",
            observation_id="x",
            ref="x",
            type="select",
            value="value",
            wait_seconds=0,
            idempotency_key="x",
            include_observation=True,
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_5(self, client: Telnyx) -> None:
        response = client.browser_sessions.actions.with_raw_response.create(
            id="id",
            observation_id="x",
            ref="x",
            type="select",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_5(self, client: Telnyx) -> None:
        with client.browser_sessions.actions.with_streaming_response.create(
            id="id",
            observation_id="x",
            ref="x",
            type="select",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionCreateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_5(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browser_sessions.actions.with_raw_response.create(
                id="",
                observation_id="x",
                ref="x",
                type="select",
                value="value",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_6(self, client: Telnyx) -> None:
        action = client.browser_sessions.actions.create(
            id="id",
            key="Enter",
            type="press",
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_6(self, client: Telnyx) -> None:
        action = client.browser_sessions.actions.create(
            id="id",
            key="Enter",
            type="press",
            wait_seconds=0,
            idempotency_key="x",
            include_observation=True,
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_6(self, client: Telnyx) -> None:
        response = client.browser_sessions.actions.with_raw_response.create(
            id="id",
            key="Enter",
            type="press",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_6(self, client: Telnyx) -> None:
        with client.browser_sessions.actions.with_streaming_response.create(
            id="id",
            key="Enter",
            type="press",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionCreateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_6(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browser_sessions.actions.with_raw_response.create(
                id="",
                key="Enter",
                type="press",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_7(self, client: Telnyx) -> None:
        action = client.browser_sessions.actions.create(
            id="id",
            type="scroll",
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_7(self, client: Telnyx) -> None:
        action = client.browser_sessions.actions.create(
            id="id",
            type="scroll",
            wait_seconds=0,
            delta_x=-5000,
            delta_y=-5000,
            idempotency_key="x",
            include_observation=True,
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_7(self, client: Telnyx) -> None:
        response = client.browser_sessions.actions.with_raw_response.create(
            id="id",
            type="scroll",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_7(self, client: Telnyx) -> None:
        with client.browser_sessions.actions.with_streaming_response.create(
            id="id",
            type="scroll",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionCreateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_7(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browser_sessions.actions.with_raw_response.create(
                id="",
                type="scroll",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_8(self, client: Telnyx) -> None:
        action = client.browser_sessions.actions.create(
            id="id",
            type="screenshot",
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_8(self, client: Telnyx) -> None:
        action = client.browser_sessions.actions.create(
            id="id",
            type="screenshot",
            wait_seconds=0,
            idempotency_key="x",
            include_observation=True,
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_8(self, client: Telnyx) -> None:
        response = client.browser_sessions.actions.with_raw_response.create(
            id="id",
            type="screenshot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_8(self, client: Telnyx) -> None:
        with client.browser_sessions.actions.with_streaming_response.create(
            id="id",
            type="screenshot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionCreateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_8(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browser_sessions.actions.with_raw_response.create(
                id="",
                type="screenshot",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_9(self, client: Telnyx) -> None:
        action = client.browser_sessions.actions.create(
            id="id",
            condition={
                "kind": "url_pattern",
                "pattern": "x",
            },
            type="wait_for",
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_9(self, client: Telnyx) -> None:
        action = client.browser_sessions.actions.create(
            id="id",
            condition={
                "kind": "url_pattern",
                "pattern": "x",
            },
            type="wait_for",
            wait_seconds=0,
            idempotency_key="x",
            include_observation=True,
            timeout_ms=100,
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_9(self, client: Telnyx) -> None:
        response = client.browser_sessions.actions.with_raw_response.create(
            id="id",
            condition={
                "kind": "url_pattern",
                "pattern": "x",
            },
            type="wait_for",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_9(self, client: Telnyx) -> None:
        with client.browser_sessions.actions.with_streaming_response.create(
            id="id",
            condition={
                "kind": "url_pattern",
                "pattern": "x",
            },
            type="wait_for",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionCreateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_9(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browser_sessions.actions.with_raw_response.create(
                id="",
                condition={
                    "kind": "url_pattern",
                    "pattern": "x",
                },
                type="wait_for",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_10(self, client: Telnyx) -> None:
        action = client.browser_sessions.actions.create(
            id="id",
            actions=[
                {
                    "type": "navigate",
                    "url": "https://example.com",
                }
            ],
            type="batch",
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_10(self, client: Telnyx) -> None:
        action = client.browser_sessions.actions.create(
            id="id",
            actions=[
                {
                    "type": "navigate",
                    "url": "https://example.com",
                    "idempotency_key": "x",
                    "include_observation": True,
                    "wait_until": "load",
                }
            ],
            type="batch",
            wait_seconds=0,
            idempotency_key="x",
            include_observation=True,
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_10(self, client: Telnyx) -> None:
        response = client.browser_sessions.actions.with_raw_response.create(
            id="id",
            actions=[
                {
                    "type": "navigate",
                    "url": "https://example.com",
                }
            ],
            type="batch",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_10(self, client: Telnyx) -> None:
        with client.browser_sessions.actions.with_streaming_response.create(
            id="id",
            actions=[
                {
                    "type": "navigate",
                    "url": "https://example.com",
                }
            ],
            type="batch",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionCreateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_10(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browser_sessions.actions.with_raw_response.create(
                id="",
                actions=[
                    {
                        "type": "navigate",
                        "url": "https://example.com",
                    }
                ],
                type="batch",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        action = client.browser_sessions.actions.retrieve(
            action_id="actionId",
            id="id",
        )
        assert_matches_type(ActionRetrieveResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.browser_sessions.actions.with_raw_response.retrieve(
            action_id="actionId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(ActionRetrieveResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.browser_sessions.actions.with_streaming_response.retrieve(
            action_id="actionId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(ActionRetrieveResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.browser_sessions.actions.with_raw_response.retrieve(
                action_id="actionId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action_id` but received ''"):
            client.browser_sessions.actions.with_raw_response.retrieve(
                action_id="",
                id="id",
            )


class TestAsyncActions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.browser_sessions.actions.create(
            id="id",
            type="navigate",
            url="https://example.com",
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.browser_sessions.actions.create(
            id="id",
            type="navigate",
            url="https://example.com",
            wait_seconds=0,
            idempotency_key="x",
            include_observation=True,
            wait_until="load",
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.browser_sessions.actions.with_raw_response.create(
            id="id",
            type="navigate",
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncTelnyx) -> None:
        async with async_client.browser_sessions.actions.with_streaming_response.create(
            id="id",
            type="navigate",
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionCreateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browser_sessions.actions.with_raw_response.create(
                id="",
                type="navigate",
                url="https://example.com",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.browser_sessions.actions.create(
            id="id",
            type="observe",
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.browser_sessions.actions.create(
            id="id",
            type="observe",
            wait_seconds=0,
            idempotency_key="x",
            include_observation=True,
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.browser_sessions.actions.with_raw_response.create(
            id="id",
            type="observe",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncTelnyx) -> None:
        async with async_client.browser_sessions.actions.with_streaming_response.create(
            id="id",
            type="observe",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionCreateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browser_sessions.actions.with_raw_response.create(
                id="",
                type="observe",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.browser_sessions.actions.create(
            id="id",
            observation_id="x",
            ref="x",
            type="click",
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.browser_sessions.actions.create(
            id="id",
            observation_id="x",
            ref="x",
            type="click",
            wait_seconds=0,
            idempotency_key="x",
            include_observation=True,
            timeout_ms=100,
            wait="no_wait",
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.browser_sessions.actions.with_raw_response.create(
            id="id",
            observation_id="x",
            ref="x",
            type="click",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncTelnyx) -> None:
        async with async_client.browser_sessions.actions.with_streaming_response.create(
            id="id",
            observation_id="x",
            ref="x",
            type="click",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionCreateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_3(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browser_sessions.actions.with_raw_response.create(
                id="",
                observation_id="x",
                ref="x",
                type="click",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_4(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.browser_sessions.actions.create(
            id="id",
            observation_id="x",
            ref="x",
            type="fill",
            value="value",
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_4(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.browser_sessions.actions.create(
            id="id",
            observation_id="x",
            ref="x",
            type="fill",
            value="value",
            wait_seconds=0,
            idempotency_key="x",
            include_observation=True,
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_4(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.browser_sessions.actions.with_raw_response.create(
            id="id",
            observation_id="x",
            ref="x",
            type="fill",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_4(self, async_client: AsyncTelnyx) -> None:
        async with async_client.browser_sessions.actions.with_streaming_response.create(
            id="id",
            observation_id="x",
            ref="x",
            type="fill",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionCreateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_4(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browser_sessions.actions.with_raw_response.create(
                id="",
                observation_id="x",
                ref="x",
                type="fill",
                value="value",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_5(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.browser_sessions.actions.create(
            id="id",
            observation_id="x",
            ref="x",
            type="select",
            value="value",
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_5(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.browser_sessions.actions.create(
            id="id",
            observation_id="x",
            ref="x",
            type="select",
            value="value",
            wait_seconds=0,
            idempotency_key="x",
            include_observation=True,
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_5(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.browser_sessions.actions.with_raw_response.create(
            id="id",
            observation_id="x",
            ref="x",
            type="select",
            value="value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_5(self, async_client: AsyncTelnyx) -> None:
        async with async_client.browser_sessions.actions.with_streaming_response.create(
            id="id",
            observation_id="x",
            ref="x",
            type="select",
            value="value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionCreateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_5(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browser_sessions.actions.with_raw_response.create(
                id="",
                observation_id="x",
                ref="x",
                type="select",
                value="value",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_6(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.browser_sessions.actions.create(
            id="id",
            key="Enter",
            type="press",
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_6(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.browser_sessions.actions.create(
            id="id",
            key="Enter",
            type="press",
            wait_seconds=0,
            idempotency_key="x",
            include_observation=True,
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_6(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.browser_sessions.actions.with_raw_response.create(
            id="id",
            key="Enter",
            type="press",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_6(self, async_client: AsyncTelnyx) -> None:
        async with async_client.browser_sessions.actions.with_streaming_response.create(
            id="id",
            key="Enter",
            type="press",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionCreateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_6(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browser_sessions.actions.with_raw_response.create(
                id="",
                key="Enter",
                type="press",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_7(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.browser_sessions.actions.create(
            id="id",
            type="scroll",
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_7(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.browser_sessions.actions.create(
            id="id",
            type="scroll",
            wait_seconds=0,
            delta_x=-5000,
            delta_y=-5000,
            idempotency_key="x",
            include_observation=True,
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_7(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.browser_sessions.actions.with_raw_response.create(
            id="id",
            type="scroll",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_7(self, async_client: AsyncTelnyx) -> None:
        async with async_client.browser_sessions.actions.with_streaming_response.create(
            id="id",
            type="scroll",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionCreateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_7(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browser_sessions.actions.with_raw_response.create(
                id="",
                type="scroll",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_8(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.browser_sessions.actions.create(
            id="id",
            type="screenshot",
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_8(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.browser_sessions.actions.create(
            id="id",
            type="screenshot",
            wait_seconds=0,
            idempotency_key="x",
            include_observation=True,
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_8(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.browser_sessions.actions.with_raw_response.create(
            id="id",
            type="screenshot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_8(self, async_client: AsyncTelnyx) -> None:
        async with async_client.browser_sessions.actions.with_streaming_response.create(
            id="id",
            type="screenshot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionCreateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_8(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browser_sessions.actions.with_raw_response.create(
                id="",
                type="screenshot",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_9(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.browser_sessions.actions.create(
            id="id",
            condition={
                "kind": "url_pattern",
                "pattern": "x",
            },
            type="wait_for",
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_9(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.browser_sessions.actions.create(
            id="id",
            condition={
                "kind": "url_pattern",
                "pattern": "x",
            },
            type="wait_for",
            wait_seconds=0,
            idempotency_key="x",
            include_observation=True,
            timeout_ms=100,
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_9(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.browser_sessions.actions.with_raw_response.create(
            id="id",
            condition={
                "kind": "url_pattern",
                "pattern": "x",
            },
            type="wait_for",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_9(self, async_client: AsyncTelnyx) -> None:
        async with async_client.browser_sessions.actions.with_streaming_response.create(
            id="id",
            condition={
                "kind": "url_pattern",
                "pattern": "x",
            },
            type="wait_for",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionCreateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_9(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browser_sessions.actions.with_raw_response.create(
                id="",
                condition={
                    "kind": "url_pattern",
                    "pattern": "x",
                },
                type="wait_for",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_10(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.browser_sessions.actions.create(
            id="id",
            actions=[
                {
                    "type": "navigate",
                    "url": "https://example.com",
                }
            ],
            type="batch",
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_10(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.browser_sessions.actions.create(
            id="id",
            actions=[
                {
                    "type": "navigate",
                    "url": "https://example.com",
                    "idempotency_key": "x",
                    "include_observation": True,
                    "wait_until": "load",
                }
            ],
            type="batch",
            wait_seconds=0,
            idempotency_key="x",
            include_observation=True,
        )
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_10(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.browser_sessions.actions.with_raw_response.create(
            id="id",
            actions=[
                {
                    "type": "navigate",
                    "url": "https://example.com",
                }
            ],
            type="batch",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionCreateResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_10(self, async_client: AsyncTelnyx) -> None:
        async with async_client.browser_sessions.actions.with_streaming_response.create(
            id="id",
            actions=[
                {
                    "type": "navigate",
                    "url": "https://example.com",
                }
            ],
            type="batch",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionCreateResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_10(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browser_sessions.actions.with_raw_response.create(
                id="",
                actions=[
                    {
                        "type": "navigate",
                        "url": "https://example.com",
                    }
                ],
                type="batch",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        action = await async_client.browser_sessions.actions.retrieve(
            action_id="actionId",
            id="id",
        )
        assert_matches_type(ActionRetrieveResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.browser_sessions.actions.with_raw_response.retrieve(
            action_id="actionId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(ActionRetrieveResponse, action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.browser_sessions.actions.with_streaming_response.retrieve(
            action_id="actionId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(ActionRetrieveResponse, action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.browser_sessions.actions.with_raw_response.retrieve(
                action_id="actionId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `action_id` but received ''"):
            await async_client.browser_sessions.actions.with_raw_response.retrieve(
                action_id="",
                id="id",
            )
