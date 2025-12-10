# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    AuthenticationProviderListResponse,
    AuthenticationProviderCreateResponse,
    AuthenticationProviderDeleteResponse,
    AuthenticationProviderUpdateResponse,
    AuthenticationProviderRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuthenticationProviders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        authentication_provider = client.authentication_providers.create(
            name="Okta",
            settings={
                "idp_cert_fingerprint": "13:38:C7:BB:C9:FF:4A:70:38:3A:E3:D9:5C:CD:DB:2E:50:1E:80:A7",
                "idp_entity_id": "https://myorg.myidp.com/saml/metadata",
                "idp_sso_target_url": "https://myorg.myidp.com/trust/saml2/http-post/sso",
            },
            short_name="myorg",
        )
        assert_matches_type(AuthenticationProviderCreateResponse, authentication_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        authentication_provider = client.authentication_providers.create(
            name="Okta",
            settings={
                "idp_cert_fingerprint": "13:38:C7:BB:C9:FF:4A:70:38:3A:E3:D9:5C:CD:DB:2E:50:1E:80:A7",
                "idp_entity_id": "https://myorg.myidp.com/saml/metadata",
                "idp_sso_target_url": "https://myorg.myidp.com/trust/saml2/http-post/sso",
                "idp_cert_fingerprint_algorithm": "sha256",
            },
            short_name="myorg",
            active=True,
            settings_url="https://myorg.myidp.com/saml/metadata",
        )
        assert_matches_type(AuthenticationProviderCreateResponse, authentication_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.authentication_providers.with_raw_response.create(
            name="Okta",
            settings={
                "idp_cert_fingerprint": "13:38:C7:BB:C9:FF:4A:70:38:3A:E3:D9:5C:CD:DB:2E:50:1E:80:A7",
                "idp_entity_id": "https://myorg.myidp.com/saml/metadata",
                "idp_sso_target_url": "https://myorg.myidp.com/trust/saml2/http-post/sso",
            },
            short_name="myorg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication_provider = response.parse()
        assert_matches_type(AuthenticationProviderCreateResponse, authentication_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.authentication_providers.with_streaming_response.create(
            name="Okta",
            settings={
                "idp_cert_fingerprint": "13:38:C7:BB:C9:FF:4A:70:38:3A:E3:D9:5C:CD:DB:2E:50:1E:80:A7",
                "idp_entity_id": "https://myorg.myidp.com/saml/metadata",
                "idp_sso_target_url": "https://myorg.myidp.com/trust/saml2/http-post/sso",
            },
            short_name="myorg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication_provider = response.parse()
            assert_matches_type(AuthenticationProviderCreateResponse, authentication_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        authentication_provider = client.authentication_providers.retrieve(
            "id",
        )
        assert_matches_type(AuthenticationProviderRetrieveResponse, authentication_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.authentication_providers.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication_provider = response.parse()
        assert_matches_type(AuthenticationProviderRetrieveResponse, authentication_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.authentication_providers.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication_provider = response.parse()
            assert_matches_type(AuthenticationProviderRetrieveResponse, authentication_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.authentication_providers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        authentication_provider = client.authentication_providers.update(
            id="id",
        )
        assert_matches_type(AuthenticationProviderUpdateResponse, authentication_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        authentication_provider = client.authentication_providers.update(
            id="id",
            active=True,
            name="Okta",
            settings={
                "idp_cert_fingerprint": "13:38:C7:BB:C9:FF:4A:70:38:3A:E3:D9:5C:CD:DB:2E:50:1E:80:A7",
                "idp_entity_id": "https://myorg.myidp.com/saml/metadata",
                "idp_sso_target_url": "https://myorg.myidp.com/trust/saml2/http-post/sso",
                "idp_cert_fingerprint_algorithm": "sha1",
            },
            settings_url="https://myorg.myidp.com/saml/metadata",
            short_name="myorg",
        )
        assert_matches_type(AuthenticationProviderUpdateResponse, authentication_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.authentication_providers.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication_provider = response.parse()
        assert_matches_type(AuthenticationProviderUpdateResponse, authentication_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.authentication_providers.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication_provider = response.parse()
            assert_matches_type(AuthenticationProviderUpdateResponse, authentication_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.authentication_providers.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        authentication_provider = client.authentication_providers.list()
        assert_matches_type(AuthenticationProviderListResponse, authentication_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        authentication_provider = client.authentication_providers.list(
            page={
                "number": 1,
                "size": 1,
            },
            sort="name",
        )
        assert_matches_type(AuthenticationProviderListResponse, authentication_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.authentication_providers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication_provider = response.parse()
        assert_matches_type(AuthenticationProviderListResponse, authentication_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.authentication_providers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication_provider = response.parse()
            assert_matches_type(AuthenticationProviderListResponse, authentication_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Telnyx) -> None:
        authentication_provider = client.authentication_providers.delete(
            "id",
        )
        assert_matches_type(AuthenticationProviderDeleteResponse, authentication_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Telnyx) -> None:
        response = client.authentication_providers.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication_provider = response.parse()
        assert_matches_type(AuthenticationProviderDeleteResponse, authentication_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Telnyx) -> None:
        with client.authentication_providers.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication_provider = response.parse()
            assert_matches_type(AuthenticationProviderDeleteResponse, authentication_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.authentication_providers.with_raw_response.delete(
                "",
            )


class TestAsyncAuthenticationProviders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        authentication_provider = await async_client.authentication_providers.create(
            name="Okta",
            settings={
                "idp_cert_fingerprint": "13:38:C7:BB:C9:FF:4A:70:38:3A:E3:D9:5C:CD:DB:2E:50:1E:80:A7",
                "idp_entity_id": "https://myorg.myidp.com/saml/metadata",
                "idp_sso_target_url": "https://myorg.myidp.com/trust/saml2/http-post/sso",
            },
            short_name="myorg",
        )
        assert_matches_type(AuthenticationProviderCreateResponse, authentication_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        authentication_provider = await async_client.authentication_providers.create(
            name="Okta",
            settings={
                "idp_cert_fingerprint": "13:38:C7:BB:C9:FF:4A:70:38:3A:E3:D9:5C:CD:DB:2E:50:1E:80:A7",
                "idp_entity_id": "https://myorg.myidp.com/saml/metadata",
                "idp_sso_target_url": "https://myorg.myidp.com/trust/saml2/http-post/sso",
                "idp_cert_fingerprint_algorithm": "sha256",
            },
            short_name="myorg",
            active=True,
            settings_url="https://myorg.myidp.com/saml/metadata",
        )
        assert_matches_type(AuthenticationProviderCreateResponse, authentication_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.authentication_providers.with_raw_response.create(
            name="Okta",
            settings={
                "idp_cert_fingerprint": "13:38:C7:BB:C9:FF:4A:70:38:3A:E3:D9:5C:CD:DB:2E:50:1E:80:A7",
                "idp_entity_id": "https://myorg.myidp.com/saml/metadata",
                "idp_sso_target_url": "https://myorg.myidp.com/trust/saml2/http-post/sso",
            },
            short_name="myorg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication_provider = await response.parse()
        assert_matches_type(AuthenticationProviderCreateResponse, authentication_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.authentication_providers.with_streaming_response.create(
            name="Okta",
            settings={
                "idp_cert_fingerprint": "13:38:C7:BB:C9:FF:4A:70:38:3A:E3:D9:5C:CD:DB:2E:50:1E:80:A7",
                "idp_entity_id": "https://myorg.myidp.com/saml/metadata",
                "idp_sso_target_url": "https://myorg.myidp.com/trust/saml2/http-post/sso",
            },
            short_name="myorg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication_provider = await response.parse()
            assert_matches_type(AuthenticationProviderCreateResponse, authentication_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        authentication_provider = await async_client.authentication_providers.retrieve(
            "id",
        )
        assert_matches_type(AuthenticationProviderRetrieveResponse, authentication_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.authentication_providers.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication_provider = await response.parse()
        assert_matches_type(AuthenticationProviderRetrieveResponse, authentication_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.authentication_providers.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication_provider = await response.parse()
            assert_matches_type(AuthenticationProviderRetrieveResponse, authentication_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.authentication_providers.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        authentication_provider = await async_client.authentication_providers.update(
            id="id",
        )
        assert_matches_type(AuthenticationProviderUpdateResponse, authentication_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        authentication_provider = await async_client.authentication_providers.update(
            id="id",
            active=True,
            name="Okta",
            settings={
                "idp_cert_fingerprint": "13:38:C7:BB:C9:FF:4A:70:38:3A:E3:D9:5C:CD:DB:2E:50:1E:80:A7",
                "idp_entity_id": "https://myorg.myidp.com/saml/metadata",
                "idp_sso_target_url": "https://myorg.myidp.com/trust/saml2/http-post/sso",
                "idp_cert_fingerprint_algorithm": "sha1",
            },
            settings_url="https://myorg.myidp.com/saml/metadata",
            short_name="myorg",
        )
        assert_matches_type(AuthenticationProviderUpdateResponse, authentication_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.authentication_providers.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication_provider = await response.parse()
        assert_matches_type(AuthenticationProviderUpdateResponse, authentication_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.authentication_providers.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication_provider = await response.parse()
            assert_matches_type(AuthenticationProviderUpdateResponse, authentication_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.authentication_providers.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        authentication_provider = await async_client.authentication_providers.list()
        assert_matches_type(AuthenticationProviderListResponse, authentication_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        authentication_provider = await async_client.authentication_providers.list(
            page={
                "number": 1,
                "size": 1,
            },
            sort="name",
        )
        assert_matches_type(AuthenticationProviderListResponse, authentication_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.authentication_providers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication_provider = await response.parse()
        assert_matches_type(AuthenticationProviderListResponse, authentication_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.authentication_providers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication_provider = await response.parse()
            assert_matches_type(AuthenticationProviderListResponse, authentication_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncTelnyx) -> None:
        authentication_provider = await async_client.authentication_providers.delete(
            "id",
        )
        assert_matches_type(AuthenticationProviderDeleteResponse, authentication_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.authentication_providers.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication_provider = await response.parse()
        assert_matches_type(AuthenticationProviderDeleteResponse, authentication_provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTelnyx) -> None:
        async with async_client.authentication_providers.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication_provider = await response.parse()
            assert_matches_type(AuthenticationProviderDeleteResponse, authentication_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.authentication_providers.with_raw_response.delete(
                "",
            )
