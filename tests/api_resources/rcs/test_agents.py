# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types.rcs import (
    AgentResponse,
    AgentListResponse,
    AgentRetrieveCarrierApprovalsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Telnyx) -> None:
        agent = client.rcs.agents.create(
            brand_id="11111111-1111-4111-8111-111111111111",
            configuration={
                "basics": {
                    "email": {
                        "address": "support@example.com",
                        "label": "Support",
                    }
                }
            },
            display_name="Acme Order Updates",
            use_case="TRANSACTIONAL",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Telnyx) -> None:
        agent = client.rcs.agents.create(
            brand_id="11111111-1111-4111-8111-111111111111",
            configuration={
                "basics": {
                    "email": {
                        "address": "support@example.com",
                        "label": "Support",
                    },
                    "brand_color": "#123456",
                    "description": "Order confirmations and delivery updates",
                    "hero_url": "https://www.example.com/rcs/hero.png",
                    "logo_url": "https://www.example.com/rcs/logo.png",
                    "phone_number": {
                        "label": "x",
                        "number": "+49605132",
                    },
                    "privacy_policy_url": "https://www.example.com/privacy",
                    "terms_and_conditions_url": "https://www.example.com/terms",
                    "website": {
                        "label": "x",
                        "url": "https://example.com",
                    },
                },
                "campaign": {
                    "company_overview": "x",
                    "additional_information": "x",
                    "agent_overview": "x",
                    "consent_settings": {
                        "call_to_action": "x",
                        "double_opt_in": True,
                        "help_response": "x",
                        "opt_in_message": "x",
                        "opt_in_methods": [
                            {
                                "method_type": "SMS",
                                "description": "x",
                            }
                        ],
                        "opt_out_response": "x",
                        "call_to_action_media_url": "https://example.com",
                        "call_to_action_url": "https://example.com",
                        "double_opt_in_message": "x",
                    },
                    "interactions": [
                        {
                            "interaction_type": "TRANSACTIONAL_UPDATES",
                            "description": "x",
                        }
                    ],
                    "message_examples": ["x"],
                },
                "testing": {
                    "test_url": "https://example.com",
                    "additional_information": "x",
                    "message_id": "x",
                },
            },
            display_name="Acme Order Updates",
            use_case="TRANSACTIONAL",
            idempotency_key="Idempotency-Key",
            hosting_region="hosting_region",
            profile_id="profile_id",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Telnyx) -> None:
        response = client.rcs.agents.with_raw_response.create(
            brand_id="11111111-1111-4111-8111-111111111111",
            configuration={
                "basics": {
                    "email": {
                        "address": "support@example.com",
                        "label": "Support",
                    }
                }
            },
            display_name="Acme Order Updates",
            use_case="TRANSACTIONAL",
            idempotency_key="Idempotency-Key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Telnyx) -> None:
        with client.rcs.agents.with_streaming_response.create(
            brand_id="11111111-1111-4111-8111-111111111111",
            configuration={
                "basics": {
                    "email": {
                        "address": "support@example.com",
                        "label": "Support",
                    }
                }
            },
            display_name="Acme Order Updates",
            use_case="TRANSACTIONAL",
            idempotency_key="Idempotency-Key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Telnyx) -> None:
        agent = client.rcs.agents.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Telnyx) -> None:
        response = client.rcs.agents.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Telnyx) -> None:
        with client.rcs.agents.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rcs.agents.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Telnyx) -> None:
        agent = client.rcs.agents.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Telnyx) -> None:
        agent = client.rcs.agents.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            configuration={
                "basics": {
                    "phone_number": {
                        "label": "x",
                        "number": "+49605132",
                    },
                    "brand_color": "#2FDCd1",
                    "description": "x",
                    "email": {
                        "address": "dev@stainless.com",
                        "label": "x",
                    },
                    "hero_url": "https://example.com",
                    "logo_url": "https://example.com",
                    "privacy_policy_url": "https://example.com",
                    "terms_and_conditions_url": "https://example.com",
                    "website": {
                        "label": "x",
                        "url": "https://example.com",
                    },
                },
                "campaign": {
                    "company_overview": "x",
                    "additional_information": "x",
                    "agent_overview": "x",
                    "consent_settings": {
                        "call_to_action": "x",
                        "double_opt_in": True,
                        "help_response": "x",
                        "opt_in_message": "x",
                        "opt_in_methods": [
                            {
                                "method_type": "SMS",
                                "description": "x",
                            }
                        ],
                        "opt_out_response": "x",
                        "call_to_action_media_url": "https://example.com",
                        "call_to_action_url": "https://example.com",
                        "double_opt_in_message": "x",
                    },
                    "interactions": [
                        {
                            "interaction_type": "TRANSACTIONAL_UPDATES",
                            "description": "x",
                        }
                    ],
                    "message_examples": ["x"],
                },
                "testing": {
                    "test_url": "https://example.com",
                    "additional_information": "x",
                    "message_id": "x",
                },
            },
            display_name="Acme Delivery Updates",
            hosting_region="hosting_region",
            profile_id="profile_id",
            use_case="MULTI_USE",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Telnyx) -> None:
        response = client.rcs.agents.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Telnyx) -> None:
        with client.rcs.agents.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rcs.agents.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Telnyx) -> None:
        agent = client.rcs.agents.list()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Telnyx) -> None:
        agent = client.rcs.agents.list(
            brand_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Telnyx) -> None:
        response = client.rcs.agents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Telnyx) -> None:
        with client.rcs.agents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_launch(self, client: Telnyx) -> None:
        agent = client.rcs.agents.launch(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            campaign={
                "company_overview": "Acme provides online retail services.",
                "agent_overview": "The agent sends order confirmations and delivery updates.",
                "consent_settings": {
                    "call_to_action": "Select RCS updates during checkout.",
                    "double_opt_in": False,
                    "help_response": "Contact support@example.com for help.",
                    "opt_in_message": "You are subscribed to Acme order updates.",
                    "opt_in_methods": [{"method_type": "WEBSITE"}],
                    "opt_out_response": "You will receive no more messages.",
                },
                "interactions": [{"interaction_type": "TRANSACTIONAL_UPDATES"}],
                "message_examples": [
                    "Your Acme order is confirmed.",
                    "Your Acme order has shipped.",
                    "Your Acme order was delivered.",
                ],
            },
            testing={"test_url": "https://www.example.com/rcs/test-video"},
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_launch_with_all_params(self, client: Telnyx) -> None:
        agent = client.rcs.agents.launch(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            campaign={
                "company_overview": "Acme provides online retail services.",
                "additional_information": "x",
                "agent_overview": "The agent sends order confirmations and delivery updates.",
                "consent_settings": {
                    "call_to_action": "Select RCS updates during checkout.",
                    "double_opt_in": False,
                    "help_response": "Contact support@example.com for help.",
                    "opt_in_message": "You are subscribed to Acme order updates.",
                    "opt_in_methods": [
                        {
                            "method_type": "WEBSITE",
                            "description": "x",
                        }
                    ],
                    "opt_out_response": "You will receive no more messages.",
                    "call_to_action_media_url": "https://www.example.com/rcs/opt-in.png",
                    "call_to_action_url": "https://www.example.com/checkout",
                    "double_opt_in_message": "x",
                },
                "interactions": [
                    {
                        "interaction_type": "TRANSACTIONAL_UPDATES",
                        "description": "x",
                    }
                ],
                "message_examples": [
                    "Your Acme order is confirmed.",
                    "Your Acme order has shipped.",
                    "Your Acme order was delivered.",
                ],
            },
            testing={
                "test_url": "https://www.example.com/rcs/test-video",
                "additional_information": "Demonstrates START, STOP, HELP, and an order-status interaction.",
                "message_id": "x",
            },
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_launch(self, client: Telnyx) -> None:
        response = client.rcs.agents.with_raw_response.launch(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            campaign={
                "company_overview": "Acme provides online retail services.",
                "agent_overview": "The agent sends order confirmations and delivery updates.",
                "consent_settings": {
                    "call_to_action": "Select RCS updates during checkout.",
                    "double_opt_in": False,
                    "help_response": "Contact support@example.com for help.",
                    "opt_in_message": "You are subscribed to Acme order updates.",
                    "opt_in_methods": [{"method_type": "WEBSITE"}],
                    "opt_out_response": "You will receive no more messages.",
                },
                "interactions": [{"interaction_type": "TRANSACTIONAL_UPDATES"}],
                "message_examples": [
                    "Your Acme order is confirmed.",
                    "Your Acme order has shipped.",
                    "Your Acme order was delivered.",
                ],
            },
            testing={"test_url": "https://www.example.com/rcs/test-video"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_launch(self, client: Telnyx) -> None:
        with client.rcs.agents.with_streaming_response.launch(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            campaign={
                "company_overview": "Acme provides online retail services.",
                "agent_overview": "The agent sends order confirmations and delivery updates.",
                "consent_settings": {
                    "call_to_action": "Select RCS updates during checkout.",
                    "double_opt_in": False,
                    "help_response": "Contact support@example.com for help.",
                    "opt_in_message": "You are subscribed to Acme order updates.",
                    "opt_in_methods": [{"method_type": "WEBSITE"}],
                    "opt_out_response": "You will receive no more messages.",
                },
                "interactions": [{"interaction_type": "TRANSACTIONAL_UPDATES"}],
                "message_examples": [
                    "Your Acme order is confirmed.",
                    "Your Acme order has shipped.",
                    "Your Acme order was delivered.",
                ],
            },
            testing={"test_url": "https://www.example.com/rcs/test-video"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_launch(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rcs.agents.with_raw_response.launch(
                id="",
                campaign={
                    "company_overview": "Acme provides online retail services.",
                    "agent_overview": "The agent sends order confirmations and delivery updates.",
                    "consent_settings": {
                        "call_to_action": "Select RCS updates during checkout.",
                        "double_opt_in": False,
                        "help_response": "Contact support@example.com for help.",
                        "opt_in_message": "You are subscribed to Acme order updates.",
                        "opt_in_methods": [{"method_type": "WEBSITE"}],
                        "opt_out_response": "You will receive no more messages.",
                    },
                    "interactions": [{"interaction_type": "TRANSACTIONAL_UPDATES"}],
                    "message_examples": [
                        "Your Acme order is confirmed.",
                        "Your Acme order has shipped.",
                        "Your Acme order was delivered.",
                    ],
                },
                testing={"test_url": "https://www.example.com/rcs/test-video"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_carrier_approvals(self, client: Telnyx) -> None:
        agent = client.rcs.agents.retrieve_carrier_approvals(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentRetrieveCarrierApprovalsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_carrier_approvals(self, client: Telnyx) -> None:
        response = client.rcs.agents.with_raw_response.retrieve_carrier_approvals(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentRetrieveCarrierApprovalsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_carrier_approvals(self, client: Telnyx) -> None:
        with client.rcs.agents.with_streaming_response.retrieve_carrier_approvals(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentRetrieveCarrierApprovalsResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_carrier_approvals(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rcs.agents.with_raw_response.retrieve_carrier_approvals(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit(self, client: Telnyx) -> None:
        agent = client.rcs.agents.submit(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit(self, client: Telnyx) -> None:
        response = client.rcs.agents.with_raw_response.submit(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit(self, client: Telnyx) -> None:
        with client.rcs.agents.with_streaming_response.submit(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_submit(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.rcs.agents.with_raw_response.submit(
                "",
            )


class TestAsyncAgents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncTelnyx) -> None:
        agent = await async_client.rcs.agents.create(
            brand_id="11111111-1111-4111-8111-111111111111",
            configuration={
                "basics": {
                    "email": {
                        "address": "support@example.com",
                        "label": "Support",
                    }
                }
            },
            display_name="Acme Order Updates",
            use_case="TRANSACTIONAL",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTelnyx) -> None:
        agent = await async_client.rcs.agents.create(
            brand_id="11111111-1111-4111-8111-111111111111",
            configuration={
                "basics": {
                    "email": {
                        "address": "support@example.com",
                        "label": "Support",
                    },
                    "brand_color": "#123456",
                    "description": "Order confirmations and delivery updates",
                    "hero_url": "https://www.example.com/rcs/hero.png",
                    "logo_url": "https://www.example.com/rcs/logo.png",
                    "phone_number": {
                        "label": "x",
                        "number": "+49605132",
                    },
                    "privacy_policy_url": "https://www.example.com/privacy",
                    "terms_and_conditions_url": "https://www.example.com/terms",
                    "website": {
                        "label": "x",
                        "url": "https://example.com",
                    },
                },
                "campaign": {
                    "company_overview": "x",
                    "additional_information": "x",
                    "agent_overview": "x",
                    "consent_settings": {
                        "call_to_action": "x",
                        "double_opt_in": True,
                        "help_response": "x",
                        "opt_in_message": "x",
                        "opt_in_methods": [
                            {
                                "method_type": "SMS",
                                "description": "x",
                            }
                        ],
                        "opt_out_response": "x",
                        "call_to_action_media_url": "https://example.com",
                        "call_to_action_url": "https://example.com",
                        "double_opt_in_message": "x",
                    },
                    "interactions": [
                        {
                            "interaction_type": "TRANSACTIONAL_UPDATES",
                            "description": "x",
                        }
                    ],
                    "message_examples": ["x"],
                },
                "testing": {
                    "test_url": "https://example.com",
                    "additional_information": "x",
                    "message_id": "x",
                },
            },
            display_name="Acme Order Updates",
            use_case="TRANSACTIONAL",
            idempotency_key="Idempotency-Key",
            hosting_region="hosting_region",
            profile_id="profile_id",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.rcs.agents.with_raw_response.create(
            brand_id="11111111-1111-4111-8111-111111111111",
            configuration={
                "basics": {
                    "email": {
                        "address": "support@example.com",
                        "label": "Support",
                    }
                }
            },
            display_name="Acme Order Updates",
            use_case="TRANSACTIONAL",
            idempotency_key="Idempotency-Key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTelnyx) -> None:
        async with async_client.rcs.agents.with_streaming_response.create(
            brand_id="11111111-1111-4111-8111-111111111111",
            configuration={
                "basics": {
                    "email": {
                        "address": "support@example.com",
                        "label": "Support",
                    }
                }
            },
            display_name="Acme Order Updates",
            use_case="TRANSACTIONAL",
            idempotency_key="Idempotency-Key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTelnyx) -> None:
        agent = await async_client.rcs.agents.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.rcs.agents.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTelnyx) -> None:
        async with async_client.rcs.agents.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rcs.agents.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncTelnyx) -> None:
        agent = await async_client.rcs.agents.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTelnyx) -> None:
        agent = await async_client.rcs.agents.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            configuration={
                "basics": {
                    "phone_number": {
                        "label": "x",
                        "number": "+49605132",
                    },
                    "brand_color": "#2FDCd1",
                    "description": "x",
                    "email": {
                        "address": "dev@stainless.com",
                        "label": "x",
                    },
                    "hero_url": "https://example.com",
                    "logo_url": "https://example.com",
                    "privacy_policy_url": "https://example.com",
                    "terms_and_conditions_url": "https://example.com",
                    "website": {
                        "label": "x",
                        "url": "https://example.com",
                    },
                },
                "campaign": {
                    "company_overview": "x",
                    "additional_information": "x",
                    "agent_overview": "x",
                    "consent_settings": {
                        "call_to_action": "x",
                        "double_opt_in": True,
                        "help_response": "x",
                        "opt_in_message": "x",
                        "opt_in_methods": [
                            {
                                "method_type": "SMS",
                                "description": "x",
                            }
                        ],
                        "opt_out_response": "x",
                        "call_to_action_media_url": "https://example.com",
                        "call_to_action_url": "https://example.com",
                        "double_opt_in_message": "x",
                    },
                    "interactions": [
                        {
                            "interaction_type": "TRANSACTIONAL_UPDATES",
                            "description": "x",
                        }
                    ],
                    "message_examples": ["x"],
                },
                "testing": {
                    "test_url": "https://example.com",
                    "additional_information": "x",
                    "message_id": "x",
                },
            },
            display_name="Acme Delivery Updates",
            hosting_region="hosting_region",
            profile_id="profile_id",
            use_case="MULTI_USE",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.rcs.agents.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTelnyx) -> None:
        async with async_client.rcs.agents.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rcs.agents.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncTelnyx) -> None:
        agent = await async_client.rcs.agents.list()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTelnyx) -> None:
        agent = await async_client.rcs.agents.list(
            brand_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.rcs.agents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTelnyx) -> None:
        async with async_client.rcs.agents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_launch(self, async_client: AsyncTelnyx) -> None:
        agent = await async_client.rcs.agents.launch(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            campaign={
                "company_overview": "Acme provides online retail services.",
                "agent_overview": "The agent sends order confirmations and delivery updates.",
                "consent_settings": {
                    "call_to_action": "Select RCS updates during checkout.",
                    "double_opt_in": False,
                    "help_response": "Contact support@example.com for help.",
                    "opt_in_message": "You are subscribed to Acme order updates.",
                    "opt_in_methods": [{"method_type": "WEBSITE"}],
                    "opt_out_response": "You will receive no more messages.",
                },
                "interactions": [{"interaction_type": "TRANSACTIONAL_UPDATES"}],
                "message_examples": [
                    "Your Acme order is confirmed.",
                    "Your Acme order has shipped.",
                    "Your Acme order was delivered.",
                ],
            },
            testing={"test_url": "https://www.example.com/rcs/test-video"},
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_launch_with_all_params(self, async_client: AsyncTelnyx) -> None:
        agent = await async_client.rcs.agents.launch(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            campaign={
                "company_overview": "Acme provides online retail services.",
                "additional_information": "x",
                "agent_overview": "The agent sends order confirmations and delivery updates.",
                "consent_settings": {
                    "call_to_action": "Select RCS updates during checkout.",
                    "double_opt_in": False,
                    "help_response": "Contact support@example.com for help.",
                    "opt_in_message": "You are subscribed to Acme order updates.",
                    "opt_in_methods": [
                        {
                            "method_type": "WEBSITE",
                            "description": "x",
                        }
                    ],
                    "opt_out_response": "You will receive no more messages.",
                    "call_to_action_media_url": "https://www.example.com/rcs/opt-in.png",
                    "call_to_action_url": "https://www.example.com/checkout",
                    "double_opt_in_message": "x",
                },
                "interactions": [
                    {
                        "interaction_type": "TRANSACTIONAL_UPDATES",
                        "description": "x",
                    }
                ],
                "message_examples": [
                    "Your Acme order is confirmed.",
                    "Your Acme order has shipped.",
                    "Your Acme order was delivered.",
                ],
            },
            testing={
                "test_url": "https://www.example.com/rcs/test-video",
                "additional_information": "Demonstrates START, STOP, HELP, and an order-status interaction.",
                "message_id": "x",
            },
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_launch(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.rcs.agents.with_raw_response.launch(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            campaign={
                "company_overview": "Acme provides online retail services.",
                "agent_overview": "The agent sends order confirmations and delivery updates.",
                "consent_settings": {
                    "call_to_action": "Select RCS updates during checkout.",
                    "double_opt_in": False,
                    "help_response": "Contact support@example.com for help.",
                    "opt_in_message": "You are subscribed to Acme order updates.",
                    "opt_in_methods": [{"method_type": "WEBSITE"}],
                    "opt_out_response": "You will receive no more messages.",
                },
                "interactions": [{"interaction_type": "TRANSACTIONAL_UPDATES"}],
                "message_examples": [
                    "Your Acme order is confirmed.",
                    "Your Acme order has shipped.",
                    "Your Acme order was delivered.",
                ],
            },
            testing={"test_url": "https://www.example.com/rcs/test-video"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_launch(self, async_client: AsyncTelnyx) -> None:
        async with async_client.rcs.agents.with_streaming_response.launch(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            campaign={
                "company_overview": "Acme provides online retail services.",
                "agent_overview": "The agent sends order confirmations and delivery updates.",
                "consent_settings": {
                    "call_to_action": "Select RCS updates during checkout.",
                    "double_opt_in": False,
                    "help_response": "Contact support@example.com for help.",
                    "opt_in_message": "You are subscribed to Acme order updates.",
                    "opt_in_methods": [{"method_type": "WEBSITE"}],
                    "opt_out_response": "You will receive no more messages.",
                },
                "interactions": [{"interaction_type": "TRANSACTIONAL_UPDATES"}],
                "message_examples": [
                    "Your Acme order is confirmed.",
                    "Your Acme order has shipped.",
                    "Your Acme order was delivered.",
                ],
            },
            testing={"test_url": "https://www.example.com/rcs/test-video"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_launch(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rcs.agents.with_raw_response.launch(
                id="",
                campaign={
                    "company_overview": "Acme provides online retail services.",
                    "agent_overview": "The agent sends order confirmations and delivery updates.",
                    "consent_settings": {
                        "call_to_action": "Select RCS updates during checkout.",
                        "double_opt_in": False,
                        "help_response": "Contact support@example.com for help.",
                        "opt_in_message": "You are subscribed to Acme order updates.",
                        "opt_in_methods": [{"method_type": "WEBSITE"}],
                        "opt_out_response": "You will receive no more messages.",
                    },
                    "interactions": [{"interaction_type": "TRANSACTIONAL_UPDATES"}],
                    "message_examples": [
                        "Your Acme order is confirmed.",
                        "Your Acme order has shipped.",
                        "Your Acme order was delivered.",
                    ],
                },
                testing={"test_url": "https://www.example.com/rcs/test-video"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_carrier_approvals(self, async_client: AsyncTelnyx) -> None:
        agent = await async_client.rcs.agents.retrieve_carrier_approvals(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentRetrieveCarrierApprovalsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_carrier_approvals(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.rcs.agents.with_raw_response.retrieve_carrier_approvals(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentRetrieveCarrierApprovalsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_carrier_approvals(self, async_client: AsyncTelnyx) -> None:
        async with async_client.rcs.agents.with_streaming_response.retrieve_carrier_approvals(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentRetrieveCarrierApprovalsResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_carrier_approvals(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rcs.agents.with_raw_response.retrieve_carrier_approvals(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit(self, async_client: AsyncTelnyx) -> None:
        agent = await async_client.rcs.agents.submit(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.rcs.agents.with_raw_response.submit(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncTelnyx) -> None:
        async with async_client.rcs.agents.with_streaming_response.submit(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_submit(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.rcs.agents.with_raw_response.submit(
                "",
            )
