# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import RegulatoryRequirementRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRegulatoryRequirements:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        regulatory_requirement = client.regulatory_requirements.retrieve()
        assert_matches_type(RegulatoryRequirementRetrieveResponse, regulatory_requirement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Telnyx) -> None:
        regulatory_requirement = client.regulatory_requirements.retrieve(
            filter={
                "action": "ordering",
                "country_code": "DE",
                "phone_number": "+41215470622",
                "phone_number_type": "local",
                "requirement_group_id": "d4c0b4a6-7bd2-40c5-a3b9-2acd99e212b2",
            },
        )
        assert_matches_type(RegulatoryRequirementRetrieveResponse, regulatory_requirement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.regulatory_requirements.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regulatory_requirement = response.parse()
        assert_matches_type(RegulatoryRequirementRetrieveResponse, regulatory_requirement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.regulatory_requirements.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regulatory_requirement = response.parse()
            assert_matches_type(RegulatoryRequirementRetrieveResponse, regulatory_requirement, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRegulatoryRequirements:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        regulatory_requirement = await async_client.regulatory_requirements.retrieve()
        assert_matches_type(RegulatoryRequirementRetrieveResponse, regulatory_requirement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTelnyx) -> None:
        regulatory_requirement = await async_client.regulatory_requirements.retrieve(
            filter={
                "action": "ordering",
                "country_code": "DE",
                "phone_number": "+41215470622",
                "phone_number_type": "local",
                "requirement_group_id": "d4c0b4a6-7bd2-40c5-a3b9-2acd99e212b2",
            },
        )
        assert_matches_type(RegulatoryRequirementRetrieveResponse, regulatory_requirement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.regulatory_requirements.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regulatory_requirement = await response.parse()
        assert_matches_type(RegulatoryRequirementRetrieveResponse, regulatory_requirement, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.regulatory_requirements.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regulatory_requirement = await response.parse()
            assert_matches_type(RegulatoryRequirementRetrieveResponse, regulatory_requirement, path=["response"])

        assert cast(Any, response.is_closed) is True
