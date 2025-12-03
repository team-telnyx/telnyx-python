# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    PortoutListResponse,
    PortoutRetrieveResponse,
    PortoutUpdateStatusResponse,
    PortoutListRejectionCodesResponse,
)
from telnyx._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPortouts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        portout = client.portouts.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PortoutRetrieveResponse, portout, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.portouts.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portout = response.parse()
        assert_matches_type(PortoutRetrieveResponse, portout, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.portouts.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portout = response.parse()
            assert_matches_type(PortoutRetrieveResponse, portout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.portouts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        portout = client.portouts.list()
        assert_matches_type(PortoutListResponse, portout, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        portout = client.portouts.list(
            filter={
                "carrier_name": "carrier_name",
                "country_code": "US",
                "country_code_in": ["CA", "US"],
                "foc_date": parse_datetime("2024-09-04T00:00:00.000Z"),
                "inserted_at": {
                    "gte": parse_datetime("2024-09-04T00:00:00.000Z"),
                    "lte": parse_datetime("2024-09-04T00:00:00.000Z"),
                },
                "phone_number": "+13035551212",
                "pon": "pon",
                "ported_out_at": {
                    "gte": parse_datetime("2024-09-04T00:00:00.000Z"),
                    "lte": parse_datetime("2024-09-04T00:00:00.000Z"),
                },
                "spid": "spid",
                "status": "pending",
                "status_in": ["pending"],
                "support_key": "PO_abc123",
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(PortoutListResponse, portout, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.portouts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portout = response.parse()
        assert_matches_type(PortoutListResponse, portout, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.portouts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portout = response.parse()
            assert_matches_type(PortoutListResponse, portout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_rejection_codes(self, client: Telnyx) -> None:
        portout = client.portouts.list_rejection_codes(
            portout_id="329d6658-8f93-405d-862f-648776e8afd7",
        )
        assert_matches_type(PortoutListRejectionCodesResponse, portout, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_rejection_codes_with_all_params(self, client: Telnyx) -> None:
        portout = client.portouts.list_rejection_codes(
            portout_id="329d6658-8f93-405d-862f-648776e8afd7",
            filter={"code": 1002},
        )
        assert_matches_type(PortoutListRejectionCodesResponse, portout, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_rejection_codes(self, client: Telnyx) -> None:
        response = client.portouts.with_raw_response.list_rejection_codes(
            portout_id="329d6658-8f93-405d-862f-648776e8afd7",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portout = response.parse()
        assert_matches_type(PortoutListRejectionCodesResponse, portout, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_rejection_codes(self, client: Telnyx) -> None:
        with client.portouts.with_streaming_response.list_rejection_codes(
            portout_id="329d6658-8f93-405d-862f-648776e8afd7",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portout = response.parse()
            assert_matches_type(PortoutListRejectionCodesResponse, portout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_rejection_codes(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `portout_id` but received ''"):
            client.portouts.with_raw_response.list_rejection_codes(
                portout_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_status(self, client: Telnyx) -> None:
        portout = client.portouts.update_status(
            status="authorized",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="I do not recognize this transaction",
        )
        assert_matches_type(PortoutUpdateStatusResponse, portout, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_status_with_all_params(self, client: Telnyx) -> None:
        portout = client.portouts.update_status(
            status="authorized",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="I do not recognize this transaction",
            host_messaging=False,
        )
        assert_matches_type(PortoutUpdateStatusResponse, portout, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_status(self, client: Telnyx) -> None:
        response = client.portouts.with_raw_response.update_status(
            status="authorized",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="I do not recognize this transaction",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portout = response.parse()
        assert_matches_type(PortoutUpdateStatusResponse, portout, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_status(self, client: Telnyx) -> None:
        with client.portouts.with_streaming_response.update_status(
            status="authorized",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="I do not recognize this transaction",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portout = response.parse()
            assert_matches_type(PortoutUpdateStatusResponse, portout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_status(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.portouts.with_raw_response.update_status(
                status="authorized",
                id="",
                reason="I do not recognize this transaction",
            )


class TestAsyncPortouts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        portout = await async_client.portouts.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PortoutRetrieveResponse, portout, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.portouts.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portout = await response.parse()
        assert_matches_type(PortoutRetrieveResponse, portout, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.portouts.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portout = await response.parse()
            assert_matches_type(PortoutRetrieveResponse, portout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.portouts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        portout = await async_client.portouts.list()
        assert_matches_type(PortoutListResponse, portout, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        portout = await async_client.portouts.list(
            filter={
                "carrier_name": "carrier_name",
                "country_code": "US",
                "country_code_in": ["CA", "US"],
                "foc_date": parse_datetime("2024-09-04T00:00:00.000Z"),
                "inserted_at": {
                    "gte": parse_datetime("2024-09-04T00:00:00.000Z"),
                    "lte": parse_datetime("2024-09-04T00:00:00.000Z"),
                },
                "phone_number": "+13035551212",
                "pon": "pon",
                "ported_out_at": {
                    "gte": parse_datetime("2024-09-04T00:00:00.000Z"),
                    "lte": parse_datetime("2024-09-04T00:00:00.000Z"),
                },
                "spid": "spid",
                "status": "pending",
                "status_in": ["pending"],
                "support_key": "PO_abc123",
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(PortoutListResponse, portout, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.portouts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portout = await response.parse()
        assert_matches_type(PortoutListResponse, portout, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.portouts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portout = await response.parse()
            assert_matches_type(PortoutListResponse, portout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_rejection_codes(self, async_client: AsyncTelnyx) -> None:
        portout = await async_client.portouts.list_rejection_codes(
            portout_id="329d6658-8f93-405d-862f-648776e8afd7",
        )
        assert_matches_type(PortoutListRejectionCodesResponse, portout, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_rejection_codes_with_all_params(self, async_client: AsyncTelnyx) -> None:
        portout = await async_client.portouts.list_rejection_codes(
            portout_id="329d6658-8f93-405d-862f-648776e8afd7",
            filter={"code": 1002},
        )
        assert_matches_type(PortoutListRejectionCodesResponse, portout, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_rejection_codes(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.portouts.with_raw_response.list_rejection_codes(
            portout_id="329d6658-8f93-405d-862f-648776e8afd7",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portout = await response.parse()
        assert_matches_type(PortoutListRejectionCodesResponse, portout, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_rejection_codes(self, async_client: AsyncTelnyx) -> None:
        async with async_client.portouts.with_streaming_response.list_rejection_codes(
            portout_id="329d6658-8f93-405d-862f-648776e8afd7",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portout = await response.parse()
            assert_matches_type(PortoutListRejectionCodesResponse, portout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_rejection_codes(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `portout_id` but received ''"):
            await async_client.portouts.with_raw_response.list_rejection_codes(
                portout_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_status(self, async_client: AsyncTelnyx) -> None:
        portout = await async_client.portouts.update_status(
            status="authorized",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="I do not recognize this transaction",
        )
        assert_matches_type(PortoutUpdateStatusResponse, portout, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_status_with_all_params(self, async_client: AsyncTelnyx) -> None:
        portout = await async_client.portouts.update_status(
            status="authorized",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="I do not recognize this transaction",
            host_messaging=False,
        )
        assert_matches_type(PortoutUpdateStatusResponse, portout, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_status(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.portouts.with_raw_response.update_status(
            status="authorized",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="I do not recognize this transaction",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portout = await response.parse()
        assert_matches_type(PortoutUpdateStatusResponse, portout, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_status(self, async_client: AsyncTelnyx) -> None:
        async with async_client.portouts.with_streaming_response.update_status(
            status="authorized",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="I do not recognize this transaction",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portout = await response.parse()
            assert_matches_type(PortoutUpdateStatusResponse, portout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_status(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.portouts.with_raw_response.update_status(
                status="authorized",
                id="",
                reason="I do not recognize this transaction",
            )
