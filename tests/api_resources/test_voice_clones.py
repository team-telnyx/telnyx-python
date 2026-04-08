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
    VoiceCloneData,
    VoiceCloneCreateResponse,
    VoiceCloneUpdateResponse,
    VoiceCloneCreateFromUploadResponse,
)
from telnyx._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from telnyx.pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVoiceClones:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Telnyx) -> None:
        voice_clone = client.voice_clones.create(
            gender="male",
            language="en",
            name="clone-narrator",
            voice_design_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(VoiceCloneCreateResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Telnyx) -> None:
        voice_clone = client.voice_clones.create(
            gender="male",
            language="en",
            name="clone-narrator",
            voice_design_id="550e8400-e29b-41d4-a716-446655440000",
            provider="telnyx",
        )
        assert_matches_type(VoiceCloneCreateResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Telnyx) -> None:
        response = client.voice_clones.with_raw_response.create(
            gender="male",
            language="en",
            name="clone-narrator",
            voice_design_id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_clone = response.parse()
        assert_matches_type(VoiceCloneCreateResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Telnyx) -> None:
        with client.voice_clones.with_streaming_response.create(
            gender="male",
            language="en",
            name="clone-narrator",
            voice_design_id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_clone = response.parse()
            assert_matches_type(VoiceCloneCreateResponse, voice_clone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Telnyx) -> None:
        voice_clone = client.voice_clones.create(
            gender="male",
            language="en",
            name="clone-narrator",
            provider="minimax",
            voice_design_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(VoiceCloneCreateResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Telnyx) -> None:
        response = client.voice_clones.with_raw_response.create(
            gender="male",
            language="en",
            name="clone-narrator",
            provider="minimax",
            voice_design_id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_clone = response.parse()
        assert_matches_type(VoiceCloneCreateResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Telnyx) -> None:
        with client.voice_clones.with_streaming_response.create(
            gender="male",
            language="en",
            name="clone-narrator",
            provider="minimax",
            voice_design_id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_clone = response.parse()
            assert_matches_type(VoiceCloneCreateResponse, voice_clone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        voice_clone = client.voice_clones.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="updated-clone",
        )
        assert_matches_type(VoiceCloneUpdateResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        voice_clone = client.voice_clones.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="updated-clone",
            gender="male",
            language="language",
        )
        assert_matches_type(VoiceCloneUpdateResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.voice_clones.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="updated-clone",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_clone = response.parse()
        assert_matches_type(VoiceCloneUpdateResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.voice_clones.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="updated-clone",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_clone = response.parse()
            assert_matches_type(VoiceCloneUpdateResponse, voice_clone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.voice_clones.with_raw_response.update(
                id="",
                name="updated-clone",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        voice_clone = client.voice_clones.list()
        assert_matches_type(SyncDefaultFlatPagination[VoiceCloneData], voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        voice_clone = client.voice_clones.list(
            filter_name="filter[name]",
            filter_provider="telnyx",
            page_number=1,
            page_size=1,
            sort="name",
        )
        assert_matches_type(SyncDefaultFlatPagination[VoiceCloneData], voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.voice_clones.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_clone = response.parse()
        assert_matches_type(SyncDefaultFlatPagination[VoiceCloneData], voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.voice_clones.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_clone = response.parse()
            assert_matches_type(SyncDefaultFlatPagination[VoiceCloneData], voice_clone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        voice_clone = client.voice_clones.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert voice_clone is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.voice_clones.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_clone = response.parse()
        assert voice_clone is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.voice_clones.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_clone = response.parse()
            assert voice_clone is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.voice_clones.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_from_upload_overload_1(self, client: Telnyx) -> None:
        voice_clone = client.voice_clones.create_from_upload(
            audio_file=b"Example data",
            gender="male",
            language="lkf-Lz1vLbBu-9uDh-9AHaOS2D-Cbf",
            name="name",
            provider="telnyx",
        )
        assert_matches_type(VoiceCloneCreateFromUploadResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_from_upload_with_all_params_overload_1(self, client: Telnyx) -> None:
        voice_clone = client.voice_clones.create_from_upload(
            audio_file=b"Example data",
            gender="male",
            language="lkf-Lz1vLbBu-9uDh-9AHaOS2D-Cbf",
            name="name",
            provider="telnyx",
            label="label",
            model_id="Qwen3TTS",
            ref_text="ref_text",
        )
        assert_matches_type(VoiceCloneCreateFromUploadResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_from_upload_overload_1(self, client: Telnyx) -> None:
        response = client.voice_clones.with_raw_response.create_from_upload(
            audio_file=b"Example data",
            gender="male",
            language="lkf-Lz1vLbBu-9uDh-9AHaOS2D-Cbf",
            name="name",
            provider="telnyx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_clone = response.parse()
        assert_matches_type(VoiceCloneCreateFromUploadResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_from_upload_overload_1(self, client: Telnyx) -> None:
        with client.voice_clones.with_streaming_response.create_from_upload(
            audio_file=b"Example data",
            gender="male",
            language="lkf-Lz1vLbBu-9uDh-9AHaOS2D-Cbf",
            name="name",
            provider="telnyx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_clone = response.parse()
            assert_matches_type(VoiceCloneCreateFromUploadResponse, voice_clone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_from_upload_overload_2(self, client: Telnyx) -> None:
        voice_clone = client.voice_clones.create_from_upload(
            audio_file=b"Example data",
            gender="male",
            language="lkf-Lz1vLbBu-9uDh-9AHaOS2D-Cbf",
            model_id="Ultra",
            name="name",
            provider="telnyx",
        )
        assert_matches_type(VoiceCloneCreateFromUploadResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_from_upload_with_all_params_overload_2(self, client: Telnyx) -> None:
        voice_clone = client.voice_clones.create_from_upload(
            audio_file=b"Example data",
            gender="male",
            language="lkf-Lz1vLbBu-9uDh-9AHaOS2D-Cbf",
            model_id="Ultra",
            name="name",
            provider="telnyx",
            label="label",
            ref_text="ref_text",
        )
        assert_matches_type(VoiceCloneCreateFromUploadResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_from_upload_overload_2(self, client: Telnyx) -> None:
        response = client.voice_clones.with_raw_response.create_from_upload(
            audio_file=b"Example data",
            gender="male",
            language="lkf-Lz1vLbBu-9uDh-9AHaOS2D-Cbf",
            model_id="Ultra",
            name="name",
            provider="telnyx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_clone = response.parse()
        assert_matches_type(VoiceCloneCreateFromUploadResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_from_upload_overload_2(self, client: Telnyx) -> None:
        with client.voice_clones.with_streaming_response.create_from_upload(
            audio_file=b"Example data",
            gender="male",
            language="lkf-Lz1vLbBu-9uDh-9AHaOS2D-Cbf",
            model_id="Ultra",
            name="name",
            provider="telnyx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_clone = response.parse()
            assert_matches_type(VoiceCloneCreateFromUploadResponse, voice_clone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_from_upload_overload_3(self, client: Telnyx) -> None:
        voice_clone = client.voice_clones.create_from_upload(
            audio_file=b"Example data",
            gender="male",
            language="lkf-Lz1vLbBu-9uDh-9AHaOS2D-Cbf",
            name="name",
            provider="minimax",
        )
        assert_matches_type(VoiceCloneCreateFromUploadResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_from_upload_with_all_params_overload_3(self, client: Telnyx) -> None:
        voice_clone = client.voice_clones.create_from_upload(
            audio_file=b"Example data",
            gender="male",
            language="lkf-Lz1vLbBu-9uDh-9AHaOS2D-Cbf",
            name="name",
            provider="minimax",
            label="label",
            model_id="speech-2.8-turbo",
            ref_text="ref_text",
        )
        assert_matches_type(VoiceCloneCreateFromUploadResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_from_upload_overload_3(self, client: Telnyx) -> None:
        response = client.voice_clones.with_raw_response.create_from_upload(
            audio_file=b"Example data",
            gender="male",
            language="lkf-Lz1vLbBu-9uDh-9AHaOS2D-Cbf",
            name="name",
            provider="minimax",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_clone = response.parse()
        assert_matches_type(VoiceCloneCreateFromUploadResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_from_upload_overload_3(self, client: Telnyx) -> None:
        with client.voice_clones.with_streaming_response.create_from_upload(
            audio_file=b"Example data",
            gender="male",
            language="lkf-Lz1vLbBu-9uDh-9AHaOS2D-Cbf",
            name="name",
            provider="minimax",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_clone = response.parse()
            assert_matches_type(VoiceCloneCreateFromUploadResponse, voice_clone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download_sample(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/voice_clones/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/sample").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        voice_clone = client.voice_clones.download_sample(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert voice_clone.is_closed
        assert voice_clone.json() == {"foo": "bar"}
        assert cast(Any, voice_clone.is_closed) is True
        assert isinstance(voice_clone, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download_sample(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/voice_clones/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/sample").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        voice_clone = client.voice_clones.with_raw_response.download_sample(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert voice_clone.is_closed is True
        assert voice_clone.http_request.headers.get("X-Stainless-Lang") == "python"
        assert voice_clone.json() == {"foo": "bar"}
        assert isinstance(voice_clone, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download_sample(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/voice_clones/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/sample").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.voice_clones.with_streaming_response.download_sample(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as voice_clone:
            assert not voice_clone.is_closed
            assert voice_clone.http_request.headers.get("X-Stainless-Lang") == "python"

            assert voice_clone.json() == {"foo": "bar"}
            assert cast(Any, voice_clone.is_closed) is True
            assert isinstance(voice_clone, StreamedBinaryAPIResponse)

        assert cast(Any, voice_clone.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_download_sample(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.voice_clones.with_raw_response.download_sample(
                "",
            )


class TestAsyncVoiceClones:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncTelnyx) -> None:
        voice_clone = await async_client.voice_clones.create(
            gender="male",
            language="en",
            name="clone-narrator",
            voice_design_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(VoiceCloneCreateResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncTelnyx) -> None:
        voice_clone = await async_client.voice_clones.create(
            gender="male",
            language="en",
            name="clone-narrator",
            voice_design_id="550e8400-e29b-41d4-a716-446655440000",
            provider="telnyx",
        )
        assert_matches_type(VoiceCloneCreateResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.voice_clones.with_raw_response.create(
            gender="male",
            language="en",
            name="clone-narrator",
            voice_design_id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_clone = await response.parse()
        assert_matches_type(VoiceCloneCreateResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncTelnyx) -> None:
        async with async_client.voice_clones.with_streaming_response.create(
            gender="male",
            language="en",
            name="clone-narrator",
            voice_design_id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_clone = await response.parse()
            assert_matches_type(VoiceCloneCreateResponse, voice_clone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncTelnyx) -> None:
        voice_clone = await async_client.voice_clones.create(
            gender="male",
            language="en",
            name="clone-narrator",
            provider="minimax",
            voice_design_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(VoiceCloneCreateResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.voice_clones.with_raw_response.create(
            gender="male",
            language="en",
            name="clone-narrator",
            provider="minimax",
            voice_design_id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_clone = await response.parse()
        assert_matches_type(VoiceCloneCreateResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncTelnyx) -> None:
        async with async_client.voice_clones.with_streaming_response.create(
            gender="male",
            language="en",
            name="clone-narrator",
            provider="minimax",
            voice_design_id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_clone = await response.parse()
            assert_matches_type(VoiceCloneCreateResponse, voice_clone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        voice_clone = await async_client.voice_clones.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="updated-clone",
        )
        assert_matches_type(VoiceCloneUpdateResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        voice_clone = await async_client.voice_clones.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="updated-clone",
            gender="male",
            language="language",
        )
        assert_matches_type(VoiceCloneUpdateResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.voice_clones.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="updated-clone",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_clone = await response.parse()
        assert_matches_type(VoiceCloneUpdateResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.voice_clones.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="updated-clone",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_clone = await response.parse()
            assert_matches_type(VoiceCloneUpdateResponse, voice_clone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.voice_clones.with_raw_response.update(
                id="",
                name="updated-clone",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        voice_clone = await async_client.voice_clones.list()
        assert_matches_type(AsyncDefaultFlatPagination[VoiceCloneData], voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        voice_clone = await async_client.voice_clones.list(
            filter_name="filter[name]",
            filter_provider="telnyx",
            page_number=1,
            page_size=1,
            sort="name",
        )
        assert_matches_type(AsyncDefaultFlatPagination[VoiceCloneData], voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.voice_clones.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_clone = await response.parse()
        assert_matches_type(AsyncDefaultFlatPagination[VoiceCloneData], voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.voice_clones.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_clone = await response.parse()
            assert_matches_type(AsyncDefaultFlatPagination[VoiceCloneData], voice_clone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        voice_clone = await async_client.voice_clones.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert voice_clone is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.voice_clones.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_clone = await response.parse()
        assert voice_clone is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.voice_clones.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_clone = await response.parse()
            assert voice_clone is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.voice_clones.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_from_upload_overload_1(self, async_client: AsyncTelnyx) -> None:
        voice_clone = await async_client.voice_clones.create_from_upload(
            audio_file=b"Example data",
            gender="male",
            language="lkf-Lz1vLbBu-9uDh-9AHaOS2D-Cbf",
            name="name",
            provider="telnyx",
        )
        assert_matches_type(VoiceCloneCreateFromUploadResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_from_upload_with_all_params_overload_1(self, async_client: AsyncTelnyx) -> None:
        voice_clone = await async_client.voice_clones.create_from_upload(
            audio_file=b"Example data",
            gender="male",
            language="lkf-Lz1vLbBu-9uDh-9AHaOS2D-Cbf",
            name="name",
            provider="telnyx",
            label="label",
            model_id="Qwen3TTS",
            ref_text="ref_text",
        )
        assert_matches_type(VoiceCloneCreateFromUploadResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_from_upload_overload_1(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.voice_clones.with_raw_response.create_from_upload(
            audio_file=b"Example data",
            gender="male",
            language="lkf-Lz1vLbBu-9uDh-9AHaOS2D-Cbf",
            name="name",
            provider="telnyx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_clone = await response.parse()
        assert_matches_type(VoiceCloneCreateFromUploadResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_from_upload_overload_1(self, async_client: AsyncTelnyx) -> None:
        async with async_client.voice_clones.with_streaming_response.create_from_upload(
            audio_file=b"Example data",
            gender="male",
            language="lkf-Lz1vLbBu-9uDh-9AHaOS2D-Cbf",
            name="name",
            provider="telnyx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_clone = await response.parse()
            assert_matches_type(VoiceCloneCreateFromUploadResponse, voice_clone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_from_upload_overload_2(self, async_client: AsyncTelnyx) -> None:
        voice_clone = await async_client.voice_clones.create_from_upload(
            audio_file=b"Example data",
            gender="male",
            language="lkf-Lz1vLbBu-9uDh-9AHaOS2D-Cbf",
            model_id="Ultra",
            name="name",
            provider="telnyx",
        )
        assert_matches_type(VoiceCloneCreateFromUploadResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_from_upload_with_all_params_overload_2(self, async_client: AsyncTelnyx) -> None:
        voice_clone = await async_client.voice_clones.create_from_upload(
            audio_file=b"Example data",
            gender="male",
            language="lkf-Lz1vLbBu-9uDh-9AHaOS2D-Cbf",
            model_id="Ultra",
            name="name",
            provider="telnyx",
            label="label",
            ref_text="ref_text",
        )
        assert_matches_type(VoiceCloneCreateFromUploadResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_from_upload_overload_2(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.voice_clones.with_raw_response.create_from_upload(
            audio_file=b"Example data",
            gender="male",
            language="lkf-Lz1vLbBu-9uDh-9AHaOS2D-Cbf",
            model_id="Ultra",
            name="name",
            provider="telnyx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_clone = await response.parse()
        assert_matches_type(VoiceCloneCreateFromUploadResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_from_upload_overload_2(self, async_client: AsyncTelnyx) -> None:
        async with async_client.voice_clones.with_streaming_response.create_from_upload(
            audio_file=b"Example data",
            gender="male",
            language="lkf-Lz1vLbBu-9uDh-9AHaOS2D-Cbf",
            model_id="Ultra",
            name="name",
            provider="telnyx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_clone = await response.parse()
            assert_matches_type(VoiceCloneCreateFromUploadResponse, voice_clone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_from_upload_overload_3(self, async_client: AsyncTelnyx) -> None:
        voice_clone = await async_client.voice_clones.create_from_upload(
            audio_file=b"Example data",
            gender="male",
            language="lkf-Lz1vLbBu-9uDh-9AHaOS2D-Cbf",
            name="name",
            provider="minimax",
        )
        assert_matches_type(VoiceCloneCreateFromUploadResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_from_upload_with_all_params_overload_3(self, async_client: AsyncTelnyx) -> None:
        voice_clone = await async_client.voice_clones.create_from_upload(
            audio_file=b"Example data",
            gender="male",
            language="lkf-Lz1vLbBu-9uDh-9AHaOS2D-Cbf",
            name="name",
            provider="minimax",
            label="label",
            model_id="speech-2.8-turbo",
            ref_text="ref_text",
        )
        assert_matches_type(VoiceCloneCreateFromUploadResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_from_upload_overload_3(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.voice_clones.with_raw_response.create_from_upload(
            audio_file=b"Example data",
            gender="male",
            language="lkf-Lz1vLbBu-9uDh-9AHaOS2D-Cbf",
            name="name",
            provider="minimax",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice_clone = await response.parse()
        assert_matches_type(VoiceCloneCreateFromUploadResponse, voice_clone, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_from_upload_overload_3(self, async_client: AsyncTelnyx) -> None:
        async with async_client.voice_clones.with_streaming_response.create_from_upload(
            audio_file=b"Example data",
            gender="male",
            language="lkf-Lz1vLbBu-9uDh-9AHaOS2D-Cbf",
            name="name",
            provider="minimax",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice_clone = await response.parse()
            assert_matches_type(VoiceCloneCreateFromUploadResponse, voice_clone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download_sample(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/voice_clones/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/sample").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        voice_clone = await async_client.voice_clones.download_sample(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert voice_clone.is_closed
        assert await voice_clone.json() == {"foo": "bar"}
        assert cast(Any, voice_clone.is_closed) is True
        assert isinstance(voice_clone, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download_sample(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/voice_clones/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/sample").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        voice_clone = await async_client.voice_clones.with_raw_response.download_sample(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert voice_clone.is_closed is True
        assert voice_clone.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await voice_clone.json() == {"foo": "bar"}
        assert isinstance(voice_clone, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download_sample(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/voice_clones/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/sample").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.voice_clones.with_streaming_response.download_sample(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as voice_clone:
            assert not voice_clone.is_closed
            assert voice_clone.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await voice_clone.json() == {"foo": "bar"}
            assert cast(Any, voice_clone.is_closed) is True
            assert isinstance(voice_clone, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, voice_clone.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_download_sample(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.voice_clones.with_raw_response.download_sample(
                "",
            )
