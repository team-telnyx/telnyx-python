# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.terms_of_service import TosAgreementWrapped

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBrandedCalling:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_agree(self, client: Telnyx) -> None:
        branded_calling = client.terms_of_service.branded_calling.agree()
        assert_matches_type(TosAgreementWrapped, branded_calling, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_agree(self, client: Telnyx) -> None:
        response = client.terms_of_service.branded_calling.with_raw_response.agree()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        branded_calling = response.parse()
        assert_matches_type(TosAgreementWrapped, branded_calling, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_agree(self, client: Telnyx) -> None:
        with client.terms_of_service.branded_calling.with_streaming_response.agree() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            branded_calling = response.parse()
            assert_matches_type(TosAgreementWrapped, branded_calling, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBrandedCalling:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_agree(self, async_client: AsyncTelnyx) -> None:
        branded_calling = await async_client.terms_of_service.branded_calling.agree()
        assert_matches_type(TosAgreementWrapped, branded_calling, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_agree(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.terms_of_service.branded_calling.with_raw_response.agree()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        branded_calling = await response.parse()
        assert_matches_type(TosAgreementWrapped, branded_calling, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_agree(self, async_client: AsyncTelnyx) -> None:
        async with async_client.terms_of_service.branded_calling.with_streaming_response.agree() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            branded_calling = await response.parse()
            assert_matches_type(TosAgreementWrapped, branded_calling, path=["response"])

        assert cast(Any, response.is_closed) is True
