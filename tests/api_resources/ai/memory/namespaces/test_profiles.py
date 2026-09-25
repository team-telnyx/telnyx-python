# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from telnyx.types.ai.memory.namespaces import (
    ProfileListResponse,
    ProfileDeleteResponse,
    ProfileIngestResponse,
    ProfileRecallResponse,
    ProfileRememberResponse,
    ProfileRetrieveSummaryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProfiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        profile = client.ai.memory.namespaces.profiles.list(
            namespace="namespace",
        )
        assert_matches_type(SyncDefaultFlatPagination[ProfileListResponse], profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        profile = client.ai.memory.namespaces.profiles.list(
            namespace="namespace",
            page_number=1,
            page_size=1,
        )
        assert_matches_type(SyncDefaultFlatPagination[ProfileListResponse], profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.ai.memory.namespaces.profiles.with_raw_response.list(
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[ProfileListResponse], profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.ai.memory.namespaces.profiles.with_streaming_response.list(
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[ProfileListResponse], profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.ai.memory.namespaces.profiles.with_raw_response.list(
                namespace="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        profile = client.ai.memory.namespaces.profiles.delete(
            profile_id="profile_id",
            namespace="namespace",
        )
        assert_matches_type(ProfileDeleteResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.ai.memory.namespaces.profiles.with_raw_response.delete(
            profile_id="profile_id",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileDeleteResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.ai.memory.namespaces.profiles.with_streaming_response.delete(
            profile_id="profile_id",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileDeleteResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.ai.memory.namespaces.profiles.with_raw_response.delete(
                profile_id="profile_id",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.ai.memory.namespaces.profiles.with_raw_response.delete(
                profile_id="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_ingest_overload_1(self, client: Telnyx) -> None:
        profile = client.ai.memory.namespaces.profiles.ingest(
            profile_id="profile_id",
            namespace="namespace",
            body={"foo": "bar"},
        )
        assert_matches_type(ProfileIngestResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_ingest_with_all_params_overload_1(self, client: Telnyx) -> None:
        profile = client.ai.memory.namespaces.profiles.ingest(
            profile_id="profile_id",
            namespace="namespace",
            body={"foo": "bar"},
            session_id="session_id",
        )
        assert_matches_type(ProfileIngestResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_ingest_overload_1(self, client: Telnyx) -> None:
        response = client.ai.memory.namespaces.profiles.with_raw_response.ingest(
            profile_id="profile_id",
            namespace="namespace",
            body={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileIngestResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_ingest_overload_1(self, client: Telnyx) -> None:
        with client.ai.memory.namespaces.profiles.with_streaming_response.ingest(
            profile_id="profile_id",
            namespace="namespace",
            body={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileIngestResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_ingest_overload_1(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.ai.memory.namespaces.profiles.with_raw_response.ingest(
                profile_id="profile_id",
                namespace="",
                body={"foo": "bar"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.ai.memory.namespaces.profiles.with_raw_response.ingest(
                profile_id="",
                namespace="namespace",
                body={"foo": "bar"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_ingest_overload_2(self, client: Telnyx) -> None:
        profile = client.ai.memory.namespaces.profiles.ingest(
            profile_id="profile_id",
            namespace="namespace",
            body=[{}],
        )
        assert_matches_type(ProfileIngestResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_ingest_with_all_params_overload_2(self, client: Telnyx) -> None:
        profile = client.ai.memory.namespaces.profiles.ingest(
            profile_id="profile_id",
            namespace="namespace",
            body=[{}],
            session_id="session_id",
        )
        assert_matches_type(ProfileIngestResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_ingest_overload_2(self, client: Telnyx) -> None:
        response = client.ai.memory.namespaces.profiles.with_raw_response.ingest(
            profile_id="profile_id",
            namespace="namespace",
            body=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileIngestResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_ingest_overload_2(self, client: Telnyx) -> None:
        with client.ai.memory.namespaces.profiles.with_streaming_response.ingest(
            profile_id="profile_id",
            namespace="namespace",
            body=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileIngestResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_ingest_overload_2(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.ai.memory.namespaces.profiles.with_raw_response.ingest(
                profile_id="profile_id",
                namespace="",
                body=[{}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.ai.memory.namespaces.profiles.with_raw_response.ingest(
                profile_id="",
                namespace="namespace",
                body=[{}],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_recall(self, client: Telnyx) -> None:
        profile = client.ai.memory.namespaces.profiles.recall(
            profile_id="profile_id",
            namespace="namespace",
            query="where do invoices go?",
        )
        assert_matches_type(ProfileRecallResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_recall_with_all_params(self, client: Telnyx) -> None:
        profile = client.ai.memory.namespaces.profiles.recall(
            profile_id="profile_id",
            namespace="namespace",
            query="where do invoices go?",
            top_k=5,
        )
        assert_matches_type(ProfileRecallResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_recall(self, client: Telnyx) -> None:
        response = client.ai.memory.namespaces.profiles.with_raw_response.recall(
            profile_id="profile_id",
            namespace="namespace",
            query="where do invoices go?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileRecallResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_recall(self, client: Telnyx) -> None:
        with client.ai.memory.namespaces.profiles.with_streaming_response.recall(
            profile_id="profile_id",
            namespace="namespace",
            query="where do invoices go?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileRecallResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_recall(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.ai.memory.namespaces.profiles.with_raw_response.recall(
                profile_id="profile_id",
                namespace="",
                query="where do invoices go?",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.ai.memory.namespaces.profiles.with_raw_response.recall(
                profile_id="",
                namespace="namespace",
                query="where do invoices go?",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remember(self, client: Telnyx) -> None:
        profile = client.ai.memory.namespaces.profiles.remember(
            profile_id="profile_id",
            namespace="namespace",
            text="Prefers window seats and flies out of ORD",
        )
        assert_matches_type(ProfileRememberResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remember(self, client: Telnyx) -> None:
        response = client.ai.memory.namespaces.profiles.with_raw_response.remember(
            profile_id="profile_id",
            namespace="namespace",
            text="Prefers window seats and flies out of ORD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileRememberResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remember(self, client: Telnyx) -> None:
        with client.ai.memory.namespaces.profiles.with_streaming_response.remember(
            profile_id="profile_id",
            namespace="namespace",
            text="Prefers window seats and flies out of ORD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileRememberResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remember(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.ai.memory.namespaces.profiles.with_raw_response.remember(
                profile_id="profile_id",
                namespace="",
                text="Prefers window seats and flies out of ORD",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.ai.memory.namespaces.profiles.with_raw_response.remember(
                profile_id="",
                namespace="namespace",
                text="Prefers window seats and flies out of ORD",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_summary(self, client: Telnyx) -> None:
        profile = client.ai.memory.namespaces.profiles.retrieve_summary(
            profile_id="profile_id",
            namespace="namespace",
        )
        assert_matches_type(ProfileRetrieveSummaryResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_summary(self, client: Telnyx) -> None:
        response = client.ai.memory.namespaces.profiles.with_raw_response.retrieve_summary(
            profile_id="profile_id",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileRetrieveSummaryResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_summary(self, client: Telnyx) -> None:
        with client.ai.memory.namespaces.profiles.with_streaming_response.retrieve_summary(
            profile_id="profile_id",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileRetrieveSummaryResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_summary(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            client.ai.memory.namespaces.profiles.with_raw_response.retrieve_summary(
                profile_id="profile_id",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.ai.memory.namespaces.profiles.with_raw_response.retrieve_summary(
                profile_id="",
                namespace="namespace",
            )


class TestAsyncProfiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        profile = await async_client.ai.memory.namespaces.profiles.list(
            namespace="namespace",
        )
        assert_matches_type(AsyncDefaultFlatPagination[ProfileListResponse], profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        profile = await async_client.ai.memory.namespaces.profiles.list(
            namespace="namespace",
            page_number=1,
            page_size=1,
        )
        assert_matches_type(AsyncDefaultFlatPagination[ProfileListResponse], profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.memory.namespaces.profiles.with_raw_response.list(
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[ProfileListResponse], profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.memory.namespaces.profiles.with_streaming_response.list(
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[ProfileListResponse], profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.ai.memory.namespaces.profiles.with_raw_response.list(
                namespace="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        profile = await async_client.ai.memory.namespaces.profiles.delete(
            profile_id="profile_id",
            namespace="namespace",
        )
        assert_matches_type(ProfileDeleteResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.memory.namespaces.profiles.with_raw_response.delete(
            profile_id="profile_id",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileDeleteResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.memory.namespaces.profiles.with_streaming_response.delete(
            profile_id="profile_id",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileDeleteResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.ai.memory.namespaces.profiles.with_raw_response.delete(
                profile_id="profile_id",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.ai.memory.namespaces.profiles.with_raw_response.delete(
                profile_id="",
                namespace="namespace",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_ingest_overload_1(self, async_client: AsyncTelnyx) -> None:
        profile = await async_client.ai.memory.namespaces.profiles.ingest(
            profile_id="profile_id",
            namespace="namespace",
            body={"foo": "bar"},
        )
        assert_matches_type(ProfileIngestResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_ingest_with_all_params_overload_1(self, async_client: AsyncTelnyx) -> None:
        profile = await async_client.ai.memory.namespaces.profiles.ingest(
            profile_id="profile_id",
            namespace="namespace",
            body={"foo": "bar"},
            session_id="session_id",
        )
        assert_matches_type(ProfileIngestResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_ingest_overload_1(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.memory.namespaces.profiles.with_raw_response.ingest(
            profile_id="profile_id",
            namespace="namespace",
            body={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileIngestResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_ingest_overload_1(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.memory.namespaces.profiles.with_streaming_response.ingest(
            profile_id="profile_id",
            namespace="namespace",
            body={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileIngestResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_ingest_overload_1(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.ai.memory.namespaces.profiles.with_raw_response.ingest(
                profile_id="profile_id",
                namespace="",
                body={"foo": "bar"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.ai.memory.namespaces.profiles.with_raw_response.ingest(
                profile_id="",
                namespace="namespace",
                body={"foo": "bar"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_ingest_overload_2(self, async_client: AsyncTelnyx) -> None:
        profile = await async_client.ai.memory.namespaces.profiles.ingest(
            profile_id="profile_id",
            namespace="namespace",
            body=[{}],
        )
        assert_matches_type(ProfileIngestResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_ingest_with_all_params_overload_2(self, async_client: AsyncTelnyx) -> None:
        profile = await async_client.ai.memory.namespaces.profiles.ingest(
            profile_id="profile_id",
            namespace="namespace",
            body=[{}],
            session_id="session_id",
        )
        assert_matches_type(ProfileIngestResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_ingest_overload_2(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.memory.namespaces.profiles.with_raw_response.ingest(
            profile_id="profile_id",
            namespace="namespace",
            body=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileIngestResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_ingest_overload_2(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.memory.namespaces.profiles.with_streaming_response.ingest(
            profile_id="profile_id",
            namespace="namespace",
            body=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileIngestResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_ingest_overload_2(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.ai.memory.namespaces.profiles.with_raw_response.ingest(
                profile_id="profile_id",
                namespace="",
                body=[{}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.ai.memory.namespaces.profiles.with_raw_response.ingest(
                profile_id="",
                namespace="namespace",
                body=[{}],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_recall(self, async_client: AsyncTelnyx) -> None:
        profile = await async_client.ai.memory.namespaces.profiles.recall(
            profile_id="profile_id",
            namespace="namespace",
            query="where do invoices go?",
        )
        assert_matches_type(ProfileRecallResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_recall_with_all_params(self, async_client: AsyncTelnyx) -> None:
        profile = await async_client.ai.memory.namespaces.profiles.recall(
            profile_id="profile_id",
            namespace="namespace",
            query="where do invoices go?",
            top_k=5,
        )
        assert_matches_type(ProfileRecallResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_recall(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.memory.namespaces.profiles.with_raw_response.recall(
            profile_id="profile_id",
            namespace="namespace",
            query="where do invoices go?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileRecallResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_recall(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.memory.namespaces.profiles.with_streaming_response.recall(
            profile_id="profile_id",
            namespace="namespace",
            query="where do invoices go?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileRecallResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_recall(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.ai.memory.namespaces.profiles.with_raw_response.recall(
                profile_id="profile_id",
                namespace="",
                query="where do invoices go?",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.ai.memory.namespaces.profiles.with_raw_response.recall(
                profile_id="",
                namespace="namespace",
                query="where do invoices go?",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remember(self, async_client: AsyncTelnyx) -> None:
        profile = await async_client.ai.memory.namespaces.profiles.remember(
            profile_id="profile_id",
            namespace="namespace",
            text="Prefers window seats and flies out of ORD",
        )
        assert_matches_type(ProfileRememberResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remember(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.memory.namespaces.profiles.with_raw_response.remember(
            profile_id="profile_id",
            namespace="namespace",
            text="Prefers window seats and flies out of ORD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileRememberResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remember(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.memory.namespaces.profiles.with_streaming_response.remember(
            profile_id="profile_id",
            namespace="namespace",
            text="Prefers window seats and flies out of ORD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileRememberResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remember(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.ai.memory.namespaces.profiles.with_raw_response.remember(
                profile_id="profile_id",
                namespace="",
                text="Prefers window seats and flies out of ORD",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.ai.memory.namespaces.profiles.with_raw_response.remember(
                profile_id="",
                namespace="namespace",
                text="Prefers window seats and flies out of ORD",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_summary(self, async_client: AsyncTelnyx) -> None:
        profile = await async_client.ai.memory.namespaces.profiles.retrieve_summary(
            profile_id="profile_id",
            namespace="namespace",
        )
        assert_matches_type(ProfileRetrieveSummaryResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_summary(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.ai.memory.namespaces.profiles.with_raw_response.retrieve_summary(
            profile_id="profile_id",
            namespace="namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileRetrieveSummaryResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_summary(self, async_client: AsyncTelnyx) -> None:
        async with async_client.ai.memory.namespaces.profiles.with_streaming_response.retrieve_summary(
            profile_id="profile_id",
            namespace="namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileRetrieveSummaryResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_summary(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace` but received ''"):
            await async_client.ai.memory.namespaces.profiles.with_raw_response.retrieve_summary(
                profile_id="profile_id",
                namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.ai.memory.namespaces.profiles.with_raw_response.retrieve_summary(
                profile_id="",
                namespace="namespace",
            )
