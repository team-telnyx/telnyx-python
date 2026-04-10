# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.whatsapp.phone_numbers.profile import PhotoUploadResponse, PhotoRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhoto:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        photo = client.whatsapp.phone_numbers.profile.photo.retrieve(
            "phone_number",
        )
        assert_matches_type(PhotoRetrieveResponse, photo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.whatsapp.phone_numbers.profile.photo.with_raw_response.retrieve(
            "phone_number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        photo = response.parse()
        assert_matches_type(PhotoRetrieveResponse, photo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.whatsapp.phone_numbers.profile.photo.with_streaming_response.retrieve(
            "phone_number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            photo = response.parse()
            assert_matches_type(PhotoRetrieveResponse, photo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.whatsapp.phone_numbers.profile.photo.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        photo = client.whatsapp.phone_numbers.profile.photo.delete(
            "phone_number",
        )
        assert photo is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.whatsapp.phone_numbers.profile.photo.with_raw_response.delete(
            "phone_number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        photo = response.parse()
        assert photo is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.whatsapp.phone_numbers.profile.photo.with_streaming_response.delete(
            "phone_number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            photo = response.parse()
            assert photo is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.whatsapp.phone_numbers.profile.photo.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload(self, client: Telnyx) -> None:
        photo = client.whatsapp.phone_numbers.profile.photo.upload(
            phone_number="phone_number",
            file=b"Example data",
        )
        assert_matches_type(PhotoUploadResponse, photo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: Telnyx) -> None:
        response = client.whatsapp.phone_numbers.profile.photo.with_raw_response.upload(
            phone_number="phone_number",
            file=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        photo = response.parse()
        assert_matches_type(PhotoUploadResponse, photo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: Telnyx) -> None:
        with client.whatsapp.phone_numbers.profile.photo.with_streaming_response.upload(
            phone_number="phone_number",
            file=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            photo = response.parse()
            assert_matches_type(PhotoUploadResponse, photo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upload(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.whatsapp.phone_numbers.profile.photo.with_raw_response.upload(
                phone_number="",
                file=b"Example data",
            )


class TestAsyncPhoto:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        photo = await async_client.whatsapp.phone_numbers.profile.photo.retrieve(
            "phone_number",
        )
        assert_matches_type(PhotoRetrieveResponse, photo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.whatsapp.phone_numbers.profile.photo.with_raw_response.retrieve(
            "phone_number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        photo = await response.parse()
        assert_matches_type(PhotoRetrieveResponse, photo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.whatsapp.phone_numbers.profile.photo.with_streaming_response.retrieve(
            "phone_number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            photo = await response.parse()
            assert_matches_type(PhotoRetrieveResponse, photo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.whatsapp.phone_numbers.profile.photo.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        photo = await async_client.whatsapp.phone_numbers.profile.photo.delete(
            "phone_number",
        )
        assert photo is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.whatsapp.phone_numbers.profile.photo.with_raw_response.delete(
            "phone_number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        photo = await response.parse()
        assert photo is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.whatsapp.phone_numbers.profile.photo.with_streaming_response.delete(
            "phone_number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            photo = await response.parse()
            assert photo is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.whatsapp.phone_numbers.profile.photo.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncTelnyx) -> None:
        photo = await async_client.whatsapp.phone_numbers.profile.photo.upload(
            phone_number="phone_number",
            file=b"Example data",
        )
        assert_matches_type(PhotoUploadResponse, photo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.whatsapp.phone_numbers.profile.photo.with_raw_response.upload(
            phone_number="phone_number",
            file=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        photo = await response.parse()
        assert_matches_type(PhotoUploadResponse, photo, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncTelnyx) -> None:
        async with async_client.whatsapp.phone_numbers.profile.photo.with_streaming_response.upload(
            phone_number="phone_number",
            file=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            photo = await response.parse()
            assert_matches_type(PhotoUploadResponse, photo, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upload(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.whatsapp.phone_numbers.profile.photo.with_raw_response.upload(
                phone_number="",
                file=b"Example data",
            )
