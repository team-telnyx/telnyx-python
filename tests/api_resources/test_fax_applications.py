# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    FaxApplicationListResponse,
    FaxApplicationCreateResponse,
    FaxApplicationDeleteResponse,
    FaxApplicationUpdateResponse,
    FaxApplicationRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFaxApplications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        fax_application = client.fax_applications.create(
            application_name="fax-router",
            webhook_event_url="https://example.com",
        )
        assert_matches_type(FaxApplicationCreateResponse, fax_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        fax_application = client.fax_applications.create(
            application_name="fax-router",
            webhook_event_url="https://example.com",
            active=False,
            anchorsite_override="Amsterdam, Netherlands",
            inbound={
                "channel_limit": 10,
                "sip_subdomain": "example",
                "sip_subdomain_receive_settings": "only_my_connections",
            },
            outbound={
                "channel_limit": 10,
                "outbound_voice_profile_id": "1293384261075731499",
            },
            tags=["tag1", "tag2"],
            webhook_event_failover_url="https://failover.example.com",
            webhook_timeout_secs=25,
        )
        assert_matches_type(FaxApplicationCreateResponse, fax_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.fax_applications.with_raw_response.create(
            application_name="fax-router",
            webhook_event_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fax_application = response.parse()
        assert_matches_type(FaxApplicationCreateResponse, fax_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.fax_applications.with_streaming_response.create(
            application_name="fax-router",
            webhook_event_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fax_application = response.parse()
            assert_matches_type(FaxApplicationCreateResponse, fax_application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        fax_application = client.fax_applications.retrieve(
            "1293384261075731499",
        )
        assert_matches_type(FaxApplicationRetrieveResponse, fax_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.fax_applications.with_raw_response.retrieve(
            "1293384261075731499",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fax_application = response.parse()
        assert_matches_type(FaxApplicationRetrieveResponse, fax_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.fax_applications.with_streaming_response.retrieve(
            "1293384261075731499",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fax_application = response.parse()
            assert_matches_type(FaxApplicationRetrieveResponse, fax_application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.fax_applications.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        fax_application = client.fax_applications.update(
            id="1293384261075731499",
            application_name="fax-router",
            webhook_event_url="https://example.com",
        )
        assert_matches_type(FaxApplicationUpdateResponse, fax_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        fax_application = client.fax_applications.update(
            id="1293384261075731499",
            application_name="fax-router",
            webhook_event_url="https://example.com",
            active=False,
            anchorsite_override="Amsterdam, Netherlands",
            fax_email_recipient="user@example.com",
            inbound={
                "channel_limit": 10,
                "sip_subdomain": "example",
                "sip_subdomain_receive_settings": "only_my_connections",
            },
            outbound={
                "channel_limit": 10,
                "outbound_voice_profile_id": "1293384261075731499",
            },
            tags=["tag1", "tag2"],
            webhook_event_failover_url="https://failover.example.com",
            webhook_timeout_secs=25,
        )
        assert_matches_type(FaxApplicationUpdateResponse, fax_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.fax_applications.with_raw_response.update(
            id="1293384261075731499",
            application_name="fax-router",
            webhook_event_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fax_application = response.parse()
        assert_matches_type(FaxApplicationUpdateResponse, fax_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.fax_applications.with_streaming_response.update(
            id="1293384261075731499",
            application_name="fax-router",
            webhook_event_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fax_application = response.parse()
            assert_matches_type(FaxApplicationUpdateResponse, fax_application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.fax_applications.with_raw_response.update(
                id="",
                application_name="fax-router",
                webhook_event_url="https://example.com",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        fax_application = client.fax_applications.list()
        assert_matches_type(FaxApplicationListResponse, fax_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        fax_application = client.fax_applications.list(
            filter={
                "application_name": {"contains": "fax-app"},
                "outbound_voice_profile_id": "1293384261075731499",
            },
            page={
                "number": 1,
                "size": 1,
            },
            sort="application_name",
        )
        assert_matches_type(FaxApplicationListResponse, fax_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.fax_applications.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fax_application = response.parse()
        assert_matches_type(FaxApplicationListResponse, fax_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.fax_applications.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fax_application = response.parse()
            assert_matches_type(FaxApplicationListResponse, fax_application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        fax_application = client.fax_applications.delete(
            "1293384261075731499",
        )
        assert_matches_type(FaxApplicationDeleteResponse, fax_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.fax_applications.with_raw_response.delete(
            "1293384261075731499",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fax_application = response.parse()
        assert_matches_type(FaxApplicationDeleteResponse, fax_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.fax_applications.with_streaming_response.delete(
            "1293384261075731499",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fax_application = response.parse()
            assert_matches_type(FaxApplicationDeleteResponse, fax_application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.fax_applications.with_raw_response.delete(
                "",
            )


class TestAsyncFaxApplications:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        fax_application = await async_client.fax_applications.create(
            application_name="fax-router",
            webhook_event_url="https://example.com",
        )
        assert_matches_type(FaxApplicationCreateResponse, fax_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        fax_application = await async_client.fax_applications.create(
            application_name="fax-router",
            webhook_event_url="https://example.com",
            active=False,
            anchorsite_override="Amsterdam, Netherlands",
            inbound={
                "channel_limit": 10,
                "sip_subdomain": "example",
                "sip_subdomain_receive_settings": "only_my_connections",
            },
            outbound={
                "channel_limit": 10,
                "outbound_voice_profile_id": "1293384261075731499",
            },
            tags=["tag1", "tag2"],
            webhook_event_failover_url="https://failover.example.com",
            webhook_timeout_secs=25,
        )
        assert_matches_type(FaxApplicationCreateResponse, fax_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.fax_applications.with_raw_response.create(
            application_name="fax-router",
            webhook_event_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fax_application = await response.parse()
        assert_matches_type(FaxApplicationCreateResponse, fax_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.fax_applications.with_streaming_response.create(
            application_name="fax-router",
            webhook_event_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fax_application = await response.parse()
            assert_matches_type(FaxApplicationCreateResponse, fax_application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        fax_application = await async_client.fax_applications.retrieve(
            "1293384261075731499",
        )
        assert_matches_type(FaxApplicationRetrieveResponse, fax_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.fax_applications.with_raw_response.retrieve(
            "1293384261075731499",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fax_application = await response.parse()
        assert_matches_type(FaxApplicationRetrieveResponse, fax_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.fax_applications.with_streaming_response.retrieve(
            "1293384261075731499",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fax_application = await response.parse()
            assert_matches_type(FaxApplicationRetrieveResponse, fax_application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.fax_applications.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        fax_application = await async_client.fax_applications.update(
            id="1293384261075731499",
            application_name="fax-router",
            webhook_event_url="https://example.com",
        )
        assert_matches_type(FaxApplicationUpdateResponse, fax_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        fax_application = await async_client.fax_applications.update(
            id="1293384261075731499",
            application_name="fax-router",
            webhook_event_url="https://example.com",
            active=False,
            anchorsite_override="Amsterdam, Netherlands",
            fax_email_recipient="user@example.com",
            inbound={
                "channel_limit": 10,
                "sip_subdomain": "example",
                "sip_subdomain_receive_settings": "only_my_connections",
            },
            outbound={
                "channel_limit": 10,
                "outbound_voice_profile_id": "1293384261075731499",
            },
            tags=["tag1", "tag2"],
            webhook_event_failover_url="https://failover.example.com",
            webhook_timeout_secs=25,
        )
        assert_matches_type(FaxApplicationUpdateResponse, fax_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.fax_applications.with_raw_response.update(
            id="1293384261075731499",
            application_name="fax-router",
            webhook_event_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fax_application = await response.parse()
        assert_matches_type(FaxApplicationUpdateResponse, fax_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.fax_applications.with_streaming_response.update(
            id="1293384261075731499",
            application_name="fax-router",
            webhook_event_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fax_application = await response.parse()
            assert_matches_type(FaxApplicationUpdateResponse, fax_application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.fax_applications.with_raw_response.update(
                id="",
                application_name="fax-router",
                webhook_event_url="https://example.com",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        fax_application = await async_client.fax_applications.list()
        assert_matches_type(FaxApplicationListResponse, fax_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        fax_application = await async_client.fax_applications.list(
            filter={
                "application_name": {"contains": "fax-app"},
                "outbound_voice_profile_id": "1293384261075731499",
            },
            page={
                "number": 1,
                "size": 1,
            },
            sort="application_name",
        )
        assert_matches_type(FaxApplicationListResponse, fax_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.fax_applications.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fax_application = await response.parse()
        assert_matches_type(FaxApplicationListResponse, fax_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.fax_applications.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fax_application = await response.parse()
            assert_matches_type(FaxApplicationListResponse, fax_application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        fax_application = await async_client.fax_applications.delete(
            "1293384261075731499",
        )
        assert_matches_type(FaxApplicationDeleteResponse, fax_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.fax_applications.with_raw_response.delete(
            "1293384261075731499",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fax_application = await response.parse()
        assert_matches_type(FaxApplicationDeleteResponse, fax_application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.fax_applications.with_streaming_response.delete(
            "1293384261075731499",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fax_application = await response.parse()
            assert_matches_type(FaxApplicationDeleteResponse, fax_application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.fax_applications.with_raw_response.delete(
                "",
            )
