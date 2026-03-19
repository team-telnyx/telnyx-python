# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .message_templates import (
    MessageTemplatesResource,
    AsyncMessageTemplatesResource,
    MessageTemplatesResourceWithRawResponse,
    AsyncMessageTemplatesResourceWithRawResponse,
    MessageTemplatesResourceWithStreamingResponse,
    AsyncMessageTemplatesResourceWithStreamingResponse,
)
from .phone_numbers.phone_numbers import (
    PhoneNumbersResource,
    AsyncPhoneNumbersResource,
    PhoneNumbersResourceWithRawResponse,
    AsyncPhoneNumbersResourceWithRawResponse,
    PhoneNumbersResourceWithStreamingResponse,
    AsyncPhoneNumbersResourceWithStreamingResponse,
)
from .business_accounts.business_accounts import (
    BusinessAccountsResource,
    AsyncBusinessAccountsResource,
    BusinessAccountsResourceWithRawResponse,
    AsyncBusinessAccountsResourceWithRawResponse,
    BusinessAccountsResourceWithStreamingResponse,
    AsyncBusinessAccountsResourceWithStreamingResponse,
)

__all__ = ["WhatsappResource", "AsyncWhatsappResource"]


class WhatsappResource(SyncAPIResource):
    @cached_property
    def business_accounts(self) -> BusinessAccountsResource:
        """Manage Whatsapp business accounts"""
        return BusinessAccountsResource(self._client)

    @cached_property
    def message_templates(self) -> MessageTemplatesResource:
        """Manage Whatsapp message templates"""
        return MessageTemplatesResource(self._client)

    @cached_property
    def phone_numbers(self) -> PhoneNumbersResource:
        """Manage Whatsapp phone numbers"""
        return PhoneNumbersResource(self._client)

    @cached_property
    def with_raw_response(self) -> WhatsappResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return WhatsappResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WhatsappResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return WhatsappResourceWithStreamingResponse(self)


class AsyncWhatsappResource(AsyncAPIResource):
    @cached_property
    def business_accounts(self) -> AsyncBusinessAccountsResource:
        """Manage Whatsapp business accounts"""
        return AsyncBusinessAccountsResource(self._client)

    @cached_property
    def message_templates(self) -> AsyncMessageTemplatesResource:
        """Manage Whatsapp message templates"""
        return AsyncMessageTemplatesResource(self._client)

    @cached_property
    def phone_numbers(self) -> AsyncPhoneNumbersResource:
        """Manage Whatsapp phone numbers"""
        return AsyncPhoneNumbersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWhatsappResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWhatsappResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWhatsappResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncWhatsappResourceWithStreamingResponse(self)


class WhatsappResourceWithRawResponse:
    def __init__(self, whatsapp: WhatsappResource) -> None:
        self._whatsapp = whatsapp

    @cached_property
    def business_accounts(self) -> BusinessAccountsResourceWithRawResponse:
        """Manage Whatsapp business accounts"""
        return BusinessAccountsResourceWithRawResponse(self._whatsapp.business_accounts)

    @cached_property
    def message_templates(self) -> MessageTemplatesResourceWithRawResponse:
        """Manage Whatsapp message templates"""
        return MessageTemplatesResourceWithRawResponse(self._whatsapp.message_templates)

    @cached_property
    def phone_numbers(self) -> PhoneNumbersResourceWithRawResponse:
        """Manage Whatsapp phone numbers"""
        return PhoneNumbersResourceWithRawResponse(self._whatsapp.phone_numbers)


class AsyncWhatsappResourceWithRawResponse:
    def __init__(self, whatsapp: AsyncWhatsappResource) -> None:
        self._whatsapp = whatsapp

    @cached_property
    def business_accounts(self) -> AsyncBusinessAccountsResourceWithRawResponse:
        """Manage Whatsapp business accounts"""
        return AsyncBusinessAccountsResourceWithRawResponse(self._whatsapp.business_accounts)

    @cached_property
    def message_templates(self) -> AsyncMessageTemplatesResourceWithRawResponse:
        """Manage Whatsapp message templates"""
        return AsyncMessageTemplatesResourceWithRawResponse(self._whatsapp.message_templates)

    @cached_property
    def phone_numbers(self) -> AsyncPhoneNumbersResourceWithRawResponse:
        """Manage Whatsapp phone numbers"""
        return AsyncPhoneNumbersResourceWithRawResponse(self._whatsapp.phone_numbers)


class WhatsappResourceWithStreamingResponse:
    def __init__(self, whatsapp: WhatsappResource) -> None:
        self._whatsapp = whatsapp

    @cached_property
    def business_accounts(self) -> BusinessAccountsResourceWithStreamingResponse:
        """Manage Whatsapp business accounts"""
        return BusinessAccountsResourceWithStreamingResponse(self._whatsapp.business_accounts)

    @cached_property
    def message_templates(self) -> MessageTemplatesResourceWithStreamingResponse:
        """Manage Whatsapp message templates"""
        return MessageTemplatesResourceWithStreamingResponse(self._whatsapp.message_templates)

    @cached_property
    def phone_numbers(self) -> PhoneNumbersResourceWithStreamingResponse:
        """Manage Whatsapp phone numbers"""
        return PhoneNumbersResourceWithStreamingResponse(self._whatsapp.phone_numbers)


class AsyncWhatsappResourceWithStreamingResponse:
    def __init__(self, whatsapp: AsyncWhatsappResource) -> None:
        self._whatsapp = whatsapp

    @cached_property
    def business_accounts(self) -> AsyncBusinessAccountsResourceWithStreamingResponse:
        """Manage Whatsapp business accounts"""
        return AsyncBusinessAccountsResourceWithStreamingResponse(self._whatsapp.business_accounts)

    @cached_property
    def message_templates(self) -> AsyncMessageTemplatesResourceWithStreamingResponse:
        """Manage Whatsapp message templates"""
        return AsyncMessageTemplatesResourceWithStreamingResponse(self._whatsapp.message_templates)

    @cached_property
    def phone_numbers(self) -> AsyncPhoneNumbersResourceWithStreamingResponse:
        """Manage Whatsapp phone numbers"""
        return AsyncPhoneNumbersResourceWithStreamingResponse(self._whatsapp.phone_numbers)
