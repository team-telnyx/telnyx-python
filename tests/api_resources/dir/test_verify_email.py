# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.dir import (
    VerifyEmailStatusResponse,
    VerifyEmailSendCodeResponse,
    VerifyEmailConfirmCodeResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVerifyEmail:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_confirm_code(self, client: Telnyx) -> None:
        verify_email = client.dir.verify_email.confirm_code(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            code="482915",
        )
        assert_matches_type(VerifyEmailConfirmCodeResponse, verify_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_confirm_code(self, client: Telnyx) -> None:
        response = client.dir.verify_email.with_raw_response.confirm_code(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            code="482915",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verify_email = response.parse()
        assert_matches_type(VerifyEmailConfirmCodeResponse, verify_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_confirm_code(self, client: Telnyx) -> None:
        with client.dir.verify_email.with_streaming_response.confirm_code(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            code="482915",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verify_email = response.parse()
            assert_matches_type(VerifyEmailConfirmCodeResponse, verify_email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_confirm_code(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            client.dir.verify_email.with_raw_response.confirm_code(
                dir_id="",
                code="482915",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_code(self, client: Telnyx) -> None:
        verify_email = client.dir.verify_email.send_code(
            "16635d38-75a6-4481-82e8-69af60e05011",
        )
        assert_matches_type(VerifyEmailSendCodeResponse, verify_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send_code(self, client: Telnyx) -> None:
        response = client.dir.verify_email.with_raw_response.send_code(
            "16635d38-75a6-4481-82e8-69af60e05011",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verify_email = response.parse()
        assert_matches_type(VerifyEmailSendCodeResponse, verify_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send_code(self, client: Telnyx) -> None:
        with client.dir.verify_email.with_streaming_response.send_code(
            "16635d38-75a6-4481-82e8-69af60e05011",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verify_email = response.parse()
            assert_matches_type(VerifyEmailSendCodeResponse, verify_email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_send_code(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            client.dir.verify_email.with_raw_response.send_code(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_status(self, client: Telnyx) -> None:
        verify_email = client.dir.verify_email.status(
            "16635d38-75a6-4481-82e8-69af60e05011",
        )
        assert_matches_type(VerifyEmailStatusResponse, verify_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_status(self, client: Telnyx) -> None:
        response = client.dir.verify_email.with_raw_response.status(
            "16635d38-75a6-4481-82e8-69af60e05011",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verify_email = response.parse()
        assert_matches_type(VerifyEmailStatusResponse, verify_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_status(self, client: Telnyx) -> None:
        with client.dir.verify_email.with_streaming_response.status(
            "16635d38-75a6-4481-82e8-69af60e05011",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verify_email = response.parse()
            assert_matches_type(VerifyEmailStatusResponse, verify_email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_status(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            client.dir.verify_email.with_raw_response.status(
                "",
            )


class TestAsyncVerifyEmail:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_confirm_code(self, async_client: AsyncTelnyx) -> None:
        verify_email = await async_client.dir.verify_email.confirm_code(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            code="482915",
        )
        assert_matches_type(VerifyEmailConfirmCodeResponse, verify_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_confirm_code(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dir.verify_email.with_raw_response.confirm_code(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            code="482915",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verify_email = await response.parse()
        assert_matches_type(VerifyEmailConfirmCodeResponse, verify_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_confirm_code(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dir.verify_email.with_streaming_response.confirm_code(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            code="482915",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verify_email = await response.parse()
            assert_matches_type(VerifyEmailConfirmCodeResponse, verify_email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_confirm_code(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            await async_client.dir.verify_email.with_raw_response.confirm_code(
                dir_id="",
                code="482915",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_code(self, async_client: AsyncTelnyx) -> None:
        verify_email = await async_client.dir.verify_email.send_code(
            "16635d38-75a6-4481-82e8-69af60e05011",
        )
        assert_matches_type(VerifyEmailSendCodeResponse, verify_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send_code(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dir.verify_email.with_raw_response.send_code(
            "16635d38-75a6-4481-82e8-69af60e05011",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verify_email = await response.parse()
        assert_matches_type(VerifyEmailSendCodeResponse, verify_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send_code(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dir.verify_email.with_streaming_response.send_code(
            "16635d38-75a6-4481-82e8-69af60e05011",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verify_email = await response.parse()
            assert_matches_type(VerifyEmailSendCodeResponse, verify_email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_send_code(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            await async_client.dir.verify_email.with_raw_response.send_code(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_status(self, async_client: AsyncTelnyx) -> None:
        verify_email = await async_client.dir.verify_email.status(
            "16635d38-75a6-4481-82e8-69af60e05011",
        )
        assert_matches_type(VerifyEmailStatusResponse, verify_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_status(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dir.verify_email.with_raw_response.status(
            "16635d38-75a6-4481-82e8-69af60e05011",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verify_email = await response.parse()
        assert_matches_type(VerifyEmailStatusResponse, verify_email, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dir.verify_email.with_streaming_response.status(
            "16635d38-75a6-4481-82e8-69af60e05011",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verify_email = await response.parse()
            assert_matches_type(VerifyEmailStatusResponse, verify_email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_status(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            await async_client.dir.verify_email.with_raw_response.status(
                "",
            )
