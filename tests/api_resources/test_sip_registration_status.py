# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import SipRegistrationStatusRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSipRegistrationStatus:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        sip_registration_status = client.sip_registration_status.retrieve(
            connection_id="connection_id",
            credential_type="uac_external_credential",
            user_id="user_id",
        )
        assert_matches_type(SipRegistrationStatusRetrieveResponse, sip_registration_status, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.sip_registration_status.with_raw_response.retrieve(
            connection_id="connection_id",
            credential_type="uac_external_credential",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sip_registration_status = response.parse()
        assert_matches_type(SipRegistrationStatusRetrieveResponse, sip_registration_status, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.sip_registration_status.with_streaming_response.retrieve(
            connection_id="connection_id",
            credential_type="uac_external_credential",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sip_registration_status = response.parse()
            assert_matches_type(SipRegistrationStatusRetrieveResponse, sip_registration_status, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSipRegistrationStatus:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        sip_registration_status = await async_client.sip_registration_status.retrieve(
            connection_id="connection_id",
            credential_type="uac_external_credential",
            user_id="user_id",
        )
        assert_matches_type(SipRegistrationStatusRetrieveResponse, sip_registration_status, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.sip_registration_status.with_raw_response.retrieve(
            connection_id="connection_id",
            credential_type="uac_external_credential",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sip_registration_status = await response.parse()
        assert_matches_type(SipRegistrationStatusRetrieveResponse, sip_registration_status, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.sip_registration_status.with_streaming_response.retrieve(
            connection_id="connection_id",
            credential_type="uac_external_credential",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sip_registration_status = await response.parse()
            assert_matches_type(SipRegistrationStatusRetrieveResponse, sip_registration_status, path=["response"])

        assert cast(Any, response.is_closed) is True
