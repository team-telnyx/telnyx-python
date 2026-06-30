# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.dir import (
    ReferenceListResponse,
    ReferenceSubmitResponse,
    ReferenceUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReferences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        reference = client.dir.references.update(
            slot=0,
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            ref_type="business",
        )
        assert_matches_type(ReferenceUpdateResponse, reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        reference = client.dir.references.update(
            slot=0,
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            ref_type="business",
            email="dana.reyes@example.com",
            full_name="Dana Reyes",
            job_title="VP of Operations",
            organization="Acme Logistics",
            phone_e164="+14155550123",
            relationship_to_registrant="Supplier",
            timezone="America/New_York",
        )
        assert_matches_type(ReferenceUpdateResponse, reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.dir.references.with_raw_response.update(
            slot=0,
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            ref_type="business",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reference = response.parse()
        assert_matches_type(ReferenceUpdateResponse, reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.dir.references.with_streaming_response.update(
            slot=0,
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            ref_type="business",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reference = response.parse()
            assert_matches_type(ReferenceUpdateResponse, reference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            client.dir.references.with_raw_response.update(
                slot=0,
                dir_id="",
                ref_type="business",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        reference = client.dir.references.list(
            "16635d38-75a6-4481-82e8-69af60e05011",
        )
        assert_matches_type(ReferenceListResponse, reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.dir.references.with_raw_response.list(
            "16635d38-75a6-4481-82e8-69af60e05011",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reference = response.parse()
        assert_matches_type(ReferenceListResponse, reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.dir.references.with_streaming_response.list(
            "16635d38-75a6-4481-82e8-69af60e05011",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reference = response.parse()
            assert_matches_type(ReferenceListResponse, reference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            client.dir.references.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit(self, client: Telnyx) -> None:
        reference = client.dir.references.submit(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            business_references=[
                {
                    "email": "dana.reyes@example.com",
                    "full_name": "Dana Reyes",
                    "phone_e164": "+14155550123",
                    "timezone": "America/New_York",
                },
                {
                    "email": "dana.reyes@example.com",
                    "full_name": "Dana Reyes",
                    "phone_e164": "+14155550123",
                    "timezone": "America/New_York",
                },
            ],
            financial_reference={
                "email": "dana.reyes@example.com",
                "full_name": "Dana Reyes",
                "phone_e164": "+14155550123",
                "timezone": "America/New_York",
            },
        )
        assert_matches_type(ReferenceSubmitResponse, reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_with_all_params(self, client: Telnyx) -> None:
        reference = client.dir.references.submit(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            business_references=[
                {
                    "email": "dana.reyes@example.com",
                    "full_name": "Dana Reyes",
                    "phone_e164": "+14155550123",
                    "timezone": "America/New_York",
                    "job_title": "VP of Operations",
                    "organization": "Acme Logistics",
                    "relationship_to_registrant": "Supplier",
                },
                {
                    "email": "dana.reyes@example.com",
                    "full_name": "Dana Reyes",
                    "phone_e164": "+14155550123",
                    "timezone": "America/New_York",
                    "job_title": "VP of Operations",
                    "organization": "Acme Logistics",
                    "relationship_to_registrant": "Supplier",
                },
            ],
            financial_reference={
                "email": "dana.reyes@example.com",
                "full_name": "Dana Reyes",
                "phone_e164": "+14155550123",
                "timezone": "America/New_York",
                "job_title": "VP of Operations",
                "organization": "Acme Logistics",
                "relationship_to_registrant": "Supplier",
            },
        )
        assert_matches_type(ReferenceSubmitResponse, reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit(self, client: Telnyx) -> None:
        response = client.dir.references.with_raw_response.submit(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            business_references=[
                {
                    "email": "dana.reyes@example.com",
                    "full_name": "Dana Reyes",
                    "phone_e164": "+14155550123",
                    "timezone": "America/New_York",
                },
                {
                    "email": "dana.reyes@example.com",
                    "full_name": "Dana Reyes",
                    "phone_e164": "+14155550123",
                    "timezone": "America/New_York",
                },
            ],
            financial_reference={
                "email": "dana.reyes@example.com",
                "full_name": "Dana Reyes",
                "phone_e164": "+14155550123",
                "timezone": "America/New_York",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reference = response.parse()
        assert_matches_type(ReferenceSubmitResponse, reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit(self, client: Telnyx) -> None:
        with client.dir.references.with_streaming_response.submit(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            business_references=[
                {
                    "email": "dana.reyes@example.com",
                    "full_name": "Dana Reyes",
                    "phone_e164": "+14155550123",
                    "timezone": "America/New_York",
                },
                {
                    "email": "dana.reyes@example.com",
                    "full_name": "Dana Reyes",
                    "phone_e164": "+14155550123",
                    "timezone": "America/New_York",
                },
            ],
            financial_reference={
                "email": "dana.reyes@example.com",
                "full_name": "Dana Reyes",
                "phone_e164": "+14155550123",
                "timezone": "America/New_York",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reference = response.parse()
            assert_matches_type(ReferenceSubmitResponse, reference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_submit(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            client.dir.references.with_raw_response.submit(
                dir_id="",
                business_references=[
                    {
                        "email": "dana.reyes@example.com",
                        "full_name": "Dana Reyes",
                        "phone_e164": "+14155550123",
                        "timezone": "America/New_York",
                    },
                    {
                        "email": "dana.reyes@example.com",
                        "full_name": "Dana Reyes",
                        "phone_e164": "+14155550123",
                        "timezone": "America/New_York",
                    },
                ],
                financial_reference={
                    "email": "dana.reyes@example.com",
                    "full_name": "Dana Reyes",
                    "phone_e164": "+14155550123",
                    "timezone": "America/New_York",
                },
            )


class TestAsyncReferences:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        reference = await async_client.dir.references.update(
            slot=0,
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            ref_type="business",
        )
        assert_matches_type(ReferenceUpdateResponse, reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        reference = await async_client.dir.references.update(
            slot=0,
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            ref_type="business",
            email="dana.reyes@example.com",
            full_name="Dana Reyes",
            job_title="VP of Operations",
            organization="Acme Logistics",
            phone_e164="+14155550123",
            relationship_to_registrant="Supplier",
            timezone="America/New_York",
        )
        assert_matches_type(ReferenceUpdateResponse, reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dir.references.with_raw_response.update(
            slot=0,
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            ref_type="business",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reference = await response.parse()
        assert_matches_type(ReferenceUpdateResponse, reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dir.references.with_streaming_response.update(
            slot=0,
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            ref_type="business",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reference = await response.parse()
            assert_matches_type(ReferenceUpdateResponse, reference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            await async_client.dir.references.with_raw_response.update(
                slot=0,
                dir_id="",
                ref_type="business",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        reference = await async_client.dir.references.list(
            "16635d38-75a6-4481-82e8-69af60e05011",
        )
        assert_matches_type(ReferenceListResponse, reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dir.references.with_raw_response.list(
            "16635d38-75a6-4481-82e8-69af60e05011",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reference = await response.parse()
        assert_matches_type(ReferenceListResponse, reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dir.references.with_streaming_response.list(
            "16635d38-75a6-4481-82e8-69af60e05011",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reference = await response.parse()
            assert_matches_type(ReferenceListResponse, reference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            await async_client.dir.references.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit(self, async_client: AsyncTelnyx) -> None:
        reference = await async_client.dir.references.submit(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            business_references=[
                {
                    "email": "dana.reyes@example.com",
                    "full_name": "Dana Reyes",
                    "phone_e164": "+14155550123",
                    "timezone": "America/New_York",
                },
                {
                    "email": "dana.reyes@example.com",
                    "full_name": "Dana Reyes",
                    "phone_e164": "+14155550123",
                    "timezone": "America/New_York",
                },
            ],
            financial_reference={
                "email": "dana.reyes@example.com",
                "full_name": "Dana Reyes",
                "phone_e164": "+14155550123",
                "timezone": "America/New_York",
            },
        )
        assert_matches_type(ReferenceSubmitResponse, reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_with_all_params(self, async_client: AsyncTelnyx) -> None:
        reference = await async_client.dir.references.submit(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            business_references=[
                {
                    "email": "dana.reyes@example.com",
                    "full_name": "Dana Reyes",
                    "phone_e164": "+14155550123",
                    "timezone": "America/New_York",
                    "job_title": "VP of Operations",
                    "organization": "Acme Logistics",
                    "relationship_to_registrant": "Supplier",
                },
                {
                    "email": "dana.reyes@example.com",
                    "full_name": "Dana Reyes",
                    "phone_e164": "+14155550123",
                    "timezone": "America/New_York",
                    "job_title": "VP of Operations",
                    "organization": "Acme Logistics",
                    "relationship_to_registrant": "Supplier",
                },
            ],
            financial_reference={
                "email": "dana.reyes@example.com",
                "full_name": "Dana Reyes",
                "phone_e164": "+14155550123",
                "timezone": "America/New_York",
                "job_title": "VP of Operations",
                "organization": "Acme Logistics",
                "relationship_to_registrant": "Supplier",
            },
        )
        assert_matches_type(ReferenceSubmitResponse, reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.dir.references.with_raw_response.submit(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            business_references=[
                {
                    "email": "dana.reyes@example.com",
                    "full_name": "Dana Reyes",
                    "phone_e164": "+14155550123",
                    "timezone": "America/New_York",
                },
                {
                    "email": "dana.reyes@example.com",
                    "full_name": "Dana Reyes",
                    "phone_e164": "+14155550123",
                    "timezone": "America/New_York",
                },
            ],
            financial_reference={
                "email": "dana.reyes@example.com",
                "full_name": "Dana Reyes",
                "phone_e164": "+14155550123",
                "timezone": "America/New_York",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reference = await response.parse()
        assert_matches_type(ReferenceSubmitResponse, reference, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncTelnyx) -> None:
        async with async_client.dir.references.with_streaming_response.submit(
            dir_id="16635d38-75a6-4481-82e8-69af60e05011",
            business_references=[
                {
                    "email": "dana.reyes@example.com",
                    "full_name": "Dana Reyes",
                    "phone_e164": "+14155550123",
                    "timezone": "America/New_York",
                },
                {
                    "email": "dana.reyes@example.com",
                    "full_name": "Dana Reyes",
                    "phone_e164": "+14155550123",
                    "timezone": "America/New_York",
                },
            ],
            financial_reference={
                "email": "dana.reyes@example.com",
                "full_name": "Dana Reyes",
                "phone_e164": "+14155550123",
                "timezone": "America/New_York",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reference = await response.parse()
            assert_matches_type(ReferenceSubmitResponse, reference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_submit(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dir_id` but received ''"):
            await async_client.dir.references.with_raw_response.submit(
                dir_id="",
                business_references=[
                    {
                        "email": "dana.reyes@example.com",
                        "full_name": "Dana Reyes",
                        "phone_e164": "+14155550123",
                        "timezone": "America/New_York",
                    },
                    {
                        "email": "dana.reyes@example.com",
                        "full_name": "Dana Reyes",
                        "phone_e164": "+14155550123",
                        "timezone": "America/New_York",
                    },
                ],
                financial_reference={
                    "email": "dana.reyes@example.com",
                    "full_name": "Dana Reyes",
                    "phone_e164": "+14155550123",
                    "timezone": "America/New_York",
                },
            )
