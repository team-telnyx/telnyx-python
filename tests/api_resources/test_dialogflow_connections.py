# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    DialogflowConnectionCreateResponse,
    DialogflowConnectionUpdateResponse,
    DialogflowConnectionRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDialogflowConnections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        dialogflow_connection = client.dialogflow_connections.create(
            connection_id="connection_id",
            service_account={
                "type": "bar",
                "project_id": "bar",
                "private_key_id": "bar",
                "private_key": "bar",
                "client_email": "bar",
                "client_id": "bar",
                "auth_uri": "bar",
                "token_uri": "bar",
                "auth_provider_x509_cert_url": "bar",
                "client_x509_cert_url": "bar",
            },
        )
        assert_matches_type(DialogflowConnectionCreateResponse, dialogflow_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        dialogflow_connection = client.dialogflow_connections.create(
            connection_id="connection_id",
            service_account={
                "type": "bar",
                "project_id": "bar",
                "private_key_id": "bar",
                "private_key": "bar",
                "client_email": "bar",
                "client_id": "bar",
                "auth_uri": "bar",
                "token_uri": "bar",
                "auth_provider_x509_cert_url": "bar",
                "client_x509_cert_url": "bar",
            },
            conversation_profile_id="a-VMHLWzTmKjiJw5S6O0-w",
            dialogflow_api="cx",
            environment="development",
            location="global",
        )
        assert_matches_type(DialogflowConnectionCreateResponse, dialogflow_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.dialogflow_connections.with_raw_response.create(
            connection_id="connection_id",
            service_account={
                "type": "bar",
                "project_id": "bar",
                "private_key_id": "bar",
                "private_key": "bar",
                "client_email": "bar",
                "client_id": "bar",
                "auth_uri": "bar",
                "token_uri": "bar",
                "auth_provider_x509_cert_url": "bar",
                "client_x509_cert_url": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dialogflow_connection = response.parse()
        assert_matches_type(DialogflowConnectionCreateResponse, dialogflow_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.dialogflow_connections.with_streaming_response.create(
            connection_id="connection_id",
            service_account={
                "type": "bar",
                "project_id": "bar",
                "private_key_id": "bar",
                "private_key": "bar",
                "client_email": "bar",
                "client_id": "bar",
                "auth_uri": "bar",
                "token_uri": "bar",
                "auth_provider_x509_cert_url": "bar",
                "client_x509_cert_url": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dialogflow_connection = response.parse()
            assert_matches_type(DialogflowConnectionCreateResponse, dialogflow_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.dialogflow_connections.with_raw_response.create(
                connection_id="",
                service_account={
                    "type": "bar",
                    "project_id": "bar",
                    "private_key_id": "bar",
                    "private_key": "bar",
                    "client_email": "bar",
                    "client_id": "bar",
                    "auth_uri": "bar",
                    "token_uri": "bar",
                    "auth_provider_x509_cert_url": "bar",
                    "client_x509_cert_url": "bar",
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        dialogflow_connection = client.dialogflow_connections.retrieve(
            "connection_id",
        )
        assert_matches_type(DialogflowConnectionRetrieveResponse, dialogflow_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.dialogflow_connections.with_raw_response.retrieve(
            "connection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dialogflow_connection = response.parse()
        assert_matches_type(DialogflowConnectionRetrieveResponse, dialogflow_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.dialogflow_connections.with_streaming_response.retrieve(
            "connection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dialogflow_connection = response.parse()
            assert_matches_type(DialogflowConnectionRetrieveResponse, dialogflow_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.dialogflow_connections.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        dialogflow_connection = client.dialogflow_connections.update(
            connection_id="connection_id",
            service_account={
                "type": "bar",
                "project_id": "bar",
                "private_key_id": "bar",
                "private_key": "bar",
                "client_email": "bar",
                "client_id": "bar",
                "auth_uri": "bar",
                "token_uri": "bar",
                "auth_provider_x509_cert_url": "bar",
                "client_x509_cert_url": "bar",
            },
        )
        assert_matches_type(DialogflowConnectionUpdateResponse, dialogflow_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        dialogflow_connection = client.dialogflow_connections.update(
            connection_id="connection_id",
            service_account={
                "type": "bar",
                "project_id": "bar",
                "private_key_id": "bar",
                "private_key": "bar",
                "client_email": "bar",
                "client_id": "bar",
                "auth_uri": "bar",
                "token_uri": "bar",
                "auth_provider_x509_cert_url": "bar",
                "client_x509_cert_url": "bar",
            },
            conversation_profile_id="a-VMHLWzTmKjiJw5S6O0-w",
            dialogflow_api="cx",
            environment="development",
            location="global",
        )
        assert_matches_type(DialogflowConnectionUpdateResponse, dialogflow_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.dialogflow_connections.with_raw_response.update(
            connection_id="connection_id",
            service_account={
                "type": "bar",
                "project_id": "bar",
                "private_key_id": "bar",
                "private_key": "bar",
                "client_email": "bar",
                "client_id": "bar",
                "auth_uri": "bar",
                "token_uri": "bar",
                "auth_provider_x509_cert_url": "bar",
                "client_x509_cert_url": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dialogflow_connection = response.parse()
        assert_matches_type(DialogflowConnectionUpdateResponse, dialogflow_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.dialogflow_connections.with_streaming_response.update(
            connection_id="connection_id",
            service_account={
                "type": "bar",
                "project_id": "bar",
                "private_key_id": "bar",
                "private_key": "bar",
                "client_email": "bar",
                "client_id": "bar",
                "auth_uri": "bar",
                "token_uri": "bar",
                "auth_provider_x509_cert_url": "bar",
                "client_x509_cert_url": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dialogflow_connection = response.parse()
            assert_matches_type(DialogflowConnectionUpdateResponse, dialogflow_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.dialogflow_connections.with_raw_response.update(
                connection_id="",
                service_account={
                    "type": "bar",
                    "project_id": "bar",
                    "private_key_id": "bar",
                    "private_key": "bar",
                    "client_email": "bar",
                    "client_id": "bar",
                    "auth_uri": "bar",
                    "token_uri": "bar",
                    "auth_provider_x509_cert_url": "bar",
                    "client_x509_cert_url": "bar",
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        dialogflow_connection = client.dialogflow_connections.delete(
            "connection_id",
        )
        assert dialogflow_connection is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.dialogflow_connections.with_raw_response.delete(
            "connection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dialogflow_connection = response.parse()
        assert dialogflow_connection is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.dialogflow_connections.with_streaming_response.delete(
            "connection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dialogflow_connection = response.parse()
            assert dialogflow_connection is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.dialogflow_connections.with_raw_response.delete(
                "",
            )


class TestAsyncDialogflowConnections:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        dialogflow_connection = await async_client.dialogflow_connections.create(
            connection_id="connection_id",
            service_account={
                "type": "bar",
                "project_id": "bar",
                "private_key_id": "bar",
                "private_key": "bar",
                "client_email": "bar",
                "client_id": "bar",
                "auth_uri": "bar",
                "token_uri": "bar",
                "auth_provider_x509_cert_url": "bar",
                "client_x509_cert_url": "bar",
            },
        )
        assert_matches_type(DialogflowConnectionCreateResponse, dialogflow_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        dialogflow_connection = await async_client.dialogflow_connections.create(
            connection_id="connection_id",
            service_account={
                "type": "bar",
                "project_id": "bar",
                "private_key_id": "bar",
                "private_key": "bar",
                "client_email": "bar",
                "client_id": "bar",
                "auth_uri": "bar",
                "token_uri": "bar",
                "auth_provider_x509_cert_url": "bar",
                "client_x509_cert_url": "bar",
            },
            conversation_profile_id="a-VMHLWzTmKjiJw5S6O0-w",
            dialogflow_api="cx",
            environment="development",
            location="global",
        )
        assert_matches_type(DialogflowConnectionCreateResponse, dialogflow_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dialogflow_connections.with_raw_response.create(
            connection_id="connection_id",
            service_account={
                "type": "bar",
                "project_id": "bar",
                "private_key_id": "bar",
                "private_key": "bar",
                "client_email": "bar",
                "client_id": "bar",
                "auth_uri": "bar",
                "token_uri": "bar",
                "auth_provider_x509_cert_url": "bar",
                "client_x509_cert_url": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dialogflow_connection = await response.parse()
        assert_matches_type(DialogflowConnectionCreateResponse, dialogflow_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dialogflow_connections.with_streaming_response.create(
            connection_id="connection_id",
            service_account={
                "type": "bar",
                "project_id": "bar",
                "private_key_id": "bar",
                "private_key": "bar",
                "client_email": "bar",
                "client_id": "bar",
                "auth_uri": "bar",
                "token_uri": "bar",
                "auth_provider_x509_cert_url": "bar",
                "client_x509_cert_url": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dialogflow_connection = await response.parse()
            assert_matches_type(DialogflowConnectionCreateResponse, dialogflow_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.dialogflow_connections.with_raw_response.create(
                connection_id="",
                service_account={
                    "type": "bar",
                    "project_id": "bar",
                    "private_key_id": "bar",
                    "private_key": "bar",
                    "client_email": "bar",
                    "client_id": "bar",
                    "auth_uri": "bar",
                    "token_uri": "bar",
                    "auth_provider_x509_cert_url": "bar",
                    "client_x509_cert_url": "bar",
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        dialogflow_connection = await async_client.dialogflow_connections.retrieve(
            "connection_id",
        )
        assert_matches_type(DialogflowConnectionRetrieveResponse, dialogflow_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dialogflow_connections.with_raw_response.retrieve(
            "connection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dialogflow_connection = await response.parse()
        assert_matches_type(DialogflowConnectionRetrieveResponse, dialogflow_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dialogflow_connections.with_streaming_response.retrieve(
            "connection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dialogflow_connection = await response.parse()
            assert_matches_type(DialogflowConnectionRetrieveResponse, dialogflow_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.dialogflow_connections.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        dialogflow_connection = await async_client.dialogflow_connections.update(
            connection_id="connection_id",
            service_account={
                "type": "bar",
                "project_id": "bar",
                "private_key_id": "bar",
                "private_key": "bar",
                "client_email": "bar",
                "client_id": "bar",
                "auth_uri": "bar",
                "token_uri": "bar",
                "auth_provider_x509_cert_url": "bar",
                "client_x509_cert_url": "bar",
            },
        )
        assert_matches_type(DialogflowConnectionUpdateResponse, dialogflow_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        dialogflow_connection = await async_client.dialogflow_connections.update(
            connection_id="connection_id",
            service_account={
                "type": "bar",
                "project_id": "bar",
                "private_key_id": "bar",
                "private_key": "bar",
                "client_email": "bar",
                "client_id": "bar",
                "auth_uri": "bar",
                "token_uri": "bar",
                "auth_provider_x509_cert_url": "bar",
                "client_x509_cert_url": "bar",
            },
            conversation_profile_id="a-VMHLWzTmKjiJw5S6O0-w",
            dialogflow_api="cx",
            environment="development",
            location="global",
        )
        assert_matches_type(DialogflowConnectionUpdateResponse, dialogflow_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dialogflow_connections.with_raw_response.update(
            connection_id="connection_id",
            service_account={
                "type": "bar",
                "project_id": "bar",
                "private_key_id": "bar",
                "private_key": "bar",
                "client_email": "bar",
                "client_id": "bar",
                "auth_uri": "bar",
                "token_uri": "bar",
                "auth_provider_x509_cert_url": "bar",
                "client_x509_cert_url": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dialogflow_connection = await response.parse()
        assert_matches_type(DialogflowConnectionUpdateResponse, dialogflow_connection, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dialogflow_connections.with_streaming_response.update(
            connection_id="connection_id",
            service_account={
                "type": "bar",
                "project_id": "bar",
                "private_key_id": "bar",
                "private_key": "bar",
                "client_email": "bar",
                "client_id": "bar",
                "auth_uri": "bar",
                "token_uri": "bar",
                "auth_provider_x509_cert_url": "bar",
                "client_x509_cert_url": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dialogflow_connection = await response.parse()
            assert_matches_type(DialogflowConnectionUpdateResponse, dialogflow_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.dialogflow_connections.with_raw_response.update(
                connection_id="",
                service_account={
                    "type": "bar",
                    "project_id": "bar",
                    "private_key_id": "bar",
                    "private_key": "bar",
                    "client_email": "bar",
                    "client_id": "bar",
                    "auth_uri": "bar",
                    "token_uri": "bar",
                    "auth_provider_x509_cert_url": "bar",
                    "client_x509_cert_url": "bar",
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        dialogflow_connection = await async_client.dialogflow_connections.delete(
            "connection_id",
        )
        assert dialogflow_connection is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dialogflow_connections.with_raw_response.delete(
            "connection_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dialogflow_connection = await response.parse()
        assert dialogflow_connection is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dialogflow_connections.with_streaming_response.delete(
            "connection_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dialogflow_connection = await response.parse()
            assert dialogflow_connection is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.dialogflow_connections.with_raw_response.delete(
                "",
            )
