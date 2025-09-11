# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.phone_numbers import (
    VoicemailCreateResponse,
    VoicemailUpdateResponse,
    VoicemailRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVoicemail:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        voicemail = client.phone_numbers.voicemail.create(
            phone_number_id="123455678900",
        )
        assert_matches_type(VoicemailCreateResponse, voicemail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        voicemail = client.phone_numbers.voicemail.create(
            phone_number_id="123455678900",
            enabled=True,
            pin="pin",
        )
        assert_matches_type(VoicemailCreateResponse, voicemail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.phone_numbers.voicemail.with_raw_response.create(
            phone_number_id="123455678900",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voicemail = response.parse()
        assert_matches_type(VoicemailCreateResponse, voicemail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.phone_numbers.voicemail.with_streaming_response.create(
            phone_number_id="123455678900",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voicemail = response.parse()
            assert_matches_type(VoicemailCreateResponse, voicemail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number_id` but received ''"):
            client.phone_numbers.voicemail.with_raw_response.create(
                phone_number_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        voicemail = client.phone_numbers.voicemail.retrieve(
            "phone_number_id",
        )
        assert_matches_type(VoicemailRetrieveResponse, voicemail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.phone_numbers.voicemail.with_raw_response.retrieve(
            "phone_number_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voicemail = response.parse()
        assert_matches_type(VoicemailRetrieveResponse, voicemail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.phone_numbers.voicemail.with_streaming_response.retrieve(
            "phone_number_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voicemail = response.parse()
            assert_matches_type(VoicemailRetrieveResponse, voicemail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number_id` but received ''"):
            client.phone_numbers.voicemail.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        voicemail = client.phone_numbers.voicemail.update(
            phone_number_id="123455678900",
        )
        assert_matches_type(VoicemailUpdateResponse, voicemail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        voicemail = client.phone_numbers.voicemail.update(
            phone_number_id="123455678900",
            enabled=True,
            pin="pin",
        )
        assert_matches_type(VoicemailUpdateResponse, voicemail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.phone_numbers.voicemail.with_raw_response.update(
            phone_number_id="123455678900",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voicemail = response.parse()
        assert_matches_type(VoicemailUpdateResponse, voicemail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.phone_numbers.voicemail.with_streaming_response.update(
            phone_number_id="123455678900",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voicemail = response.parse()
            assert_matches_type(VoicemailUpdateResponse, voicemail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number_id` but received ''"):
            client.phone_numbers.voicemail.with_raw_response.update(
                phone_number_id="",
            )


class TestAsyncVoicemail:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        voicemail = await async_client.phone_numbers.voicemail.create(
            phone_number_id="123455678900",
        )
        assert_matches_type(VoicemailCreateResponse, voicemail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        voicemail = await async_client.phone_numbers.voicemail.create(
            phone_number_id="123455678900",
            enabled=True,
            pin="pin",
        )
        assert_matches_type(VoicemailCreateResponse, voicemail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.phone_numbers.voicemail.with_raw_response.create(
            phone_number_id="123455678900",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voicemail = await response.parse()
        assert_matches_type(VoicemailCreateResponse, voicemail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.phone_numbers.voicemail.with_streaming_response.create(
            phone_number_id="123455678900",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voicemail = await response.parse()
            assert_matches_type(VoicemailCreateResponse, voicemail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number_id` but received ''"):
            await async_client.phone_numbers.voicemail.with_raw_response.create(
                phone_number_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        voicemail = await async_client.phone_numbers.voicemail.retrieve(
            "phone_number_id",
        )
        assert_matches_type(VoicemailRetrieveResponse, voicemail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.phone_numbers.voicemail.with_raw_response.retrieve(
            "phone_number_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voicemail = await response.parse()
        assert_matches_type(VoicemailRetrieveResponse, voicemail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.phone_numbers.voicemail.with_streaming_response.retrieve(
            "phone_number_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voicemail = await response.parse()
            assert_matches_type(VoicemailRetrieveResponse, voicemail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number_id` but received ''"):
            await async_client.phone_numbers.voicemail.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        voicemail = await async_client.phone_numbers.voicemail.update(
            phone_number_id="123455678900",
        )
        assert_matches_type(VoicemailUpdateResponse, voicemail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        voicemail = await async_client.phone_numbers.voicemail.update(
            phone_number_id="123455678900",
            enabled=True,
            pin="pin",
        )
        assert_matches_type(VoicemailUpdateResponse, voicemail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.phone_numbers.voicemail.with_raw_response.update(
            phone_number_id="123455678900",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voicemail = await response.parse()
        assert_matches_type(VoicemailUpdateResponse, voicemail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.phone_numbers.voicemail.with_streaming_response.update(
            phone_number_id="123455678900",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voicemail = await response.parse()
            assert_matches_type(VoicemailUpdateResponse, voicemail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number_id` but received ''"):
            await async_client.phone_numbers.voicemail.with_raw_response.update(
                phone_number_id="",
            )
