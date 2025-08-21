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
    MediaListResponse,
    MediaUpdateResponse,
    MediaUploadResponse,
    MediaRetrieveResponse,
)
from telnyx._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMedia:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        media = client.media.retrieve(
            "media_name",
        )
        assert_matches_type(MediaRetrieveResponse, media, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.media.with_raw_response.retrieve(
            "media_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = response.parse()
        assert_matches_type(MediaRetrieveResponse, media, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.media.with_streaming_response.retrieve(
            "media_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = response.parse()
            assert_matches_type(MediaRetrieveResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `media_name` but received ''"):
            client.media.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        media = client.media.update(
            media_name="media_name",
        )
        assert_matches_type(MediaUpdateResponse, media, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        media = client.media.update(
            media_name="media_name",
            media_url="http://www.example.com/audio.mp3",
            ttl_secs=86400,
        )
        assert_matches_type(MediaUpdateResponse, media, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.media.with_raw_response.update(
            media_name="media_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = response.parse()
        assert_matches_type(MediaUpdateResponse, media, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.media.with_streaming_response.update(
            media_name="media_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = response.parse()
            assert_matches_type(MediaUpdateResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `media_name` but received ''"):
            client.media.with_raw_response.update(
                media_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        media = client.media.list()
        assert_matches_type(MediaListResponse, media, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        media = client.media.list(
            filter={"content_type": ["application_xml"]},
        )
        assert_matches_type(MediaListResponse, media, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.media.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = response.parse()
        assert_matches_type(MediaListResponse, media, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.media.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = response.parse()
            assert_matches_type(MediaListResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        media = client.media.delete(
            "media_name",
        )
        assert media is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.media.with_raw_response.delete(
            "media_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = response.parse()
        assert media is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.media.with_streaming_response.delete(
            "media_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = response.parse()
            assert media is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `media_name` but received ''"):
            client.media.with_raw_response.delete(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/media/media_name/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        media = client.media.download(
            "media_name",
        )
        assert media.is_closed
        assert media.json() == {"foo": "bar"}
        assert cast(Any, media.is_closed) is True
        assert isinstance(media, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/media/media_name/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        media = client.media.with_raw_response.download(
            "media_name",
        )

        assert media.is_closed is True
        assert media.http_request.headers.get("X-Stainless-Lang") == "python"
        assert media.json() == {"foo": "bar"}
        assert isinstance(media, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/media/media_name/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.media.with_streaming_response.download(
            "media_name",
        ) as media:
            assert not media.is_closed
            assert media.http_request.headers.get("X-Stainless-Lang") == "python"

            assert media.json() == {"foo": "bar"}
            assert cast(Any, media.is_closed) is True
            assert isinstance(media, StreamedBinaryAPIResponse)

        assert cast(Any, media.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_download(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `media_name` but received ''"):
            client.media.with_raw_response.download(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload(self, client: Telnyx) -> None:
        media = client.media.upload(
            media_url="http://www.example.com/audio.mp3",
        )
        assert_matches_type(MediaUploadResponse, media, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_with_all_params(self, client: Telnyx) -> None:
        media = client.media.upload(
            media_url="http://www.example.com/audio.mp3",
            media_name="my-file",
            ttl_secs=86400,
        )
        assert_matches_type(MediaUploadResponse, media, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: Telnyx) -> None:
        response = client.media.with_raw_response.upload(
            media_url="http://www.example.com/audio.mp3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = response.parse()
        assert_matches_type(MediaUploadResponse, media, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: Telnyx) -> None:
        with client.media.with_streaming_response.upload(
            media_url="http://www.example.com/audio.mp3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = response.parse()
            assert_matches_type(MediaUploadResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMedia:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        media = await async_client.media.retrieve(
            "media_name",
        )
        assert_matches_type(MediaRetrieveResponse, media, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.media.with_raw_response.retrieve(
            "media_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = await response.parse()
        assert_matches_type(MediaRetrieveResponse, media, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.media.with_streaming_response.retrieve(
            "media_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = await response.parse()
            assert_matches_type(MediaRetrieveResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `media_name` but received ''"):
            await async_client.media.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        media = await async_client.media.update(
            media_name="media_name",
        )
        assert_matches_type(MediaUpdateResponse, media, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        media = await async_client.media.update(
            media_name="media_name",
            media_url="http://www.example.com/audio.mp3",
            ttl_secs=86400,
        )
        assert_matches_type(MediaUpdateResponse, media, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.media.with_raw_response.update(
            media_name="media_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = await response.parse()
        assert_matches_type(MediaUpdateResponse, media, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.media.with_streaming_response.update(
            media_name="media_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = await response.parse()
            assert_matches_type(MediaUpdateResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `media_name` but received ''"):
            await async_client.media.with_raw_response.update(
                media_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        media = await async_client.media.list()
        assert_matches_type(MediaListResponse, media, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        media = await async_client.media.list(
            filter={"content_type": ["application_xml"]},
        )
        assert_matches_type(MediaListResponse, media, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.media.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = await response.parse()
        assert_matches_type(MediaListResponse, media, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.media.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = await response.parse()
            assert_matches_type(MediaListResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        media = await async_client.media.delete(
            "media_name",
        )
        assert media is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.media.with_raw_response.delete(
            "media_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = await response.parse()
        assert media is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.media.with_streaming_response.delete(
            "media_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = await response.parse()
            assert media is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `media_name` but received ''"):
            await async_client.media.with_raw_response.delete(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/media/media_name/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        media = await async_client.media.download(
            "media_name",
        )
        assert media.is_closed
        assert await media.json() == {"foo": "bar"}
        assert cast(Any, media.is_closed) is True
        assert isinstance(media, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/media/media_name/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        media = await async_client.media.with_raw_response.download(
            "media_name",
        )

        assert media.is_closed is True
        assert media.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await media.json() == {"foo": "bar"}
        assert isinstance(media, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/media/media_name/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.media.with_streaming_response.download(
            "media_name",
        ) as media:
            assert not media.is_closed
            assert media.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await media.json() == {"foo": "bar"}
            assert cast(Any, media.is_closed) is True
            assert isinstance(media, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, media.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_download(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `media_name` but received ''"):
            await async_client.media.with_raw_response.download(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncTelnyx) -> None:
        media = await async_client.media.upload(
            media_url="http://www.example.com/audio.mp3",
        )
        assert_matches_type(MediaUploadResponse, media, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncTelnyx) -> None:
        media = await async_client.media.upload(
            media_url="http://www.example.com/audio.mp3",
            media_name="my-file",
            ttl_secs=86400,
        )
        assert_matches_type(MediaUploadResponse, media, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.media.with_raw_response.upload(
            media_url="http://www.example.com/audio.mp3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = await response.parse()
        assert_matches_type(MediaUploadResponse, media, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncTelnyx) -> None:
        async with async_client.media.with_streaming_response.upload(
            media_url="http://www.example.com/audio.mp3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = await response.parse()
            assert_matches_type(MediaUploadResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True
