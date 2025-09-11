# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from telnyx.types.porting import (
    LoaConfigurationListResponse,
    LoaConfigurationCreateResponse,
    LoaConfigurationUpdateResponse,
    LoaConfigurationRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLoaConfigurations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        loa_configuration = client.porting.loa_configurations.create(
            address={
                "city": "Austin",
                "country_code": "US",
                "state": "TX",
                "street_address": "600 Congress Avenue",
                "zip_code": "78701",
            },
            company_name="Telnyx",
            contact={
                "email": "testing@telnyx.com",
                "phone_number": "+12003270001",
            },
            logo={"document_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            name="My LOA Configuration",
        )
        assert_matches_type(LoaConfigurationCreateResponse, loa_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        loa_configuration = client.porting.loa_configurations.create(
            address={
                "city": "Austin",
                "country_code": "US",
                "state": "TX",
                "street_address": "600 Congress Avenue",
                "zip_code": "78701",
                "extended_address": "14th Floor",
            },
            company_name="Telnyx",
            contact={
                "email": "testing@telnyx.com",
                "phone_number": "+12003270001",
            },
            logo={"document_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            name="My LOA Configuration",
        )
        assert_matches_type(LoaConfigurationCreateResponse, loa_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.porting.loa_configurations.with_raw_response.create(
            address={
                "city": "Austin",
                "country_code": "US",
                "state": "TX",
                "street_address": "600 Congress Avenue",
                "zip_code": "78701",
            },
            company_name="Telnyx",
            contact={
                "email": "testing@telnyx.com",
                "phone_number": "+12003270001",
            },
            logo={"document_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            name="My LOA Configuration",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loa_configuration = response.parse()
        assert_matches_type(LoaConfigurationCreateResponse, loa_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.porting.loa_configurations.with_streaming_response.create(
            address={
                "city": "Austin",
                "country_code": "US",
                "state": "TX",
                "street_address": "600 Congress Avenue",
                "zip_code": "78701",
            },
            company_name="Telnyx",
            contact={
                "email": "testing@telnyx.com",
                "phone_number": "+12003270001",
            },
            logo={"document_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            name="My LOA Configuration",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loa_configuration = response.parse()
            assert_matches_type(LoaConfigurationCreateResponse, loa_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        loa_configuration = client.porting.loa_configurations.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(LoaConfigurationRetrieveResponse, loa_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.porting.loa_configurations.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loa_configuration = response.parse()
        assert_matches_type(LoaConfigurationRetrieveResponse, loa_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.porting.loa_configurations.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loa_configuration = response.parse()
            assert_matches_type(LoaConfigurationRetrieveResponse, loa_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.porting.loa_configurations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        loa_configuration = client.porting.loa_configurations.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "city": "Austin",
                "country_code": "US",
                "state": "TX",
                "street_address": "600 Congress Avenue",
                "zip_code": "78701",
            },
            company_name="Telnyx",
            contact={
                "email": "testing@telnyx.com",
                "phone_number": "+12003270001",
            },
            logo={"document_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            name="My LOA Configuration",
        )
        assert_matches_type(LoaConfigurationUpdateResponse, loa_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        loa_configuration = client.porting.loa_configurations.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "city": "Austin",
                "country_code": "US",
                "state": "TX",
                "street_address": "600 Congress Avenue",
                "zip_code": "78701",
                "extended_address": "14th Floor",
            },
            company_name="Telnyx",
            contact={
                "email": "testing@telnyx.com",
                "phone_number": "+12003270001",
            },
            logo={"document_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            name="My LOA Configuration",
        )
        assert_matches_type(LoaConfigurationUpdateResponse, loa_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.porting.loa_configurations.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "city": "Austin",
                "country_code": "US",
                "state": "TX",
                "street_address": "600 Congress Avenue",
                "zip_code": "78701",
            },
            company_name="Telnyx",
            contact={
                "email": "testing@telnyx.com",
                "phone_number": "+12003270001",
            },
            logo={"document_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            name="My LOA Configuration",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loa_configuration = response.parse()
        assert_matches_type(LoaConfigurationUpdateResponse, loa_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.porting.loa_configurations.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "city": "Austin",
                "country_code": "US",
                "state": "TX",
                "street_address": "600 Congress Avenue",
                "zip_code": "78701",
            },
            company_name="Telnyx",
            contact={
                "email": "testing@telnyx.com",
                "phone_number": "+12003270001",
            },
            logo={"document_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            name="My LOA Configuration",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loa_configuration = response.parse()
            assert_matches_type(LoaConfigurationUpdateResponse, loa_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.porting.loa_configurations.with_raw_response.update(
                id="",
                address={
                    "city": "Austin",
                    "country_code": "US",
                    "state": "TX",
                    "street_address": "600 Congress Avenue",
                    "zip_code": "78701",
                },
                company_name="Telnyx",
                contact={
                    "email": "testing@telnyx.com",
                    "phone_number": "+12003270001",
                },
                logo={"document_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                name="My LOA Configuration",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        loa_configuration = client.porting.loa_configurations.list()
        assert_matches_type(LoaConfigurationListResponse, loa_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        loa_configuration = client.porting.loa_configurations.list(
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(LoaConfigurationListResponse, loa_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.porting.loa_configurations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loa_configuration = response.parse()
        assert_matches_type(LoaConfigurationListResponse, loa_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.porting.loa_configurations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loa_configuration = response.parse()
            assert_matches_type(LoaConfigurationListResponse, loa_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        loa_configuration = client.porting.loa_configurations.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert loa_configuration is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.porting.loa_configurations.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loa_configuration = response.parse()
        assert loa_configuration is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.porting.loa_configurations.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loa_configuration = response.parse()
            assert loa_configuration is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.porting.loa_configurations.with_raw_response.delete(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_preview_0(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.post("/porting/loa_configuration/preview").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        loa_configuration = client.porting.loa_configurations.preview_0(
            address={
                "city": "Austin",
                "country_code": "US",
                "state": "TX",
                "street_address": "600 Congress Avenue",
                "zip_code": "78701",
            },
            company_name="Telnyx",
            contact={
                "email": "testing@telnyx.com",
                "phone_number": "+12003270001",
            },
            logo={"document_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            name="My LOA Configuration",
        )
        assert loa_configuration.is_closed
        assert loa_configuration.json() == {"foo": "bar"}
        assert cast(Any, loa_configuration.is_closed) is True
        assert isinstance(loa_configuration, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_preview_0_with_all_params(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.post("/porting/loa_configuration/preview").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        loa_configuration = client.porting.loa_configurations.preview_0(
            address={
                "city": "Austin",
                "country_code": "US",
                "state": "TX",
                "street_address": "600 Congress Avenue",
                "zip_code": "78701",
                "extended_address": "14th Floor",
            },
            company_name="Telnyx",
            contact={
                "email": "testing@telnyx.com",
                "phone_number": "+12003270001",
            },
            logo={"document_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            name="My LOA Configuration",
        )
        assert loa_configuration.is_closed
        assert loa_configuration.json() == {"foo": "bar"}
        assert cast(Any, loa_configuration.is_closed) is True
        assert isinstance(loa_configuration, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_preview_0(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.post("/porting/loa_configuration/preview").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        loa_configuration = client.porting.loa_configurations.with_raw_response.preview_0(
            address={
                "city": "Austin",
                "country_code": "US",
                "state": "TX",
                "street_address": "600 Congress Avenue",
                "zip_code": "78701",
            },
            company_name="Telnyx",
            contact={
                "email": "testing@telnyx.com",
                "phone_number": "+12003270001",
            },
            logo={"document_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            name="My LOA Configuration",
        )

        assert loa_configuration.is_closed is True
        assert loa_configuration.http_request.headers.get("X-Stainless-Lang") == "python"
        assert loa_configuration.json() == {"foo": "bar"}
        assert isinstance(loa_configuration, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_preview_0(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.post("/porting/loa_configuration/preview").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.porting.loa_configurations.with_streaming_response.preview_0(
            address={
                "city": "Austin",
                "country_code": "US",
                "state": "TX",
                "street_address": "600 Congress Avenue",
                "zip_code": "78701",
            },
            company_name="Telnyx",
            contact={
                "email": "testing@telnyx.com",
                "phone_number": "+12003270001",
            },
            logo={"document_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            name="My LOA Configuration",
        ) as loa_configuration:
            assert not loa_configuration.is_closed
            assert loa_configuration.http_request.headers.get("X-Stainless-Lang") == "python"

            assert loa_configuration.json() == {"foo": "bar"}
            assert cast(Any, loa_configuration.is_closed) is True
            assert isinstance(loa_configuration, StreamedBinaryAPIResponse)

        assert cast(Any, loa_configuration.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_preview_1(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/porting/loa_configurations/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/preview").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        loa_configuration = client.porting.loa_configurations.preview_1(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert loa_configuration.is_closed
        assert loa_configuration.json() == {"foo": "bar"}
        assert cast(Any, loa_configuration.is_closed) is True
        assert isinstance(loa_configuration, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_preview_1(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/porting/loa_configurations/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/preview").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        loa_configuration = client.porting.loa_configurations.with_raw_response.preview_1(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert loa_configuration.is_closed is True
        assert loa_configuration.http_request.headers.get("X-Stainless-Lang") == "python"
        assert loa_configuration.json() == {"foo": "bar"}
        assert isinstance(loa_configuration, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_preview_1(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/porting/loa_configurations/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/preview").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.porting.loa_configurations.with_streaming_response.preview_1(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as loa_configuration:
            assert not loa_configuration.is_closed
            assert loa_configuration.http_request.headers.get("X-Stainless-Lang") == "python"

            assert loa_configuration.json() == {"foo": "bar"}
            assert cast(Any, loa_configuration.is_closed) is True
            assert isinstance(loa_configuration, StreamedBinaryAPIResponse)

        assert cast(Any, loa_configuration.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_preview_1(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.porting.loa_configurations.with_raw_response.preview_1(
                "",
            )


class TestAsyncLoaConfigurations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        loa_configuration = await async_client.porting.loa_configurations.create(
            address={
                "city": "Austin",
                "country_code": "US",
                "state": "TX",
                "street_address": "600 Congress Avenue",
                "zip_code": "78701",
            },
            company_name="Telnyx",
            contact={
                "email": "testing@telnyx.com",
                "phone_number": "+12003270001",
            },
            logo={"document_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            name="My LOA Configuration",
        )
        assert_matches_type(LoaConfigurationCreateResponse, loa_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        loa_configuration = await async_client.porting.loa_configurations.create(
            address={
                "city": "Austin",
                "country_code": "US",
                "state": "TX",
                "street_address": "600 Congress Avenue",
                "zip_code": "78701",
                "extended_address": "14th Floor",
            },
            company_name="Telnyx",
            contact={
                "email": "testing@telnyx.com",
                "phone_number": "+12003270001",
            },
            logo={"document_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            name="My LOA Configuration",
        )
        assert_matches_type(LoaConfigurationCreateResponse, loa_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting.loa_configurations.with_raw_response.create(
            address={
                "city": "Austin",
                "country_code": "US",
                "state": "TX",
                "street_address": "600 Congress Avenue",
                "zip_code": "78701",
            },
            company_name="Telnyx",
            contact={
                "email": "testing@telnyx.com",
                "phone_number": "+12003270001",
            },
            logo={"document_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            name="My LOA Configuration",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loa_configuration = await response.parse()
        assert_matches_type(LoaConfigurationCreateResponse, loa_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting.loa_configurations.with_streaming_response.create(
            address={
                "city": "Austin",
                "country_code": "US",
                "state": "TX",
                "street_address": "600 Congress Avenue",
                "zip_code": "78701",
            },
            company_name="Telnyx",
            contact={
                "email": "testing@telnyx.com",
                "phone_number": "+12003270001",
            },
            logo={"document_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            name="My LOA Configuration",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loa_configuration = await response.parse()
            assert_matches_type(LoaConfigurationCreateResponse, loa_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        loa_configuration = await async_client.porting.loa_configurations.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(LoaConfigurationRetrieveResponse, loa_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting.loa_configurations.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loa_configuration = await response.parse()
        assert_matches_type(LoaConfigurationRetrieveResponse, loa_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting.loa_configurations.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loa_configuration = await response.parse()
            assert_matches_type(LoaConfigurationRetrieveResponse, loa_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.porting.loa_configurations.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        loa_configuration = await async_client.porting.loa_configurations.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "city": "Austin",
                "country_code": "US",
                "state": "TX",
                "street_address": "600 Congress Avenue",
                "zip_code": "78701",
            },
            company_name="Telnyx",
            contact={
                "email": "testing@telnyx.com",
                "phone_number": "+12003270001",
            },
            logo={"document_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            name="My LOA Configuration",
        )
        assert_matches_type(LoaConfigurationUpdateResponse, loa_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        loa_configuration = await async_client.porting.loa_configurations.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "city": "Austin",
                "country_code": "US",
                "state": "TX",
                "street_address": "600 Congress Avenue",
                "zip_code": "78701",
                "extended_address": "14th Floor",
            },
            company_name="Telnyx",
            contact={
                "email": "testing@telnyx.com",
                "phone_number": "+12003270001",
            },
            logo={"document_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            name="My LOA Configuration",
        )
        assert_matches_type(LoaConfigurationUpdateResponse, loa_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting.loa_configurations.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "city": "Austin",
                "country_code": "US",
                "state": "TX",
                "street_address": "600 Congress Avenue",
                "zip_code": "78701",
            },
            company_name="Telnyx",
            contact={
                "email": "testing@telnyx.com",
                "phone_number": "+12003270001",
            },
            logo={"document_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            name="My LOA Configuration",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loa_configuration = await response.parse()
        assert_matches_type(LoaConfigurationUpdateResponse, loa_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting.loa_configurations.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "city": "Austin",
                "country_code": "US",
                "state": "TX",
                "street_address": "600 Congress Avenue",
                "zip_code": "78701",
            },
            company_name="Telnyx",
            contact={
                "email": "testing@telnyx.com",
                "phone_number": "+12003270001",
            },
            logo={"document_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            name="My LOA Configuration",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loa_configuration = await response.parse()
            assert_matches_type(LoaConfigurationUpdateResponse, loa_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.porting.loa_configurations.with_raw_response.update(
                id="",
                address={
                    "city": "Austin",
                    "country_code": "US",
                    "state": "TX",
                    "street_address": "600 Congress Avenue",
                    "zip_code": "78701",
                },
                company_name="Telnyx",
                contact={
                    "email": "testing@telnyx.com",
                    "phone_number": "+12003270001",
                },
                logo={"document_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
                name="My LOA Configuration",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        loa_configuration = await async_client.porting.loa_configurations.list()
        assert_matches_type(LoaConfigurationListResponse, loa_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        loa_configuration = await async_client.porting.loa_configurations.list(
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(LoaConfigurationListResponse, loa_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting.loa_configurations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loa_configuration = await response.parse()
        assert_matches_type(LoaConfigurationListResponse, loa_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting.loa_configurations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loa_configuration = await response.parse()
            assert_matches_type(LoaConfigurationListResponse, loa_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        loa_configuration = await async_client.porting.loa_configurations.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert loa_configuration is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting.loa_configurations.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loa_configuration = await response.parse()
        assert loa_configuration is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting.loa_configurations.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loa_configuration = await response.parse()
            assert loa_configuration is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.porting.loa_configurations.with_raw_response.delete(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_preview_0(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.post("/porting/loa_configuration/preview").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        loa_configuration = await async_client.porting.loa_configurations.preview_0(
            address={
                "city": "Austin",
                "country_code": "US",
                "state": "TX",
                "street_address": "600 Congress Avenue",
                "zip_code": "78701",
            },
            company_name="Telnyx",
            contact={
                "email": "testing@telnyx.com",
                "phone_number": "+12003270001",
            },
            logo={"document_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            name="My LOA Configuration",
        )
        assert loa_configuration.is_closed
        assert await loa_configuration.json() == {"foo": "bar"}
        assert cast(Any, loa_configuration.is_closed) is True
        assert isinstance(loa_configuration, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_preview_0_with_all_params(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.post("/porting/loa_configuration/preview").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        loa_configuration = await async_client.porting.loa_configurations.preview_0(
            address={
                "city": "Austin",
                "country_code": "US",
                "state": "TX",
                "street_address": "600 Congress Avenue",
                "zip_code": "78701",
                "extended_address": "14th Floor",
            },
            company_name="Telnyx",
            contact={
                "email": "testing@telnyx.com",
                "phone_number": "+12003270001",
            },
            logo={"document_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            name="My LOA Configuration",
        )
        assert loa_configuration.is_closed
        assert await loa_configuration.json() == {"foo": "bar"}
        assert cast(Any, loa_configuration.is_closed) is True
        assert isinstance(loa_configuration, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_preview_0(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.post("/porting/loa_configuration/preview").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        loa_configuration = await async_client.porting.loa_configurations.with_raw_response.preview_0(
            address={
                "city": "Austin",
                "country_code": "US",
                "state": "TX",
                "street_address": "600 Congress Avenue",
                "zip_code": "78701",
            },
            company_name="Telnyx",
            contact={
                "email": "testing@telnyx.com",
                "phone_number": "+12003270001",
            },
            logo={"document_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            name="My LOA Configuration",
        )

        assert loa_configuration.is_closed is True
        assert loa_configuration.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await loa_configuration.json() == {"foo": "bar"}
        assert isinstance(loa_configuration, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_preview_0(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.post("/porting/loa_configuration/preview").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.porting.loa_configurations.with_streaming_response.preview_0(
            address={
                "city": "Austin",
                "country_code": "US",
                "state": "TX",
                "street_address": "600 Congress Avenue",
                "zip_code": "78701",
            },
            company_name="Telnyx",
            contact={
                "email": "testing@telnyx.com",
                "phone_number": "+12003270001",
            },
            logo={"document_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            name="My LOA Configuration",
        ) as loa_configuration:
            assert not loa_configuration.is_closed
            assert loa_configuration.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await loa_configuration.json() == {"foo": "bar"}
            assert cast(Any, loa_configuration.is_closed) is True
            assert isinstance(loa_configuration, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, loa_configuration.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_preview_1(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/porting/loa_configurations/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/preview").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        loa_configuration = await async_client.porting.loa_configurations.preview_1(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert loa_configuration.is_closed
        assert await loa_configuration.json() == {"foo": "bar"}
        assert cast(Any, loa_configuration.is_closed) is True
        assert isinstance(loa_configuration, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_preview_1(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/porting/loa_configurations/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/preview").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        loa_configuration = await async_client.porting.loa_configurations.with_raw_response.preview_1(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert loa_configuration.is_closed is True
        assert loa_configuration.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await loa_configuration.json() == {"foo": "bar"}
        assert isinstance(loa_configuration, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_preview_1(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/porting/loa_configurations/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/preview").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.porting.loa_configurations.with_streaming_response.preview_1(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as loa_configuration:
            assert not loa_configuration.is_closed
            assert loa_configuration.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await loa_configuration.json() == {"foo": "bar"}
            assert cast(Any, loa_configuration.is_closed) is True
            assert isinstance(loa_configuration, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, loa_configuration.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_preview_1(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.porting.loa_configurations.with_raw_response.preview_1(
                "",
            )
