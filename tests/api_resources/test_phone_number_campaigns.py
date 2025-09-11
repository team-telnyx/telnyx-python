# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    PhoneNumberCampaign,
    PhoneNumberCampaignListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhoneNumberCampaigns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        phone_number_campaign = client.phone_number_campaigns.create(
            campaign_id="4b300178-131c-d902-d54e-72d90ba1620j",
            phone_number="+18005550199",
        )
        assert_matches_type(PhoneNumberCampaign, phone_number_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.phone_number_campaigns.with_raw_response.create(
            campaign_id="4b300178-131c-d902-d54e-72d90ba1620j",
            phone_number="+18005550199",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_campaign = response.parse()
        assert_matches_type(PhoneNumberCampaign, phone_number_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.phone_number_campaigns.with_streaming_response.create(
            campaign_id="4b300178-131c-d902-d54e-72d90ba1620j",
            phone_number="+18005550199",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_campaign = response.parse()
            assert_matches_type(PhoneNumberCampaign, phone_number_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        phone_number_campaign = client.phone_number_campaigns.retrieve(
            "phoneNumber",
        )
        assert_matches_type(PhoneNumberCampaign, phone_number_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.phone_number_campaigns.with_raw_response.retrieve(
            "phoneNumber",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_campaign = response.parse()
        assert_matches_type(PhoneNumberCampaign, phone_number_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.phone_number_campaigns.with_streaming_response.retrieve(
            "phoneNumber",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_campaign = response.parse()
            assert_matches_type(PhoneNumberCampaign, phone_number_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.phone_number_campaigns.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        phone_number_campaign = client.phone_number_campaigns.update(
            path_phone_number="phoneNumber",
            campaign_id="4b300178-131c-d902-d54e-72d90ba1620j",
            body_phone_number="+18005550199",
        )
        assert_matches_type(PhoneNumberCampaign, phone_number_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.phone_number_campaigns.with_raw_response.update(
            path_phone_number="phoneNumber",
            campaign_id="4b300178-131c-d902-d54e-72d90ba1620j",
            body_phone_number="+18005550199",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_campaign = response.parse()
        assert_matches_type(PhoneNumberCampaign, phone_number_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.phone_number_campaigns.with_streaming_response.update(
            path_phone_number="phoneNumber",
            campaign_id="4b300178-131c-d902-d54e-72d90ba1620j",
            body_phone_number="+18005550199",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_campaign = response.parse()
            assert_matches_type(PhoneNumberCampaign, phone_number_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_phone_number` but received ''"):
            client.phone_number_campaigns.with_raw_response.update(
                path_phone_number="",
                campaign_id="4b300178-131c-d902-d54e-72d90ba1620j",
                body_phone_number="+18005550199",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        phone_number_campaign = client.phone_number_campaigns.list()
        assert_matches_type(PhoneNumberCampaignListResponse, phone_number_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        phone_number_campaign = client.phone_number_campaigns.list(
            filter={
                "tcr_brand_id": "BRANDID",
                "tcr_campaign_id": "CAMPID3",
                "telnyx_brand_id": "f3575e15-32ce-400e-a4c0-dd78800c20b0",
                "telnyx_campaign_id": "f3575e15-32ce-400e-a4c0-dd78800c20b0",
            },
            page=0,
            records_per_page=0,
            sort="assignmentStatus",
        )
        assert_matches_type(PhoneNumberCampaignListResponse, phone_number_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.phone_number_campaigns.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_campaign = response.parse()
        assert_matches_type(PhoneNumberCampaignListResponse, phone_number_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.phone_number_campaigns.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_campaign = response.parse()
            assert_matches_type(PhoneNumberCampaignListResponse, phone_number_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        phone_number_campaign = client.phone_number_campaigns.delete(
            "phoneNumber",
        )
        assert_matches_type(PhoneNumberCampaign, phone_number_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.phone_number_campaigns.with_raw_response.delete(
            "phoneNumber",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_campaign = response.parse()
        assert_matches_type(PhoneNumberCampaign, phone_number_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.phone_number_campaigns.with_streaming_response.delete(
            "phoneNumber",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_campaign = response.parse()
            assert_matches_type(PhoneNumberCampaign, phone_number_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.phone_number_campaigns.with_raw_response.delete(
                "",
            )


class TestAsyncPhoneNumberCampaigns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        phone_number_campaign = await async_client.phone_number_campaigns.create(
            campaign_id="4b300178-131c-d902-d54e-72d90ba1620j",
            phone_number="+18005550199",
        )
        assert_matches_type(PhoneNumberCampaign, phone_number_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.phone_number_campaigns.with_raw_response.create(
            campaign_id="4b300178-131c-d902-d54e-72d90ba1620j",
            phone_number="+18005550199",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_campaign = await response.parse()
        assert_matches_type(PhoneNumberCampaign, phone_number_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.phone_number_campaigns.with_streaming_response.create(
            campaign_id="4b300178-131c-d902-d54e-72d90ba1620j",
            phone_number="+18005550199",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_campaign = await response.parse()
            assert_matches_type(PhoneNumberCampaign, phone_number_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        phone_number_campaign = await async_client.phone_number_campaigns.retrieve(
            "phoneNumber",
        )
        assert_matches_type(PhoneNumberCampaign, phone_number_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.phone_number_campaigns.with_raw_response.retrieve(
            "phoneNumber",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_campaign = await response.parse()
        assert_matches_type(PhoneNumberCampaign, phone_number_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.phone_number_campaigns.with_streaming_response.retrieve(
            "phoneNumber",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_campaign = await response.parse()
            assert_matches_type(PhoneNumberCampaign, phone_number_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.phone_number_campaigns.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        phone_number_campaign = await async_client.phone_number_campaigns.update(
            path_phone_number="phoneNumber",
            campaign_id="4b300178-131c-d902-d54e-72d90ba1620j",
            body_phone_number="+18005550199",
        )
        assert_matches_type(PhoneNumberCampaign, phone_number_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.phone_number_campaigns.with_raw_response.update(
            path_phone_number="phoneNumber",
            campaign_id="4b300178-131c-d902-d54e-72d90ba1620j",
            body_phone_number="+18005550199",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_campaign = await response.parse()
        assert_matches_type(PhoneNumberCampaign, phone_number_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.phone_number_campaigns.with_streaming_response.update(
            path_phone_number="phoneNumber",
            campaign_id="4b300178-131c-d902-d54e-72d90ba1620j",
            body_phone_number="+18005550199",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_campaign = await response.parse()
            assert_matches_type(PhoneNumberCampaign, phone_number_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_phone_number` but received ''"):
            await async_client.phone_number_campaigns.with_raw_response.update(
                path_phone_number="",
                campaign_id="4b300178-131c-d902-d54e-72d90ba1620j",
                body_phone_number="+18005550199",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        phone_number_campaign = await async_client.phone_number_campaigns.list()
        assert_matches_type(PhoneNumberCampaignListResponse, phone_number_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        phone_number_campaign = await async_client.phone_number_campaigns.list(
            filter={
                "tcr_brand_id": "BRANDID",
                "tcr_campaign_id": "CAMPID3",
                "telnyx_brand_id": "f3575e15-32ce-400e-a4c0-dd78800c20b0",
                "telnyx_campaign_id": "f3575e15-32ce-400e-a4c0-dd78800c20b0",
            },
            page=0,
            records_per_page=0,
            sort="assignmentStatus",
        )
        assert_matches_type(PhoneNumberCampaignListResponse, phone_number_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.phone_number_campaigns.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_campaign = await response.parse()
        assert_matches_type(PhoneNumberCampaignListResponse, phone_number_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.phone_number_campaigns.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_campaign = await response.parse()
            assert_matches_type(PhoneNumberCampaignListResponse, phone_number_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        phone_number_campaign = await async_client.phone_number_campaigns.delete(
            "phoneNumber",
        )
        assert_matches_type(PhoneNumberCampaign, phone_number_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.phone_number_campaigns.with_raw_response.delete(
            "phoneNumber",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number_campaign = await response.parse()
        assert_matches_type(PhoneNumberCampaign, phone_number_campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.phone_number_campaigns.with_streaming_response.delete(
            "phoneNumber",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number_campaign = await response.parse()
            assert_matches_type(PhoneNumberCampaign, phone_number_campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.phone_number_campaigns.with_raw_response.delete(
                "",
            )
