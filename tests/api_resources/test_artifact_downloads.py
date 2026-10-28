# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from telnyx import Telnyx, AsyncTelnyx
from telnyx._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestArtifactDownloads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/artifact_downloads/artifactId").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        artifact_download = client.artifact_downloads.retrieve(
            artifact_id="artifactId",
            expires="expires",
            sig="sig",
        )
        assert artifact_download.is_closed
        assert artifact_download.json() == {"foo": "bar"}
        assert cast(Any, artifact_download.is_closed) is True
        assert isinstance(artifact_download, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/artifact_downloads/artifactId").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        artifact_download = client.artifact_downloads.with_raw_response.retrieve(
            artifact_id="artifactId",
            expires="expires",
            sig="sig",
        )

        assert artifact_download.is_closed is True
        assert artifact_download.http_request.headers.get("X-Stainless-Lang") == "python"
        assert artifact_download.json() == {"foo": "bar"}
        assert isinstance(artifact_download, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/artifact_downloads/artifactId").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.artifact_downloads.with_streaming_response.retrieve(
            artifact_id="artifactId",
            expires="expires",
            sig="sig",
        ) as artifact_download:
            assert not artifact_download.is_closed
            assert artifact_download.http_request.headers.get("X-Stainless-Lang") == "python"

            assert artifact_download.json() == {"foo": "bar"}
            assert cast(Any, artifact_download.is_closed) is True
            assert isinstance(artifact_download, StreamedBinaryAPIResponse)

        assert cast(Any, artifact_download.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `artifact_id` but received ''"):
            client.artifact_downloads.with_raw_response.retrieve(
                artifact_id="",
                expires="expires",
                sig="sig",
            )


class TestAsyncArtifactDownloads:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/artifact_downloads/artifactId").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        artifact_download = await async_client.artifact_downloads.retrieve(
            artifact_id="artifactId",
            expires="expires",
            sig="sig",
        )
        assert artifact_download.is_closed
        assert await artifact_download.json() == {"foo": "bar"}
        assert cast(Any, artifact_download.is_closed) is True
        assert isinstance(artifact_download, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/artifact_downloads/artifactId").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        artifact_download = await async_client.artifact_downloads.with_raw_response.retrieve(
            artifact_id="artifactId",
            expires="expires",
            sig="sig",
        )

        assert artifact_download.is_closed is True
        assert artifact_download.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await artifact_download.json() == {"foo": "bar"}
        assert isinstance(artifact_download, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/artifact_downloads/artifactId").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.artifact_downloads.with_streaming_response.retrieve(
            artifact_id="artifactId",
            expires="expires",
            sig="sig",
        ) as artifact_download:
            assert not artifact_download.is_closed
            assert artifact_download.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await artifact_download.json() == {"foo": "bar"}
            assert cast(Any, artifact_download.is_closed) is True
            assert isinstance(artifact_download, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, artifact_download.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `artifact_id` but received ''"):
            await async_client.artifact_downloads.with_raw_response.retrieve(
                artifact_id="",
                expires="expires",
                sig="sig",
            )
