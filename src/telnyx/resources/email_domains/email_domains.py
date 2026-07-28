# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...types import (
    EmailDomainType,
    EmailDomainStatus,
    email_domain_list_params,
    email_domain_create_params,
    email_domain_delete_params,
    email_domain_update_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .webhooks import (
    WebhooksResource,
    AsyncWebhooksResource,
    WebhooksResourceWithRawResponse,
    AsyncWebhooksResourceWithRawResponse,
    WebhooksResourceWithStreamingResponse,
    AsyncWebhooksResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.email_domain import EmailDomain
from ...types.email_domain_type import EmailDomainType
from ...types.email_domain_status import EmailDomainStatus
from ...types.email_domain_response import EmailDomainResponse
from ...types.email_dmarc_policy_param import EmailDmarcPolicyParam
from ...types.domains_tracking_settings_param import DomainsTrackingSettingsParam
from ...types.email_domain_retrieve_health_response import EmailDomainRetrieveHealthResponse
from ...types.email_domain_retrieve_dns_records_response import EmailDomainRetrieveDNSRecordsResponse

__all__ = ["EmailDomainsResource", "AsyncEmailDomainsResource"]


class EmailDomainsResource(SyncAPIResource):
    @cached_property
    def webhooks(self) -> WebhooksResource:
        """Per-domain webhook endpoints with event subscriptions"""
        return WebhooksResource(self._client)

    @cached_property
    def with_raw_response(self) -> EmailDomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return EmailDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailDomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return EmailDomainsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        domain: str,
        dmarc_policy: Optional[EmailDmarcPolicyParam] | Omit = omit,
        inbound_enabled: bool | Omit = omit,
        tracking: DomainsTrackingSettingsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailDomainResponse:
        """Create an email domain

        Args:
          dmarc_policy: DMARC policy for a sending domain.

        Drives the recommended \\__dmarc.<domain> TXT
              record. DMARC is advisory and never blocks sending. When omitted or null, the
              domain uses the advisory default (v=DMARC1; p=none;
              rua=mailto:dmarc@telnyx.com).

          inbound_enabled: Enable inbound routing for this domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/email_domains",
            body=maybe_transform(
                {
                    "domain": domain,
                    "dmarc_policy": dmarc_policy,
                    "inbound_enabled": inbound_enabled,
                    "tracking": tracking,
                },
                email_domain_create_params.EmailDomainCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailDomainResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailDomainResponse:
        """
        Shared (`type: shared`) Telnyx-managed domains are included/readable for every
        account, in addition to the account's own custom domains.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/email_domains/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailDomainResponse,
        )

    def update(
        self,
        id: str,
        *,
        dmarc_policy: Optional[EmailDmarcPolicyParam] | Omit = omit,
        inbound_enabled: bool | Omit = omit,
        tracking: DomainsTrackingSettingsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailDomainResponse:
        """Update an email domain

        Args:
          dmarc_policy: DMARC policy for a sending domain.

        Drives the recommended \\__dmarc.<domain> TXT
              record. DMARC is advisory and never blocks sending. When omitted or null, the
              domain uses the advisory default (v=DMARC1; p=none;
              rua=mailto:dmarc@telnyx.com).

          inbound_enabled: Enable or disable inbound routing for this domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/email_domains/{id}", id=id),
            body=maybe_transform(
                {
                    "dmarc_policy": dmarc_policy,
                    "inbound_enabled": inbound_enabled,
                    "tracking": tracking,
                },
                email_domain_update_params.EmailDomainUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailDomainResponse,
        )

    def list(
        self,
        *,
        filter_domain: str | Omit = omit,
        filter_profile_id: str | Omit = omit,
        filter_status: EmailDomainStatus | Omit = omit,
        filter_type: EmailDomainType | Omit = omit,
        filter_usable_for_inbound: bool | Omit = omit,
        filter_usable_for_sending: bool | Omit = omit,
        page_after: str | Omit = omit,
        page_before: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal["created_at", "-created_at", "domain", "-domain"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[EmailDomain]:
        """
        Shared (`type: shared`) Telnyx-managed domains are included/readable for every
        account, in addition to the account's own custom domains.

        Args:
          filter_domain: Partial match on domain name (case-insensitive)

          filter_profile_id: Filter by profile UUID

          page_after: Cursor for records after the provided value (cursor pagination)

          page_before: Cursor for records before the provided value (cursor pagination)

          page_number: Page number to return (offset pagination)

          page_size: Number of records per page

          sort: Field to sort by. Prefix with `-` for descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/email_domains",
            page=SyncDefaultFlatPagination[EmailDomain],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_domain": filter_domain,
                        "filter_profile_id": filter_profile_id,
                        "filter_status": filter_status,
                        "filter_type": filter_type,
                        "filter_usable_for_inbound": filter_usable_for_inbound,
                        "filter_usable_for_sending": filter_usable_for_sending,
                        "page_after": page_after,
                        "page_before": page_before,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    email_domain_list_params.EmailDomainListParams,
                ),
            ),
            model=EmailDomain,
        )

    def delete(
        self,
        id: str,
        *,
        force: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailDomainResponse:
        """
        Delete an email domain

        Args:
          force: Required as true when deleting verified domains

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/email_domains/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"force": force}, email_domain_delete_params.EmailDomainDeleteParams),
            ),
            cast_to=EmailDomainResponse,
        )

    def retrieve_dns_records(
        self,
        domain_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailDomainRetrieveDNSRecordsResponse:
        """
        List DNS records for an email domain

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return self._get(
            path_template("/email_domains/{domain_id}/dns_records", domain_id=domain_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailDomainRetrieveDNSRecordsResponse,
        )

    def retrieve_health(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailDomainRetrieveHealthResponse:
        """
        Returns a summary of domain health including verification status and usability.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/email_domains/{id}/health", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailDomainRetrieveHealthResponse,
        )

    def verify(
        self,
        domain_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailDomainResponse:
        """
        Verify DNS records for an email domain

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return self._post(
            path_template("/email_domains/{domain_id}/verify", domain_id=domain_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailDomainResponse,
        )


class AsyncEmailDomainsResource(AsyncAPIResource):
    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        """Per-domain webhook endpoints with event subscriptions"""
        return AsyncWebhooksResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmailDomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailDomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncEmailDomainsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        domain: str,
        dmarc_policy: Optional[EmailDmarcPolicyParam] | Omit = omit,
        inbound_enabled: bool | Omit = omit,
        tracking: DomainsTrackingSettingsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailDomainResponse:
        """Create an email domain

        Args:
          dmarc_policy: DMARC policy for a sending domain.

        Drives the recommended \\__dmarc.<domain> TXT
              record. DMARC is advisory and never blocks sending. When omitted or null, the
              domain uses the advisory default (v=DMARC1; p=none;
              rua=mailto:dmarc@telnyx.com).

          inbound_enabled: Enable inbound routing for this domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/email_domains",
            body=await async_maybe_transform(
                {
                    "domain": domain,
                    "dmarc_policy": dmarc_policy,
                    "inbound_enabled": inbound_enabled,
                    "tracking": tracking,
                },
                email_domain_create_params.EmailDomainCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailDomainResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailDomainResponse:
        """
        Shared (`type: shared`) Telnyx-managed domains are included/readable for every
        account, in addition to the account's own custom domains.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/email_domains/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailDomainResponse,
        )

    async def update(
        self,
        id: str,
        *,
        dmarc_policy: Optional[EmailDmarcPolicyParam] | Omit = omit,
        inbound_enabled: bool | Omit = omit,
        tracking: DomainsTrackingSettingsParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailDomainResponse:
        """Update an email domain

        Args:
          dmarc_policy: DMARC policy for a sending domain.

        Drives the recommended \\__dmarc.<domain> TXT
              record. DMARC is advisory and never blocks sending. When omitted or null, the
              domain uses the advisory default (v=DMARC1; p=none;
              rua=mailto:dmarc@telnyx.com).

          inbound_enabled: Enable or disable inbound routing for this domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/email_domains/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "dmarc_policy": dmarc_policy,
                    "inbound_enabled": inbound_enabled,
                    "tracking": tracking,
                },
                email_domain_update_params.EmailDomainUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailDomainResponse,
        )

    def list(
        self,
        *,
        filter_domain: str | Omit = omit,
        filter_profile_id: str | Omit = omit,
        filter_status: EmailDomainStatus | Omit = omit,
        filter_type: EmailDomainType | Omit = omit,
        filter_usable_for_inbound: bool | Omit = omit,
        filter_usable_for_sending: bool | Omit = omit,
        page_after: str | Omit = omit,
        page_before: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal["created_at", "-created_at", "domain", "-domain"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[EmailDomain, AsyncDefaultFlatPagination[EmailDomain]]:
        """
        Shared (`type: shared`) Telnyx-managed domains are included/readable for every
        account, in addition to the account's own custom domains.

        Args:
          filter_domain: Partial match on domain name (case-insensitive)

          filter_profile_id: Filter by profile UUID

          page_after: Cursor for records after the provided value (cursor pagination)

          page_before: Cursor for records before the provided value (cursor pagination)

          page_number: Page number to return (offset pagination)

          page_size: Number of records per page

          sort: Field to sort by. Prefix with `-` for descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/email_domains",
            page=AsyncDefaultFlatPagination[EmailDomain],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_domain": filter_domain,
                        "filter_profile_id": filter_profile_id,
                        "filter_status": filter_status,
                        "filter_type": filter_type,
                        "filter_usable_for_inbound": filter_usable_for_inbound,
                        "filter_usable_for_sending": filter_usable_for_sending,
                        "page_after": page_after,
                        "page_before": page_before,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    email_domain_list_params.EmailDomainListParams,
                ),
            ),
            model=EmailDomain,
        )

    async def delete(
        self,
        id: str,
        *,
        force: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailDomainResponse:
        """
        Delete an email domain

        Args:
          force: Required as true when deleting verified domains

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/email_domains/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"force": force}, email_domain_delete_params.EmailDomainDeleteParams),
            ),
            cast_to=EmailDomainResponse,
        )

    async def retrieve_dns_records(
        self,
        domain_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailDomainRetrieveDNSRecordsResponse:
        """
        List DNS records for an email domain

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return await self._get(
            path_template("/email_domains/{domain_id}/dns_records", domain_id=domain_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailDomainRetrieveDNSRecordsResponse,
        )

    async def retrieve_health(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailDomainRetrieveHealthResponse:
        """
        Returns a summary of domain health including verification status and usability.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/email_domains/{id}/health", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailDomainRetrieveHealthResponse,
        )

    async def verify(
        self,
        domain_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailDomainResponse:
        """
        Verify DNS records for an email domain

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return await self._post(
            path_template("/email_domains/{domain_id}/verify", domain_id=domain_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailDomainResponse,
        )


class EmailDomainsResourceWithRawResponse:
    def __init__(self, email_domains: EmailDomainsResource) -> None:
        self._email_domains = email_domains

        self.create = to_raw_response_wrapper(
            email_domains.create,
        )
        self.retrieve = to_raw_response_wrapper(
            email_domains.retrieve,
        )
        self.update = to_raw_response_wrapper(
            email_domains.update,
        )
        self.list = to_raw_response_wrapper(
            email_domains.list,
        )
        self.delete = to_raw_response_wrapper(
            email_domains.delete,
        )
        self.retrieve_dns_records = to_raw_response_wrapper(
            email_domains.retrieve_dns_records,
        )
        self.retrieve_health = to_raw_response_wrapper(
            email_domains.retrieve_health,
        )
        self.verify = to_raw_response_wrapper(
            email_domains.verify,
        )

    @cached_property
    def webhooks(self) -> WebhooksResourceWithRawResponse:
        """Per-domain webhook endpoints with event subscriptions"""
        return WebhooksResourceWithRawResponse(self._email_domains.webhooks)


class AsyncEmailDomainsResourceWithRawResponse:
    def __init__(self, email_domains: AsyncEmailDomainsResource) -> None:
        self._email_domains = email_domains

        self.create = async_to_raw_response_wrapper(
            email_domains.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            email_domains.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            email_domains.update,
        )
        self.list = async_to_raw_response_wrapper(
            email_domains.list,
        )
        self.delete = async_to_raw_response_wrapper(
            email_domains.delete,
        )
        self.retrieve_dns_records = async_to_raw_response_wrapper(
            email_domains.retrieve_dns_records,
        )
        self.retrieve_health = async_to_raw_response_wrapper(
            email_domains.retrieve_health,
        )
        self.verify = async_to_raw_response_wrapper(
            email_domains.verify,
        )

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithRawResponse:
        """Per-domain webhook endpoints with event subscriptions"""
        return AsyncWebhooksResourceWithRawResponse(self._email_domains.webhooks)


class EmailDomainsResourceWithStreamingResponse:
    def __init__(self, email_domains: EmailDomainsResource) -> None:
        self._email_domains = email_domains

        self.create = to_streamed_response_wrapper(
            email_domains.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            email_domains.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            email_domains.update,
        )
        self.list = to_streamed_response_wrapper(
            email_domains.list,
        )
        self.delete = to_streamed_response_wrapper(
            email_domains.delete,
        )
        self.retrieve_dns_records = to_streamed_response_wrapper(
            email_domains.retrieve_dns_records,
        )
        self.retrieve_health = to_streamed_response_wrapper(
            email_domains.retrieve_health,
        )
        self.verify = to_streamed_response_wrapper(
            email_domains.verify,
        )

    @cached_property
    def webhooks(self) -> WebhooksResourceWithStreamingResponse:
        """Per-domain webhook endpoints with event subscriptions"""
        return WebhooksResourceWithStreamingResponse(self._email_domains.webhooks)


class AsyncEmailDomainsResourceWithStreamingResponse:
    def __init__(self, email_domains: AsyncEmailDomainsResource) -> None:
        self._email_domains = email_domains

        self.create = async_to_streamed_response_wrapper(
            email_domains.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            email_domains.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            email_domains.update,
        )
        self.list = async_to_streamed_response_wrapper(
            email_domains.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            email_domains.delete,
        )
        self.retrieve_dns_records = async_to_streamed_response_wrapper(
            email_domains.retrieve_dns_records,
        )
        self.retrieve_health = async_to_streamed_response_wrapper(
            email_domains.retrieve_health,
        )
        self.verify = async_to_streamed_response_wrapper(
            email_domains.verify,
        )

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithStreamingResponse:
        """Per-domain webhook endpoints with event subscriptions"""
        return AsyncWebhooksResourceWithStreamingResponse(self._email_domains.webhooks)
