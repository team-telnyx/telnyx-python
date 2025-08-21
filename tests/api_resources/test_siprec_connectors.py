# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    SiprecConnectorCreateResponse,
    SiprecConnectorUpdateResponse,
    SiprecConnectorRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSiprecConnectors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        siprec_connector = client.siprec_connectors.create(
            host="siprec.telnyx.com",
            name="my-siprec-connector",
            port=5060,
        )
        assert_matches_type(SiprecConnectorCreateResponse, siprec_connector, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        siprec_connector = client.siprec_connectors.create(
            host="siprec.telnyx.com",
            name="my-siprec-connector",
            port=5060,
            app_subdomain="my-app",
        )
        assert_matches_type(SiprecConnectorCreateResponse, siprec_connector, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.siprec_connectors.with_raw_response.create(
            host="siprec.telnyx.com",
            name="my-siprec-connector",
            port=5060,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        siprec_connector = response.parse()
        assert_matches_type(SiprecConnectorCreateResponse, siprec_connector, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.siprec_connectors.with_streaming_response.create(
            host="siprec.telnyx.com",
            name="my-siprec-connector",
            port=5060,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            siprec_connector = response.parse()
            assert_matches_type(SiprecConnectorCreateResponse, siprec_connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        siprec_connector = client.siprec_connectors.retrieve(
            "connector_name",
        )
        assert_matches_type(SiprecConnectorRetrieveResponse, siprec_connector, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.siprec_connectors.with_raw_response.retrieve(
            "connector_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        siprec_connector = response.parse()
        assert_matches_type(SiprecConnectorRetrieveResponse, siprec_connector, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.siprec_connectors.with_streaming_response.retrieve(
            "connector_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            siprec_connector = response.parse()
            assert_matches_type(SiprecConnectorRetrieveResponse, siprec_connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_name` but received ''"):
            client.siprec_connectors.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        siprec_connector = client.siprec_connectors.update(
            connector_name="connector_name",
            host="siprec.telnyx.com",
            name="my-siprec-connector",
            port=5060,
        )
        assert_matches_type(SiprecConnectorUpdateResponse, siprec_connector, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        siprec_connector = client.siprec_connectors.update(
            connector_name="connector_name",
            host="siprec.telnyx.com",
            name="my-siprec-connector",
            port=5060,
            app_subdomain="my-app",
        )
        assert_matches_type(SiprecConnectorUpdateResponse, siprec_connector, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.siprec_connectors.with_raw_response.update(
            connector_name="connector_name",
            host="siprec.telnyx.com",
            name="my-siprec-connector",
            port=5060,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        siprec_connector = response.parse()
        assert_matches_type(SiprecConnectorUpdateResponse, siprec_connector, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.siprec_connectors.with_streaming_response.update(
            connector_name="connector_name",
            host="siprec.telnyx.com",
            name="my-siprec-connector",
            port=5060,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            siprec_connector = response.parse()
            assert_matches_type(SiprecConnectorUpdateResponse, siprec_connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_name` but received ''"):
            client.siprec_connectors.with_raw_response.update(
                connector_name="",
                host="siprec.telnyx.com",
                name="my-siprec-connector",
                port=5060,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        siprec_connector = client.siprec_connectors.delete(
            "connector_name",
        )
        assert siprec_connector is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.siprec_connectors.with_raw_response.delete(
            "connector_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        siprec_connector = response.parse()
        assert siprec_connector is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.siprec_connectors.with_streaming_response.delete(
            "connector_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            siprec_connector = response.parse()
            assert siprec_connector is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_name` but received ''"):
            client.siprec_connectors.with_raw_response.delete(
                "",
            )


class TestAsyncSiprecConnectors:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        siprec_connector = await async_client.siprec_connectors.create(
            host="siprec.telnyx.com",
            name="my-siprec-connector",
            port=5060,
        )
        assert_matches_type(SiprecConnectorCreateResponse, siprec_connector, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        siprec_connector = await async_client.siprec_connectors.create(
            host="siprec.telnyx.com",
            name="my-siprec-connector",
            port=5060,
            app_subdomain="my-app",
        )
        assert_matches_type(SiprecConnectorCreateResponse, siprec_connector, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.siprec_connectors.with_raw_response.create(
            host="siprec.telnyx.com",
            name="my-siprec-connector",
            port=5060,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        siprec_connector = await response.parse()
        assert_matches_type(SiprecConnectorCreateResponse, siprec_connector, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.siprec_connectors.with_streaming_response.create(
            host="siprec.telnyx.com",
            name="my-siprec-connector",
            port=5060,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            siprec_connector = await response.parse()
            assert_matches_type(SiprecConnectorCreateResponse, siprec_connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        siprec_connector = await async_client.siprec_connectors.retrieve(
            "connector_name",
        )
        assert_matches_type(SiprecConnectorRetrieveResponse, siprec_connector, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.siprec_connectors.with_raw_response.retrieve(
            "connector_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        siprec_connector = await response.parse()
        assert_matches_type(SiprecConnectorRetrieveResponse, siprec_connector, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.siprec_connectors.with_streaming_response.retrieve(
            "connector_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            siprec_connector = await response.parse()
            assert_matches_type(SiprecConnectorRetrieveResponse, siprec_connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_name` but received ''"):
            await async_client.siprec_connectors.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        siprec_connector = await async_client.siprec_connectors.update(
            connector_name="connector_name",
            host="siprec.telnyx.com",
            name="my-siprec-connector",
            port=5060,
        )
        assert_matches_type(SiprecConnectorUpdateResponse, siprec_connector, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        siprec_connector = await async_client.siprec_connectors.update(
            connector_name="connector_name",
            host="siprec.telnyx.com",
            name="my-siprec-connector",
            port=5060,
            app_subdomain="my-app",
        )
        assert_matches_type(SiprecConnectorUpdateResponse, siprec_connector, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.siprec_connectors.with_raw_response.update(
            connector_name="connector_name",
            host="siprec.telnyx.com",
            name="my-siprec-connector",
            port=5060,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        siprec_connector = await response.parse()
        assert_matches_type(SiprecConnectorUpdateResponse, siprec_connector, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.siprec_connectors.with_streaming_response.update(
            connector_name="connector_name",
            host="siprec.telnyx.com",
            name="my-siprec-connector",
            port=5060,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            siprec_connector = await response.parse()
            assert_matches_type(SiprecConnectorUpdateResponse, siprec_connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_name` but received ''"):
            await async_client.siprec_connectors.with_raw_response.update(
                connector_name="",
                host="siprec.telnyx.com",
                name="my-siprec-connector",
                port=5060,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        siprec_connector = await async_client.siprec_connectors.delete(
            "connector_name",
        )
        assert siprec_connector is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.siprec_connectors.with_raw_response.delete(
            "connector_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        siprec_connector = await response.parse()
        assert siprec_connector is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.siprec_connectors.with_streaming_response.delete(
            "connector_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            siprec_connector = await response.parse()
            assert siprec_connector is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_name` but received ''"):
            await async_client.siprec_connectors.with_raw_response.delete(
                "",
            )
