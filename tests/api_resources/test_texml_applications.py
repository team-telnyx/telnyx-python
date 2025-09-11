# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    TexmlApplicationListResponse,
    TexmlApplicationCreateResponse,
    TexmlApplicationDeleteResponse,
    TexmlApplicationUpdateResponse,
    TexmlApplicationRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTexmlApplications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        texml_application = client.texml_applications.create(
            friendly_name="call-router",
            voice_url="https://example.com",
        )
        assert_matches_type(TexmlApplicationCreateResponse, texml_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        texml_application = client.texml_applications.create(
            friendly_name="call-router",
            voice_url="https://example.com",
            active=False,
            anchorsite_override="Amsterdam, Netherlands",
            dtmf_type="Inband",
            first_command_timeout=True,
            first_command_timeout_secs=10,
            inbound={
                "channel_limit": 10,
                "shaken_stir_enabled": True,
                "sip_subdomain": "example",
                "sip_subdomain_receive_settings": "only_my_connections",
            },
            outbound={
                "channel_limit": 10,
                "outbound_voice_profile_id": "1293384261075731499",
            },
            status_callback="https://example.com",
            status_callback_method="get",
            tags=["tag1", "tag2"],
            voice_fallback_url="https://fallback.example.com",
            voice_method="get",
        )
        assert_matches_type(TexmlApplicationCreateResponse, texml_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.texml_applications.with_raw_response.create(
            friendly_name="call-router",
            voice_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        texml_application = response.parse()
        assert_matches_type(TexmlApplicationCreateResponse, texml_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.texml_applications.with_streaming_response.create(
            friendly_name="call-router",
            voice_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            texml_application = response.parse()
            assert_matches_type(TexmlApplicationCreateResponse, texml_application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        texml_application = client.texml_applications.retrieve(
            "1293384261075731499",
        )
        assert_matches_type(TexmlApplicationRetrieveResponse, texml_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.texml_applications.with_raw_response.retrieve(
            "1293384261075731499",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        texml_application = response.parse()
        assert_matches_type(TexmlApplicationRetrieveResponse, texml_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.texml_applications.with_streaming_response.retrieve(
            "1293384261075731499",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            texml_application = response.parse()
            assert_matches_type(TexmlApplicationRetrieveResponse, texml_application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.texml_applications.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        texml_application = client.texml_applications.update(
            id="1293384261075731499",
            friendly_name="call-router",
            voice_url="https://example.com",
        )
        assert_matches_type(TexmlApplicationUpdateResponse, texml_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        texml_application = client.texml_applications.update(
            id="1293384261075731499",
            friendly_name="call-router",
            voice_url="https://example.com",
            active=False,
            anchorsite_override="Amsterdam, Netherlands",
            dtmf_type="Inband",
            first_command_timeout=True,
            first_command_timeout_secs=10,
            inbound={
                "channel_limit": 10,
                "shaken_stir_enabled": True,
                "sip_subdomain": "example",
                "sip_subdomain_receive_settings": "only_my_connections",
            },
            outbound={
                "channel_limit": 10,
                "outbound_voice_profile_id": "1293384261075731499",
            },
            status_callback="https://example.com",
            status_callback_method="get",
            tags=["tag1", "tag2"],
            voice_fallback_url="https://fallback.example.com",
            voice_method="get",
        )
        assert_matches_type(TexmlApplicationUpdateResponse, texml_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.texml_applications.with_raw_response.update(
            id="1293384261075731499",
            friendly_name="call-router",
            voice_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        texml_application = response.parse()
        assert_matches_type(TexmlApplicationUpdateResponse, texml_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.texml_applications.with_streaming_response.update(
            id="1293384261075731499",
            friendly_name="call-router",
            voice_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            texml_application = response.parse()
            assert_matches_type(TexmlApplicationUpdateResponse, texml_application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.texml_applications.with_raw_response.update(
                id="",
                friendly_name="call-router",
                voice_url="https://example.com",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        texml_application = client.texml_applications.list()
        assert_matches_type(TexmlApplicationListResponse, texml_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        texml_application = client.texml_applications.list(
            filter={
                "friendly_name": "friendly_name",
                "outbound_voice_profile_id": "1293384261075731499",
            },
            page={
                "number": 1,
                "size": 1,
            },
            sort="friendly_name",
        )
        assert_matches_type(TexmlApplicationListResponse, texml_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.texml_applications.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        texml_application = response.parse()
        assert_matches_type(TexmlApplicationListResponse, texml_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.texml_applications.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            texml_application = response.parse()
            assert_matches_type(TexmlApplicationListResponse, texml_application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        texml_application = client.texml_applications.delete(
            "1293384261075731499",
        )
        assert_matches_type(TexmlApplicationDeleteResponse, texml_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.texml_applications.with_raw_response.delete(
            "1293384261075731499",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        texml_application = response.parse()
        assert_matches_type(TexmlApplicationDeleteResponse, texml_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.texml_applications.with_streaming_response.delete(
            "1293384261075731499",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            texml_application = response.parse()
            assert_matches_type(TexmlApplicationDeleteResponse, texml_application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.texml_applications.with_raw_response.delete(
                "",
            )


class TestAsyncTexmlApplications:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        texml_application = await async_client.texml_applications.create(
            friendly_name="call-router",
            voice_url="https://example.com",
        )
        assert_matches_type(TexmlApplicationCreateResponse, texml_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        texml_application = await async_client.texml_applications.create(
            friendly_name="call-router",
            voice_url="https://example.com",
            active=False,
            anchorsite_override="Amsterdam, Netherlands",
            dtmf_type="Inband",
            first_command_timeout=True,
            first_command_timeout_secs=10,
            inbound={
                "channel_limit": 10,
                "shaken_stir_enabled": True,
                "sip_subdomain": "example",
                "sip_subdomain_receive_settings": "only_my_connections",
            },
            outbound={
                "channel_limit": 10,
                "outbound_voice_profile_id": "1293384261075731499",
            },
            status_callback="https://example.com",
            status_callback_method="get",
            tags=["tag1", "tag2"],
            voice_fallback_url="https://fallback.example.com",
            voice_method="get",
        )
        assert_matches_type(TexmlApplicationCreateResponse, texml_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml_applications.with_raw_response.create(
            friendly_name="call-router",
            voice_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        texml_application = await response.parse()
        assert_matches_type(TexmlApplicationCreateResponse, texml_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml_applications.with_streaming_response.create(
            friendly_name="call-router",
            voice_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            texml_application = await response.parse()
            assert_matches_type(TexmlApplicationCreateResponse, texml_application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        texml_application = await async_client.texml_applications.retrieve(
            "1293384261075731499",
        )
        assert_matches_type(TexmlApplicationRetrieveResponse, texml_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml_applications.with_raw_response.retrieve(
            "1293384261075731499",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        texml_application = await response.parse()
        assert_matches_type(TexmlApplicationRetrieveResponse, texml_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml_applications.with_streaming_response.retrieve(
            "1293384261075731499",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            texml_application = await response.parse()
            assert_matches_type(TexmlApplicationRetrieveResponse, texml_application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.texml_applications.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        texml_application = await async_client.texml_applications.update(
            id="1293384261075731499",
            friendly_name="call-router",
            voice_url="https://example.com",
        )
        assert_matches_type(TexmlApplicationUpdateResponse, texml_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        texml_application = await async_client.texml_applications.update(
            id="1293384261075731499",
            friendly_name="call-router",
            voice_url="https://example.com",
            active=False,
            anchorsite_override="Amsterdam, Netherlands",
            dtmf_type="Inband",
            first_command_timeout=True,
            first_command_timeout_secs=10,
            inbound={
                "channel_limit": 10,
                "shaken_stir_enabled": True,
                "sip_subdomain": "example",
                "sip_subdomain_receive_settings": "only_my_connections",
            },
            outbound={
                "channel_limit": 10,
                "outbound_voice_profile_id": "1293384261075731499",
            },
            status_callback="https://example.com",
            status_callback_method="get",
            tags=["tag1", "tag2"],
            voice_fallback_url="https://fallback.example.com",
            voice_method="get",
        )
        assert_matches_type(TexmlApplicationUpdateResponse, texml_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml_applications.with_raw_response.update(
            id="1293384261075731499",
            friendly_name="call-router",
            voice_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        texml_application = await response.parse()
        assert_matches_type(TexmlApplicationUpdateResponse, texml_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml_applications.with_streaming_response.update(
            id="1293384261075731499",
            friendly_name="call-router",
            voice_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            texml_application = await response.parse()
            assert_matches_type(TexmlApplicationUpdateResponse, texml_application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.texml_applications.with_raw_response.update(
                id="",
                friendly_name="call-router",
                voice_url="https://example.com",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        texml_application = await async_client.texml_applications.list()
        assert_matches_type(TexmlApplicationListResponse, texml_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        texml_application = await async_client.texml_applications.list(
            filter={
                "friendly_name": "friendly_name",
                "outbound_voice_profile_id": "1293384261075731499",
            },
            page={
                "number": 1,
                "size": 1,
            },
            sort="friendly_name",
        )
        assert_matches_type(TexmlApplicationListResponse, texml_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml_applications.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        texml_application = await response.parse()
        assert_matches_type(TexmlApplicationListResponse, texml_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml_applications.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            texml_application = await response.parse()
            assert_matches_type(TexmlApplicationListResponse, texml_application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        texml_application = await async_client.texml_applications.delete(
            "1293384261075731499",
        )
        assert_matches_type(TexmlApplicationDeleteResponse, texml_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.texml_applications.with_raw_response.delete(
            "1293384261075731499",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        texml_application = await response.parse()
        assert_matches_type(TexmlApplicationDeleteResponse, texml_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.texml_applications.with_streaming_response.delete(
            "1293384261075731499",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            texml_application = await response.parse()
            assert_matches_type(TexmlApplicationDeleteResponse, texml_application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.texml_applications.with_raw_response.delete(
                "",
            )
