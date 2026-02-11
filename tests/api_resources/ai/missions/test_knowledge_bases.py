# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKnowledgeBases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_knowledge_base(self, client: Telnyx) -> None:
        knowledge_base = client.ai.missions.knowledge_bases.create_knowledge_base(
            "mission_id",
        )
        assert_matches_type(object, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_knowledge_base(self, client: Telnyx) -> None:
        response = client.ai.missions.knowledge_bases.with_raw_response.create_knowledge_base(
            "mission_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(object, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_knowledge_base(self, client: Telnyx) -> None:
        with client.ai.missions.knowledge_bases.with_streaming_response.create_knowledge_base(
            "mission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(object, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_knowledge_base(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.knowledge_bases.with_raw_response.create_knowledge_base(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_knowledge_base(self, client: Telnyx) -> None:
        knowledge_base = client.ai.missions.knowledge_bases.delete_knowledge_base(
            knowledge_base_id="knowledge_base_id",
            mission_id="mission_id",
        )
        assert knowledge_base is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_knowledge_base(self, client: Telnyx) -> None:
        response = client.ai.missions.knowledge_bases.with_raw_response.delete_knowledge_base(
            knowledge_base_id="knowledge_base_id",
            mission_id="mission_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert knowledge_base is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_knowledge_base(self, client: Telnyx) -> None:
        with client.ai.missions.knowledge_bases.with_streaming_response.delete_knowledge_base(
            knowledge_base_id="knowledge_base_id",
            mission_id="mission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert knowledge_base is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_knowledge_base(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.knowledge_bases.with_raw_response.delete_knowledge_base(
                knowledge_base_id="knowledge_base_id",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_id` but received ''"):
            client.ai.missions.knowledge_bases.with_raw_response.delete_knowledge_base(
                knowledge_base_id="",
                mission_id="mission_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_knowledge_base(self, client: Telnyx) -> None:
        knowledge_base = client.ai.missions.knowledge_bases.get_knowledge_base(
            knowledge_base_id="knowledge_base_id",
            mission_id="mission_id",
        )
        assert_matches_type(object, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_knowledge_base(self, client: Telnyx) -> None:
        response = client.ai.missions.knowledge_bases.with_raw_response.get_knowledge_base(
            knowledge_base_id="knowledge_base_id",
            mission_id="mission_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(object, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_knowledge_base(self, client: Telnyx) -> None:
        with client.ai.missions.knowledge_bases.with_streaming_response.get_knowledge_base(
            knowledge_base_id="knowledge_base_id",
            mission_id="mission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(object, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_knowledge_base(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.knowledge_bases.with_raw_response.get_knowledge_base(
                knowledge_base_id="knowledge_base_id",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_id` but received ''"):
            client.ai.missions.knowledge_bases.with_raw_response.get_knowledge_base(
                knowledge_base_id="",
                mission_id="mission_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_knowledge_bases(self, client: Telnyx) -> None:
        knowledge_base = client.ai.missions.knowledge_bases.list_knowledge_bases(
            "mission_id",
        )
        assert_matches_type(object, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_knowledge_bases(self, client: Telnyx) -> None:
        response = client.ai.missions.knowledge_bases.with_raw_response.list_knowledge_bases(
            "mission_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(object, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_knowledge_bases(self, client: Telnyx) -> None:
        with client.ai.missions.knowledge_bases.with_streaming_response.list_knowledge_bases(
            "mission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(object, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_knowledge_bases(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.knowledge_bases.with_raw_response.list_knowledge_bases(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_knowledge_base(self, client: Telnyx) -> None:
        knowledge_base = client.ai.missions.knowledge_bases.update_knowledge_base(
            knowledge_base_id="knowledge_base_id",
            mission_id="mission_id",
        )
        assert_matches_type(object, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_knowledge_base(self, client: Telnyx) -> None:
        response = client.ai.missions.knowledge_bases.with_raw_response.update_knowledge_base(
            knowledge_base_id="knowledge_base_id",
            mission_id="mission_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(object, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_knowledge_base(self, client: Telnyx) -> None:
        with client.ai.missions.knowledge_bases.with_streaming_response.update_knowledge_base(
            knowledge_base_id="knowledge_base_id",
            mission_id="mission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(object, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_knowledge_base(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            client.ai.missions.knowledge_bases.with_raw_response.update_knowledge_base(
                knowledge_base_id="knowledge_base_id",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_id` but received ''"):
            client.ai.missions.knowledge_bases.with_raw_response.update_knowledge_base(
                knowledge_base_id="",
                mission_id="mission_id",
            )


class TestAsyncKnowledgeBases:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_knowledge_base(self, async_client: AsyncTelnyx) -> None:
        knowledge_base = await async_client.ai.missions.knowledge_bases.create_knowledge_base(
            "mission_id",
        )
        assert_matches_type(object, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_knowledge_base(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.knowledge_bases.with_raw_response.create_knowledge_base(
            "mission_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(object, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_knowledge_base(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.knowledge_bases.with_streaming_response.create_knowledge_base(
            "mission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(object, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_knowledge_base(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.knowledge_bases.with_raw_response.create_knowledge_base(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_knowledge_base(self, async_client: AsyncTelnyx) -> None:
        knowledge_base = await async_client.ai.missions.knowledge_bases.delete_knowledge_base(
            knowledge_base_id="knowledge_base_id",
            mission_id="mission_id",
        )
        assert knowledge_base is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_knowledge_base(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.knowledge_bases.with_raw_response.delete_knowledge_base(
            knowledge_base_id="knowledge_base_id",
            mission_id="mission_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert knowledge_base is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_knowledge_base(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.knowledge_bases.with_streaming_response.delete_knowledge_base(
            knowledge_base_id="knowledge_base_id",
            mission_id="mission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert knowledge_base is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_knowledge_base(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.knowledge_bases.with_raw_response.delete_knowledge_base(
                knowledge_base_id="knowledge_base_id",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_id` but received ''"):
            await async_client.ai.missions.knowledge_bases.with_raw_response.delete_knowledge_base(
                knowledge_base_id="",
                mission_id="mission_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_knowledge_base(self, async_client: AsyncTelnyx) -> None:
        knowledge_base = await async_client.ai.missions.knowledge_bases.get_knowledge_base(
            knowledge_base_id="knowledge_base_id",
            mission_id="mission_id",
        )
        assert_matches_type(object, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_knowledge_base(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.knowledge_bases.with_raw_response.get_knowledge_base(
            knowledge_base_id="knowledge_base_id",
            mission_id="mission_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(object, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_knowledge_base(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.knowledge_bases.with_streaming_response.get_knowledge_base(
            knowledge_base_id="knowledge_base_id",
            mission_id="mission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(object, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_knowledge_base(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.knowledge_bases.with_raw_response.get_knowledge_base(
                knowledge_base_id="knowledge_base_id",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_id` but received ''"):
            await async_client.ai.missions.knowledge_bases.with_raw_response.get_knowledge_base(
                knowledge_base_id="",
                mission_id="mission_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_knowledge_bases(self, async_client: AsyncTelnyx) -> None:
        knowledge_base = await async_client.ai.missions.knowledge_bases.list_knowledge_bases(
            "mission_id",
        )
        assert_matches_type(object, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_knowledge_bases(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.knowledge_bases.with_raw_response.list_knowledge_bases(
            "mission_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(object, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_knowledge_bases(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.knowledge_bases.with_streaming_response.list_knowledge_bases(
            "mission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(object, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_knowledge_bases(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.knowledge_bases.with_raw_response.list_knowledge_bases(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_knowledge_base(self, async_client: AsyncTelnyx) -> None:
        knowledge_base = await async_client.ai.missions.knowledge_bases.update_knowledge_base(
            knowledge_base_id="knowledge_base_id",
            mission_id="mission_id",
        )
        assert_matches_type(object, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_knowledge_base(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.missions.knowledge_bases.with_raw_response.update_knowledge_base(
            knowledge_base_id="knowledge_base_id",
            mission_id="mission_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(object, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_knowledge_base(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.missions.knowledge_bases.with_streaming_response.update_knowledge_base(
            knowledge_base_id="knowledge_base_id",
            mission_id="mission_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(object, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_knowledge_base(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mission_id` but received ''"):
            await async_client.ai.missions.knowledge_bases.with_raw_response.update_knowledge_base(
                knowledge_base_id="knowledge_base_id",
                mission_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_id` but received ''"):
            await async_client.ai.missions.knowledge_bases.with_raw_response.update_knowledge_base(
                knowledge_base_id="",
                mission_id="mission_id",
            )
