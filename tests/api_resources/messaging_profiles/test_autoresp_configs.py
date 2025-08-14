# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.messaging_profiles import (
    AutoRespConfigResponse,
    AutorespConfigListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAutorespConfigs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        autoresp_config = client.messaging_profiles.autoresp_configs.create(
            profile_id="profile_id",
            country_code="US",
            keywords=["keyword1", "keyword2"],
            op="start",
        )
        assert_matches_type(AutoRespConfigResponse, autoresp_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        autoresp_config = client.messaging_profiles.autoresp_configs.create(
            profile_id="profile_id",
            country_code="US",
            keywords=["keyword1", "keyword2"],
            op="start",
            resp_text="Thank you for your message",
        )
        assert_matches_type(AutoRespConfigResponse, autoresp_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.messaging_profiles.autoresp_configs.with_raw_response.create(
            profile_id="profile_id",
            country_code="US",
            keywords=["keyword1", "keyword2"],
            op="start",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoresp_config = response.parse()
        assert_matches_type(AutoRespConfigResponse, autoresp_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.messaging_profiles.autoresp_configs.with_streaming_response.create(
            profile_id="profile_id",
            country_code="US",
            keywords=["keyword1", "keyword2"],
            op="start",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoresp_config = response.parse()
            assert_matches_type(AutoRespConfigResponse, autoresp_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.messaging_profiles.autoresp_configs.with_raw_response.create(
                profile_id="",
                country_code="US",
                keywords=["keyword1", "keyword2"],
                op="start",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        autoresp_config = client.messaging_profiles.autoresp_configs.retrieve(
            autoresp_cfg_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AutoRespConfigResponse, autoresp_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.messaging_profiles.autoresp_configs.with_raw_response.retrieve(
            autoresp_cfg_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoresp_config = response.parse()
        assert_matches_type(AutoRespConfigResponse, autoresp_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.messaging_profiles.autoresp_configs.with_streaming_response.retrieve(
            autoresp_cfg_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoresp_config = response.parse()
            assert_matches_type(AutoRespConfigResponse, autoresp_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.messaging_profiles.autoresp_configs.with_raw_response.retrieve(
                autoresp_cfg_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                profile_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `autoresp_cfg_id` but received ''"):
            client.messaging_profiles.autoresp_configs.with_raw_response.retrieve(
                autoresp_cfg_id="",
                profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        autoresp_config = client.messaging_profiles.autoresp_configs.update(
            autoresp_cfg_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            country_code="US",
            keywords=["keyword1", "keyword2"],
            op="start",
        )
        assert_matches_type(AutoRespConfigResponse, autoresp_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        autoresp_config = client.messaging_profiles.autoresp_configs.update(
            autoresp_cfg_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            country_code="US",
            keywords=["keyword1", "keyword2"],
            op="start",
            resp_text="Thank you for your message",
        )
        assert_matches_type(AutoRespConfigResponse, autoresp_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.messaging_profiles.autoresp_configs.with_raw_response.update(
            autoresp_cfg_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            country_code="US",
            keywords=["keyword1", "keyword2"],
            op="start",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoresp_config = response.parse()
        assert_matches_type(AutoRespConfigResponse, autoresp_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.messaging_profiles.autoresp_configs.with_streaming_response.update(
            autoresp_cfg_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            country_code="US",
            keywords=["keyword1", "keyword2"],
            op="start",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoresp_config = response.parse()
            assert_matches_type(AutoRespConfigResponse, autoresp_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.messaging_profiles.autoresp_configs.with_raw_response.update(
                autoresp_cfg_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                profile_id="",
                country_code="US",
                keywords=["keyword1", "keyword2"],
                op="start",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `autoresp_cfg_id` but received ''"):
            client.messaging_profiles.autoresp_configs.with_raw_response.update(
                autoresp_cfg_id="",
                profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                country_code="US",
                keywords=["keyword1", "keyword2"],
                op="start",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        autoresp_config = client.messaging_profiles.autoresp_configs.list(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AutorespConfigListResponse, autoresp_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        autoresp_config = client.messaging_profiles.autoresp_configs.list(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            country_code="country_code",
            created_at={
                "gte": "gte",
                "lte": "lte",
            },
            updated_at={
                "gte": "gte",
                "lte": "lte",
            },
        )
        assert_matches_type(AutorespConfigListResponse, autoresp_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.messaging_profiles.autoresp_configs.with_raw_response.list(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoresp_config = response.parse()
        assert_matches_type(AutorespConfigListResponse, autoresp_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.messaging_profiles.autoresp_configs.with_streaming_response.list(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoresp_config = response.parse()
            assert_matches_type(AutorespConfigListResponse, autoresp_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.messaging_profiles.autoresp_configs.with_raw_response.list(
                profile_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        autoresp_config = client.messaging_profiles.autoresp_configs.delete(
            autoresp_cfg_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, autoresp_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.messaging_profiles.autoresp_configs.with_raw_response.delete(
            autoresp_cfg_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoresp_config = response.parse()
        assert_matches_type(object, autoresp_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.messaging_profiles.autoresp_configs.with_streaming_response.delete(
            autoresp_cfg_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoresp_config = response.parse()
            assert_matches_type(object, autoresp_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.messaging_profiles.autoresp_configs.with_raw_response.delete(
                autoresp_cfg_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                profile_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `autoresp_cfg_id` but received ''"):
            client.messaging_profiles.autoresp_configs.with_raw_response.delete(
                autoresp_cfg_id="",
                profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncAutorespConfigs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        autoresp_config = await async_client.messaging_profiles.autoresp_configs.create(
            profile_id="profile_id",
            country_code="US",
            keywords=["keyword1", "keyword2"],
            op="start",
        )
        assert_matches_type(AutoRespConfigResponse, autoresp_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        autoresp_config = await async_client.messaging_profiles.autoresp_configs.create(
            profile_id="profile_id",
            country_code="US",
            keywords=["keyword1", "keyword2"],
            op="start",
            resp_text="Thank you for your message",
        )
        assert_matches_type(AutoRespConfigResponse, autoresp_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_profiles.autoresp_configs.with_raw_response.create(
            profile_id="profile_id",
            country_code="US",
            keywords=["keyword1", "keyword2"],
            op="start",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoresp_config = await response.parse()
        assert_matches_type(AutoRespConfigResponse, autoresp_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_profiles.autoresp_configs.with_streaming_response.create(
            profile_id="profile_id",
            country_code="US",
            keywords=["keyword1", "keyword2"],
            op="start",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoresp_config = await response.parse()
            assert_matches_type(AutoRespConfigResponse, autoresp_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.messaging_profiles.autoresp_configs.with_raw_response.create(
                profile_id="",
                country_code="US",
                keywords=["keyword1", "keyword2"],
                op="start",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        autoresp_config = await async_client.messaging_profiles.autoresp_configs.retrieve(
            autoresp_cfg_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AutoRespConfigResponse, autoresp_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_profiles.autoresp_configs.with_raw_response.retrieve(
            autoresp_cfg_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoresp_config = await response.parse()
        assert_matches_type(AutoRespConfigResponse, autoresp_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_profiles.autoresp_configs.with_streaming_response.retrieve(
            autoresp_cfg_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoresp_config = await response.parse()
            assert_matches_type(AutoRespConfigResponse, autoresp_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.messaging_profiles.autoresp_configs.with_raw_response.retrieve(
                autoresp_cfg_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                profile_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `autoresp_cfg_id` but received ''"):
            await async_client.messaging_profiles.autoresp_configs.with_raw_response.retrieve(
                autoresp_cfg_id="",
                profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        autoresp_config = await async_client.messaging_profiles.autoresp_configs.update(
            autoresp_cfg_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            country_code="US",
            keywords=["keyword1", "keyword2"],
            op="start",
        )
        assert_matches_type(AutoRespConfigResponse, autoresp_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        autoresp_config = await async_client.messaging_profiles.autoresp_configs.update(
            autoresp_cfg_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            country_code="US",
            keywords=["keyword1", "keyword2"],
            op="start",
            resp_text="Thank you for your message",
        )
        assert_matches_type(AutoRespConfigResponse, autoresp_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_profiles.autoresp_configs.with_raw_response.update(
            autoresp_cfg_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            country_code="US",
            keywords=["keyword1", "keyword2"],
            op="start",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoresp_config = await response.parse()
        assert_matches_type(AutoRespConfigResponse, autoresp_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_profiles.autoresp_configs.with_streaming_response.update(
            autoresp_cfg_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            country_code="US",
            keywords=["keyword1", "keyword2"],
            op="start",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoresp_config = await response.parse()
            assert_matches_type(AutoRespConfigResponse, autoresp_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.messaging_profiles.autoresp_configs.with_raw_response.update(
                autoresp_cfg_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                profile_id="",
                country_code="US",
                keywords=["keyword1", "keyword2"],
                op="start",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `autoresp_cfg_id` but received ''"):
            await async_client.messaging_profiles.autoresp_configs.with_raw_response.update(
                autoresp_cfg_id="",
                profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                country_code="US",
                keywords=["keyword1", "keyword2"],
                op="start",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        autoresp_config = await async_client.messaging_profiles.autoresp_configs.list(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AutorespConfigListResponse, autoresp_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        autoresp_config = await async_client.messaging_profiles.autoresp_configs.list(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            country_code="country_code",
            created_at={
                "gte": "gte",
                "lte": "lte",
            },
            updated_at={
                "gte": "gte",
                "lte": "lte",
            },
        )
        assert_matches_type(AutorespConfigListResponse, autoresp_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_profiles.autoresp_configs.with_raw_response.list(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoresp_config = await response.parse()
        assert_matches_type(AutorespConfigListResponse, autoresp_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_profiles.autoresp_configs.with_streaming_response.list(
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoresp_config = await response.parse()
            assert_matches_type(AutorespConfigListResponse, autoresp_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.messaging_profiles.autoresp_configs.with_raw_response.list(
                profile_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        autoresp_config = await async_client.messaging_profiles.autoresp_configs.delete(
            autoresp_cfg_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, autoresp_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_profiles.autoresp_configs.with_raw_response.delete(
            autoresp_cfg_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        autoresp_config = await response.parse()
        assert_matches_type(object, autoresp_config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_profiles.autoresp_configs.with_streaming_response.delete(
            autoresp_cfg_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            autoresp_config = await response.parse()
            assert_matches_type(object, autoresp_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.messaging_profiles.autoresp_configs.with_raw_response.delete(
                autoresp_cfg_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                profile_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `autoresp_cfg_id` but received ''"):
            await async_client.messaging_profiles.autoresp_configs.with_raw_response.delete(
                autoresp_cfg_id="",
                profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
