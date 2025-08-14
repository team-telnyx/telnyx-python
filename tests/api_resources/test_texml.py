# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import TexmlSecretsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTexml:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_secrets(self, client: Telnyx) -> None:
        texml = client.texml.secrets(
            name="My Secret Name",
            value="My Secret Value",
        )
        assert_matches_type(TexmlSecretsResponse, texml, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_secrets(self, client: Telnyx) -> None:
        response = client.texml.with_raw_response.secrets(
            name="My Secret Name",
            value="My Secret Value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        texml = response.parse()
        assert_matches_type(TexmlSecretsResponse, texml, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_secrets(self, client: Telnyx) -> None:
        with client.texml.with_streaming_response.secrets(
            name="My Secret Name",
            value="My Secret Value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            texml = response.parse()
            assert_matches_type(TexmlSecretsResponse, texml, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTexml:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_secrets(self, async_client: AsyncTelnyx) -> None:
        texml = await async_client.texml.secrets(
            name="My Secret Name",
            value="My Secret Value",
        )
        assert_matches_type(TexmlSecretsResponse, texml, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_secrets(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml.with_raw_response.secrets(
            name="My Secret Name",
            value="My Secret Value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        texml = await response.parse()
        assert_matches_type(TexmlSecretsResponse, texml, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_secrets(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml.with_streaming_response.secrets(
            name="My Secret Name",
            value="My Secret Value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            texml = await response.parse()
            assert_matches_type(TexmlSecretsResponse, texml, path=["response"])

        assert cast(Any, response.is_closed) is True
