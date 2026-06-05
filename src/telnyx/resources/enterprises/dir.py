# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
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
from ...types.enterprises import dir_list_params, dir_create_params
from ...types.enterprises.dir_list_response import DirListResponse
from ...types.enterprises.dir_create_response import DirCreateResponse

__all__ = ["DirResource", "AsyncDirResource"]


class DirResource(SyncAPIResource):
    """
    A Display Identity Record (DIR) is the verified calling identity (display name, logo, call reasons) shown to recipients on outbound calls.
    """

    @cached_property
    def with_raw_response(self) -> DirResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return DirResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DirResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return DirResourceWithStreamingResponse(self)

    def create(
        self,
        enterprise_id: str,
        *,
        authorizer_email: str,
        authorizer_name: str,
        certify_brand_is_accurate: Literal[True],
        certify_ip_ownership: Literal[True],
        certify_no_shaft_content: Literal[True],
        display_name: str,
        call_reasons: SequenceNotStr[str] | Omit = omit,
        documents: Iterable[dir_create_params.Document] | Omit = omit,
        logo_url: str | Omit = omit,
        reselling: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirCreateResponse:
        """Create a new DIR under the given enterprise.

        The DIR starts in `draft` status;
        it must be submitted (`POST .../submit`) and approved by Telnyx before any phone
        number can be attached.

        **Field rules**

        - `display_name`: 1–35 characters, no emoji or whitespace-only strings; this is
          the name shown to recipients.
        - `call_reasons`: 1–10 strings, each ≤64 characters; describe why your business
          calls customers (e.g. 'Appointment reminders', 'Billing inquiries'). Validate
          the wording against `POST /call_reasons/validate`.
        - `logo_url`: HTTPS URL (max 128 chars) to a 256×256 BMP (max 1 MB). The image
          is downloaded and hashed at submission time.
        - `documents`: up to 20 entries; each `document_id` must be obtained by
          uploading the file via the Telnyx Documents API first. Within one DIR a
          `document_id` may only appear once.
        - `certify_brand_is_accurate`, `certify_no_shaft_content`,
          `certify_ip_ownership` MUST all be `true`.

        **Failure modes**

        - `422` — validation error; `errors[].source.pointer` names the offending field.
        - `403` — Branded Calling not activated on this enterprise (see
          `POST /enterprises/{id}/branded_calling`).
        - `404` — enterprise does not exist or does not belong to your account.

        Args:
          authorizer_email: Contact email of the authorizer. Telnyx may send verification or
              infringement-notice email here; use a monitored mailbox.

          authorizer_name: Name of the person at your enterprise who is authorizing this DIR registration.
              Must be a real individual (used for audit and trademark-claim contests).

          certify_brand_is_accurate: Must be `true`.

          certify_ip_ownership: Must be `true`. Confirms ownership of any logos/trademarks shown.

          certify_no_shaft_content: Must be `true`. Confirms this DIR is not used for SHAFT content (Sex, Hate,
              Alcohol, Firearms, Tobacco) where prohibited.

          display_name: Name shown to call recipients. No emoji; not whitespace-only.

          call_reasons: 1–10 reasons your business calls customers. Validate phrasing against
              `POST /call_reasons/validate`.

          documents: Supporting documents. Each `document_id` may appear at most once on a DIR.

          logo_url: Publicly accessible HTTPS URL (max 128 chars) to a 256x256 BMP logo (max 1 MB).

          reselling: Set to true if your organization places calls on behalf of other enterprises
              (BPO/reseller).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return self._post(
            path_template("/enterprises/{enterprise_id}/dir", enterprise_id=enterprise_id),
            body=maybe_transform(
                {
                    "authorizer_email": authorizer_email,
                    "authorizer_name": authorizer_name,
                    "certify_brand_is_accurate": certify_brand_is_accurate,
                    "certify_ip_ownership": certify_ip_ownership,
                    "certify_no_shaft_content": certify_no_shaft_content,
                    "display_name": display_name,
                    "call_reasons": call_reasons,
                    "documents": documents,
                    "logo_url": logo_url,
                    "reselling": reselling,
                },
                dir_create_params.DirCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirCreateResponse,
        )

    def list(
        self,
        enterprise_id: str,
        *,
        filter_expiring_at_gte: Union[str, datetime] | Omit = omit,
        filter_expiring_at_lte: Union[str, datetime] | Omit = omit,
        filter_expiring_within_days: int | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        search: str | Omit = omit,
        sort: Literal[
            "created_at",
            "-created_at",
            "updated_at",
            "-updated_at",
            "display_name",
            "-display_name",
            "status",
            "-status",
            "submitted_at",
            "-submitted_at",
            "verified_at",
            "-verified_at",
            "expiring_at",
            "-expiring_at",
        ]
        | Omit = omit,
        status: Literal[
            "draft",
            "submitted",
            "in_review",
            "verified",
            "rejected",
            "unsuccessful",
            "suspended",
            "expired",
            "infringement_claimed",
            "permanently_rejected",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[DirListResponse]:
        """
        Return the DIRs (Display Identity Records) belonging to a single enterprise.
        Pagination is JSON:API style (`page[number]`, `page[size]`, max 250). Filterable
        by `status`. Searchable by case-insensitive partial match on `display_name`
        (`search=`). Sortable by any of `created_at`, `updated_at`, `display_name`,
        `status`, `submitted_at`, `verified_at`, `expiring_at` (prefix `-` for
        descending; default `-created_at`). Supports the renewal-window filters
        `filter[expiring_at][gte]` / `filter[expiring_at][lte]` and the convenience
        `filter[expiring_within_days]` (mutually exclusive with the explicit gte/lte
        form).

        Args:
          filter_expiring_at_gte: Return only DIRs whose `expiring_at` is at or after this ISO-8601 timestamp.

          filter_expiring_at_lte: Return only DIRs whose `expiring_at` is at or before this ISO-8601 timestamp.

          filter_expiring_within_days: Convenience: returns DIRs whose `expiring_at` falls within the next N days
              (1–365). Equivalent to setting `filter[expiring_at][gte]=<now>` +
              `filter[expiring_at][lte]=<now+N>`. Mutually exclusive with the explicit
              `[gte]`/`[lte]` filters — combining returns 400.

          page_number: 1-based page number. Out-of-range values return an empty page with correct meta.

          page_size: Items per page. Maximum 250; values above are clamped to 250.

          search: Case-insensitive partial match on `display_name`.

          sort: Sort field. Allowed: `created_at`, `updated_at`, `display_name`, `status`,
              `submitted_at`, `verified_at`, `expiring_at`. Prefix with `-` for descending.
              Default `-created_at`.

          status: Filter by DIR status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return self._get_api_list(
            path_template("/enterprises/{enterprise_id}/dir", enterprise_id=enterprise_id),
            page=SyncDefaultFlatPagination[DirListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_expiring_at_gte": filter_expiring_at_gte,
                        "filter_expiring_at_lte": filter_expiring_at_lte,
                        "filter_expiring_within_days": filter_expiring_within_days,
                        "page_number": page_number,
                        "page_size": page_size,
                        "search": search,
                        "sort": sort,
                        "status": status,
                    },
                    dir_list_params.DirListParams,
                ),
            ),
            model=DirListResponse,
        )


