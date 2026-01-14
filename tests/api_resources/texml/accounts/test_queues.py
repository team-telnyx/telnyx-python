# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.pagination import SyncDefaultPaginationForQueues, AsyncDefaultPaginationForQueues
from telnyx.types.texml.accounts import (
    QueueListResponse,
    QueueCreateResponse,
    QueueUpdateResponse,
    QueueRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQueues:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        queue = client.texml.accounts.queues.create(
            account_sid="account_sid",
        )
        assert_matches_type(QueueCreateResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        queue = client.texml.accounts.queues.create(
            account_sid="account_sid",
            friendly_name="Support Queue",
            max_size=10,
        )
        assert_matches_type(QueueCreateResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.texml.accounts.queues.with_raw_response.create(
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        queue = response.parse()
        assert_matches_type(QueueCreateResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.texml.accounts.queues.with_streaming_response.create(
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            queue = response.parse()
            assert_matches_type(QueueCreateResponse, queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            client.texml.accounts.queues.with_raw_response.create(
                account_sid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        queue = client.texml.accounts.queues.retrieve(
            queue_sid="queue_sid",
            account_sid="account_sid",
        )
        assert_matches_type(QueueRetrieveResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.texml.accounts.queues.with_raw_response.retrieve(
            queue_sid="queue_sid",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        queue = response.parse()
        assert_matches_type(QueueRetrieveResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.texml.accounts.queues.with_streaming_response.retrieve(
            queue_sid="queue_sid",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            queue = response.parse()
            assert_matches_type(QueueRetrieveResponse, queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            client.texml.accounts.queues.with_raw_response.retrieve(
                queue_sid="queue_sid",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_sid` but received ''"):
            client.texml.accounts.queues.with_raw_response.retrieve(
                queue_sid="",
                account_sid="account_sid",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        queue = client.texml.accounts.queues.update(
            queue_sid="queue_sid",
            account_sid="account_sid",
        )
        assert_matches_type(QueueUpdateResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        queue = client.texml.accounts.queues.update(
            queue_sid="queue_sid",
            account_sid="account_sid",
            max_size=10,
        )
        assert_matches_type(QueueUpdateResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.texml.accounts.queues.with_raw_response.update(
            queue_sid="queue_sid",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        queue = response.parse()
        assert_matches_type(QueueUpdateResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.texml.accounts.queues.with_streaming_response.update(
            queue_sid="queue_sid",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            queue = response.parse()
            assert_matches_type(QueueUpdateResponse, queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            client.texml.accounts.queues.with_raw_response.update(
                queue_sid="queue_sid",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_sid` but received ''"):
            client.texml.accounts.queues.with_raw_response.update(
                queue_sid="",
                account_sid="account_sid",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        queue = client.texml.accounts.queues.list(
            account_sid="account_sid",
        )
        assert_matches_type(SyncDefaultPaginationForQueues[QueueListResponse], queue, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        queue = client.texml.accounts.queues.list(
            account_sid="account_sid",
            date_created="DateCreated",
            date_updated="DateUpdated",
            page=0,
            page_size=0,
            page_token="PageToken",
        )
        assert_matches_type(SyncDefaultPaginationForQueues[QueueListResponse], queue, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.texml.accounts.queues.with_raw_response.list(
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        queue = response.parse()
        assert_matches_type(SyncDefaultPaginationForQueues[QueueListResponse], queue, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.texml.accounts.queues.with_streaming_response.list(
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            queue = response.parse()
            assert_matches_type(SyncDefaultPaginationForQueues[QueueListResponse], queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            client.texml.accounts.queues.with_raw_response.list(
                account_sid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        queue = client.texml.accounts.queues.delete(
            queue_sid="queue_sid",
            account_sid="account_sid",
        )
        assert queue is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.texml.accounts.queues.with_raw_response.delete(
            queue_sid="queue_sid",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        queue = response.parse()
        assert queue is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.texml.accounts.queues.with_streaming_response.delete(
            queue_sid="queue_sid",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            queue = response.parse()
            assert queue is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            client.texml.accounts.queues.with_raw_response.delete(
                queue_sid="queue_sid",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_sid` but received ''"):
            client.texml.accounts.queues.with_raw_response.delete(
                queue_sid="",
                account_sid="account_sid",
            )


class TestAsyncQueues:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        queue = await async_client.texml.accounts.queues.create(
            account_sid="account_sid",
        )
        assert_matches_type(QueueCreateResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        queue = await async_client.texml.accounts.queues.create(
            account_sid="account_sid",
            friendly_name="Support Queue",
            max_size=10,
        )
        assert_matches_type(QueueCreateResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.accounts.queues.with_raw_response.create(
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        queue = await response.parse()
        assert_matches_type(QueueCreateResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.accounts.queues.with_streaming_response.create(
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            queue = await response.parse()
            assert_matches_type(QueueCreateResponse, queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            await async_client.texml.accounts.queues.with_raw_response.create(
                account_sid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        queue = await async_client.texml.accounts.queues.retrieve(
            queue_sid="queue_sid",
            account_sid="account_sid",
        )
        assert_matches_type(QueueRetrieveResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.accounts.queues.with_raw_response.retrieve(
            queue_sid="queue_sid",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        queue = await response.parse()
        assert_matches_type(QueueRetrieveResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.accounts.queues.with_streaming_response.retrieve(
            queue_sid="queue_sid",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            queue = await response.parse()
            assert_matches_type(QueueRetrieveResponse, queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            await async_client.texml.accounts.queues.with_raw_response.retrieve(
                queue_sid="queue_sid",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_sid` but received ''"):
            await async_client.texml.accounts.queues.with_raw_response.retrieve(
                queue_sid="",
                account_sid="account_sid",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        queue = await async_client.texml.accounts.queues.update(
            queue_sid="queue_sid",
            account_sid="account_sid",
        )
        assert_matches_type(QueueUpdateResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        queue = await async_client.texml.accounts.queues.update(
            queue_sid="queue_sid",
            account_sid="account_sid",
            max_size=10,
        )
        assert_matches_type(QueueUpdateResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.accounts.queues.with_raw_response.update(
            queue_sid="queue_sid",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        queue = await response.parse()
        assert_matches_type(QueueUpdateResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.accounts.queues.with_streaming_response.update(
            queue_sid="queue_sid",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            queue = await response.parse()
            assert_matches_type(QueueUpdateResponse, queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            await async_client.texml.accounts.queues.with_raw_response.update(
                queue_sid="queue_sid",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_sid` but received ''"):
            await async_client.texml.accounts.queues.with_raw_response.update(
                queue_sid="",
                account_sid="account_sid",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        queue = await async_client.texml.accounts.queues.list(
            account_sid="account_sid",
        )
        assert_matches_type(AsyncDefaultPaginationForQueues[QueueListResponse], queue, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        queue = await async_client.texml.accounts.queues.list(
            account_sid="account_sid",
            date_created="DateCreated",
            date_updated="DateUpdated",
            page=0,
            page_size=0,
            page_token="PageToken",
        )
        assert_matches_type(AsyncDefaultPaginationForQueues[QueueListResponse], queue, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.accounts.queues.with_raw_response.list(
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        queue = await response.parse()
        assert_matches_type(AsyncDefaultPaginationForQueues[QueueListResponse], queue, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.accounts.queues.with_streaming_response.list(
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            queue = await response.parse()
            assert_matches_type(AsyncDefaultPaginationForQueues[QueueListResponse], queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            await async_client.texml.accounts.queues.with_raw_response.list(
                account_sid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        queue = await async_client.texml.accounts.queues.delete(
            queue_sid="queue_sid",
            account_sid="account_sid",
        )
        assert queue is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.accounts.queues.with_raw_response.delete(
            queue_sid="queue_sid",
            account_sid="account_sid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        queue = await response.parse()
        assert queue is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.accounts.queues.with_streaming_response.delete(
            queue_sid="queue_sid",
            account_sid="account_sid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            queue = await response.parse()
            assert queue is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_sid` but received ''"):
            await async_client.texml.accounts.queues.with_raw_response.delete(
                queue_sid="queue_sid",
                account_sid="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_sid` but received ''"):
            await async_client.texml.accounts.queues.with_raw_response.delete(
                queue_sid="",
                account_sid="account_sid",
            )
