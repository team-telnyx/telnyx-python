# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    MesssageRcsResponse,
    MesssageWhatsappResponse,
)
from telnyx._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMesssages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_rcs(self, client: Telnyx) -> None:
        messsage = client.messsages.rcs(
            agent_id="Agent007",
            agent_message={},
            messaging_profile_id="messaging_profile_id",
            to="+13125551234",
        )
        assert_matches_type(MesssageRcsResponse, messsage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_rcs_with_all_params(self, client: Telnyx) -> None:
        messsage = client.messsages.rcs(
            agent_id="Agent007",
            agent_message={
                "content_message": {
                    "content_info": {
                        "file_url": "https://example.com/elephant.jpg",
                        "force_refresh": True,
                        "thumbnail_url": "thumbnail_url",
                    },
                    "rich_card": {
                        "carousel_card": {
                            "card_contents": [
                                {
                                    "description": "description",
                                    "media": {
                                        "content_info": {
                                            "file_url": "https://example.com/elephant.jpg",
                                            "force_refresh": True,
                                            "thumbnail_url": "thumbnail_url",
                                        },
                                        "height": "MEDIUM",
                                    },
                                    "suggestions": [
                                        {
                                            "action": {
                                                "create_calendar_event_action": {
                                                    "description": "description",
                                                    "end_time": parse_datetime("2024-10-02T15:02:31Z"),
                                                    "start_time": parse_datetime("2024-10-02T15:01:23Z"),
                                                    "title": "title",
                                                },
                                                "dial_action": {"phone_number": "+13125551234"},
                                                "fallback_url": "fallback_url",
                                                "open_url_action": {
                                                    "application": "BROWSER",
                                                    "url": "http://example.com",
                                                    "webview_view_mode": "HALF",
                                                    "description": "description",
                                                },
                                                "postback_data": "postback_data",
                                                "share_location_action": {"foo": "bar"},
                                                "text": "Hello world",
                                                "view_location_action": {
                                                    "label": "label",
                                                    "lat_long": {
                                                        "latitude": 41.8,
                                                        "longitude": -87.6,
                                                    },
                                                    "query": "query",
                                                },
                                            },
                                            "reply": {
                                                "postback_data": "postback_data",
                                                "text": "text",
                                            },
                                        }
                                    ],
                                    "title": "Elephant",
                                }
                            ],
                            "card_width": "SMALL",
                        },
                        "standalone_card": {
                            "card_content": {
                                "description": "description",
                                "media": {
                                    "content_info": {
                                        "file_url": "https://example.com/elephant.jpg",
                                        "force_refresh": True,
                                        "thumbnail_url": "thumbnail_url",
                                    },
                                    "height": "MEDIUM",
                                },
                                "suggestions": [
                                    {
                                        "action": {
                                            "create_calendar_event_action": {
                                                "description": "description",
                                                "end_time": parse_datetime("2024-10-02T15:02:31Z"),
                                                "start_time": parse_datetime("2024-10-02T15:01:23Z"),
                                                "title": "title",
                                            },
                                            "dial_action": {"phone_number": "+13125551234"},
                                            "fallback_url": "fallback_url",
                                            "open_url_action": {
                                                "application": "BROWSER",
                                                "url": "http://example.com",
                                                "webview_view_mode": "HALF",
                                                "description": "description",
                                            },
                                            "postback_data": "postback_data",
                                            "share_location_action": {"foo": "bar"},
                                            "text": "Hello world",
                                            "view_location_action": {
                                                "label": "label",
                                                "lat_long": {
                                                    "latitude": 41.8,
                                                    "longitude": -87.6,
                                                },
                                                "query": "query",
                                            },
                                        },
                                        "reply": {
                                            "postback_data": "postback_data",
                                            "text": "text",
                                        },
                                    }
                                ],
                                "title": "Elephant",
                            },
                            "card_orientation": "HORIZONTAL",
                            "thumbnail_image_alignment": "LEFT",
                        },
                    },
                    "suggestions": [
                        {
                            "action": {
                                "create_calendar_event_action": {
                                    "description": "description",
                                    "end_time": parse_datetime("2024-10-02T15:02:31Z"),
                                    "start_time": parse_datetime("2024-10-02T15:01:23Z"),
                                    "title": "title",
                                },
                                "dial_action": {"phone_number": "+13125551234"},
                                "fallback_url": "fallback_url",
                                "open_url_action": {
                                    "application": "BROWSER",
                                    "url": "http://example.com",
                                    "webview_view_mode": "HALF",
                                    "description": "description",
                                },
                                "postback_data": "postback_data",
                                "share_location_action": {"foo": "bar"},
                                "text": "Hello world",
                                "view_location_action": {
                                    "label": "label",
                                    "lat_long": {
                                        "latitude": 41.8,
                                        "longitude": -87.6,
                                    },
                                    "query": "query",
                                },
                            },
                            "reply": {
                                "postback_data": "postback_data",
                                "text": "text",
                            },
                        }
                    ],
                    "text": "Hello world!",
                },
                "event": {"event_type": "IS_TYPING"},
                "expire_time": parse_datetime("2024-10-02T15:01:23Z"),
                "ttl": "10.5s",
            },
            messaging_profile_id="messaging_profile_id",
            to="+13125551234",
            mms_fallback={
                "from": "+13125551234",
                "media_urls": ["string"],
                "subject": "Test Message",
                "text": "Hello world!",
            },
            sms_fallback={
                "from": "+13125551234",
                "text": "Hello world!",
            },
            type="RCS",
            webhook_url="webhook_url",
        )
        assert_matches_type(MesssageRcsResponse, messsage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_rcs(self, client: Telnyx) -> None:
        response = client.messsages.with_raw_response.rcs(
            agent_id="Agent007",
            agent_message={},
            messaging_profile_id="messaging_profile_id",
            to="+13125551234",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messsage = response.parse()
        assert_matches_type(MesssageRcsResponse, messsage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_rcs(self, client: Telnyx) -> None:
        with client.messsages.with_streaming_response.rcs(
            agent_id="Agent007",
            agent_message={},
            messaging_profile_id="messaging_profile_id",
            to="+13125551234",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messsage = response.parse()
            assert_matches_type(MesssageRcsResponse, messsage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_whatsapp(self, client: Telnyx) -> None:
        messsage = client.messsages.whatsapp(
            from_="+13125551234",
            to="+13125551234",
            whatsapp_message={},
        )
        assert_matches_type(MesssageWhatsappResponse, messsage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_whatsapp_with_all_params(self, client: Telnyx) -> None:
        messsage = client.messsages.whatsapp(
            from_="+13125551234",
            to="+13125551234",
            whatsapp_message={
                "audio": {
                    "caption": "caption",
                    "filename": "filename",
                    "link": "http://example.com/media.jpg",
                    "voice": True,
                },
                "biz_opaque_callback_data": "biz_opaque_callback_data",
                "contacts": [
                    {
                        "addresses": [
                            {
                                "city": "city",
                                "country": "country",
                                "country_code": "country_code",
                                "state": "state",
                                "street": "street",
                                "type": "type",
                                "zip": "zip",
                            }
                        ],
                        "birthday": "birthday",
                        "emails": [
                            {
                                "email": "email",
                                "type": "type",
                            }
                        ],
                        "name": "name",
                        "org": {
                            "company": "company",
                            "department": "department",
                            "title": "title",
                        },
                        "phones": [
                            {
                                "phone": "phone",
                                "type": "type",
                                "wa_id": "wa_id",
                            }
                        ],
                        "urls": [
                            {
                                "type": "type",
                                "url": "url",
                            }
                        ],
                    }
                ],
                "document": {
                    "caption": "caption",
                    "filename": "filename",
                    "link": "http://example.com/media.jpg",
                    "voice": True,
                },
                "image": {
                    "caption": "caption",
                    "filename": "filename",
                    "link": "http://example.com/media.jpg",
                    "voice": True,
                },
                "interactive": {
                    "action": {
                        "button": "button",
                        "buttons": [
                            {
                                "reply": {
                                    "id": "id",
                                    "title": "title",
                                },
                                "type": "reply",
                            }
                        ],
                        "cards": [
                            {
                                "action": {
                                    "catalog_id": "catalog_id",
                                    "product_retailer_id": "product_retailer_id",
                                },
                                "body": {"text": "text"},
                                "card_index": 0,
                                "header": {
                                    "image": {
                                        "caption": "caption",
                                        "filename": "filename",
                                        "link": "http://example.com/media.jpg",
                                        "voice": True,
                                    },
                                    "type": "image",
                                    "video": {
                                        "caption": "caption",
                                        "filename": "filename",
                                        "link": "http://example.com/media.jpg",
                                        "voice": True,
                                    },
                                },
                                "type": "cta_url",
                            }
                        ],
                        "catalog_id": "catalog_id",
                        "mode": "mode",
                        "name": "name",
                        "parameters": {
                            "display_text": "display_text",
                            "url": "url",
                        },
                        "product_retailer_id": "product_retailer_id",
                        "sections": [
                            {
                                "product_items": [{"product_retailer_id": "product_retailer_id"}],
                                "rows": [
                                    {
                                        "id": "id",
                                        "description": "description",
                                        "title": "title",
                                    }
                                ],
                                "title": "title",
                            }
                        ],
                    },
                    "body": {"text": "text"},
                    "footer": {"text": "text"},
                    "header": {
                        "document": {
                            "caption": "caption",
                            "filename": "filename",
                            "link": "http://example.com/media.jpg",
                            "voice": True,
                        },
                        "image": {
                            "caption": "caption",
                            "filename": "filename",
                            "link": "http://example.com/media.jpg",
                            "voice": True,
                        },
                        "sub_text": "sub_text",
                        "text": "text",
                        "video": {
                            "caption": "caption",
                            "filename": "filename",
                            "link": "http://example.com/media.jpg",
                            "voice": True,
                        },
                    },
                    "type": "cta_url",
                },
                "location": {
                    "address": "address",
                    "latitude": "latitude",
                    "longitude": "longitude",
                    "name": "name",
                },
                "reaction": {
                    "empji": "empji",
                    "message_id": "message_id",
                },
                "sticker": {
                    "caption": "caption",
                    "filename": "filename",
                    "link": "http://example.com/media.jpg",
                    "voice": True,
                },
                "type": "audio",
                "video": {
                    "caption": "caption",
                    "filename": "filename",
                    "link": "http://example.com/media.jpg",
                    "voice": True,
                },
            },
            type="WHATSAPP",
            webhook_url="webhook_url",
        )
        assert_matches_type(MesssageWhatsappResponse, messsage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_whatsapp(self, client: Telnyx) -> None:
        response = client.messsages.with_raw_response.whatsapp(
            from_="+13125551234",
            to="+13125551234",
            whatsapp_message={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messsage = response.parse()
        assert_matches_type(MesssageWhatsappResponse, messsage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_whatsapp(self, client: Telnyx) -> None:
        with client.messsages.with_streaming_response.whatsapp(
            from_="+13125551234",
            to="+13125551234",
            whatsapp_message={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messsage = response.parse()
            assert_matches_type(MesssageWhatsappResponse, messsage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMesssages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_rcs(self, async_client: AsyncTelnyx) -> None:
        messsage = await async_client.messsages.rcs(
            agent_id="Agent007",
            agent_message={},
            messaging_profile_id="messaging_profile_id",
            to="+13125551234",
        )
        assert_matches_type(MesssageRcsResponse, messsage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_rcs_with_all_params(self, async_client: AsyncTelnyx) -> None:
        messsage = await async_client.messsages.rcs(
            agent_id="Agent007",
            agent_message={
                "content_message": {
                    "content_info": {
                        "file_url": "https://example.com/elephant.jpg",
                        "force_refresh": True,
                        "thumbnail_url": "thumbnail_url",
                    },
                    "rich_card": {
                        "carousel_card": {
                            "card_contents": [
                                {
                                    "description": "description",
                                    "media": {
                                        "content_info": {
                                            "file_url": "https://example.com/elephant.jpg",
                                            "force_refresh": True,
                                            "thumbnail_url": "thumbnail_url",
                                        },
                                        "height": "MEDIUM",
                                    },
                                    "suggestions": [
                                        {
                                            "action": {
                                                "create_calendar_event_action": {
                                                    "description": "description",
                                                    "end_time": parse_datetime("2024-10-02T15:02:31Z"),
                                                    "start_time": parse_datetime("2024-10-02T15:01:23Z"),
                                                    "title": "title",
                                                },
                                                "dial_action": {"phone_number": "+13125551234"},
                                                "fallback_url": "fallback_url",
                                                "open_url_action": {
                                                    "application": "BROWSER",
                                                    "url": "http://example.com",
                                                    "webview_view_mode": "HALF",
                                                    "description": "description",
                                                },
                                                "postback_data": "postback_data",
                                                "share_location_action": {"foo": "bar"},
                                                "text": "Hello world",
                                                "view_location_action": {
                                                    "label": "label",
                                                    "lat_long": {
                                                        "latitude": 41.8,
                                                        "longitude": -87.6,
                                                    },
                                                    "query": "query",
                                                },
                                            },
                                            "reply": {
                                                "postback_data": "postback_data",
                                                "text": "text",
                                            },
                                        }
                                    ],
                                    "title": "Elephant",
                                }
                            ],
                            "card_width": "SMALL",
                        },
                        "standalone_card": {
                            "card_content": {
                                "description": "description",
                                "media": {
                                    "content_info": {
                                        "file_url": "https://example.com/elephant.jpg",
                                        "force_refresh": True,
                                        "thumbnail_url": "thumbnail_url",
                                    },
                                    "height": "MEDIUM",
                                },
                                "suggestions": [
                                    {
                                        "action": {
                                            "create_calendar_event_action": {
                                                "description": "description",
                                                "end_time": parse_datetime("2024-10-02T15:02:31Z"),
                                                "start_time": parse_datetime("2024-10-02T15:01:23Z"),
                                                "title": "title",
                                            },
                                            "dial_action": {"phone_number": "+13125551234"},
                                            "fallback_url": "fallback_url",
                                            "open_url_action": {
                                                "application": "BROWSER",
                                                "url": "http://example.com",
                                                "webview_view_mode": "HALF",
                                                "description": "description",
                                            },
                                            "postback_data": "postback_data",
                                            "share_location_action": {"foo": "bar"},
                                            "text": "Hello world",
                                            "view_location_action": {
                                                "label": "label",
                                                "lat_long": {
                                                    "latitude": 41.8,
                                                    "longitude": -87.6,
                                                },
                                                "query": "query",
                                            },
                                        },
                                        "reply": {
                                            "postback_data": "postback_data",
                                            "text": "text",
                                        },
                                    }
                                ],
                                "title": "Elephant",
                            },
                            "card_orientation": "HORIZONTAL",
                            "thumbnail_image_alignment": "LEFT",
                        },
                    },
                    "suggestions": [
                        {
                            "action": {
                                "create_calendar_event_action": {
                                    "description": "description",
                                    "end_time": parse_datetime("2024-10-02T15:02:31Z"),
                                    "start_time": parse_datetime("2024-10-02T15:01:23Z"),
                                    "title": "title",
                                },
                                "dial_action": {"phone_number": "+13125551234"},
                                "fallback_url": "fallback_url",
                                "open_url_action": {
                                    "application": "BROWSER",
                                    "url": "http://example.com",
                                    "webview_view_mode": "HALF",
                                    "description": "description",
                                },
                                "postback_data": "postback_data",
                                "share_location_action": {"foo": "bar"},
                                "text": "Hello world",
                                "view_location_action": {
                                    "label": "label",
                                    "lat_long": {
                                        "latitude": 41.8,
                                        "longitude": -87.6,
                                    },
                                    "query": "query",
                                },
                            },
                            "reply": {
                                "postback_data": "postback_data",
                                "text": "text",
                            },
                        }
                    ],
                    "text": "Hello world!",
                },
                "event": {"event_type": "IS_TYPING"},
                "expire_time": parse_datetime("2024-10-02T15:01:23Z"),
                "ttl": "10.5s",
            },
            messaging_profile_id="messaging_profile_id",
            to="+13125551234",
            mms_fallback={
                "from": "+13125551234",
                "media_urls": ["string"],
                "subject": "Test Message",
                "text": "Hello world!",
            },
            sms_fallback={
                "from": "+13125551234",
                "text": "Hello world!",
            },
            type="RCS",
            webhook_url="webhook_url",
        )
        assert_matches_type(MesssageRcsResponse, messsage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_rcs(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messsages.with_raw_response.rcs(
            agent_id="Agent007",
            agent_message={},
            messaging_profile_id="messaging_profile_id",
            to="+13125551234",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messsage = await response.parse()
        assert_matches_type(MesssageRcsResponse, messsage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_rcs(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messsages.with_streaming_response.rcs(
            agent_id="Agent007",
            agent_message={},
            messaging_profile_id="messaging_profile_id",
            to="+13125551234",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messsage = await response.parse()
            assert_matches_type(MesssageRcsResponse, messsage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_whatsapp(self, async_client: AsyncTelnyx) -> None:
        messsage = await async_client.messsages.whatsapp(
            from_="+13125551234",
            to="+13125551234",
            whatsapp_message={},
        )
        assert_matches_type(MesssageWhatsappResponse, messsage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_whatsapp_with_all_params(self, async_client: AsyncTelnyx) -> None:
        messsage = await async_client.messsages.whatsapp(
            from_="+13125551234",
            to="+13125551234",
            whatsapp_message={
                "audio": {
                    "caption": "caption",
                    "filename": "filename",
                    "link": "http://example.com/media.jpg",
                    "voice": True,
                },
                "biz_opaque_callback_data": "biz_opaque_callback_data",
                "contacts": [
                    {
                        "addresses": [
                            {
                                "city": "city",
                                "country": "country",
                                "country_code": "country_code",
                                "state": "state",
                                "street": "street",
                                "type": "type",
                                "zip": "zip",
                            }
                        ],
                        "birthday": "birthday",
                        "emails": [
                            {
                                "email": "email",
                                "type": "type",
                            }
                        ],
                        "name": "name",
                        "org": {
                            "company": "company",
                            "department": "department",
                            "title": "title",
                        },
                        "phones": [
                            {
                                "phone": "phone",
                                "type": "type",
                                "wa_id": "wa_id",
                            }
                        ],
                        "urls": [
                            {
                                "type": "type",
                                "url": "url",
                            }
                        ],
                    }
                ],
                "document": {
                    "caption": "caption",
                    "filename": "filename",
                    "link": "http://example.com/media.jpg",
                    "voice": True,
                },
                "image": {
                    "caption": "caption",
                    "filename": "filename",
                    "link": "http://example.com/media.jpg",
                    "voice": True,
                },
                "interactive": {
                    "action": {
                        "button": "button",
                        "buttons": [
                            {
                                "reply": {
                                    "id": "id",
                                    "title": "title",
                                },
                                "type": "reply",
                            }
                        ],
                        "cards": [
                            {
                                "action": {
                                    "catalog_id": "catalog_id",
                                    "product_retailer_id": "product_retailer_id",
                                },
                                "body": {"text": "text"},
                                "card_index": 0,
                                "header": {
                                    "image": {
                                        "caption": "caption",
                                        "filename": "filename",
                                        "link": "http://example.com/media.jpg",
                                        "voice": True,
                                    },
                                    "type": "image",
                                    "video": {
                                        "caption": "caption",
                                        "filename": "filename",
                                        "link": "http://example.com/media.jpg",
                                        "voice": True,
                                    },
                                },
                                "type": "cta_url",
                            }
                        ],
                        "catalog_id": "catalog_id",
                        "mode": "mode",
                        "name": "name",
                        "parameters": {
                            "display_text": "display_text",
                            "url": "url",
                        },
                        "product_retailer_id": "product_retailer_id",
                        "sections": [
                            {
                                "product_items": [{"product_retailer_id": "product_retailer_id"}],
                                "rows": [
                                    {
                                        "id": "id",
                                        "description": "description",
                                        "title": "title",
                                    }
                                ],
                                "title": "title",
                            }
                        ],
                    },
                    "body": {"text": "text"},
                    "footer": {"text": "text"},
                    "header": {
                        "document": {
                            "caption": "caption",
                            "filename": "filename",
                            "link": "http://example.com/media.jpg",
                            "voice": True,
                        },
                        "image": {
                            "caption": "caption",
                            "filename": "filename",
                            "link": "http://example.com/media.jpg",
                            "voice": True,
                        },
                        "sub_text": "sub_text",
                        "text": "text",
                        "video": {
                            "caption": "caption",
                            "filename": "filename",
                            "link": "http://example.com/media.jpg",
                            "voice": True,
                        },
                    },
                    "type": "cta_url",
                },
                "location": {
                    "address": "address",
                    "latitude": "latitude",
                    "longitude": "longitude",
                    "name": "name",
                },
                "reaction": {
                    "empji": "empji",
                    "message_id": "message_id",
                },
                "sticker": {
                    "caption": "caption",
                    "filename": "filename",
                    "link": "http://example.com/media.jpg",
                    "voice": True,
                },
                "type": "audio",
                "video": {
                    "caption": "caption",
                    "filename": "filename",
                    "link": "http://example.com/media.jpg",
                    "voice": True,
                },
            },
            type="WHATSAPP",
            webhook_url="webhook_url",
        )
        assert_matches_type(MesssageWhatsappResponse, messsage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_whatsapp(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.messsages.with_raw_response.whatsapp(
            from_="+13125551234",
            to="+13125551234",
            whatsapp_message={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        messsage = await response.parse()
        assert_matches_type(MesssageWhatsappResponse, messsage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_whatsapp(self, async_client: AsyncTelnyx) -> None:
        async with async_client.messsages.with_streaming_response.whatsapp(
            from_="+13125551234",
            to="+13125551234",
            whatsapp_message={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            messsage = await response.parse()
            assert_matches_type(MesssageWhatsappResponse, messsage, path=["response"])

        assert cast(Any, response.is_closed) is True