class AsyncDirResource(AsyncAPIResource):
    """
    A Display Identity Record (DIR) is the verified calling identity (display name, logo, call reasons) shown to recipients on outbound calls.
    """

    @cached_property
    def with_raw_response(self) -> AsyncDirResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDirResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDirResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncDirResourceWithStreamingResponse(self)

    async def create(
        self,
        enterprise_id: str,
        *,
        authorizer_email: str,
        authorizer_name: str,
        certify_brand_is_accurate: Literal[True],
        certify_ip_ownership: Literal[True],
        certify_no_shaft_content: Literal[True],
        display_name: str,
        call_reasons: SequenceNotStr[str] | Omit = omit,
        documents: Iterable[dir_create_params.Document] | Omit = omit,
        logo_url: str | Omit = omit,
        reselling: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirCreateResponse:
        """Create a new DIR under the given enterprise.

        The DIR starts in `draft` status;
        it must be submitted (`POST .../submit`) and approved by Telnyx before any phone
        number can be attached.

        **Field rules**

        - `display_name`: 1–35 characters, no emoji or whitespace-only strings; this is
          the name shown to recipients.
        - `call_reasons`: 1–10 strings, each ≤64 characters; describe why your business
          calls customers (e.g. 'Appointment reminders', 'Billing inquiries'). Validate
          the wording against `POST /call_reasons/validate`.
        - `logo_url`: HTTPS URL (max 128 chars) to a 256×256 BMP (max 1 MB). The image
          is downloaded and hashed at submission time.
        - `documents`: up to 20 entries; each `document_id` must be obtained by
          uploading the file via the Telnyx Documents API first. Within one DIR a
          `document_id` may only appear once.
        - `certify_brand_is_accurate`, `certify_no_shaft_content`,
          `certify_ip_ownership` MUST all be `true`.

        **Failure modes**

        - `422` — validation error; `errors[].source.pointer` names the offending field.
        - `403` — Branded Calling not activated on this enterprise (see
          `POST /enterprises/{id}/branded_calling`).
        - `404` — enterprise does not exist or does not belong to your account.

        Args:
          authorizer_email: Contact email of the authorizer. Telnyx may send verification or
              infringement-notice email here; use a monitored mailbox.

          authorizer_name: Name of the person at your enterprise who is authorizing this DIR registration.
              Must be a real individual (used for audit and trademark-claim contests).

          certify_brand_is_accurate: Must be `true`.

          certify_ip_ownership: Must be `true`. Confirms ownership of any logos/trademarks shown.

          certify_no_shaft_content: Must be `true`. Confirms this DIR is not used for SHAFT content (Sex, Hate,
              Alcohol, Firearms, Tobacco) where prohibited.

          display_name: Name shown to call recipients. No emoji; not whitespace-only.

          call_reasons: 1–10 reasons your business calls customers. Validate phrasing against
              `POST /call_reasons/validate`.

          documents: Supporting documents. Each `document_id` may appear at most once on a DIR.

          logo_url: Publicly accessible HTTPS URL (max 128 chars) to a 256x256 BMP logo (max 1 MB).

          reselling: Set to true if your organization places calls on behalf of other enterprises
              (BPO/reseller).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return await self._post(
            path_template("/enterprises/{enterprise_id}/dir", enterprise_id=enterprise_id),
            body=await async_maybe_transform(
                {
                    "authorizer_email": authorizer_email,
                    "authorizer_name": authorizer_name,
                    "certify_brand_is_accurate": certify_brand_is_accurate,
                    "certify_ip_ownership": certify_ip_ownership,
                    "certify_no_shaft_content": certify_no_shaft_content,
                    "display_name": display_name,
                    "call_reasons": call_reasons,
                    "documents": documents,
                    "logo_url": logo_url,
                    "reselling": reselling,
                },
                dir_create_params.DirCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirCreateResponse,
        )

    def list(
        self,
        enterprise_id: str,
        *,
        filter_expiring_at_gte: Union[str, datetime] | Omit = omit,
        filter_expiring_at_lte: Union[str, datetime] | Omit = omit,
        filter_expiring_within_days: int | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        search: str | Omit = omit,
        sort: Literal[
            "created_at",
            "-created_at",
            "updated_at",
            "-updated_at",
            "display_name",
            "-display_name",
            "status",
            "-status",
            "submitted_at",
            "-submitted_at",
            "verified_at",
            "-verified_at",
            "expiring_at",
            "-expiring_at",
        ]
        | Omit = omit,
        status: Literal[
            "draft",
            "submitted",
            "in_review",
            "verified",
            "rejected",
            "unsuccessful",
            "suspended",
            "expired",
            "infringement_claimed",
            "permanently_rejected",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[DirListResponse, AsyncDefaultFlatPagination[DirListResponse]]:
        """
        Return the DIRs (Display Identity Records) belonging to a single enterprise.
        Pagination is JSON:API style (`page[number]`, `page[size]`, max 250). Filterable
        by `status`. Searchable by case-insensitive partial match on `display_name`
        (`search=`). Sortable by any of `created_at`, `updated_at`, `display_name`,
        `status`, `submitted_at`, `verified_at`, `expiring_at` (prefix `-` for
        descending; default `-created_at`). Supports the renewal-window filters
        `filter[expiring_at][gte]` / `filter[expiring_at][lte]` and the convenience
        `filter[expiring_within_days]` (mutually exclusive with the explicit gte/lte
        form).

        Args:
          filter_expiring_at_gte: Return only DIRs whose `expiring_at` is at or after this ISO-8601 timestamp.

          filter_expiring_at_lte: Return only DIRs whose `expiring_at` is at or before this ISO-8601 timestamp.

          filter_expiring_within_days: Convenience: returns DIRs whose `expiring_at` falls within the next N days
              (1–365). Equivalent to setting `filter[expiring_at][gte]=<now>` +
              `filter[expiring_at][lte]=<now+N>`. Mutually exclusive with the explicit
              `[gte]`/`[lte]` filters — combining returns 400.

          page_number: 1-based page number. Out-of-range values return an empty page with correct meta.

          page_size: Items per page. Maximum 250; values above are clamped to 250.

          search: Case-insensitive partial match on `display_name`.

          sort: Sort field. Allowed: `created_at`, `updated_at`, `display_name`, `status`,
              `submitted_at`, `verified_at`, `expiring_at`. Prefix with `-` for descending.
              Default `-created_at`.

          status: Filter by DIR status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return self._get_api_list(
            path_template("/enterprises/{enterprise_id}/dir", enterprise_id=enterprise_id),
            page=AsyncDefaultFlatPagination[DirListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_expiring_at_gte": filter_expiring_at_gte,
                        "filter_expiring_at_lte": filter_expiring_at_lte,
                        "filter_expiring_within_days": filter_expiring_within_days,
                        "page_number": page_number,
                        "page_size": page_size,
                        "search": search,
                        "sort": sort,
                        "status": status,
                    },
                    dir_list_params.DirListParams,
                ),
            ),
            model=DirListResponse,
        )


class DirResourceWithRawResponse:
    def __init__(self, dir: DirResource) -> None:
        self._dir = dir

        self.create = to_raw_response_wrapper(
            dir.create,
        )
        self.list = to_raw_response_wrapper(
            dir.list,
        )


class AsyncDirResourceWithRawResponse:
    def __init__(self, dir: AsyncDirResource) -> None:
        self._dir = dir

        self.create = async_to_raw_response_wrapper(
            dir.create,
        )
        self.list = async_to_raw_response_wrapper(
            dir.list,
        )


class DirResourceWithStreamingResponse:
    def __init__(self, dir: DirResource) -> None:
        self._dir = dir

        self.create = to_streamed_response_wrapper(
            dir.create,
        )
        self.list = to_streamed_response_wrapper(
            dir.list,
        )


class AsyncDirResourceWithStreamingResponse:
    def __init__(self, dir: AsyncDirResource) -> None:
        self._dir = dir

        self.create = async_to_streamed_response_wrapper(
            dir.create,
        )
        self.list = async_to_streamed_response_wrapper(
            dir.list,
        )
