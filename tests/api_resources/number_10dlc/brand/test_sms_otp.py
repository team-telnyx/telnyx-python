# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.number_10dlc.brand import (
    SMSOtpTriggerResponse,
    SMSOtpGetStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSMSOtp:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_status(self, client: Telnyx) -> None:
        sms_otp = client.number_10dlc.brand.sms_otp.get_status(
            reference_id="OTP4B2001",
        )
        assert_matches_type(SMSOtpGetStatusResponse, sms_otp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_status_with_all_params(self, client: Telnyx) -> None:
        sms_otp = client.number_10dlc.brand.sms_otp.get_status(
            reference_id="OTP4B2001",
            brand_id="B123ABC",
        )
        assert_matches_type(SMSOtpGetStatusResponse, sms_otp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_status(self, client: Telnyx) -> None:
        response = client.number_10dlc.brand.sms_otp.with_raw_response.get_status(
            reference_id="OTP4B2001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sms_otp = response.parse()
        assert_matches_type(SMSOtpGetStatusResponse, sms_otp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_status(self, client: Telnyx) -> None:
        with client.number_10dlc.brand.sms_otp.with_streaming_response.get_status(
            reference_id="OTP4B2001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sms_otp = response.parse()
            assert_matches_type(SMSOtpGetStatusResponse, sms_otp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_status(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reference_id` but received ''"):
            client.number_10dlc.brand.sms_otp.with_raw_response.get_status(
                reference_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_trigger(self, client: Telnyx) -> None:
        sms_otp = client.number_10dlc.brand.sms_otp.trigger(
            brand_id="4b20019b-043a-78f8-0657-b3be3f4b4002",
            pin_sms="Your PIN is @OTP_PIN@",
            success_sms="Verification successful!",
        )
        assert_matches_type(SMSOtpTriggerResponse, sms_otp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_trigger(self, client: Telnyx) -> None:
        response = client.number_10dlc.brand.sms_otp.with_raw_response.trigger(
            brand_id="4b20019b-043a-78f8-0657-b3be3f4b4002",
            pin_sms="Your PIN is @OTP_PIN@",
            success_sms="Verification successful!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sms_otp = response.parse()
        assert_matches_type(SMSOtpTriggerResponse, sms_otp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_trigger(self, client: Telnyx) -> None:
        with client.number_10dlc.brand.sms_otp.with_streaming_response.trigger(
            brand_id="4b20019b-043a-78f8-0657-b3be3f4b4002",
            pin_sms="Your PIN is @OTP_PIN@",
            success_sms="Verification successful!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sms_otp = response.parse()
            assert_matches_type(SMSOtpTriggerResponse, sms_otp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_trigger(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            client.number_10dlc.brand.sms_otp.with_raw_response.trigger(
                brand_id="",
                pin_sms="Your PIN is @OTP_PIN@",
                success_sms="Verification successful!",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_verify(self, client: Telnyx) -> None:
        sms_otp = client.number_10dlc.brand.sms_otp.verify(
            brand_id="4b20019b-043a-78f8-0657-b3be3f4b4002",
            otp_pin="123456",
        )
        assert sms_otp is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_verify(self, client: Telnyx) -> None:
        response = client.number_10dlc.brand.sms_otp.with_raw_response.verify(
            brand_id="4b20019b-043a-78f8-0657-b3be3f4b4002",
            otp_pin="123456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sms_otp = response.parse()
        assert sms_otp is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_verify(self, client: Telnyx) -> None:
        with client.number_10dlc.brand.sms_otp.with_streaming_response.verify(
            brand_id="4b20019b-043a-78f8-0657-b3be3f4b4002",
            otp_pin="123456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sms_otp = response.parse()
            assert sms_otp is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_verify(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            client.number_10dlc.brand.sms_otp.with_raw_response.verify(
                brand_id="",
                otp_pin="123456",
            )


class TestAsyncSMSOtp:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_status(self, async_client: AsyncTelnyx) -> None:
        sms_otp = await async_client.number_10dlc.brand.sms_otp.get_status(
            reference_id="OTP4B2001",
        )
        assert_matches_type(SMSOtpGetStatusResponse, sms_otp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_status_with_all_params(self, async_client: AsyncTelnyx) -> None:
        sms_otp = await async_client.number_10dlc.brand.sms_otp.get_status(
            reference_id="OTP4B2001",
            brand_id="B123ABC",
        )
        assert_matches_type(SMSOtpGetStatusResponse, sms_otp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_10dlc.brand.sms_otp.with_raw_response.get_status(
            reference_id="OTP4B2001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sms_otp = await response.parse()
        assert_matches_type(SMSOtpGetStatusResponse, sms_otp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_10dlc.brand.sms_otp.with_streaming_response.get_status(
            reference_id="OTP4B2001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sms_otp = await response.parse()
            assert_matches_type(SMSOtpGetStatusResponse, sms_otp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_status(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reference_id` but received ''"):
            await async_client.number_10dlc.brand.sms_otp.with_raw_response.get_status(
                reference_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_trigger(self, async_client: AsyncTelnyx) -> None:
        sms_otp = await async_client.number_10dlc.brand.sms_otp.trigger(
            brand_id="4b20019b-043a-78f8-0657-b3be3f4b4002",
            pin_sms="Your PIN is @OTP_PIN@",
            success_sms="Verification successful!",
        )
        assert_matches_type(SMSOtpTriggerResponse, sms_otp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_trigger(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_10dlc.brand.sms_otp.with_raw_response.trigger(
            brand_id="4b20019b-043a-78f8-0657-b3be3f4b4002",
            pin_sms="Your PIN is @OTP_PIN@",
            success_sms="Verification successful!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sms_otp = await response.parse()
        assert_matches_type(SMSOtpTriggerResponse, sms_otp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_trigger(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_10dlc.brand.sms_otp.with_streaming_response.trigger(
            brand_id="4b20019b-043a-78f8-0657-b3be3f4b4002",
            pin_sms="Your PIN is @OTP_PIN@",
            success_sms="Verification successful!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sms_otp = await response.parse()
            assert_matches_type(SMSOtpTriggerResponse, sms_otp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_trigger(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            await async_client.number_10dlc.brand.sms_otp.with_raw_response.trigger(
                brand_id="",
                pin_sms="Your PIN is @OTP_PIN@",
                success_sms="Verification successful!",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_verify(self, async_client: AsyncTelnyx) -> None:
        sms_otp = await async_client.number_10dlc.brand.sms_otp.verify(
            brand_id="4b20019b-043a-78f8-0657-b3be3f4b4002",
            otp_pin="123456",
        )
        assert sms_otp is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_verify(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.number_10dlc.brand.sms_otp.with_raw_response.verify(
            brand_id="4b20019b-043a-78f8-0657-b3be3f4b4002",
            otp_pin="123456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sms_otp = await response.parse()
        assert sms_otp is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_verify(self, async_client: AsyncTelnyx) -> None:
        async with async_client.number_10dlc.brand.sms_otp.with_streaming_response.verify(
            brand_id="4b20019b-043a-78f8-0657-b3be3f4b4002",
            otp_pin="123456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sms_otp = await response.parse()
            assert sms_otp is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_verify(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            await async_client.number_10dlc.brand.sms_otp.with_raw_response.verify(
                brand_id="",
                otp_pin="123456",
            )
