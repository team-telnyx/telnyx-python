# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from telnyx.types.shared import WhatsappTemplateData
from telnyx.types.whatsapp import (
    MessageTemplateCreateResponse,
    MessageTemplateUpdateResponse,
    MessageTemplateRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessageTemplates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        message_template = client.whatsapp.message_templates.create(
            category="MARKETING",
            components=[{"foo": "bar"}],
            language="language",
            name="name",
            waba_id="waba_id",
        )
        assert_matches_type(MessageTemplateCreateResponse, message_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.whatsapp.message_templates.with_raw_response.create(
            category="MARKETING",
            components=[{"foo": "bar"}],
            language="language",
            name="name",
            waba_id="waba_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message_template = response.parse()
        assert_matches_type(MessageTemplateCreateResponse, message_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.whatsapp.message_templates.with_streaming_response.create(
            category="MARKETING",
            components=[{"foo": "bar"}],
            language="language",
            name="name",
            waba_id="waba_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message_template = response.parse()
            assert_matches_type(MessageTemplateCreateResponse, message_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        message_template = client.whatsapp.message_templates.retrieve(
            "id",
        )
        assert_matches_type(MessageTemplateRetrieveResponse, message_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.whatsapp.message_templates.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message_template = response.parse()
        assert_matches_type(MessageTemplateRetrieveResponse, message_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.whatsapp.message_templates.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message_template = response.parse()
            assert_matches_type(MessageTemplateRetrieveResponse, message_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.whatsapp.message_templates.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        message_template = client.whatsapp.message_templates.update(
            id="id",
        )
        assert_matches_type(MessageTemplateUpdateResponse, message_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        message_template = client.whatsapp.message_templates.update(
            id="id",
            category="MARKETING",
            components=[{"foo": "bar"}],
        )
        assert_matches_type(MessageTemplateUpdateResponse, message_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.whatsapp.message_templates.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message_template = response.parse()
        assert_matches_type(MessageTemplateUpdateResponse, message_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.whatsapp.message_templates.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message_template = response.parse()
            assert_matches_type(MessageTemplateUpdateResponse, message_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.whatsapp.message_templates.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        message_template = client.whatsapp.message_templates.list()
        assert_matches_type(SyncDefaultFlatPagination[WhatsappTemplateData], message_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        message_template = client.whatsapp.message_templates.list(
            filter_category="MARKETING",
            filter_search="filter[search]",
            filter_status="filter[status]",
            filter_waba_id="filter[waba_id]",
            page_number=0,
            page_size=0,
        )
        assert_matches_type(SyncDefaultFlatPagination[WhatsappTemplateData], message_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.whatsapp.message_templates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message_template = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[WhatsappTemplateData], message_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.whatsapp.message_templates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message_template = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[WhatsappTemplateData], message_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        message_template = client.whatsapp.message_templates.delete(
            "id",
        )
        assert message_template is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.whatsapp.message_templates.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message_template = response.parse()
        assert message_template is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.whatsapp.message_templates.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message_template = response.parse()
            assert message_template is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.whatsapp.message_templates.with_raw_response.delete(
                "",
            )


class TestAsyncMessageTemplates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        message_template = await async_client.whatsapp.message_templates.create(
            category="MARKETING",
            components=[{"foo": "bar"}],
            language="language",
            name="name",
            waba_id="waba_id",
        )
        assert_matches_type(MessageTemplateCreateResponse, message_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.whatsapp.message_templates.with_raw_response.create(
            category="MARKETING",
            components=[{"foo": "bar"}],
            language="language",
            name="name",
            waba_id="waba_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message_template = await response.parse()
        assert_matches_type(MessageTemplateCreateResponse, message_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.whatsapp.message_templates.with_streaming_response.create(
            category="MARKETING",
            components=[{"foo": "bar"}],
            language="language",
            name="name",
            waba_id="waba_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message_template = await response.parse()
            assert_matches_type(MessageTemplateCreateResponse, message_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        message_template = await async_client.whatsapp.message_templates.retrieve(
            "id",
        )
        assert_matches_type(MessageTemplateRetrieveResponse, message_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.whatsapp.message_templates.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message_template = await response.parse()
        assert_matches_type(MessageTemplateRetrieveResponse, message_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.whatsapp.message_templates.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message_template = await response.parse()
            assert_matches_type(MessageTemplateRetrieveResponse, message_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.whatsapp.message_templates.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        message_template = await async_client.whatsapp.message_templates.update(
            id="id",
        )
        assert_matches_type(MessageTemplateUpdateResponse, message_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        message_template = await async_client.whatsapp.message_templates.update(
            id="id",
            category="MARKETING",
            components=[{"foo": "bar"}],
        )
        assert_matches_type(MessageTemplateUpdateResponse, message_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.whatsapp.message_templates.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message_template = await response.parse()
        assert_matches_type(MessageTemplateUpdateResponse, message_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.whatsapp.message_templates.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message_template = await response.parse()
            assert_matches_type(MessageTemplateUpdateResponse, message_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.whatsapp.message_templates.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        message_template = await async_client.whatsapp.message_templates.list()
        assert_matches_type(AsyncDefaultFlatPagination[WhatsappTemplateData], message_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        message_template = await async_client.whatsapp.message_templates.list(
            filter_category="MARKETING",
            filter_search="filter[search]",
            filter_status="filter[status]",
            filter_waba_id="filter[waba_id]",
            page_number=0,
            page_size=0,
        )
        assert_matches_type(AsyncDefaultFlatPagination[WhatsappTemplateData], message_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.whatsapp.message_templates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message_template = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[WhatsappTemplateData], message_template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.whatsapp.message_templates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message_template = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[WhatsappTemplateData], message_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        message_template = await async_client.whatsapp.message_templates.delete(
            "id",
        )
        assert message_template is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.whatsapp.message_templates.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message_template = await response.parse()
        assert message_template is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.whatsapp.message_templates.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message_template = await response.parse()
            assert message_template is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.whatsapp.message_templates.with_raw_response.delete(
                "",
            )
