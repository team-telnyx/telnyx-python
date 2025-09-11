# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx._utils import parse_datetime
from telnyx.types.messaging_tollfree.verification import (
    RequestListResponse,
    VerificationRequestEgress,
    VerificationRequestStatus,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRequests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        request = client.messaging_tollfree.verification.requests.create(
            additional_information="additionalInformation",
            business_addr1="600 Congress Avenue",
            business_city="Austin",
            business_contact_email="email@example.com",
            business_contact_first_name="John",
            business_contact_last_name="Doe",
            business_contact_phone="+18005550100",
            business_name="Telnyx LLC",
            business_state="Texas",
            business_zip="78701",
            corporate_website="http://example.com",
            isv_reseller="isvReseller",
            message_volume="100,000",
            opt_in_workflow="User signs into the Telnyx portal, enters a number and is prompted to select whether they want to use 2FA verification for security purposes. If they've opted in a confirmation message is sent out to the handset",
            opt_in_workflow_image_urls=[
                {"url": "https://telnyx.com/sign-up"},
                {"url": "https://telnyx.com/company/data-privacy"},
            ],
            phone_numbers=[{"phone_number": "+18773554398"}, {"phone_number": "+18773554399"}],
            production_message_content="Your Telnyx OTP is XXXX",
            use_case="2FA",
            use_case_summary="This is a use case where Telnyx sends out 2FA codes to portal users to verify their identity in order to sign into the portal",
        )
        assert_matches_type(VerificationRequestEgress, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        request = client.messaging_tollfree.verification.requests.create(
            additional_information="additionalInformation",
            business_addr1="600 Congress Avenue",
            business_city="Austin",
            business_contact_email="email@example.com",
            business_contact_first_name="John",
            business_contact_last_name="Doe",
            business_contact_phone="+18005550100",
            business_name="Telnyx LLC",
            business_state="Texas",
            business_zip="78701",
            corporate_website="http://example.com",
            isv_reseller="isvReseller",
            message_volume="100,000",
            opt_in_workflow="User signs into the Telnyx portal, enters a number and is prompted to select whether they want to use 2FA verification for security purposes. If they've opted in a confirmation message is sent out to the handset",
            opt_in_workflow_image_urls=[
                {"url": "https://telnyx.com/sign-up"},
                {"url": "https://telnyx.com/company/data-privacy"},
            ],
            phone_numbers=[{"phone_number": "+18773554398"}, {"phone_number": "+18773554399"}],
            production_message_content="Your Telnyx OTP is XXXX",
            use_case="2FA",
            use_case_summary="This is a use case where Telnyx sends out 2FA codes to portal users to verify their identity in order to sign into the portal",
            business_addr2="14th Floor",
            webhook_url="http://example-webhook.com",
        )
        assert_matches_type(VerificationRequestEgress, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.messaging_tollfree.verification.requests.with_raw_response.create(
            additional_information="additionalInformation",
            business_addr1="600 Congress Avenue",
            business_city="Austin",
            business_contact_email="email@example.com",
            business_contact_first_name="John",
            business_contact_last_name="Doe",
            business_contact_phone="+18005550100",
            business_name="Telnyx LLC",
            business_state="Texas",
            business_zip="78701",
            corporate_website="http://example.com",
            isv_reseller="isvReseller",
            message_volume="100,000",
            opt_in_workflow="User signs into the Telnyx portal, enters a number and is prompted to select whether they want to use 2FA verification for security purposes. If they've opted in a confirmation message is sent out to the handset",
            opt_in_workflow_image_urls=[
                {"url": "https://telnyx.com/sign-up"},
                {"url": "https://telnyx.com/company/data-privacy"},
            ],
            phone_numbers=[{"phone_number": "+18773554398"}, {"phone_number": "+18773554399"}],
            production_message_content="Your Telnyx OTP is XXXX",
            use_case="2FA",
            use_case_summary="This is a use case where Telnyx sends out 2FA codes to portal users to verify their identity in order to sign into the portal",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = response.parse()
        assert_matches_type(VerificationRequestEgress, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.messaging_tollfree.verification.requests.with_streaming_response.create(
            additional_information="additionalInformation",
            business_addr1="600 Congress Avenue",
            business_city="Austin",
            business_contact_email="email@example.com",
            business_contact_first_name="John",
            business_contact_last_name="Doe",
            business_contact_phone="+18005550100",
            business_name="Telnyx LLC",
            business_state="Texas",
            business_zip="78701",
            corporate_website="http://example.com",
            isv_reseller="isvReseller",
            message_volume="100,000",
            opt_in_workflow="User signs into the Telnyx portal, enters a number and is prompted to select whether they want to use 2FA verification for security purposes. If they've opted in a confirmation message is sent out to the handset",
            opt_in_workflow_image_urls=[
                {"url": "https://telnyx.com/sign-up"},
                {"url": "https://telnyx.com/company/data-privacy"},
            ],
            phone_numbers=[{"phone_number": "+18773554398"}, {"phone_number": "+18773554399"}],
            production_message_content="Your Telnyx OTP is XXXX",
            use_case="2FA",
            use_case_summary="This is a use case where Telnyx sends out 2FA codes to portal users to verify their identity in order to sign into the portal",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = response.parse()
            assert_matches_type(VerificationRequestEgress, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        request = client.messaging_tollfree.verification.requests.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VerificationRequestStatus, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.messaging_tollfree.verification.requests.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = response.parse()
        assert_matches_type(VerificationRequestStatus, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.messaging_tollfree.verification.requests.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = response.parse()
            assert_matches_type(VerificationRequestStatus, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.messaging_tollfree.verification.requests.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        request = client.messaging_tollfree.verification.requests.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            additional_information="additionalInformation",
            business_addr1="600 Congress Avenue",
            business_city="Austin",
            business_contact_email="email@example.com",
            business_contact_first_name="John",
            business_contact_last_name="Doe",
            business_contact_phone="+18005550100",
            business_name="Telnyx LLC",
            business_state="Texas",
            business_zip="78701",
            corporate_website="http://example.com",
            isv_reseller="isvReseller",
            message_volume="100,000",
            opt_in_workflow="User signs into the Telnyx portal, enters a number and is prompted to select whether they want to use 2FA verification for security purposes. If they've opted in a confirmation message is sent out to the handset",
            opt_in_workflow_image_urls=[
                {"url": "https://telnyx.com/sign-up"},
                {"url": "https://telnyx.com/company/data-privacy"},
            ],
            phone_numbers=[{"phone_number": "+18773554398"}, {"phone_number": "+18773554399"}],
            production_message_content="Your Telnyx OTP is XXXX",
            use_case="2FA",
            use_case_summary="This is a use case where Telnyx sends out 2FA codes to portal users to verify their identity in order to sign into the portal",
        )
        assert_matches_type(VerificationRequestEgress, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        request = client.messaging_tollfree.verification.requests.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            additional_information="additionalInformation",
            business_addr1="600 Congress Avenue",
            business_city="Austin",
            business_contact_email="email@example.com",
            business_contact_first_name="John",
            business_contact_last_name="Doe",
            business_contact_phone="+18005550100",
            business_name="Telnyx LLC",
            business_state="Texas",
            business_zip="78701",
            corporate_website="http://example.com",
            isv_reseller="isvReseller",
            message_volume="100,000",
            opt_in_workflow="User signs into the Telnyx portal, enters a number and is prompted to select whether they want to use 2FA verification for security purposes. If they've opted in a confirmation message is sent out to the handset",
            opt_in_workflow_image_urls=[
                {"url": "https://telnyx.com/sign-up"},
                {"url": "https://telnyx.com/company/data-privacy"},
            ],
            phone_numbers=[{"phone_number": "+18773554398"}, {"phone_number": "+18773554399"}],
            production_message_content="Your Telnyx OTP is XXXX",
            use_case="2FA",
            use_case_summary="This is a use case where Telnyx sends out 2FA codes to portal users to verify their identity in order to sign into the portal",
            business_addr2="14th Floor",
            webhook_url="http://example-webhook.com",
        )
        assert_matches_type(VerificationRequestEgress, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.messaging_tollfree.verification.requests.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            additional_information="additionalInformation",
            business_addr1="600 Congress Avenue",
            business_city="Austin",
            business_contact_email="email@example.com",
            business_contact_first_name="John",
            business_contact_last_name="Doe",
            business_contact_phone="+18005550100",
            business_name="Telnyx LLC",
            business_state="Texas",
            business_zip="78701",
            corporate_website="http://example.com",
            isv_reseller="isvReseller",
            message_volume="100,000",
            opt_in_workflow="User signs into the Telnyx portal, enters a number and is prompted to select whether they want to use 2FA verification for security purposes. If they've opted in a confirmation message is sent out to the handset",
            opt_in_workflow_image_urls=[
                {"url": "https://telnyx.com/sign-up"},
                {"url": "https://telnyx.com/company/data-privacy"},
            ],
            phone_numbers=[{"phone_number": "+18773554398"}, {"phone_number": "+18773554399"}],
            production_message_content="Your Telnyx OTP is XXXX",
            use_case="2FA",
            use_case_summary="This is a use case where Telnyx sends out 2FA codes to portal users to verify their identity in order to sign into the portal",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = response.parse()
        assert_matches_type(VerificationRequestEgress, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.messaging_tollfree.verification.requests.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            additional_information="additionalInformation",
            business_addr1="600 Congress Avenue",
            business_city="Austin",
            business_contact_email="email@example.com",
            business_contact_first_name="John",
            business_contact_last_name="Doe",
            business_contact_phone="+18005550100",
            business_name="Telnyx LLC",
            business_state="Texas",
            business_zip="78701",
            corporate_website="http://example.com",
            isv_reseller="isvReseller",
            message_volume="100,000",
            opt_in_workflow="User signs into the Telnyx portal, enters a number and is prompted to select whether they want to use 2FA verification for security purposes. If they've opted in a confirmation message is sent out to the handset",
            opt_in_workflow_image_urls=[
                {"url": "https://telnyx.com/sign-up"},
                {"url": "https://telnyx.com/company/data-privacy"},
            ],
            phone_numbers=[{"phone_number": "+18773554398"}, {"phone_number": "+18773554399"}],
            production_message_content="Your Telnyx OTP is XXXX",
            use_case="2FA",
            use_case_summary="This is a use case where Telnyx sends out 2FA codes to portal users to verify their identity in order to sign into the portal",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = response.parse()
            assert_matches_type(VerificationRequestEgress, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.messaging_tollfree.verification.requests.with_raw_response.update(
                id="",
                additional_information="additionalInformation",
                business_addr1="600 Congress Avenue",
                business_city="Austin",
                business_contact_email="email@example.com",
                business_contact_first_name="John",
                business_contact_last_name="Doe",
                business_contact_phone="+18005550100",
                business_name="Telnyx LLC",
                business_state="Texas",
                business_zip="78701",
                corporate_website="http://example.com",
                isv_reseller="isvReseller",
                message_volume="100,000",
                opt_in_workflow="User signs into the Telnyx portal, enters a number and is prompted to select whether they want to use 2FA verification for security purposes. If they've opted in a confirmation message is sent out to the handset",
                opt_in_workflow_image_urls=[
                    {"url": "https://telnyx.com/sign-up"},
                    {"url": "https://telnyx.com/company/data-privacy"},
                ],
                phone_numbers=[{"phone_number": "+18773554398"}, {"phone_number": "+18773554399"}],
                production_message_content="Your Telnyx OTP is XXXX",
                use_case="2FA",
                use_case_summary="This is a use case where Telnyx sends out 2FA codes to portal users to verify their identity in order to sign into the portal",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        request = client.messaging_tollfree.verification.requests.list(
            page=1,
            page_size=1,
        )
        assert_matches_type(RequestListResponse, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        request = client.messaging_tollfree.verification.requests.list(
            page=1,
            page_size=1,
            date_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            phone_number="phone_number",
            status="Verified",
        )
        assert_matches_type(RequestListResponse, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.messaging_tollfree.verification.requests.with_raw_response.list(
            page=1,
            page_size=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = response.parse()
        assert_matches_type(RequestListResponse, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.messaging_tollfree.verification.requests.with_streaming_response.list(
            page=1,
            page_size=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = response.parse()
            assert_matches_type(RequestListResponse, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        request = client.messaging_tollfree.verification.requests.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.messaging_tollfree.verification.requests.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = response.parse()
        assert_matches_type(object, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.messaging_tollfree.verification.requests.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = response.parse()
            assert_matches_type(object, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.messaging_tollfree.verification.requests.with_raw_response.delete(
                "",
            )


class TestAsyncRequests:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        request = await async_client.messaging_tollfree.verification.requests.create(
            additional_information="additionalInformation",
            business_addr1="600 Congress Avenue",
            business_city="Austin",
            business_contact_email="email@example.com",
            business_contact_first_name="John",
            business_contact_last_name="Doe",
            business_contact_phone="+18005550100",
            business_name="Telnyx LLC",
            business_state="Texas",
            business_zip="78701",
            corporate_website="http://example.com",
            isv_reseller="isvReseller",
            message_volume="100,000",
            opt_in_workflow="User signs into the Telnyx portal, enters a number and is prompted to select whether they want to use 2FA verification for security purposes. If they've opted in a confirmation message is sent out to the handset",
            opt_in_workflow_image_urls=[
                {"url": "https://telnyx.com/sign-up"},
                {"url": "https://telnyx.com/company/data-privacy"},
            ],
            phone_numbers=[{"phone_number": "+18773554398"}, {"phone_number": "+18773554399"}],
            production_message_content="Your Telnyx OTP is XXXX",
            use_case="2FA",
            use_case_summary="This is a use case where Telnyx sends out 2FA codes to portal users to verify their identity in order to sign into the portal",
        )
        assert_matches_type(VerificationRequestEgress, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        request = await async_client.messaging_tollfree.verification.requests.create(
            additional_information="additionalInformation",
            business_addr1="600 Congress Avenue",
            business_city="Austin",
            business_contact_email="email@example.com",
            business_contact_first_name="John",
            business_contact_last_name="Doe",
            business_contact_phone="+18005550100",
            business_name="Telnyx LLC",
            business_state="Texas",
            business_zip="78701",
            corporate_website="http://example.com",
            isv_reseller="isvReseller",
            message_volume="100,000",
            opt_in_workflow="User signs into the Telnyx portal, enters a number and is prompted to select whether they want to use 2FA verification for security purposes. If they've opted in a confirmation message is sent out to the handset",
            opt_in_workflow_image_urls=[
                {"url": "https://telnyx.com/sign-up"},
                {"url": "https://telnyx.com/company/data-privacy"},
            ],
            phone_numbers=[{"phone_number": "+18773554398"}, {"phone_number": "+18773554399"}],
            production_message_content="Your Telnyx OTP is XXXX",
            use_case="2FA",
            use_case_summary="This is a use case where Telnyx sends out 2FA codes to portal users to verify their identity in order to sign into the portal",
            business_addr2="14th Floor",
            webhook_url="http://example-webhook.com",
        )
        assert_matches_type(VerificationRequestEgress, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_tollfree.verification.requests.with_raw_response.create(
            additional_information="additionalInformation",
            business_addr1="600 Congress Avenue",
            business_city="Austin",
            business_contact_email="email@example.com",
            business_contact_first_name="John",
            business_contact_last_name="Doe",
            business_contact_phone="+18005550100",
            business_name="Telnyx LLC",
            business_state="Texas",
            business_zip="78701",
            corporate_website="http://example.com",
            isv_reseller="isvReseller",
            message_volume="100,000",
            opt_in_workflow="User signs into the Telnyx portal, enters a number and is prompted to select whether they want to use 2FA verification for security purposes. If they've opted in a confirmation message is sent out to the handset",
            opt_in_workflow_image_urls=[
                {"url": "https://telnyx.com/sign-up"},
                {"url": "https://telnyx.com/company/data-privacy"},
            ],
            phone_numbers=[{"phone_number": "+18773554398"}, {"phone_number": "+18773554399"}],
            production_message_content="Your Telnyx OTP is XXXX",
            use_case="2FA",
            use_case_summary="This is a use case where Telnyx sends out 2FA codes to portal users to verify their identity in order to sign into the portal",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = await response.parse()
        assert_matches_type(VerificationRequestEgress, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_tollfree.verification.requests.with_streaming_response.create(
            additional_information="additionalInformation",
            business_addr1="600 Congress Avenue",
            business_city="Austin",
            business_contact_email="email@example.com",
            business_contact_first_name="John",
            business_contact_last_name="Doe",
            business_contact_phone="+18005550100",
            business_name="Telnyx LLC",
            business_state="Texas",
            business_zip="78701",
            corporate_website="http://example.com",
            isv_reseller="isvReseller",
            message_volume="100,000",
            opt_in_workflow="User signs into the Telnyx portal, enters a number and is prompted to select whether they want to use 2FA verification for security purposes. If they've opted in a confirmation message is sent out to the handset",
            opt_in_workflow_image_urls=[
                {"url": "https://telnyx.com/sign-up"},
                {"url": "https://telnyx.com/company/data-privacy"},
            ],
            phone_numbers=[{"phone_number": "+18773554398"}, {"phone_number": "+18773554399"}],
            production_message_content="Your Telnyx OTP is XXXX",
            use_case="2FA",
            use_case_summary="This is a use case where Telnyx sends out 2FA codes to portal users to verify their identity in order to sign into the portal",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = await response.parse()
            assert_matches_type(VerificationRequestEgress, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        request = await async_client.messaging_tollfree.verification.requests.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VerificationRequestStatus, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_tollfree.verification.requests.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = await response.parse()
        assert_matches_type(VerificationRequestStatus, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_tollfree.verification.requests.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = await response.parse()
            assert_matches_type(VerificationRequestStatus, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.messaging_tollfree.verification.requests.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        request = await async_client.messaging_tollfree.verification.requests.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            additional_information="additionalInformation",
            business_addr1="600 Congress Avenue",
            business_city="Austin",
            business_contact_email="email@example.com",
            business_contact_first_name="John",
            business_contact_last_name="Doe",
            business_contact_phone="+18005550100",
            business_name="Telnyx LLC",
            business_state="Texas",
            business_zip="78701",
            corporate_website="http://example.com",
            isv_reseller="isvReseller",
            message_volume="100,000",
            opt_in_workflow="User signs into the Telnyx portal, enters a number and is prompted to select whether they want to use 2FA verification for security purposes. If they've opted in a confirmation message is sent out to the handset",
            opt_in_workflow_image_urls=[
                {"url": "https://telnyx.com/sign-up"},
                {"url": "https://telnyx.com/company/data-privacy"},
            ],
            phone_numbers=[{"phone_number": "+18773554398"}, {"phone_number": "+18773554399"}],
            production_message_content="Your Telnyx OTP is XXXX",
            use_case="2FA",
            use_case_summary="This is a use case where Telnyx sends out 2FA codes to portal users to verify their identity in order to sign into the portal",
        )
        assert_matches_type(VerificationRequestEgress, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        request = await async_client.messaging_tollfree.verification.requests.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            additional_information="additionalInformation",
            business_addr1="600 Congress Avenue",
            business_city="Austin",
            business_contact_email="email@example.com",
            business_contact_first_name="John",
            business_contact_last_name="Doe",
            business_contact_phone="+18005550100",
            business_name="Telnyx LLC",
            business_state="Texas",
            business_zip="78701",
            corporate_website="http://example.com",
            isv_reseller="isvReseller",
            message_volume="100,000",
            opt_in_workflow="User signs into the Telnyx portal, enters a number and is prompted to select whether they want to use 2FA verification for security purposes. If they've opted in a confirmation message is sent out to the handset",
            opt_in_workflow_image_urls=[
                {"url": "https://telnyx.com/sign-up"},
                {"url": "https://telnyx.com/company/data-privacy"},
            ],
            phone_numbers=[{"phone_number": "+18773554398"}, {"phone_number": "+18773554399"}],
            production_message_content="Your Telnyx OTP is XXXX",
            use_case="2FA",
            use_case_summary="This is a use case where Telnyx sends out 2FA codes to portal users to verify their identity in order to sign into the portal",
            business_addr2="14th Floor",
            webhook_url="http://example-webhook.com",
        )
        assert_matches_type(VerificationRequestEgress, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_tollfree.verification.requests.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            additional_information="additionalInformation",
            business_addr1="600 Congress Avenue",
            business_city="Austin",
            business_contact_email="email@example.com",
            business_contact_first_name="John",
            business_contact_last_name="Doe",
            business_contact_phone="+18005550100",
            business_name="Telnyx LLC",
            business_state="Texas",
            business_zip="78701",
            corporate_website="http://example.com",
            isv_reseller="isvReseller",
            message_volume="100,000",
            opt_in_workflow="User signs into the Telnyx portal, enters a number and is prompted to select whether they want to use 2FA verification for security purposes. If they've opted in a confirmation message is sent out to the handset",
            opt_in_workflow_image_urls=[
                {"url": "https://telnyx.com/sign-up"},
                {"url": "https://telnyx.com/company/data-privacy"},
            ],
            phone_numbers=[{"phone_number": "+18773554398"}, {"phone_number": "+18773554399"}],
            production_message_content="Your Telnyx OTP is XXXX",
            use_case="2FA",
            use_case_summary="This is a use case where Telnyx sends out 2FA codes to portal users to verify their identity in order to sign into the portal",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = await response.parse()
        assert_matches_type(VerificationRequestEgress, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_tollfree.verification.requests.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            additional_information="additionalInformation",
            business_addr1="600 Congress Avenue",
            business_city="Austin",
            business_contact_email="email@example.com",
            business_contact_first_name="John",
            business_contact_last_name="Doe",
            business_contact_phone="+18005550100",
            business_name="Telnyx LLC",
            business_state="Texas",
            business_zip="78701",
            corporate_website="http://example.com",
            isv_reseller="isvReseller",
            message_volume="100,000",
            opt_in_workflow="User signs into the Telnyx portal, enters a number and is prompted to select whether they want to use 2FA verification for security purposes. If they've opted in a confirmation message is sent out to the handset",
            opt_in_workflow_image_urls=[
                {"url": "https://telnyx.com/sign-up"},
                {"url": "https://telnyx.com/company/data-privacy"},
            ],
            phone_numbers=[{"phone_number": "+18773554398"}, {"phone_number": "+18773554399"}],
            production_message_content="Your Telnyx OTP is XXXX",
            use_case="2FA",
            use_case_summary="This is a use case where Telnyx sends out 2FA codes to portal users to verify their identity in order to sign into the portal",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = await response.parse()
            assert_matches_type(VerificationRequestEgress, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.messaging_tollfree.verification.requests.with_raw_response.update(
                id="",
                additional_information="additionalInformation",
                business_addr1="600 Congress Avenue",
                business_city="Austin",
                business_contact_email="email@example.com",
                business_contact_first_name="John",
                business_contact_last_name="Doe",
                business_contact_phone="+18005550100",
                business_name="Telnyx LLC",
                business_state="Texas",
                business_zip="78701",
                corporate_website="http://example.com",
                isv_reseller="isvReseller",
                message_volume="100,000",
                opt_in_workflow="User signs into the Telnyx portal, enters a number and is prompted to select whether they want to use 2FA verification for security purposes. If they've opted in a confirmation message is sent out to the handset",
                opt_in_workflow_image_urls=[
                    {"url": "https://telnyx.com/sign-up"},
                    {"url": "https://telnyx.com/company/data-privacy"},
                ],
                phone_numbers=[{"phone_number": "+18773554398"}, {"phone_number": "+18773554399"}],
                production_message_content="Your Telnyx OTP is XXXX",
                use_case="2FA",
                use_case_summary="This is a use case where Telnyx sends out 2FA codes to portal users to verify their identity in order to sign into the portal",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        request = await async_client.messaging_tollfree.verification.requests.list(
            page=1,
            page_size=1,
        )
        assert_matches_type(RequestListResponse, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        request = await async_client.messaging_tollfree.verification.requests.list(
            page=1,
            page_size=1,
            date_end=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_start=parse_datetime("2019-12-27T18:11:19.117Z"),
            phone_number="phone_number",
            status="Verified",
        )
        assert_matches_type(RequestListResponse, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_tollfree.verification.requests.with_raw_response.list(
            page=1,
            page_size=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = await response.parse()
        assert_matches_type(RequestListResponse, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_tollfree.verification.requests.with_streaming_response.list(
            page=1,
            page_size=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = await response.parse()
            assert_matches_type(RequestListResponse, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        request = await async_client.messaging_tollfree.verification.requests.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messaging_tollfree.verification.requests.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        request = await response.parse()
        assert_matches_type(object, request, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messaging_tollfree.verification.requests.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            request = await response.parse()
            assert_matches_type(object, request, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.messaging_tollfree.verification.requests.with_raw_response.delete(
                "",
            )
