# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    TelephonyCredentialListResponse,
    TelephonyCredentialCreateResponse,
    TelephonyCredentialDeleteResponse,
    TelephonyCredentialUpdateResponse,
    TelephonyCredentialRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTelephonyCredentials:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        telephony_credential = client.telephony_credentials.create(
            connection_id="1234567890",
        )
        assert_matches_type(TelephonyCredentialCreateResponse, telephony_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        telephony_credential = client.telephony_credentials.create(
            connection_id="1234567890",
            expires_at="2018-02-02T22:25:27.521Z",
            name="My-new-credential",
            tag="some_tag",
        )
        assert_matches_type(TelephonyCredentialCreateResponse, telephony_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.telephony_credentials.with_raw_response.create(
            connection_id="1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telephony_credential = response.parse()
        assert_matches_type(TelephonyCredentialCreateResponse, telephony_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.telephony_credentials.with_streaming_response.create(
            connection_id="1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telephony_credential = response.parse()
            assert_matches_type(TelephonyCredentialCreateResponse, telephony_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        telephony_credential = client.telephony_credentials.retrieve(
            "id",
        )
        assert_matches_type(TelephonyCredentialRetrieveResponse, telephony_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.telephony_credentials.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telephony_credential = response.parse()
        assert_matches_type(TelephonyCredentialRetrieveResponse, telephony_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.telephony_credentials.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telephony_credential = response.parse()
            assert_matches_type(TelephonyCredentialRetrieveResponse, telephony_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.telephony_credentials.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        telephony_credential = client.telephony_credentials.update(
            id="id",
        )
        assert_matches_type(TelephonyCredentialUpdateResponse, telephony_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        telephony_credential = client.telephony_credentials.update(
            id="id",
            connection_id="987654321",
            expires_at="2018-02-02T22:25:27.521Z",
            name="My-new-updated-credential",
            tag="some_tag",
        )
        assert_matches_type(TelephonyCredentialUpdateResponse, telephony_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.telephony_credentials.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telephony_credential = response.parse()
        assert_matches_type(TelephonyCredentialUpdateResponse, telephony_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.telephony_credentials.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telephony_credential = response.parse()
            assert_matches_type(TelephonyCredentialUpdateResponse, telephony_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.telephony_credentials.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        telephony_credential = client.telephony_credentials.list()
        assert_matches_type(TelephonyCredentialListResponse, telephony_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        telephony_credential = client.telephony_credentials.list(
            filter={
                "name": "name",
                "resource_id": "resource_id",
                "sip_username": "sip_username",
                "status": "status",
                "tag": "tag",
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(TelephonyCredentialListResponse, telephony_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.telephony_credentials.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telephony_credential = response.parse()
        assert_matches_type(TelephonyCredentialListResponse, telephony_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.telephony_credentials.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telephony_credential = response.parse()
            assert_matches_type(TelephonyCredentialListResponse, telephony_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        telephony_credential = client.telephony_credentials.delete(
            "id",
        )
        assert_matches_type(TelephonyCredentialDeleteResponse, telephony_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.telephony_credentials.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telephony_credential = response.parse()
        assert_matches_type(TelephonyCredentialDeleteResponse, telephony_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.telephony_credentials.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telephony_credential = response.parse()
            assert_matches_type(TelephonyCredentialDeleteResponse, telephony_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.telephony_credentials.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_token(self, client: Telnyx) -> None:
        telephony_credential = client.telephony_credentials.create_token(
            "id",
        )
        assert_matches_type(str, telephony_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_token(self, client: Telnyx) -> None:
        response = client.telephony_credentials.with_raw_response.create_token(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telephony_credential = response.parse()
        assert_matches_type(str, telephony_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_token(self, client: Telnyx) -> None:
        with client.telephony_credentials.with_streaming_response.create_token(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telephony_credential = response.parse()
            assert_matches_type(str, telephony_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_token(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.telephony_credentials.with_raw_response.create_token(
                "",
            )


class TestAsyncTelephonyCredentials:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        telephony_credential = await async_client.telephony_credentials.create(
            connection_id="1234567890",
        )
        assert_matches_type(TelephonyCredentialCreateResponse, telephony_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        telephony_credential = await async_client.telephony_credentials.create(
            connection_id="1234567890",
            expires_at="2018-02-02T22:25:27.521Z",
            name="My-new-credential",
            tag="some_tag",
        )
        assert_matches_type(TelephonyCredentialCreateResponse, telephony_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.telephony_credentials.with_raw_response.create(
            connection_id="1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telephony_credential = await response.parse()
        assert_matches_type(TelephonyCredentialCreateResponse, telephony_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.telephony_credentials.with_streaming_response.create(
            connection_id="1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telephony_credential = await response.parse()
            assert_matches_type(TelephonyCredentialCreateResponse, telephony_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        telephony_credential = await async_client.telephony_credentials.retrieve(
            "id",
        )
        assert_matches_type(TelephonyCredentialRetrieveResponse, telephony_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.telephony_credentials.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telephony_credential = await response.parse()
        assert_matches_type(TelephonyCredentialRetrieveResponse, telephony_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.telephony_credentials.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telephony_credential = await response.parse()
            assert_matches_type(TelephonyCredentialRetrieveResponse, telephony_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.telephony_credentials.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        telephony_credential = await async_client.telephony_credentials.update(
            id="id",
        )
        assert_matches_type(TelephonyCredentialUpdateResponse, telephony_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        telephony_credential = await async_client.telephony_credentials.update(
            id="id",
            connection_id="987654321",
            expires_at="2018-02-02T22:25:27.521Z",
            name="My-new-updated-credential",
            tag="some_tag",
        )
        assert_matches_type(TelephonyCredentialUpdateResponse, telephony_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.telephony_credentials.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telephony_credential = await response.parse()
        assert_matches_type(TelephonyCredentialUpdateResponse, telephony_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.telephony_credentials.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telephony_credential = await response.parse()
            assert_matches_type(TelephonyCredentialUpdateResponse, telephony_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.telephony_credentials.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        telephony_credential = await async_client.telephony_credentials.list()
        assert_matches_type(TelephonyCredentialListResponse, telephony_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        telephony_credential = await async_client.telephony_credentials.list(
            filter={
                "name": "name",
                "resource_id": "resource_id",
                "sip_username": "sip_username",
                "status": "status",
                "tag": "tag",
            },
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(TelephonyCredentialListResponse, telephony_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.telephony_credentials.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telephony_credential = await response.parse()
        assert_matches_type(TelephonyCredentialListResponse, telephony_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.telephony_credentials.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telephony_credential = await response.parse()
            assert_matches_type(TelephonyCredentialListResponse, telephony_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        telephony_credential = await async_client.telephony_credentials.delete(
            "id",
        )
        assert_matches_type(TelephonyCredentialDeleteResponse, telephony_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.telephony_credentials.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telephony_credential = await response.parse()
        assert_matches_type(TelephonyCredentialDeleteResponse, telephony_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.telephony_credentials.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telephony_credential = await response.parse()
            assert_matches_type(TelephonyCredentialDeleteResponse, telephony_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.telephony_credentials.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_token(self, async_client: AsyncTelnyx) -> None:
        telephony_credential = await async_client.telephony_credentials.create_token(
            "id",
        )
        assert_matches_type(str, telephony_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_token(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.telephony_credentials.with_raw_response.create_token(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telephony_credential = await response.parse()
        assert_matches_type(str, telephony_credential, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_token(self, async_client: AsyncTelnyx) -> None:
        async with async_client.telephony_credentials.with_streaming_response.create_token(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telephony_credential = await response.parse()
            assert_matches_type(str, telephony_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_token(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.telephony_credentials.with_raw_response.create_token(
                "",
            )
