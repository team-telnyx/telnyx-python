# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    VoiceDesignListResponse,
    VoiceDesignCreateResponse,
    VoiceDesignUpdateResponse,
    VoiceDesignRetrieveResponse,
)
from telnyx._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVoiceDesigns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        voice_design = client.voice_designs.create(
            prompt="Speak in a warm, friendly tone",
            text="Hello, welcome to our service.",
        )
        assert_matches_type(VoiceDesignCreateResponse, voice_design, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        voice_design = client.voice_designs.create(
            prompt="Speak in a warm, friendly tone",
            text="Hello, welcome to our service.",
            language="Auto",
            max_new_tokens=100,
            name="friendly-narrator",
            repetition_penalty=1,
            temperature=0,
            top_k=1,
            top_p=0,
            voice_design_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VoiceDesignCreateResponse, voice_design, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.voice_designs.with_raw_response.create(
            prompt="Speak in a warm, friendly tone",
            text="Hello, welcome to our service.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_design = response.parse()
        assert_matches_type(VoiceDesignCreateResponse, voice_design, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.voice_designs.with_streaming_response.create(
            prompt="Speak in a warm, friendly tone",
            text="Hello, welcome to our service.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_design = response.parse()
            assert_matches_type(VoiceDesignCreateResponse, voice_design, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        voice_design = client.voice_designs.retrieve(
            id="id",
        )
        assert_matches_type(VoiceDesignRetrieveResponse, voice_design, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Telnyx) -> None:
        voice_design = client.voice_designs.retrieve(
            id="id",
            version=1,
        )
        assert_matches_type(VoiceDesignRetrieveResponse, voice_design, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.voice_designs.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_design = response.parse()
        assert_matches_type(VoiceDesignRetrieveResponse, voice_design, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.voice_designs.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_design = response.parse()
            assert_matches_type(VoiceDesignRetrieveResponse, voice_design, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.voice_designs.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        voice_design = client.voice_designs.update(
            id="id",
            name="updated-narrator",
        )
        assert_matches_type(VoiceDesignUpdateResponse, voice_design, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.voice_designs.with_raw_response.update(
            id="id",
            name="updated-narrator",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_design = response.parse()
        assert_matches_type(VoiceDesignUpdateResponse, voice_design, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.voice_designs.with_streaming_response.update(
            id="id",
            name="updated-narrator",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_design = response.parse()
            assert_matches_type(VoiceDesignUpdateResponse, voice_design, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.voice_designs.with_raw_response.update(
                id="",
                name="updated-narrator",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        voice_design = client.voice_designs.list()
        assert_matches_type(SyncDefaultFlatPagination[VoiceDesignListResponse], voice_design, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        voice_design = client.voice_designs.list(
            filter_name="filter[name]",
            page_number=1,
            page_size=1,
            sort="name",
        )
        assert_matches_type(SyncDefaultFlatPagination[VoiceDesignListResponse], voice_design, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.voice_designs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_design = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[VoiceDesignListResponse], voice_design, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.voice_designs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_design = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[VoiceDesignListResponse], voice_design, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        voice_design = client.voice_designs.delete(
            "id",
        )
        assert voice_design is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.voice_designs.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_design = response.parse()
        assert voice_design is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.voice_designs.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_design = response.parse()
            assert voice_design is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.voice_designs.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_version(self, client: Telnyx) -> None:
        voice_design = client.voice_designs.delete_version(
            version=1,
            id="id",
        )
        assert voice_design is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_version(self, client: Telnyx) -> None:
        response = client.voice_designs.with_raw_response.delete_version(
            version=1,
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_design = response.parse()
        assert voice_design is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_version(self, client: Telnyx) -> None:
        with client.voice_designs.with_streaming_response.delete_version(
            version=1,
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_design = response.parse()
            assert voice_design is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_version(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.voice_designs.with_raw_response.delete_version(
                version=1,
                id="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download_sample(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/voice_designs/id/sample").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        voice_design = client.voice_designs.download_sample(
            id="id",
        )
        assert voice_design.is_closed
        assert voice_design.json() == {"foo": "bar"}
        assert cast(Any, voice_design.is_closed) is True
        assert isinstance(voice_design, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download_sample_with_all_params(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/voice_designs/id/sample").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        voice_design = client.voice_designs.download_sample(
            id="id",
            version=1,
        )
        assert voice_design.is_closed
        assert voice_design.json() == {"foo": "bar"}
        assert cast(Any, voice_design.is_closed) is True
        assert isinstance(voice_design, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download_sample(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/voice_designs/id/sample").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        voice_design = client.voice_designs.with_raw_response.download_sample(
            id="id",
        )

        assert voice_design.is_closed is True
        assert voice_design.http_request.headers.get("X-Stainless-Lang") == "python"
        assert voice_design.json() == {"foo": "bar"}
        assert isinstance(voice_design, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download_sample(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/voice_designs/id/sample").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.voice_designs.with_streaming_response.download_sample(
            id="id",
        ) as voice_design:
            assert not voice_design.is_closed
            assert voice_design.http_request.headers.get("X-Stainless-Lang") == "python"

            assert voice_design.json() == {"foo": "bar"}
            assert cast(Any, voice_design.is_closed) is True
            assert isinstance(voice_design, StreamedBinaryAPIResponse)

        assert cast(Any, voice_design.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_download_sample(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.voice_designs.with_raw_response.download_sample(
                id="",
            )


class TestAsyncVoiceDesigns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        voice_design = await async_client.voice_designs.create(
            prompt="Speak in a warm, friendly tone",
            text="Hello, welcome to our service.",
        )
        assert_matches_type(VoiceDesignCreateResponse, voice_design, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        voice_design = await async_client.voice_designs.create(
            prompt="Speak in a warm, friendly tone",
            text="Hello, welcome to our service.",
            language="Auto",
            max_new_tokens=100,
            name="friendly-narrator",
            repetition_penalty=1,
            temperature=0,
            top_k=1,
            top_p=0,
            voice_design_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VoiceDesignCreateResponse, voice_design, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.voice_designs.with_raw_response.create(
            prompt="Speak in a warm, friendly tone",
            text="Hello, welcome to our service.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_design = await response.parse()
        assert_matches_type(VoiceDesignCreateResponse, voice_design, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.voice_designs.with_streaming_response.create(
            prompt="Speak in a warm, friendly tone",
            text="Hello, welcome to our service.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_design = await response.parse()
            assert_matches_type(VoiceDesignCreateResponse, voice_design, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        voice_design = await async_client.voice_designs.retrieve(
            id="id",
        )
        assert_matches_type(VoiceDesignRetrieveResponse, voice_design, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTelnyx) -> None:
        voice_design = await async_client.voice_designs.retrieve(
            id="id",
            version=1,
        )
        assert_matches_type(VoiceDesignRetrieveResponse, voice_design, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.voice_designs.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_design = await response.parse()
        assert_matches_type(VoiceDesignRetrieveResponse, voice_design, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.voice_designs.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_design = await response.parse()
            assert_matches_type(VoiceDesignRetrieveResponse, voice_design, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.voice_designs.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        voice_design = await async_client.voice_designs.update(
            id="id",
            name="updated-narrator",
        )
        assert_matches_type(VoiceDesignUpdateResponse, voice_design, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.voice_designs.with_raw_response.update(
            id="id",
            name="updated-narrator",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_design = await response.parse()
        assert_matches_type(VoiceDesignUpdateResponse, voice_design, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.voice_designs.with_streaming_response.update(
            id="id",
            name="updated-narrator",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_design = await response.parse()
            assert_matches_type(VoiceDesignUpdateResponse, voice_design, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.voice_designs.with_raw_response.update(
                id="",
                name="updated-narrator",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        voice_design = await async_client.voice_designs.list()
        assert_matches_type(AsyncDefaultFlatPagination[VoiceDesignListResponse], voice_design, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        voice_design = await async_client.voice_designs.list(
            filter_name="filter[name]",
            page_number=1,
            page_size=1,
            sort="name",
        )
        assert_matches_type(AsyncDefaultFlatPagination[VoiceDesignListResponse], voice_design, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.voice_designs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_design = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[VoiceDesignListResponse], voice_design, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.voice_designs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_design = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[VoiceDesignListResponse], voice_design, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        voice_design = await async_client.voice_designs.delete(
            "id",
        )
        assert voice_design is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.voice_designs.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_design = await response.parse()
        assert voice_design is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.voice_designs.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_design = await response.parse()
            assert voice_design is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.voice_designs.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_version(self, async_client: AsyncTelnyx) -> None:
        voice_design = await async_client.voice_designs.delete_version(
            version=1,
            id="id",
        )
        assert voice_design is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_version(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.voice_designs.with_raw_response.delete_version(
            version=1,
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_design = await response.parse()
        assert voice_design is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_version(self, async_client: AsyncTelnyx) -> None:
        async with async_client.voice_designs.with_streaming_response.delete_version(
            version=1,
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_design = await response.parse()
            assert voice_design is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_version(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.voice_designs.with_raw_response.delete_version(
                version=1,
                id="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download_sample(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/voice_designs/id/sample").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        voice_design = await async_client.voice_designs.download_sample(
            id="id",
        )
        assert voice_design.is_closed
        assert await voice_design.json() == {"foo": "bar"}
        assert cast(Any, voice_design.is_closed) is True
        assert isinstance(voice_design, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download_sample_with_all_params(
        self, async_client: AsyncTelnyx, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/voice_designs/id/sample").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        voice_design = await async_client.voice_designs.download_sample(
            id="id",
            version=1,
        )
        assert voice_design.is_closed
        assert await voice_design.json() == {"foo": "bar"}
        assert cast(Any, voice_design.is_closed) is True
        assert isinstance(voice_design, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download_sample(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/voice_designs/id/sample").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        voice_design = await async_client.voice_designs.with_raw_response.download_sample(
            id="id",
        )

        assert voice_design.is_closed is True
        assert voice_design.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await voice_design.json() == {"foo": "bar"}
        assert isinstance(voice_design, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download_sample(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/voice_designs/id/sample").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.voice_designs.with_streaming_response.download_sample(
            id="id",
        ) as voice_design:
            assert not voice_design.is_closed
            assert voice_design.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await voice_design.json() == {"foo": "bar"}
            assert cast(Any, voice_design.is_closed) is True
            assert isinstance(voice_design, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, voice_design.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_download_sample(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.voice_designs.with_raw_response.download_sample(
                id="",
            )
