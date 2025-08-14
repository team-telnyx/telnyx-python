# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    GlobalIPAssignmentListResponse,
    GlobalIPAssignmentCreateResponse,
    GlobalIPAssignmentDeleteResponse,
    GlobalIPAssignmentUpdateResponse,
    GlobalIPAssignmentRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGlobalIPAssignments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        global_ip_assignment = client.global_ip_assignments.create()
        assert_matches_type(GlobalIPAssignmentCreateResponse, global_ip_assignment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        global_ip_assignment = client.global_ip_assignments.create(
            global_ip_id="a836125b-20b6-452e-9c03-2653f09c7ed7",
            is_in_maintenance=True,
            wireguard_peer_id="e66c496d-4a85-423b-8b2a-8e63fac20320",
        )
        assert_matches_type(GlobalIPAssignmentCreateResponse, global_ip_assignment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.global_ip_assignments.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        global_ip_assignment = response.parse()
        assert_matches_type(GlobalIPAssignmentCreateResponse, global_ip_assignment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.global_ip_assignments.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            global_ip_assignment = response.parse()
            assert_matches_type(GlobalIPAssignmentCreateResponse, global_ip_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        global_ip_assignment = client.global_ip_assignments.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(GlobalIPAssignmentRetrieveResponse, global_ip_assignment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.global_ip_assignments.with_raw_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        global_ip_assignment = response.parse()
        assert_matches_type(GlobalIPAssignmentRetrieveResponse, global_ip_assignment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.global_ip_assignments.with_streaming_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            global_ip_assignment = response.parse()
            assert_matches_type(GlobalIPAssignmentRetrieveResponse, global_ip_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.global_ip_assignments.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        global_ip_assignment = client.global_ip_assignments.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            body={},
        )
        assert_matches_type(GlobalIPAssignmentUpdateResponse, global_ip_assignment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        global_ip_assignment = client.global_ip_assignments.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            body={
                "global_ip_id": "a836125b-20b6-452e-9c03-2653f09c7ed7",
                "wireguard_peer_id": "e66c496d-4a85-423b-8b2a-8e63fac20320",
            },
        )
        assert_matches_type(GlobalIPAssignmentUpdateResponse, global_ip_assignment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.global_ip_assignments.with_raw_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        global_ip_assignment = response.parse()
        assert_matches_type(GlobalIPAssignmentUpdateResponse, global_ip_assignment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.global_ip_assignments.with_streaming_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            global_ip_assignment = response.parse()
            assert_matches_type(GlobalIPAssignmentUpdateResponse, global_ip_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.global_ip_assignments.with_raw_response.update(
                id="",
                body={},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        global_ip_assignment = client.global_ip_assignments.list()
        assert_matches_type(GlobalIPAssignmentListResponse, global_ip_assignment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        global_ip_assignment = client.global_ip_assignments.list(
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(GlobalIPAssignmentListResponse, global_ip_assignment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.global_ip_assignments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        global_ip_assignment = response.parse()
        assert_matches_type(GlobalIPAssignmentListResponse, global_ip_assignment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.global_ip_assignments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            global_ip_assignment = response.parse()
            assert_matches_type(GlobalIPAssignmentListResponse, global_ip_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        global_ip_assignment = client.global_ip_assignments.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(GlobalIPAssignmentDeleteResponse, global_ip_assignment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.global_ip_assignments.with_raw_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        global_ip_assignment = response.parse()
        assert_matches_type(GlobalIPAssignmentDeleteResponse, global_ip_assignment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.global_ip_assignments.with_streaming_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            global_ip_assignment = response.parse()
            assert_matches_type(GlobalIPAssignmentDeleteResponse, global_ip_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.global_ip_assignments.with_raw_response.delete(
                "",
            )


class TestAsyncGlobalIPAssignments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        global_ip_assignment = await async_client.global_ip_assignments.create()
        assert_matches_type(GlobalIPAssignmentCreateResponse, global_ip_assignment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        global_ip_assignment = await async_client.global_ip_assignments.create(
            global_ip_id="a836125b-20b6-452e-9c03-2653f09c7ed7",
            is_in_maintenance=True,
            wireguard_peer_id="e66c496d-4a85-423b-8b2a-8e63fac20320",
        )
        assert_matches_type(GlobalIPAssignmentCreateResponse, global_ip_assignment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.global_ip_assignments.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        global_ip_assignment = await response.parse()
        assert_matches_type(GlobalIPAssignmentCreateResponse, global_ip_assignment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.global_ip_assignments.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            global_ip_assignment = await response.parse()
            assert_matches_type(GlobalIPAssignmentCreateResponse, global_ip_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        global_ip_assignment = await async_client.global_ip_assignments.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(GlobalIPAssignmentRetrieveResponse, global_ip_assignment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.global_ip_assignments.with_raw_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        global_ip_assignment = await response.parse()
        assert_matches_type(GlobalIPAssignmentRetrieveResponse, global_ip_assignment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.global_ip_assignments.with_streaming_response.retrieve(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            global_ip_assignment = await response.parse()
            assert_matches_type(GlobalIPAssignmentRetrieveResponse, global_ip_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.global_ip_assignments.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        global_ip_assignment = await async_client.global_ip_assignments.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            body={},
        )
        assert_matches_type(GlobalIPAssignmentUpdateResponse, global_ip_assignment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        global_ip_assignment = await async_client.global_ip_assignments.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            body={
                "global_ip_id": "a836125b-20b6-452e-9c03-2653f09c7ed7",
                "wireguard_peer_id": "e66c496d-4a85-423b-8b2a-8e63fac20320",
            },
        )
        assert_matches_type(GlobalIPAssignmentUpdateResponse, global_ip_assignment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.global_ip_assignments.with_raw_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        global_ip_assignment = await response.parse()
        assert_matches_type(GlobalIPAssignmentUpdateResponse, global_ip_assignment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.global_ip_assignments.with_streaming_response.update(
            id="6a09cdc3-8948-47f0-aa62-74ac943d6c58",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            global_ip_assignment = await response.parse()
            assert_matches_type(GlobalIPAssignmentUpdateResponse, global_ip_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.global_ip_assignments.with_raw_response.update(
                id="",
                body={},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        global_ip_assignment = await async_client.global_ip_assignments.list()
        assert_matches_type(GlobalIPAssignmentListResponse, global_ip_assignment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        global_ip_assignment = await async_client.global_ip_assignments.list(
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(GlobalIPAssignmentListResponse, global_ip_assignment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.global_ip_assignments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        global_ip_assignment = await response.parse()
        assert_matches_type(GlobalIPAssignmentListResponse, global_ip_assignment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.global_ip_assignments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            global_ip_assignment = await response.parse()
            assert_matches_type(GlobalIPAssignmentListResponse, global_ip_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        global_ip_assignment = await async_client.global_ip_assignments.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )
        assert_matches_type(GlobalIPAssignmentDeleteResponse, global_ip_assignment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.global_ip_assignments.with_raw_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        global_ip_assignment = await response.parse()
        assert_matches_type(GlobalIPAssignmentDeleteResponse, global_ip_assignment, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.global_ip_assignments.with_streaming_response.delete(
            "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            global_ip_assignment = await response.parse()
            assert_matches_type(GlobalIPAssignmentDeleteResponse, global_ip_assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.global_ip_assignments.with_raw_response.delete(
                "",
            )
