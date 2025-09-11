# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.ai.assistants import CanaryDeployResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCanaryDeploys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        canary_deploy = client.ai.assistants.canary_deploys.create(
            assistant_id="assistant_id",
            versions=[
                {
                    "percentage": 1,
                    "version_id": "version_id",
                }
            ],
        )
        assert_matches_type(CanaryDeployResponse, canary_deploy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.ai.assistants.canary_deploys.with_raw_response.create(
            assistant_id="assistant_id",
            versions=[
                {
                    "percentage": 1,
                    "version_id": "version_id",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        canary_deploy = response.parse()
        assert_matches_type(CanaryDeployResponse, canary_deploy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.ai.assistants.canary_deploys.with_streaming_response.create(
            assistant_id="assistant_id",
            versions=[
                {
                    "percentage": 1,
                    "version_id": "version_id",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            canary_deploy = response.parse()
            assert_matches_type(CanaryDeployResponse, canary_deploy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.ai.assistants.canary_deploys.with_raw_response.create(
                assistant_id="",
                versions=[
                    {
                        "percentage": 1,
                        "version_id": "version_id",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        canary_deploy = client.ai.assistants.canary_deploys.retrieve(
            "assistant_id",
        )
        assert_matches_type(CanaryDeployResponse, canary_deploy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.ai.assistants.canary_deploys.with_raw_response.retrieve(
            "assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        canary_deploy = response.parse()
        assert_matches_type(CanaryDeployResponse, canary_deploy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.ai.assistants.canary_deploys.with_streaming_response.retrieve(
            "assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            canary_deploy = response.parse()
            assert_matches_type(CanaryDeployResponse, canary_deploy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.ai.assistants.canary_deploys.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        canary_deploy = client.ai.assistants.canary_deploys.update(
            assistant_id="assistant_id",
            versions=[
                {
                    "percentage": 1,
                    "version_id": "version_id",
                }
            ],
        )
        assert_matches_type(CanaryDeployResponse, canary_deploy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.ai.assistants.canary_deploys.with_raw_response.update(
            assistant_id="assistant_id",
            versions=[
                {
                    "percentage": 1,
                    "version_id": "version_id",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        canary_deploy = response.parse()
        assert_matches_type(CanaryDeployResponse, canary_deploy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.ai.assistants.canary_deploys.with_streaming_response.update(
            assistant_id="assistant_id",
            versions=[
                {
                    "percentage": 1,
                    "version_id": "version_id",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            canary_deploy = response.parse()
            assert_matches_type(CanaryDeployResponse, canary_deploy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.ai.assistants.canary_deploys.with_raw_response.update(
                assistant_id="",
                versions=[
                    {
                        "percentage": 1,
                        "version_id": "version_id",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        canary_deploy = client.ai.assistants.canary_deploys.delete(
            "assistant_id",
        )
        assert canary_deploy is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.ai.assistants.canary_deploys.with_raw_response.delete(
            "assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        canary_deploy = response.parse()
        assert canary_deploy is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.ai.assistants.canary_deploys.with_streaming_response.delete(
            "assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            canary_deploy = response.parse()
            assert canary_deploy is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            client.ai.assistants.canary_deploys.with_raw_response.delete(
                "",
            )


class TestAsyncCanaryDeploys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        canary_deploy = await async_client.ai.assistants.canary_deploys.create(
            assistant_id="assistant_id",
            versions=[
                {
                    "percentage": 1,
                    "version_id": "version_id",
                }
            ],
        )
        assert_matches_type(CanaryDeployResponse, canary_deploy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.assistants.canary_deploys.with_raw_response.create(
            assistant_id="assistant_id",
            versions=[
                {
                    "percentage": 1,
                    "version_id": "version_id",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        canary_deploy = await response.parse()
        assert_matches_type(CanaryDeployResponse, canary_deploy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.assistants.canary_deploys.with_streaming_response.create(
            assistant_id="assistant_id",
            versions=[
                {
                    "percentage": 1,
                    "version_id": "version_id",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            canary_deploy = await response.parse()
            assert_matches_type(CanaryDeployResponse, canary_deploy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            await async_client.ai.assistants.canary_deploys.with_raw_response.create(
                assistant_id="",
                versions=[
                    {
                        "percentage": 1,
                        "version_id": "version_id",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        canary_deploy = await async_client.ai.assistants.canary_deploys.retrieve(
            "assistant_id",
        )
        assert_matches_type(CanaryDeployResponse, canary_deploy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.assistants.canary_deploys.with_raw_response.retrieve(
            "assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        canary_deploy = await response.parse()
        assert_matches_type(CanaryDeployResponse, canary_deploy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.assistants.canary_deploys.with_streaming_response.retrieve(
            "assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            canary_deploy = await response.parse()
            assert_matches_type(CanaryDeployResponse, canary_deploy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            await async_client.ai.assistants.canary_deploys.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        canary_deploy = await async_client.ai.assistants.canary_deploys.update(
            assistant_id="assistant_id",
            versions=[
                {
                    "percentage": 1,
                    "version_id": "version_id",
                }
            ],
        )
        assert_matches_type(CanaryDeployResponse, canary_deploy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.assistants.canary_deploys.with_raw_response.update(
            assistant_id="assistant_id",
            versions=[
                {
                    "percentage": 1,
                    "version_id": "version_id",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        canary_deploy = await response.parse()
        assert_matches_type(CanaryDeployResponse, canary_deploy, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.assistants.canary_deploys.with_streaming_response.update(
            assistant_id="assistant_id",
            versions=[
                {
                    "percentage": 1,
                    "version_id": "version_id",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            canary_deploy = await response.parse()
            assert_matches_type(CanaryDeployResponse, canary_deploy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            await async_client.ai.assistants.canary_deploys.with_raw_response.update(
                assistant_id="",
                versions=[
                    {
                        "percentage": 1,
                        "version_id": "version_id",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        canary_deploy = await async_client.ai.assistants.canary_deploys.delete(
            "assistant_id",
        )
        assert canary_deploy is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.assistants.canary_deploys.with_raw_response.delete(
            "assistant_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        canary_deploy = await response.parse()
        assert canary_deploy is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.assistants.canary_deploys.with_streaming_response.delete(
            "assistant_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            canary_deploy = await response.parse()
            assert canary_deploy is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `assistant_id` but received ''"):
            await async_client.ai.assistants.canary_deploys.with_raw_response.delete(
                "",
            )
