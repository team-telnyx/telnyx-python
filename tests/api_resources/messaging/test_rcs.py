# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.messaging import (
    RcInviteTestNumberResponse,
    RcListBulkCapabilitiesResponse,
    RcRetrieveCapabilitiesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRcs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_invite_test_number(self, client: Telnyx) -> None:
        rc = client.messaging.rcs.invite_test_number(
            phone_number="phone_number",
            id="id",
        )
        assert_matches_type(RcInviteTestNumberResponse, rc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_invite_test_number(self, client: Telnyx) -> None:
        response = client.messaging.rcs.with_raw_response.invite_test_number(
            phone_number="phone_number",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rc = response.parse()
        assert_matches_type(RcInviteTestNumberResponse, rc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_invite_test_number(self, client: Telnyx) -> None:
        with client.messaging.rcs.with_streaming_response.invite_test_number(
            phone_number="phone_number",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rc = response.parse()
            assert_matches_type(RcInviteTestNumberResponse, rc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_invite_test_number(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.messaging.rcs.with_raw_response.invite_test_number(
                phone_number="phone_number",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.messaging.rcs.with_raw_response.invite_test_number(
                phone_number="",
                id="id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_bulk_capabilities(self, client: Telnyx) -> None:
        rc = client.messaging.rcs.list_bulk_capabilities(
            agent_id="TestAgent",
            phone_numbers=["+13125551234"],
        )
        assert_matches_type(RcListBulkCapabilitiesResponse, rc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_bulk_capabilities(self, client: Telnyx) -> None:
        response = client.messaging.rcs.with_raw_response.list_bulk_capabilities(
            agent_id="TestAgent",
            phone_numbers=["+13125551234"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rc = response.parse()
        assert_matches_type(RcListBulkCapabilitiesResponse, rc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_bulk_capabilities(self, client: Telnyx) -> None:
        with client.messaging.rcs.with_streaming_response.list_bulk_capabilities(
            agent_id="TestAgent",
            phone_numbers=["+13125551234"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rc = response.parse()
            assert_matches_type(RcListBulkCapabilitiesResponse, rc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_capabilities(self, client: Telnyx) -> None:
        rc = client.messaging.rcs.retrieve_capabilities(
            phone_number="phone_number",
            agent_id="agent_id",
        )
        assert_matches_type(RcRetrieveCapabilitiesResponse, rc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_capabilities(self, client: Telnyx) -> None:
        response = client.messaging.rcs.with_raw_response.retrieve_capabilities(
            phone_number="phone_number",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rc = response.parse()
        assert_matches_type(RcRetrieveCapabilitiesResponse, rc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_capabilities(self, client: Telnyx) -> None:
        with client.messaging.rcs.with_streaming_response.retrieve_capabilities(
            phone_number="phone_number",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rc = response.parse()
            assert_matches_type(RcRetrieveCapabilitiesResponse, rc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_capabilities(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.messaging.rcs.with_raw_response.retrieve_capabilities(
                phone_number="phone_number",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.messaging.rcs.with_raw_response.retrieve_capabilities(
                phone_number="",
                agent_id="agent_id",
            )


class TestAsyncRcs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_invite_test_number(self, async_client: AsyncTelnyx) -> None:
        rc = await async_client.messaging.rcs.invite_test_number(
            phone_number="phone_number",
            id="id",
        )
        assert_matches_type(RcInviteTestNumberResponse, rc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_invite_test_number(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging.rcs.with_raw_response.invite_test_number(
            phone_number="phone_number",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rc = await response.parse()
        assert_matches_type(RcInviteTestNumberResponse, rc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_invite_test_number(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging.rcs.with_streaming_response.invite_test_number(
            phone_number="phone_number",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rc = await response.parse()
            assert_matches_type(RcInviteTestNumberResponse, rc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_invite_test_number(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.messaging.rcs.with_raw_response.invite_test_number(
                phone_number="phone_number",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.messaging.rcs.with_raw_response.invite_test_number(
                phone_number="",
                id="id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_bulk_capabilities(self, async_client: AsyncTelnyx) -> None:
        rc = await async_client.messaging.rcs.list_bulk_capabilities(
            agent_id="TestAgent",
            phone_numbers=["+13125551234"],
        )
        assert_matches_type(RcListBulkCapabilitiesResponse, rc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_bulk_capabilities(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging.rcs.with_raw_response.list_bulk_capabilities(
            agent_id="TestAgent",
            phone_numbers=["+13125551234"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rc = await response.parse()
        assert_matches_type(RcListBulkCapabilitiesResponse, rc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_bulk_capabilities(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging.rcs.with_streaming_response.list_bulk_capabilities(
            agent_id="TestAgent",
            phone_numbers=["+13125551234"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rc = await response.parse()
            assert_matches_type(RcListBulkCapabilitiesResponse, rc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_capabilities(self, async_client: AsyncTelnyx) -> None:
        rc = await async_client.messaging.rcs.retrieve_capabilities(
            phone_number="phone_number",
            agent_id="agent_id",
        )
        assert_matches_type(RcRetrieveCapabilitiesResponse, rc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_capabilities(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging.rcs.with_raw_response.retrieve_capabilities(
            phone_number="phone_number",
            agent_id="agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rc = await response.parse()
        assert_matches_type(RcRetrieveCapabilitiesResponse, rc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_capabilities(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging.rcs.with_streaming_response.retrieve_capabilities(
            phone_number="phone_number",
            agent_id="agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rc = await response.parse()
            assert_matches_type(RcRetrieveCapabilitiesResponse, rc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_capabilities(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.messaging.rcs.with_raw_response.retrieve_capabilities(
                phone_number="phone_number",
                agent_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.messaging.rcs.with_raw_response.retrieve_capabilities(
                phone_number="",
                agent_id="agent_id",
            )
