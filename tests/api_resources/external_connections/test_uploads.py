# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.external_connections import (
    UploadListResponse,
    UploadRetryResponse,
    UploadCreateResponse,
    UploadRetrieveResponse,
    UploadPendingCountResponse,
    UploadRefreshStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUploads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        upload = client.external_connections.uploads.create(
            id="id",
            number_ids=["3920457616934164700", "3920457616934164701", "3920457616934164702", "3920457616934164703"],
        )
        assert_matches_type(UploadCreateResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        upload = client.external_connections.uploads.create(
            id="id",
            number_ids=["3920457616934164700", "3920457616934164701", "3920457616934164702", "3920457616934164703"],
            additional_usages=["calling_user_assignment"],
            civic_address_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            location_id="67ea7693-9cd5-4a68-8c76-abb3aa5bf5d2",
            usage="first_party_app_assignment",
        )
        assert_matches_type(UploadCreateResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.external_connections.uploads.with_raw_response.create(
            id="id",
            number_ids=["3920457616934164700", "3920457616934164701", "3920457616934164702", "3920457616934164703"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(UploadCreateResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.external_connections.uploads.with_streaming_response.create(
            id="id",
            number_ids=["3920457616934164700", "3920457616934164701", "3920457616934164702", "3920457616934164703"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(UploadCreateResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.external_connections.uploads.with_raw_response.create(
                id="",
                number_ids=["3920457616934164700", "3920457616934164701", "3920457616934164702", "3920457616934164703"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        upload = client.external_connections.uploads.retrieve(
            ticket_id="7b6a6449-b055-45a6-81f6-f6f0dffa4cc6",
            id="id",
        )
        assert_matches_type(UploadRetrieveResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.external_connections.uploads.with_raw_response.retrieve(
            ticket_id="7b6a6449-b055-45a6-81f6-f6f0dffa4cc6",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(UploadRetrieveResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.external_connections.uploads.with_streaming_response.retrieve(
            ticket_id="7b6a6449-b055-45a6-81f6-f6f0dffa4cc6",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(UploadRetrieveResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.external_connections.uploads.with_raw_response.retrieve(
                ticket_id="7b6a6449-b055-45a6-81f6-f6f0dffa4cc6",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticket_id` but received ''"):
            client.external_connections.uploads.with_raw_response.retrieve(
                ticket_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        upload = client.external_connections.uploads.list(
            id="id",
        )
        assert_matches_type(UploadListResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        upload = client.external_connections.uploads.list(
            id="id",
            filter={
                "civic_address_id": {"eq": "19990261512338516954"},
                "location_id": {"eq": "19995665508264022121"},
                "phone_number": {
                    "contains": "+1970",
                    "eq": "+19705555098",
                },
                "status": {"eq": ["pending_upload", "pending"]},
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(UploadListResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.external_connections.uploads.with_raw_response.list(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(UploadListResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.external_connections.uploads.with_streaming_response.list(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(UploadListResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.external_connections.uploads.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_pending_count(self, client: Telnyx) -> None:
        upload = client.external_connections.uploads.pending_count(
            "id",
        )
        assert_matches_type(UploadPendingCountResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_pending_count(self, client: Telnyx) -> None:
        response = client.external_connections.uploads.with_raw_response.pending_count(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(UploadPendingCountResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_pending_count(self, client: Telnyx) -> None:
        with client.external_connections.uploads.with_streaming_response.pending_count(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(UploadPendingCountResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_pending_count(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.external_connections.uploads.with_raw_response.pending_count(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_refresh_status(self, client: Telnyx) -> None:
        upload = client.external_connections.uploads.refresh_status(
            "id",
        )
        assert_matches_type(UploadRefreshStatusResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_refresh_status(self, client: Telnyx) -> None:
        response = client.external_connections.uploads.with_raw_response.refresh_status(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(UploadRefreshStatusResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_refresh_status(self, client: Telnyx) -> None:
        with client.external_connections.uploads.with_streaming_response.refresh_status(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(UploadRefreshStatusResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_refresh_status(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.external_connections.uploads.with_raw_response.refresh_status(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retry(self, client: Telnyx) -> None:
        upload = client.external_connections.uploads.retry(
            ticket_id="7b6a6449-b055-45a6-81f6-f6f0dffa4cc6",
            id="id",
        )
        assert_matches_type(UploadRetryResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retry(self, client: Telnyx) -> None:
        response = client.external_connections.uploads.with_raw_response.retry(
            ticket_id="7b6a6449-b055-45a6-81f6-f6f0dffa4cc6",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(UploadRetryResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retry(self, client: Telnyx) -> None:
        with client.external_connections.uploads.with_streaming_response.retry(
            ticket_id="7b6a6449-b055-45a6-81f6-f6f0dffa4cc6",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(UploadRetryResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retry(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.external_connections.uploads.with_raw_response.retry(
                ticket_id="7b6a6449-b055-45a6-81f6-f6f0dffa4cc6",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticket_id` but received ''"):
            client.external_connections.uploads.with_raw_response.retry(
                ticket_id="",
                id="id",
            )


class TestAsyncUploads:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        upload = await async_client.external_connections.uploads.create(
            id="id",
            number_ids=["3920457616934164700", "3920457616934164701", "3920457616934164702", "3920457616934164703"],
        )
        assert_matches_type(UploadCreateResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        upload = await async_client.external_connections.uploads.create(
            id="id",
            number_ids=["3920457616934164700", "3920457616934164701", "3920457616934164702", "3920457616934164703"],
            additional_usages=["calling_user_assignment"],
            civic_address_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            location_id="67ea7693-9cd5-4a68-8c76-abb3aa5bf5d2",
            usage="first_party_app_assignment",
        )
        assert_matches_type(UploadCreateResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.external_connections.uploads.with_raw_response.create(
            id="id",
            number_ids=["3920457616934164700", "3920457616934164701", "3920457616934164702", "3920457616934164703"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(UploadCreateResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.external_connections.uploads.with_streaming_response.create(
            id="id",
            number_ids=["3920457616934164700", "3920457616934164701", "3920457616934164702", "3920457616934164703"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(UploadCreateResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.external_connections.uploads.with_raw_response.create(
                id="",
                number_ids=["3920457616934164700", "3920457616934164701", "3920457616934164702", "3920457616934164703"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        upload = await async_client.external_connections.uploads.retrieve(
            ticket_id="7b6a6449-b055-45a6-81f6-f6f0dffa4cc6",
            id="id",
        )
        assert_matches_type(UploadRetrieveResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.external_connections.uploads.with_raw_response.retrieve(
            ticket_id="7b6a6449-b055-45a6-81f6-f6f0dffa4cc6",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(UploadRetrieveResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.external_connections.uploads.with_streaming_response.retrieve(
            ticket_id="7b6a6449-b055-45a6-81f6-f6f0dffa4cc6",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(UploadRetrieveResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.external_connections.uploads.with_raw_response.retrieve(
                ticket_id="7b6a6449-b055-45a6-81f6-f6f0dffa4cc6",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticket_id` but received ''"):
            await async_client.external_connections.uploads.with_raw_response.retrieve(
                ticket_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        upload = await async_client.external_connections.uploads.list(
            id="id",
        )
        assert_matches_type(UploadListResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        upload = await async_client.external_connections.uploads.list(
            id="id",
            filter={
                "civic_address_id": {"eq": "19990261512338516954"},
                "location_id": {"eq": "19995665508264022121"},
                "phone_number": {
                    "contains": "+1970",
                    "eq": "+19705555098",
                },
                "status": {"eq": ["pending_upload", "pending"]},
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(UploadListResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.external_connections.uploads.with_raw_response.list(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(UploadListResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.external_connections.uploads.with_streaming_response.list(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(UploadListResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.external_connections.uploads.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_pending_count(self, async_client: AsyncTelnyx) -> None:
        upload = await async_client.external_connections.uploads.pending_count(
            "id",
        )
        assert_matches_type(UploadPendingCountResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_pending_count(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.external_connections.uploads.with_raw_response.pending_count(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(UploadPendingCountResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_pending_count(self, async_client: AsyncTelnyx) -> None:
        async with async_client.external_connections.uploads.with_streaming_response.pending_count(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(UploadPendingCountResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_pending_count(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.external_connections.uploads.with_raw_response.pending_count(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_refresh_status(self, async_client: AsyncTelnyx) -> None:
        upload = await async_client.external_connections.uploads.refresh_status(
            "id",
        )
        assert_matches_type(UploadRefreshStatusResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_refresh_status(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.external_connections.uploads.with_raw_response.refresh_status(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(UploadRefreshStatusResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_refresh_status(self, async_client: AsyncTelnyx) -> None:
        async with async_client.external_connections.uploads.with_streaming_response.refresh_status(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(UploadRefreshStatusResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_refresh_status(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.external_connections.uploads.with_raw_response.refresh_status(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retry(self, async_client: AsyncTelnyx) -> None:
        upload = await async_client.external_connections.uploads.retry(
            ticket_id="7b6a6449-b055-45a6-81f6-f6f0dffa4cc6",
            id="id",
        )
        assert_matches_type(UploadRetryResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retry(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.external_connections.uploads.with_raw_response.retry(
            ticket_id="7b6a6449-b055-45a6-81f6-f6f0dffa4cc6",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(UploadRetryResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retry(self, async_client: AsyncTelnyx) -> None:
        async with async_client.external_connections.uploads.with_streaming_response.retry(
            ticket_id="7b6a6449-b055-45a6-81f6-f6f0dffa4cc6",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(UploadRetryResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retry(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.external_connections.uploads.with_raw_response.retry(
                ticket_id="7b6a6449-b055-45a6-81f6-f6f0dffa4cc6",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ticket_id` but received ''"):
            await async_client.external_connections.uploads.with_raw_response.retry(
                ticket_id="",
                id="id",
            )
