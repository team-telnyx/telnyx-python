# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    PortingOrderListResponse,
    PortingOrderCreateResponse,
    PortingOrderUpdateResponse,
    PortingOrderRetrieveResponse,
    PortingOrderRetrieveSubRequestResponse,
    PortingOrderRetrieveRequirementsResponse,
    PortingOrderRetrieveExceptionTypesResponse,
    PortingOrderRetrieveAllowedFocWindowsResponse,
)
from telnyx._utils import parse_datetime
from telnyx._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPortingOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        porting_order = client.porting_orders.create(
            phone_numbers=["+13035550000", "+13035550001", "+13035550002"],
        )
        assert_matches_type(PortingOrderCreateResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        porting_order = client.porting_orders.create(
            phone_numbers=["+13035550000", "+13035550001", "+13035550002"],
            customer_reference="Acct 123abc",
        )
        assert_matches_type(PortingOrderCreateResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.porting_orders.with_raw_response.create(
            phone_numbers=["+13035550000", "+13035550001", "+13035550002"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        porting_order = response.parse()
        assert_matches_type(PortingOrderCreateResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.porting_orders.with_streaming_response.create(
            phone_numbers=["+13035550000", "+13035550001", "+13035550002"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            porting_order = response.parse()
            assert_matches_type(PortingOrderCreateResponse, porting_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        porting_order = client.porting_orders.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PortingOrderRetrieveResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Telnyx) -> None:
        porting_order = client.porting_orders.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include_phone_numbers=True,
        )
        assert_matches_type(PortingOrderRetrieveResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.porting_orders.with_raw_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        porting_order = response.parse()
        assert_matches_type(PortingOrderRetrieveResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.porting_orders.with_streaming_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            porting_order = response.parse()
            assert_matches_type(PortingOrderRetrieveResponse, porting_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.porting_orders.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        porting_order = client.porting_orders.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PortingOrderUpdateResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        porting_order = client.porting_orders.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            activation_settings={"foc_datetime_requested": parse_datetime("2021-03-19T10:07:15.527Z")},
            customer_reference="customer_reference",
            documents={
                "invoice": "ce74b771-d23d-4960-81ec-8741b3862146",
                "loa": "64ffb720-04c7-455b-92d6-20fcca92e935",
            },
            end_user={
                "admin": {
                    "account_number": "123abc",
                    "auth_person_name": "Porter McPortersen II",
                    "billing_phone_number": "billing_phone_number",
                    "business_identifier": "abc123",
                    "entity_name": "Porter McPortersen",
                    "pin_passcode": "pin_passcode",
                    "tax_identifier": "1234abcd",
                },
                "location": {
                    "administrative_area": "TX",
                    "country_code": "US",
                    "extended_address": "14th Floor",
                    "locality": "Austin",
                    "postal_code": "78701",
                    "street_address": "600 Congress Avenue",
                },
            },
            messaging={"enable_messaging": True},
            misc={
                "new_billing_phone_number": "new_billing_phone_number",
                "remaining_numbers_action": "disconnect",
                "type": "full",
            },
            phone_number_configuration={
                "billing_group_id": "f1486bae-f067-460c-ad43-73a92848f902",
                "connection_id": "f1486bae-f067-460c-ad43-73a92848f902",
                "emergency_address_id": "f1486bae-f067-460c-ad43-73a92848f902",
                "messaging_profile_id": "f1486bae-f067-460c-ad43-73a92848f901",
                "tags": ["abc", "123"],
            },
            requirement_group_id="DE748D99-06FA-4D90-9F9A-F4B62696BADA",
            requirements=[
                {
                    "field_value": "9787fb5f-cbe5-4de4-b765-3303774ee9fe",
                    "requirement_type_id": "59b0762a-b274-4f76-ac32-4d5cf0272e66",
                }
            ],
            user_feedback={
                "user_comment": "I loved my experience porting numbers with Telnyx",
                "user_rating": 5,
            },
            webhook_url="https://example.com",
        )
        assert_matches_type(PortingOrderUpdateResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.porting_orders.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        porting_order = response.parse()
        assert_matches_type(PortingOrderUpdateResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.porting_orders.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            porting_order = response.parse()
            assert_matches_type(PortingOrderUpdateResponse, porting_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.porting_orders.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        porting_order = client.porting_orders.list()
        assert_matches_type(PortingOrderListResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        porting_order = client.porting_orders.list(
            filter={
                "activation_settings_fast_port_eligible": True,
                "activation_settings_foc_datetime_requested": {
                    "gt": "2021-03-25T10:00:00.000Z",
                    "lt": "2021-03-25T10:00:00.000Z",
                },
                "customer_reference": "customer_reference",
                "end_user_admin_auth_person_name": "end_user.admin.auth_person_name",
                "end_user_admin_entity_name": "end_user.admin.entity_name",
                "misc_type": "full",
                "parent_support_key": "parent_support_key",
                "phone_numbers_carrier_name": "phone_numbers.carrier_name",
                "phone_numbers_country_code": "phone_numbers.country_code",
                "phone_numbers_phone_number": {"contains": "contains"},
            },
            include_phone_numbers=True,
            page={
                "number": 1,
                "size": 1,
            },
            sort={"value": "created_at"},
        )
        assert_matches_type(PortingOrderListResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.porting_orders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        porting_order = response.parse()
        assert_matches_type(PortingOrderListResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.porting_orders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            porting_order = response.parse()
            assert_matches_type(PortingOrderListResponse, porting_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        porting_order = client.porting_orders.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert porting_order is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.porting_orders.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        porting_order = response.parse()
        assert porting_order is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.porting_orders.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            porting_order = response.parse()
            assert porting_order is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.porting_orders.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_allowed_foc_windows(self, client: Telnyx) -> None:
        porting_order = client.porting_orders.retrieve_allowed_foc_windows(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PortingOrderRetrieveAllowedFocWindowsResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_allowed_foc_windows(self, client: Telnyx) -> None:
        response = client.porting_orders.with_raw_response.retrieve_allowed_foc_windows(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        porting_order = response.parse()
        assert_matches_type(PortingOrderRetrieveAllowedFocWindowsResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_allowed_foc_windows(self, client: Telnyx) -> None:
        with client.porting_orders.with_streaming_response.retrieve_allowed_foc_windows(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            porting_order = response.parse()
            assert_matches_type(PortingOrderRetrieveAllowedFocWindowsResponse, porting_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_allowed_foc_windows(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.porting_orders.with_raw_response.retrieve_allowed_foc_windows(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_exception_types(self, client: Telnyx) -> None:
        porting_order = client.porting_orders.retrieve_exception_types()
        assert_matches_type(PortingOrderRetrieveExceptionTypesResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_exception_types(self, client: Telnyx) -> None:
        response = client.porting_orders.with_raw_response.retrieve_exception_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        porting_order = response.parse()
        assert_matches_type(PortingOrderRetrieveExceptionTypesResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_exception_types(self, client: Telnyx) -> None:
        with client.porting_orders.with_streaming_response.retrieve_exception_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            porting_order = response.parse()
            assert_matches_type(PortingOrderRetrieveExceptionTypesResponse, porting_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve_loa_template(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/porting_orders/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/loa_template").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        porting_order = client.porting_orders.retrieve_loa_template(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert porting_order.is_closed
        assert porting_order.json() == {"foo": "bar"}
        assert cast(Any, porting_order.is_closed) is True
        assert isinstance(porting_order, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve_loa_template_with_all_params(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/porting_orders/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/loa_template").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        porting_order = client.porting_orders.retrieve_loa_template(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            loa_configuration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert porting_order.is_closed
        assert porting_order.json() == {"foo": "bar"}
        assert cast(Any, porting_order.is_closed) is True
        assert isinstance(porting_order, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve_loa_template(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/porting_orders/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/loa_template").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        porting_order = client.porting_orders.with_raw_response.retrieve_loa_template(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert porting_order.is_closed is True
        assert porting_order.http_request.headers.get("X-Stainless-Lang") == "python"
        assert porting_order.json() == {"foo": "bar"}
        assert isinstance(porting_order, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve_loa_template(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/porting_orders/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/loa_template").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.porting_orders.with_streaming_response.retrieve_loa_template(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as porting_order:
            assert not porting_order.is_closed
            assert porting_order.http_request.headers.get("X-Stainless-Lang") == "python"

            assert porting_order.json() == {"foo": "bar"}
            assert cast(Any, porting_order.is_closed) is True
            assert isinstance(porting_order, StreamedBinaryAPIResponse)

        assert cast(Any, porting_order.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve_loa_template(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.porting_orders.with_raw_response.retrieve_loa_template(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_requirements(self, client: Telnyx) -> None:
        porting_order = client.porting_orders.retrieve_requirements(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PortingOrderRetrieveRequirementsResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_requirements_with_all_params(self, client: Telnyx) -> None:
        porting_order = client.porting_orders.retrieve_requirements(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(PortingOrderRetrieveRequirementsResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_requirements(self, client: Telnyx) -> None:
        response = client.porting_orders.with_raw_response.retrieve_requirements(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        porting_order = response.parse()
        assert_matches_type(PortingOrderRetrieveRequirementsResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_requirements(self, client: Telnyx) -> None:
        with client.porting_orders.with_streaming_response.retrieve_requirements(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            porting_order = response.parse()
            assert_matches_type(PortingOrderRetrieveRequirementsResponse, porting_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_requirements(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.porting_orders.with_raw_response.retrieve_requirements(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_sub_request(self, client: Telnyx) -> None:
        porting_order = client.porting_orders.retrieve_sub_request(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PortingOrderRetrieveSubRequestResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_sub_request(self, client: Telnyx) -> None:
        response = client.porting_orders.with_raw_response.retrieve_sub_request(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        porting_order = response.parse()
        assert_matches_type(PortingOrderRetrieveSubRequestResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_sub_request(self, client: Telnyx) -> None:
        with client.porting_orders.with_streaming_response.retrieve_sub_request(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            porting_order = response.parse()
            assert_matches_type(PortingOrderRetrieveSubRequestResponse, porting_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_sub_request(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.porting_orders.with_raw_response.retrieve_sub_request(
                "",
            )


class TestAsyncPortingOrders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        porting_order = await async_client.porting_orders.create(
            phone_numbers=["+13035550000", "+13035550001", "+13035550002"],
        )
        assert_matches_type(PortingOrderCreateResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        porting_order = await async_client.porting_orders.create(
            phone_numbers=["+13035550000", "+13035550001", "+13035550002"],
            customer_reference="Acct 123abc",
        )
        assert_matches_type(PortingOrderCreateResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting_orders.with_raw_response.create(
            phone_numbers=["+13035550000", "+13035550001", "+13035550002"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        porting_order = await response.parse()
        assert_matches_type(PortingOrderCreateResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting_orders.with_streaming_response.create(
            phone_numbers=["+13035550000", "+13035550001", "+13035550002"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            porting_order = await response.parse()
            assert_matches_type(PortingOrderCreateResponse, porting_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        porting_order = await async_client.porting_orders.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PortingOrderRetrieveResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTelnyx) -> None:
        porting_order = await async_client.porting_orders.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include_phone_numbers=True,
        )
        assert_matches_type(PortingOrderRetrieveResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting_orders.with_raw_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        porting_order = await response.parse()
        assert_matches_type(PortingOrderRetrieveResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting_orders.with_streaming_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            porting_order = await response.parse()
            assert_matches_type(PortingOrderRetrieveResponse, porting_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.porting_orders.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        porting_order = await async_client.porting_orders.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PortingOrderUpdateResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        porting_order = await async_client.porting_orders.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            activation_settings={"foc_datetime_requested": parse_datetime("2021-03-19T10:07:15.527Z")},
            customer_reference="customer_reference",
            documents={
                "invoice": "ce74b771-d23d-4960-81ec-8741b3862146",
                "loa": "64ffb720-04c7-455b-92d6-20fcca92e935",
            },
            end_user={
                "admin": {
                    "account_number": "123abc",
                    "auth_person_name": "Porter McPortersen II",
                    "billing_phone_number": "billing_phone_number",
                    "business_identifier": "abc123",
                    "entity_name": "Porter McPortersen",
                    "pin_passcode": "pin_passcode",
                    "tax_identifier": "1234abcd",
                },
                "location": {
                    "administrative_area": "TX",
                    "country_code": "US",
                    "extended_address": "14th Floor",
                    "locality": "Austin",
                    "postal_code": "78701",
                    "street_address": "600 Congress Avenue",
                },
            },
            messaging={"enable_messaging": True},
            misc={
                "new_billing_phone_number": "new_billing_phone_number",
                "remaining_numbers_action": "disconnect",
                "type": "full",
            },
            phone_number_configuration={
                "billing_group_id": "f1486bae-f067-460c-ad43-73a92848f902",
                "connection_id": "f1486bae-f067-460c-ad43-73a92848f902",
                "emergency_address_id": "f1486bae-f067-460c-ad43-73a92848f902",
                "messaging_profile_id": "f1486bae-f067-460c-ad43-73a92848f901",
                "tags": ["abc", "123"],
            },
            requirement_group_id="DE748D99-06FA-4D90-9F9A-F4B62696BADA",
            requirements=[
                {
                    "field_value": "9787fb5f-cbe5-4de4-b765-3303774ee9fe",
                    "requirement_type_id": "59b0762a-b274-4f76-ac32-4d5cf0272e66",
                }
            ],
            user_feedback={
                "user_comment": "I loved my experience porting numbers with Telnyx",
                "user_rating": 5,
            },
            webhook_url="https://example.com",
        )
        assert_matches_type(PortingOrderUpdateResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting_orders.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        porting_order = await response.parse()
        assert_matches_type(PortingOrderUpdateResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting_orders.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            porting_order = await response.parse()
            assert_matches_type(PortingOrderUpdateResponse, porting_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.porting_orders.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        porting_order = await async_client.porting_orders.list()
        assert_matches_type(PortingOrderListResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        porting_order = await async_client.porting_orders.list(
            filter={
                "activation_settings_fast_port_eligible": True,
                "activation_settings_foc_datetime_requested": {
                    "gt": "2021-03-25T10:00:00.000Z",
                    "lt": "2021-03-25T10:00:00.000Z",
                },
                "customer_reference": "customer_reference",
                "end_user_admin_auth_person_name": "end_user.admin.auth_person_name",
                "end_user_admin_entity_name": "end_user.admin.entity_name",
                "misc_type": "full",
                "parent_support_key": "parent_support_key",
                "phone_numbers_carrier_name": "phone_numbers.carrier_name",
                "phone_numbers_country_code": "phone_numbers.country_code",
                "phone_numbers_phone_number": {"contains": "contains"},
            },
            include_phone_numbers=True,
            page={
                "number": 1,
                "size": 1,
            },
            sort={"value": "created_at"},
        )
        assert_matches_type(PortingOrderListResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting_orders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        porting_order = await response.parse()
        assert_matches_type(PortingOrderListResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting_orders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            porting_order = await response.parse()
            assert_matches_type(PortingOrderListResponse, porting_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        porting_order = await async_client.porting_orders.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert porting_order is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting_orders.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        porting_order = await response.parse()
        assert porting_order is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting_orders.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            porting_order = await response.parse()
            assert porting_order is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.porting_orders.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_allowed_foc_windows(self, async_client: AsyncTelnyx) -> None:
        porting_order = await async_client.porting_orders.retrieve_allowed_foc_windows(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PortingOrderRetrieveAllowedFocWindowsResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_allowed_foc_windows(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting_orders.with_raw_response.retrieve_allowed_foc_windows(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        porting_order = await response.parse()
        assert_matches_type(PortingOrderRetrieveAllowedFocWindowsResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_allowed_foc_windows(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting_orders.with_streaming_response.retrieve_allowed_foc_windows(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            porting_order = await response.parse()
            assert_matches_type(PortingOrderRetrieveAllowedFocWindowsResponse, porting_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_allowed_foc_windows(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.porting_orders.with_raw_response.retrieve_allowed_foc_windows(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_exception_types(self, async_client: AsyncTelnyx) -> None:
        porting_order = await async_client.porting_orders.retrieve_exception_types()
        assert_matches_type(PortingOrderRetrieveExceptionTypesResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_exception_types(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting_orders.with_raw_response.retrieve_exception_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        porting_order = await response.parse()
        assert_matches_type(PortingOrderRetrieveExceptionTypesResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_exception_types(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting_orders.with_streaming_response.retrieve_exception_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            porting_order = await response.parse()
            assert_matches_type(PortingOrderRetrieveExceptionTypesResponse, porting_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve_loa_template(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/porting_orders/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/loa_template").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        porting_order = await async_client.porting_orders.retrieve_loa_template(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert porting_order.is_closed
        assert await porting_order.json() == {"foo": "bar"}
        assert cast(Any, porting_order.is_closed) is True
        assert isinstance(porting_order, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve_loa_template_with_all_params(
        self, async_client: AsyncTelnyx, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/porting_orders/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/loa_template").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        porting_order = await async_client.porting_orders.retrieve_loa_template(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            loa_configuration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert porting_order.is_closed
        assert await porting_order.json() == {"foo": "bar"}
        assert cast(Any, porting_order.is_closed) is True
        assert isinstance(porting_order, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve_loa_template(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/porting_orders/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/loa_template").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        porting_order = await async_client.porting_orders.with_raw_response.retrieve_loa_template(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert porting_order.is_closed is True
        assert porting_order.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await porting_order.json() == {"foo": "bar"}
        assert isinstance(porting_order, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve_loa_template(
        self, async_client: AsyncTelnyx, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/porting_orders/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/loa_template").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.porting_orders.with_streaming_response.retrieve_loa_template(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as porting_order:
            assert not porting_order.is_closed
            assert porting_order.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await porting_order.json() == {"foo": "bar"}
            assert cast(Any, porting_order.is_closed) is True
            assert isinstance(porting_order, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, porting_order.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve_loa_template(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.porting_orders.with_raw_response.retrieve_loa_template(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_requirements(self, async_client: AsyncTelnyx) -> None:
        porting_order = await async_client.porting_orders.retrieve_requirements(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PortingOrderRetrieveRequirementsResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_requirements_with_all_params(self, async_client: AsyncTelnyx) -> None:
        porting_order = await async_client.porting_orders.retrieve_requirements(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page={
                "number": 1,
                "size": 1,
            },
        )
        assert_matches_type(PortingOrderRetrieveRequirementsResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_requirements(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting_orders.with_raw_response.retrieve_requirements(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        porting_order = await response.parse()
        assert_matches_type(PortingOrderRetrieveRequirementsResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_requirements(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting_orders.with_streaming_response.retrieve_requirements(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            porting_order = await response.parse()
            assert_matches_type(PortingOrderRetrieveRequirementsResponse, porting_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_requirements(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.porting_orders.with_raw_response.retrieve_requirements(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_sub_request(self, async_client: AsyncTelnyx) -> None:
        porting_order = await async_client.porting_orders.retrieve_sub_request(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PortingOrderRetrieveSubRequestResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_sub_request(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.porting_orders.with_raw_response.retrieve_sub_request(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        porting_order = await response.parse()
        assert_matches_type(PortingOrderRetrieveSubRequestResponse, porting_order, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_sub_request(self, async_client: AsyncTelnyx) -> None:
        async with async_client.porting_orders.with_streaming_response.retrieve_sub_request(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            porting_order = await response.parse()
            assert_matches_type(PortingOrderRetrieveSubRequestResponse, porting_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_sub_request(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.porting_orders.with_raw_response.retrieve_sub_request(
                "",
            )
