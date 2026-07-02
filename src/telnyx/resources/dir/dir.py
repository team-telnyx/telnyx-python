# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    dir_list_params,
    dir_update_params,
    dir_create_loa_params,
    dir_update_infringement_params,
    dir_list_infringement_claims_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .comments import (
    CommentsResource,
    AsyncCommentsResource,
    CommentsResourceWithRawResponse,
    AsyncCommentsResourceWithRawResponse,
    CommentsResourceWithStreamingResponse,
    AsyncCommentsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .references import (
    ReferencesResource,
    AsyncReferencesResource,
    ReferencesResourceWithRawResponse,
    AsyncReferencesResourceWithRawResponse,
    ReferencesResourceWithStreamingResponse,
    AsyncReferencesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from .verify_email import (
    VerifyEmailResource,
    AsyncVerifyEmailResource,
    VerifyEmailResourceWithRawResponse,
    AsyncVerifyEmailResourceWithRawResponse,
    VerifyEmailResourceWithStreamingResponse,
    AsyncVerifyEmailResourceWithStreamingResponse,
)
from .phone_numbers import (
    PhoneNumbersResource,
    AsyncPhoneNumbersResource,
    PhoneNumbersResourceWithRawResponse,
    AsyncPhoneNumbersResourceWithRawResponse,
    PhoneNumbersResourceWithStreamingResponse,
    AsyncPhoneNumbersResourceWithStreamingResponse,
)
from ..._base_client import AsyncPaginator, make_request_options
from .phone_number_batches import (
    PhoneNumberBatchesResource,
    AsyncPhoneNumberBatchesResource,
    PhoneNumberBatchesResourceWithRawResponse,
    AsyncPhoneNumberBatchesResourceWithRawResponse,
    PhoneNumberBatchesResourceWithStreamingResponse,
    AsyncPhoneNumberBatchesResourceWithStreamingResponse,
)
from ...types.dir_list_response import DirListResponse
from ...types.dir_submit_response import DirSubmitResponse
from ...types.dir_update_response import DirUpdateResponse
from ...types.dir_retrieve_response import DirRetrieveResponse
from ...types.dir_list_document_types_response import DirListDocumentTypesResponse
from ...types.dir_update_infringement_response import DirUpdateInfringementResponse
from ...types.dir_list_infringement_claims_response import DirListInfringementClaimsResponse

__all__ = ["DirResource", "AsyncDirResource"]


class DirResource(SyncAPIResource):
    @cached_property
    def comments(self) -> CommentsResource:
        """
        Read messages from the Telnyx vetting team and reply with clarifying information.
        """
        return CommentsResource(self._client)

    @cached_property
    def phone_number_batches(self) -> PhoneNumberBatchesResource:
        """Phone numbers are submitted to Telnyx for vetting in batches.

        Batches group all numbers added in a single request under the same Letter of Authorization.
        """
        return PhoneNumberBatchesResource(self._client)

    @cached_property
    def phone_numbers(self) -> PhoneNumbersResource:
        """
        Associate phone numbers with a verified DIR so calls from those numbers carry the DIR's display identity.
        """
        return PhoneNumbersResource(self._client)

    @cached_property
    def references(self) -> ReferencesResource:
        """
        Submit and manage the two business references and one financial reference that vouch for a DIR. References are contacted to confirm the business identity during vetting.
        """
        return ReferencesResource(self._client)

    @cached_property
    def verify_email(self) -> VerifyEmailResource:
        """Verify ownership of a DIR's authorizer email.

        A short code is emailed and confirmed; the email must be verified before references can be submitted.
        """
        return VerifyEmailResource(self._client)

    @cached_property
    def with_raw_response(self) -> DirResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return DirResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DirResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#with_streaming_response
        """
        return DirResourceWithStreamingResponse(self)

    def retrieve(
        self,
        dir_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirRetrieveResponse:
        """Returns a single DIR by id.

        The enterprise is resolved server-side from the DIR
        id. Returns `404` if the DIR does not exist or is not yours.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        return self._get(
            path_template("/dir/{dir_id}", dir_id=dir_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirRetrieveResponse,
        )

    def update(
        self,
        dir_id: str,
        *,
        authorizer_email: str | Omit = omit,
        authorizer_name: str | Omit = omit,
        call_reasons: SequenceNotStr[str] | Omit = omit,
        certify_brand_is_accurate: bool | Omit = omit,
        certify_ip_ownership: bool | Omit = omit,
        certify_no_shaft_content: bool | Omit = omit,
        display_name: str | Omit = omit,
        documents: Iterable[dir_update_params.Document] | Omit = omit,
        logo_url: str | Omit = omit,
        reselling: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirUpdateResponse:
        """Edit a DIR.

        DIRs in `draft`, `rejected`, `unsuccessful`, or `suspended` can be
        edited freely: PATCH is a pure edit, `status` is never changed, and you re-vet
        by calling `POST /v2/dir/{dir_id}/submit` explicitly. A `verified` DIR can also
        be edited in place: a PATCH that changes any value returns the DIR to `draft`
        and branded delivery stops until you re-submit and the DIR is approved again,
        while a PATCH that changes nothing (an empty body or values identical to the
        current ones) leaves the DIR `verified`, so idempotent retries are safe. DIRs in
        any other status (`submitted`, `in_review`, `expired`, `infringement_claimed`,
        `permanently_rejected`) cannot be edited.

        Args:
          authorizer_email: Contact email of the authorizer. Telnyx may send verification or infringement
              notices here.

          authorizer_name: Name of the person at your enterprise authorizing this DIR. Must be a real
              individual.

          call_reasons: 1–10 reasons your business calls customers. Validate phrasing against
              `POST /call_reasons/validate`.

          certify_brand_is_accurate: Certification that the DIR information is accurate. Must be `true` for the DIR
              to be submitted for vetting.

          certify_ip_ownership: Certification of ownership of any logos/trademarks shown. Must be `true` for the
              DIR to be submitted for vetting.

          certify_no_shaft_content: Certification that this DIR is not used for SHAFT content (Sex, Hate, Alcohol,
              Firearms, Tobacco) where prohibited. Must be `true` for the DIR to be submitted
              for vetting.

          display_name: Name shown to call recipients. 1–35 characters, no emoji, not whitespace-only.

          documents: Additional supporting documents to attach. Append-only: existing documents are
              never removed or replaced, and an empty or omitted list is a no-op. Each
              `document_id` may appear at most once on a DIR.

          logo_url: Publicly accessible HTTPS URL (max 128 chars) to a 256x256 BMP logo (max 1 MB).

          reselling: Set to true if your organization places calls on behalf of other enterprises
              (BPO/reseller). Updating this triggers re-vetting on next submit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        return self._patch(
            path_template("/dir/{dir_id}", dir_id=dir_id),
            body=maybe_transform(
                {
                    "authorizer_email": authorizer_email,
                    "authorizer_name": authorizer_name,
                    "call_reasons": call_reasons,
                    "certify_brand_is_accurate": certify_brand_is_accurate,
                    "certify_ip_ownership": certify_ip_ownership,
                    "certify_no_shaft_content": certify_no_shaft_content,
                    "display_name": display_name,
                    "documents": documents,
                    "logo_url": logo_url,
                    "reselling": reselling,
                },
                dir_update_params.DirUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirUpdateResponse,
        )

    def list(
        self,
        *,
        filter_call_reason_contains: str | Omit = omit,
        filter_display_name_contains: str | Omit = omit,
        filter_enterprise_id: str | Omit = omit,
        filter_expiring_at_gte: Union[str, datetime] | Omit = omit,
        filter_expiring_at_lte: Union[str, datetime] | Omit = omit,
        filter_status: Literal[
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
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal[
            "created_at",
            "-created_at",
            "updated_at",
            "-updated_at",
            "display_name",
            "-display_name",
            "status",
            "-status",
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
        Returns every DIR (Display Identity Record) you own, across all of your
        enterprises, as a single list. Pagination is JSON:API style (`page[number]`,
        `page[size]`, max 250). Supports `filter[]` query params:
        `filter[enterprise_id]`, `filter[status]`, `filter[display_name][contains]`,
        `filter[call_reason][contains]`, plus the renewal-window filters
        `filter[expiring_at][gte]` / `filter[expiring_at][lte]`. Sortable by
        `created_at`, `updated_at`, `display_name`, `status` (prefix `-` for descending;
        default `-created_at`).

        Args:
          filter_call_reason_contains: Case-insensitive partial match on call reason.

          filter_display_name_contains: Case-insensitive partial match on display name.

          filter_enterprise_id: Filter by enterprise ID.

          filter_expiring_at_gte: Return only DIRs whose `expiring_at` is at or after this ISO-8601 timestamp.
              Pairs with the `[lte]` variant to build renewal-window dashboards.

          filter_expiring_at_lte: Return only DIRs whose `expiring_at` is at or before this ISO-8601 timestamp.

          filter_status: Filter by DIR status.

          page_number: 1-based page number. Out-of-range values return an empty page with correct meta.

          page_size: Items per page. Maximum 250; values above are clamped to 250.

          sort: Sort field. Allowed values: `created_at`, `updated_at`, `display_name`,
              `status`. Prefix with `-` for descending. Default `-created_at`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/dir",
            page=SyncDefaultFlatPagination[DirListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_call_reason_contains": filter_call_reason_contains,
                        "filter_display_name_contains": filter_display_name_contains,
                        "filter_enterprise_id": filter_enterprise_id,
                        "filter_expiring_at_gte": filter_expiring_at_gte,
                        "filter_expiring_at_lte": filter_expiring_at_lte,
                        "filter_status": filter_status,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    dir_list_params.DirListParams,
                ),
            ),
            model=DirListResponse,
        )

    def delete(
        self,
        dir_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a DIR.

        Failure modes: `400` if a child phone number is in a non-deletable
        status, `409` if the DIR has an unresolved infringement claim, `404` if the DIR
        is not yours.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/dir/{dir_id}", dir_id=dir_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_loa(
        self,
        dir_id: str,
        *,
        phone_numbers: SequenceNotStr[str],
        agent: dir_create_loa_params.Agent | Omit = omit,
        signature: dir_create_loa_params.Signature | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """Generate a pre-filled Letter of Authorization (LOA) PDF for a DIR.

        Enterprise
        identity (legal name, DBA, address, contact, website, tax id) and the DIR
        display name are read server-side; the caller supplies the telephone numbers to
        authorize, an optional Authorized Agent block, and an optional drawn signature.

        When `signature` is omitted the PDF is returned unsigned so the customer can
        sign it externally and upload it via the Documents API. When `signature` is
        present the PDF embeds the supplied image, printed name, and signed-at date.

        Returns `application/pdf`.

        Args:
          phone_numbers: Telephone numbers to authorize on the DIR, in `+E164` format (`+` followed by
              10-15 digits). Max 15 per request.

          agent: Third-party reseller / partner managing the enterprise's phone numbers. Omit
              when the enterprise works directly with Telnyx.

          signature: Optional. When provided the rendered PDF embeds the signature image, printed
              name, and signed-at date. When absent the PDF is returned unsigned so the
              customer can sign externally and upload it via the Documents API.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        extra_headers = {"Accept": "application/pdf", **(extra_headers or {})}
        return self._post(
            path_template("/dir/{dir_id}/loa", dir_id=dir_id),
            body=maybe_transform(
                {
                    "phone_numbers": phone_numbers,
                    "agent": agent,
                    "signature": signature,
                },
                dir_create_loa_params.DirCreateLoaParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def list_document_types(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirListDocumentTypesResponse:
        """
        Reference list of `document_type` values accepted by
        `DirCreateRequest.documents[].document_type` and the infringement-contest
        endpoint. Each entry has a stable `short_name` (used in API calls) and a
        customer-facing description.
        """
        return self._get(
            "/dir/document_types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirListDocumentTypesResponse,
        )

    def list_infringement_claims(
        self,
        dir_id: str,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[DirListInfringementClaimsResponse]:
        """Return the trademark or copyright claims filed against this DIR.

        Each claim's
        `status` is `pending` (newly filed; DIR auto-suspended), `contested` (you have
        submitted contest evidence; awaiting resolution), or `resolved` (final).
        Resolution outcomes: `upheld` (claim accepted; DIR stays
        suspended/permanently_rejected), `rejected` (claim dismissed; DIR restored to
        `verified`), `modified` (partial outcome).

        Args:
          page_number: 1-based page number. Out-of-range values return an empty page with correct meta.

          page_size: Items per page. Maximum 250; values above are clamped to 250.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        return self._get_api_list(
            path_template("/dir/{dir_id}/infringement_claims", dir_id=dir_id),
            page=SyncDefaultFlatPagination[DirListInfringementClaimsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    dir_list_infringement_claims_params.DirListInfringementClaimsParams,
                ),
            ),
            model=DirListInfringementClaimsResponse,
        )

    def submit(
        self,
        dir_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirSubmitResponse:
        """Submit a DIR for vetting.

        Sends the DIR back through the vetting cycle from any
        non-terminal status. When re-submitting from `suspended` or `expired`, the DIR's
        previous Branded Calling registration is torn down transactionally and its phone
        numbers flip back to `submitted`. When re-submitting from `verified`, the
        existing registration stays live throughout the new vetting cycle.

        Returns `400` from `submitted`/`in_review`/`permanently_rejected`. Returns `409`
        if the DIR has an unresolved infringement claim.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        return self._post(
            path_template("/dir/{dir_id}/submit", dir_id=dir_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirSubmitResponse,
        )

    def update_infringement(
        self,
        dir_id: str,
        *,
        certify_brand_is_accurate: Literal[True],
        certify_ip_ownership: Literal[True],
        certify_no_infringement: Literal[True],
        certify_no_shaft_content: Literal[True],
        infringement_resolution_notes: str,
        call_reasons: Optional[SequenceNotStr[str]] | Omit = omit,
        display_name: Optional[str] | Omit = omit,
        documents: Optional[Iterable[dir_update_infringement_params.Document]] | Omit = omit,
        logo_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirUpdateInfringementResponse:
        """
        Push a fix for a DIR that is `suspended` with an open infringement claim back
        into vetting. `POST /dir/{dir_id}/submit` is blocked while a claim is open, so
        this is the customer-callable path to update the DIR's content and re-certify
        before Telnyx adjudicates the claim. All four certification booleans must be
        `true`. Optional content fields (`display_name`, `logo_url`, `call_reasons`,
        `documents`) update the DIR; documents are append-only.

        Args:
          certify_brand_is_accurate: Must be `true`.

          certify_ip_ownership: Must be `true`.

          certify_no_infringement: Must be `true`.

          certify_no_shaft_content: Must be `true`.

          infringement_resolution_notes: Explanation of how the infringement concern was addressed.

          documents: Append-only supporting documents.

          logo_url: Publicly accessible HTTPS URL (max 128 chars) to a 256x256 BMP logo (max 1 MB).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        return self._put(
            path_template("/dir/{dir_id}/infringement_update", dir_id=dir_id),
            body=maybe_transform(
                {
                    "certify_brand_is_accurate": certify_brand_is_accurate,
                    "certify_ip_ownership": certify_ip_ownership,
                    "certify_no_infringement": certify_no_infringement,
                    "certify_no_shaft_content": certify_no_shaft_content,
                    "infringement_resolution_notes": infringement_resolution_notes,
                    "call_reasons": call_reasons,
                    "display_name": display_name,
                    "documents": documents,
                    "logo_url": logo_url,
                },
                dir_update_infringement_params.DirUpdateInfringementParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirUpdateInfringementResponse,
        )


class AsyncDirResource(AsyncAPIResource):
    @cached_property
    def comments(self) -> AsyncCommentsResource:
        """
        Read messages from the Telnyx vetting team and reply with clarifying information.
        """
        return AsyncCommentsResource(self._client)

    @cached_property
    def phone_number_batches(self) -> AsyncPhoneNumberBatchesResource:
        """Phone numbers are submitted to Telnyx for vetting in batches.

        Batches group all numbers added in a single request under the same Letter of Authorization.
        """
        return AsyncPhoneNumberBatchesResource(self._client)

    @cached_property
    def phone_numbers(self) -> AsyncPhoneNumbersResource:
        """
        Associate phone numbers with a verified DIR so calls from those numbers carry the DIR's display identity.
        """
        return AsyncPhoneNumbersResource(self._client)

    @cached_property
    def references(self) -> AsyncReferencesResource:
        """
        Submit and manage the two business references and one financial reference that vouch for a DIR. References are contacted to confirm the business identity during vetting.
        """
        return AsyncReferencesResource(self._client)

    @cached_property
    def verify_email(self) -> AsyncVerifyEmailResource:
        """Verify ownership of a DIR's authorizer email.

        A short code is emailed and confirmed; the email must be verified before references can be submitted.
        """
        return AsyncVerifyEmailResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDirResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDirResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDirResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#with_streaming_response
        """
        return AsyncDirResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        dir_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirRetrieveResponse:
        """Returns a single DIR by id.

        The enterprise is resolved server-side from the DIR
        id. Returns `404` if the DIR does not exist or is not yours.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        return await self._get(
            path_template("/dir/{dir_id}", dir_id=dir_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirRetrieveResponse,
        )

    async def update(
        self,
        dir_id: str,
        *,
        authorizer_email: str | Omit = omit,
        authorizer_name: str | Omit = omit,
        call_reasons: SequenceNotStr[str] | Omit = omit,
        certify_brand_is_accurate: bool | Omit = omit,
        certify_ip_ownership: bool | Omit = omit,
        certify_no_shaft_content: bool | Omit = omit,
        display_name: str | Omit = omit,
        documents: Iterable[dir_update_params.Document] | Omit = omit,
        logo_url: str | Omit = omit,
        reselling: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirUpdateResponse:
        """Edit a DIR.

        DIRs in `draft`, `rejected`, `unsuccessful`, or `suspended` can be
        edited freely: PATCH is a pure edit, `status` is never changed, and you re-vet
        by calling `POST /v2/dir/{dir_id}/submit` explicitly. A `verified` DIR can also
        be edited in place: a PATCH that changes any value returns the DIR to `draft`
        and branded delivery stops until you re-submit and the DIR is approved again,
        while a PATCH that changes nothing (an empty body or values identical to the
        current ones) leaves the DIR `verified`, so idempotent retries are safe. DIRs in
        any other status (`submitted`, `in_review`, `expired`, `infringement_claimed`,
        `permanently_rejected`) cannot be edited.

        Args:
          authorizer_email: Contact email of the authorizer. Telnyx may send verification or infringement
              notices here.

          authorizer_name: Name of the person at your enterprise authorizing this DIR. Must be a real
              individual.

          call_reasons: 1–10 reasons your business calls customers. Validate phrasing against
              `POST /call_reasons/validate`.

          certify_brand_is_accurate: Certification that the DIR information is accurate. Must be `true` for the DIR
              to be submitted for vetting.

          certify_ip_ownership: Certification of ownership of any logos/trademarks shown. Must be `true` for the
              DIR to be submitted for vetting.

          certify_no_shaft_content: Certification that this DIR is not used for SHAFT content (Sex, Hate, Alcohol,
              Firearms, Tobacco) where prohibited. Must be `true` for the DIR to be submitted
              for vetting.

          display_name: Name shown to call recipients. 1–35 characters, no emoji, not whitespace-only.

          documents: Additional supporting documents to attach. Append-only: existing documents are
              never removed or replaced, and an empty or omitted list is a no-op. Each
              `document_id` may appear at most once on a DIR.

          logo_url: Publicly accessible HTTPS URL (max 128 chars) to a 256x256 BMP logo (max 1 MB).

          reselling: Set to true if your organization places calls on behalf of other enterprises
              (BPO/reseller). Updating this triggers re-vetting on next submit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        return await self._patch(
            path_template("/dir/{dir_id}", dir_id=dir_id),
            body=await async_maybe_transform(
                {
                    "authorizer_email": authorizer_email,
                    "authorizer_name": authorizer_name,
                    "call_reasons": call_reasons,
                    "certify_brand_is_accurate": certify_brand_is_accurate,
                    "certify_ip_ownership": certify_ip_ownership,
                    "certify_no_shaft_content": certify_no_shaft_content,
                    "display_name": display_name,
                    "documents": documents,
                    "logo_url": logo_url,
                    "reselling": reselling,
                },
                dir_update_params.DirUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirUpdateResponse,
        )

    def list(
        self,
        *,
        filter_call_reason_contains: str | Omit = omit,
        filter_display_name_contains: str | Omit = omit,
        filter_enterprise_id: str | Omit = omit,
        filter_expiring_at_gte: Union[str, datetime] | Omit = omit,
        filter_expiring_at_lte: Union[str, datetime] | Omit = omit,
        filter_status: Literal[
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
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        sort: Literal[
            "created_at",
            "-created_at",
            "updated_at",
            "-updated_at",
            "display_name",
            "-display_name",
            "status",
            "-status",
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
        Returns every DIR (Display Identity Record) you own, across all of your
        enterprises, as a single list. Pagination is JSON:API style (`page[number]`,
        `page[size]`, max 250). Supports `filter[]` query params:
        `filter[enterprise_id]`, `filter[status]`, `filter[display_name][contains]`,
        `filter[call_reason][contains]`, plus the renewal-window filters
        `filter[expiring_at][gte]` / `filter[expiring_at][lte]`. Sortable by
        `created_at`, `updated_at`, `display_name`, `status` (prefix `-` for descending;
        default `-created_at`).

        Args:
          filter_call_reason_contains: Case-insensitive partial match on call reason.

          filter_display_name_contains: Case-insensitive partial match on display name.

          filter_enterprise_id: Filter by enterprise ID.

          filter_expiring_at_gte: Return only DIRs whose `expiring_at` is at or after this ISO-8601 timestamp.
              Pairs with the `[lte]` variant to build renewal-window dashboards.

          filter_expiring_at_lte: Return only DIRs whose `expiring_at` is at or before this ISO-8601 timestamp.

          filter_status: Filter by DIR status.

          page_number: 1-based page number. Out-of-range values return an empty page with correct meta.

          page_size: Items per page. Maximum 250; values above are clamped to 250.

          sort: Sort field. Allowed values: `created_at`, `updated_at`, `display_name`,
              `status`. Prefix with `-` for descending. Default `-created_at`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/dir",
            page=AsyncDefaultFlatPagination[DirListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_call_reason_contains": filter_call_reason_contains,
                        "filter_display_name_contains": filter_display_name_contains,
                        "filter_enterprise_id": filter_enterprise_id,
                        "filter_expiring_at_gte": filter_expiring_at_gte,
                        "filter_expiring_at_lte": filter_expiring_at_lte,
                        "filter_status": filter_status,
                        "page_number": page_number,
                        "page_size": page_size,
                        "sort": sort,
                    },
                    dir_list_params.DirListParams,
                ),
            ),
            model=DirListResponse,
        )

    async def delete(
        self,
        dir_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a DIR.

        Failure modes: `400` if a child phone number is in a non-deletable
        status, `409` if the DIR has an unresolved infringement claim, `404` if the DIR
        is not yours.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/dir/{dir_id}", dir_id=dir_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_loa(
        self,
        dir_id: str,
        *,
        phone_numbers: SequenceNotStr[str],
        agent: dir_create_loa_params.Agent | Omit = omit,
        signature: dir_create_loa_params.Signature | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """Generate a pre-filled Letter of Authorization (LOA) PDF for a DIR.

        Enterprise
        identity (legal name, DBA, address, contact, website, tax id) and the DIR
        display name are read server-side; the caller supplies the telephone numbers to
        authorize, an optional Authorized Agent block, and an optional drawn signature.

        When `signature` is omitted the PDF is returned unsigned so the customer can
        sign it externally and upload it via the Documents API. When `signature` is
        present the PDF embeds the supplied image, printed name, and signed-at date.

        Returns `application/pdf`.

        Args:
          phone_numbers: Telephone numbers to authorize on the DIR, in `+E164` format (`+` followed by
              10-15 digits). Max 15 per request.

          agent: Third-party reseller / partner managing the enterprise's phone numbers. Omit
              when the enterprise works directly with Telnyx.

          signature: Optional. When provided the rendered PDF embeds the signature image, printed
              name, and signed-at date. When absent the PDF is returned unsigned so the
              customer can sign externally and upload it via the Documents API.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        extra_headers = {"Accept": "application/pdf", **(extra_headers or {})}
        return await self._post(
            path_template("/dir/{dir_id}/loa", dir_id=dir_id),
            body=await async_maybe_transform(
                {
                    "phone_numbers": phone_numbers,
                    "agent": agent,
                    "signature": signature,
                },
                dir_create_loa_params.DirCreateLoaParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def list_document_types(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirListDocumentTypesResponse:
        """
        Reference list of `document_type` values accepted by
        `DirCreateRequest.documents[].document_type` and the infringement-contest
        endpoint. Each entry has a stable `short_name` (used in API calls) and a
        customer-facing description.
        """
        return await self._get(
            "/dir/document_types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirListDocumentTypesResponse,
        )

    def list_infringement_claims(
        self,
        dir_id: str,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[
        DirListInfringementClaimsResponse, AsyncDefaultFlatPagination[DirListInfringementClaimsResponse]
    ]:
        """Return the trademark or copyright claims filed against this DIR.

        Each claim's
        `status` is `pending` (newly filed; DIR auto-suspended), `contested` (you have
        submitted contest evidence; awaiting resolution), or `resolved` (final).
        Resolution outcomes: `upheld` (claim accepted; DIR stays
        suspended/permanently_rejected), `rejected` (claim dismissed; DIR restored to
        `verified`), `modified` (partial outcome).

        Args:
          page_number: 1-based page number. Out-of-range values return an empty page with correct meta.

          page_size: Items per page. Maximum 250; values above are clamped to 250.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        return self._get_api_list(
            path_template("/dir/{dir_id}/infringement_claims", dir_id=dir_id),
            page=AsyncDefaultFlatPagination[DirListInfringementClaimsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    dir_list_infringement_claims_params.DirListInfringementClaimsParams,
                ),
            ),
            model=DirListInfringementClaimsResponse,
        )

    async def submit(
        self,
        dir_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirSubmitResponse:
        """Submit a DIR for vetting.

        Sends the DIR back through the vetting cycle from any
        non-terminal status. When re-submitting from `suspended` or `expired`, the DIR's
        previous Branded Calling registration is torn down transactionally and its phone
        numbers flip back to `submitted`. When re-submitting from `verified`, the
        existing registration stays live throughout the new vetting cycle.

        Returns `400` from `submitted`/`in_review`/`permanently_rejected`. Returns `409`
        if the DIR has an unresolved infringement claim.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        return await self._post(
            path_template("/dir/{dir_id}/submit", dir_id=dir_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirSubmitResponse,
        )

    async def update_infringement(
        self,
        dir_id: str,
        *,
        certify_brand_is_accurate: Literal[True],
        certify_ip_ownership: Literal[True],
        certify_no_infringement: Literal[True],
        certify_no_shaft_content: Literal[True],
        infringement_resolution_notes: str,
        call_reasons: Optional[SequenceNotStr[str]] | Omit = omit,
        display_name: Optional[str] | Omit = omit,
        documents: Optional[Iterable[dir_update_infringement_params.Document]] | Omit = omit,
        logo_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirUpdateInfringementResponse:
        """
        Push a fix for a DIR that is `suspended` with an open infringement claim back
        into vetting. `POST /dir/{dir_id}/submit` is blocked while a claim is open, so
        this is the customer-callable path to update the DIR's content and re-certify
        before Telnyx adjudicates the claim. All four certification booleans must be
        `true`. Optional content fields (`display_name`, `logo_url`, `call_reasons`,
        `documents`) update the DIR; documents are append-only.

        Args:
          certify_brand_is_accurate: Must be `true`.

          certify_ip_ownership: Must be `true`.

          certify_no_infringement: Must be `true`.

          certify_no_shaft_content: Must be `true`.

          infringement_resolution_notes: Explanation of how the infringement concern was addressed.

          documents: Append-only supporting documents.

          logo_url: Publicly accessible HTTPS URL (max 128 chars) to a 256x256 BMP logo (max 1 MB).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        return await self._put(
            path_template("/dir/{dir_id}/infringement_update", dir_id=dir_id),
            body=await async_maybe_transform(
                {
                    "certify_brand_is_accurate": certify_brand_is_accurate,
                    "certify_ip_ownership": certify_ip_ownership,
                    "certify_no_infringement": certify_no_infringement,
                    "certify_no_shaft_content": certify_no_shaft_content,
                    "infringement_resolution_notes": infringement_resolution_notes,
                    "call_reasons": call_reasons,
                    "display_name": display_name,
                    "documents": documents,
                    "logo_url": logo_url,
                },
                dir_update_infringement_params.DirUpdateInfringementParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirUpdateInfringementResponse,
        )


class DirResourceWithRawResponse:
    def __init__(self, dir: DirResource) -> None:
        self._dir = dir

        self.retrieve = to_raw_response_wrapper(
            dir.retrieve,
        )
        self.update = to_raw_response_wrapper(
            dir.update,
        )
        self.list = to_raw_response_wrapper(
            dir.list,
        )
        self.delete = to_raw_response_wrapper(
            dir.delete,
        )
        self.create_loa = to_custom_raw_response_wrapper(
            dir.create_loa,
            BinaryAPIResponse,
        )
        self.list_document_types = to_raw_response_wrapper(
            dir.list_document_types,
        )
        self.list_infringement_claims = to_raw_response_wrapper(
            dir.list_infringement_claims,
        )
        self.submit = to_raw_response_wrapper(
            dir.submit,
        )
        self.update_infringement = to_raw_response_wrapper(
            dir.update_infringement,
        )

    @cached_property
    def comments(self) -> CommentsResourceWithRawResponse:
        """
        Read messages from the Telnyx vetting team and reply with clarifying information.
        """
        return CommentsResourceWithRawResponse(self._dir.comments)

    @cached_property
    def phone_number_batches(self) -> PhoneNumberBatchesResourceWithRawResponse:
        """Phone numbers are submitted to Telnyx for vetting in batches.

        Batches group all numbers added in a single request under the same Letter of Authorization.
        """
        return PhoneNumberBatchesResourceWithRawResponse(self._dir.phone_number_batches)

    @cached_property
    def phone_numbers(self) -> PhoneNumbersResourceWithRawResponse:
        """
        Associate phone numbers with a verified DIR so calls from those numbers carry the DIR's display identity.
        """
        return PhoneNumbersResourceWithRawResponse(self._dir.phone_numbers)

    @cached_property
    def references(self) -> ReferencesResourceWithRawResponse:
        """
        Submit and manage the two business references and one financial reference that vouch for a DIR. References are contacted to confirm the business identity during vetting.
        """
        return ReferencesResourceWithRawResponse(self._dir.references)

    @cached_property
    def verify_email(self) -> VerifyEmailResourceWithRawResponse:
        """Verify ownership of a DIR's authorizer email.

        A short code is emailed and confirmed; the email must be verified before references can be submitted.
        """
        return VerifyEmailResourceWithRawResponse(self._dir.verify_email)


class AsyncDirResourceWithRawResponse:
    def __init__(self, dir: AsyncDirResource) -> None:
        self._dir = dir

        self.retrieve = async_to_raw_response_wrapper(
            dir.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            dir.update,
        )
        self.list = async_to_raw_response_wrapper(
            dir.list,
        )
        self.delete = async_to_raw_response_wrapper(
            dir.delete,
        )
        self.create_loa = async_to_custom_raw_response_wrapper(
            dir.create_loa,
            AsyncBinaryAPIResponse,
        )
        self.list_document_types = async_to_raw_response_wrapper(
            dir.list_document_types,
        )
        self.list_infringement_claims = async_to_raw_response_wrapper(
            dir.list_infringement_claims,
        )
        self.submit = async_to_raw_response_wrapper(
            dir.submit,
        )
        self.update_infringement = async_to_raw_response_wrapper(
            dir.update_infringement,
        )

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithRawResponse:
        """
        Read messages from the Telnyx vetting team and reply with clarifying information.
        """
        return AsyncCommentsResourceWithRawResponse(self._dir.comments)

    @cached_property
    def phone_number_batches(self) -> AsyncPhoneNumberBatchesResourceWithRawResponse:
        """Phone numbers are submitted to Telnyx for vetting in batches.

        Batches group all numbers added in a single request under the same Letter of Authorization.
        """
        return AsyncPhoneNumberBatchesResourceWithRawResponse(self._dir.phone_number_batches)

    @cached_property
    def phone_numbers(self) -> AsyncPhoneNumbersResourceWithRawResponse:
        """
        Associate phone numbers with a verified DIR so calls from those numbers carry the DIR's display identity.
        """
        return AsyncPhoneNumbersResourceWithRawResponse(self._dir.phone_numbers)

    @cached_property
    def references(self) -> AsyncReferencesResourceWithRawResponse:
        """
        Submit and manage the two business references and one financial reference that vouch for a DIR. References are contacted to confirm the business identity during vetting.
        """
        return AsyncReferencesResourceWithRawResponse(self._dir.references)

    @cached_property
    def verify_email(self) -> AsyncVerifyEmailResourceWithRawResponse:
        """Verify ownership of a DIR's authorizer email.

        A short code is emailed and confirmed; the email must be verified before references can be submitted.
        """
        return AsyncVerifyEmailResourceWithRawResponse(self._dir.verify_email)


class DirResourceWithStreamingResponse:
    def __init__(self, dir: DirResource) -> None:
        self._dir = dir

        self.retrieve = to_streamed_response_wrapper(
            dir.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            dir.update,
        )
        self.list = to_streamed_response_wrapper(
            dir.list,
        )
        self.delete = to_streamed_response_wrapper(
            dir.delete,
        )
        self.create_loa = to_custom_streamed_response_wrapper(
            dir.create_loa,
            StreamedBinaryAPIResponse,
        )
        self.list_document_types = to_streamed_response_wrapper(
            dir.list_document_types,
        )
        self.list_infringement_claims = to_streamed_response_wrapper(
            dir.list_infringement_claims,
        )
        self.submit = to_streamed_response_wrapper(
            dir.submit,
        )
        self.update_infringement = to_streamed_response_wrapper(
            dir.update_infringement,
        )

    @cached_property
    def comments(self) -> CommentsResourceWithStreamingResponse:
        """
        Read messages from the Telnyx vetting team and reply with clarifying information.
        """
        return CommentsResourceWithStreamingResponse(self._dir.comments)

    @cached_property
    def phone_number_batches(self) -> PhoneNumberBatchesResourceWithStreamingResponse:
        """Phone numbers are submitted to Telnyx for vetting in batches.

        Batches group all numbers added in a single request under the same Letter of Authorization.
        """
        return PhoneNumberBatchesResourceWithStreamingResponse(self._dir.phone_number_batches)

    @cached_property
    def phone_numbers(self) -> PhoneNumbersResourceWithStreamingResponse:
        """
        Associate phone numbers with a verified DIR so calls from those numbers carry the DIR's display identity.
        """
        return PhoneNumbersResourceWithStreamingResponse(self._dir.phone_numbers)

    @cached_property
    def references(self) -> ReferencesResourceWithStreamingResponse:
        """
        Submit and manage the two business references and one financial reference that vouch for a DIR. References are contacted to confirm the business identity during vetting.
        """
        return ReferencesResourceWithStreamingResponse(self._dir.references)

    @cached_property
    def verify_email(self) -> VerifyEmailResourceWithStreamingResponse:
        """Verify ownership of a DIR's authorizer email.

        A short code is emailed and confirmed; the email must be verified before references can be submitted.
        """
        return VerifyEmailResourceWithStreamingResponse(self._dir.verify_email)


class AsyncDirResourceWithStreamingResponse:
    def __init__(self, dir: AsyncDirResource) -> None:
        self._dir = dir

        self.retrieve = async_to_streamed_response_wrapper(
            dir.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            dir.update,
        )
        self.list = async_to_streamed_response_wrapper(
            dir.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            dir.delete,
        )
        self.create_loa = async_to_custom_streamed_response_wrapper(
            dir.create_loa,
            AsyncStreamedBinaryAPIResponse,
        )
        self.list_document_types = async_to_streamed_response_wrapper(
            dir.list_document_types,
        )
        self.list_infringement_claims = async_to_streamed_response_wrapper(
            dir.list_infringement_claims,
        )
        self.submit = async_to_streamed_response_wrapper(
            dir.submit,
        )
        self.update_infringement = async_to_streamed_response_wrapper(
            dir.update_infringement,
        )

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithStreamingResponse:
        """
        Read messages from the Telnyx vetting team and reply with clarifying information.
        """
        return AsyncCommentsResourceWithStreamingResponse(self._dir.comments)

    @cached_property
    def phone_number_batches(self) -> AsyncPhoneNumberBatchesResourceWithStreamingResponse:
        """Phone numbers are submitted to Telnyx for vetting in batches.

        Batches group all numbers added in a single request under the same Letter of Authorization.
        """
        return AsyncPhoneNumberBatchesResourceWithStreamingResponse(self._dir.phone_number_batches)

    @cached_property
    def phone_numbers(self) -> AsyncPhoneNumbersResourceWithStreamingResponse:
        """
        Associate phone numbers with a verified DIR so calls from those numbers carry the DIR's display identity.
        """
        return AsyncPhoneNumbersResourceWithStreamingResponse(self._dir.phone_numbers)

    @cached_property
    def references(self) -> AsyncReferencesResourceWithStreamingResponse:
        """
        Submit and manage the two business references and one financial reference that vouch for a DIR. References are contacted to confirm the business identity during vetting.
        """
        return AsyncReferencesResourceWithStreamingResponse(self._dir.references)

    @cached_property
    def verify_email(self) -> AsyncVerifyEmailResourceWithStreamingResponse:
        """Verify ownership of a DIR's authorizer email.

        A short code is emailed and confirmed; the email must be verified before references can be submitted.
        """
        return AsyncVerifyEmailResourceWithStreamingResponse(self._dir.verify_email)
