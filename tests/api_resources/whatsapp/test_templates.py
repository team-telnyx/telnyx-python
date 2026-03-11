# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from telnyx.types.shared import WhatsappTemplateData
from telnyx.types.whatsapp import TemplateCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTemplates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        template = client.whatsapp.templates.create(
            category="MARKETING",
            components=[{"foo": "bar"}],
            language="language",
            name="name",
            waba_id="waba_id",
        )
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.whatsapp.templates.with_raw_response.create(
            category="MARKETING",
            components=[{"foo": "bar"}],
            language="language",
            name="name",
            waba_id="waba_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.whatsapp.templates.with_streaming_response.create(
            category="MARKETING",
            components=[{"foo": "bar"}],
            language="language",
            name="name",
            waba_id="waba_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateCreateResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        template = client.whatsapp.templates.list()
        assert_matches_type(SyncDefaultFlatPagination[WhatsappTemplateData], template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        template = client.whatsapp.templates.list(
            filter_category="MARKETING",
            filter_search="filter[search]",
            filter_status="filter[status]",
            filter_waba_id="filter[waba_id]",
            page_number=0,
            page_size=0,
        )
        assert_matches_type(SyncDefaultFlatPagination[WhatsappTemplateData], template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.whatsapp.templates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[WhatsappTemplateData], template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.whatsapp.templates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[WhatsappTemplateData], template, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTemplates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        template = await async_client.whatsapp.templates.create(
            category="MARKETING",
            components=[{"foo": "bar"}],
            language="language",
            name="name",
            waba_id="waba_id",
        )
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.whatsapp.templates.with_raw_response.create(
            category="MARKETING",
            components=[{"foo": "bar"}],
            language="language",
            name="name",
            waba_id="waba_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.whatsapp.templates.with_streaming_response.create(
            category="MARKETING",
            components=[{"foo": "bar"}],
            language="language",
            name="name",
            waba_id="waba_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateCreateResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        template = await async_client.whatsapp.templates.list()
        assert_matches_type(AsyncDefaultFlatPagination[WhatsappTemplateData], template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        template = await async_client.whatsapp.templates.list(
            filter_category="MARKETING",
            filter_search="filter[search]",
            filter_status="filter[status]",
            filter_waba_id="filter[waba_id]",
            page_number=0,
            page_size=0,
        )
        assert_matches_type(AsyncDefaultFlatPagination[WhatsappTemplateData], template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.whatsapp.templates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[WhatsappTemplateData], template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.whatsapp.templates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[WhatsappTemplateData], template, path=["response"])

        assert cast(Any, response.is_closed) is True
