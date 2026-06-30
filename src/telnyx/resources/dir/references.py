# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.dir import reference_submit_params, reference_update_params
from ..._base_client import make_request_options
from ...types.dir.reference_list_response import ReferenceListResponse
from ...types.dir.reference_submit_response import ReferenceSubmitResponse
from ...types.dir.reference_update_response import ReferenceUpdateResponse

__all__ = ["ReferencesResource", "AsyncReferencesResource"]


class ReferencesResource(SyncAPIResource):
    """
    Submit and manage the two business references and one financial reference that vouch for a DIR. References are contacted to confirm the business identity during vetting.
    """

    @cached_property
    def with_raw_response(self) -> ReferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ReferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ReferencesResourceWithStreamingResponse(self)

    def update(
        self,
        slot: int,
        *,
        dir_id: str,
        ref_type: Literal["business", "financial"],
        email: str | Omit = omit,
        full_name: str | Omit = omit,
        job_title: Optional[str] | Omit = omit,
        organization: Optional[str] | Omit = omit,
        phone_e164: str | Omit = omit,
        relationship_to_registrant: Optional[str] | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReferenceUpdateResponse:
        """
        Partially update one reference, addressed by the DIR id plus the reference's
        type (business or financial) and slot.

        Cosmetic fields (full name, job title, organization, relationship, email) are
        always editable. The phone number and timezone may only be changed while a
        scheduled call has not yet been dialed; if a call is in progress or all attempts
        are complete, those fields are locked. Changing the timezone reschedules any
        pending call into the new local calling window.

        Args:
          email: Reference contact email address.

          full_name: Full name of the reference contact.

          job_title: Job title of the reference contact.

          organization: Organization the reference contact belongs to.

          phone_e164: Reference phone number in E.164 format.

          relationship_to_registrant: How the reference contact is related to the registering business.

          timezone: IANA timezone id for the reference.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        if not ref_type:
            raise ValueError(f"Expected a non-empty value for `ref_type` but received {ref_type!r}")
        return self._patch(
            path_template("/dir/{dir_id}/references/{ref_type}/{slot}", dir_id=dir_id, ref_type=ref_type, slot=slot),
            body=maybe_transform(
                {
                    "email": email,
                    "full_name": full_name,
                    "job_title": job_title,
                    "organization": organization,
                    "phone_e164": phone_e164,
                    "relationship_to_registrant": relationship_to_registrant,
                    "timezone": timezone,
                },
                reference_update_params.ReferenceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReferenceUpdateResponse,
        )

    def list(
        self,
        dir_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReferenceListResponse:
        """
        List the business and financial references submitted for a DIR.

        Returns the two business references (slots 0 and 1) followed by the single
        financial reference. Each entry carries only the customer-supplied details
        (name, title, organization, relationship, phone, email, timezone). Returns an
        empty list when no references were submitted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        return self._get(
            path_template("/dir/{dir_id}/references", dir_id=dir_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReferenceListResponse,
        )

    def submit(
        self,
        dir_id: str,
        *,
        business_references: Iterable[reference_submit_params.BusinessReference],
        financial_reference: reference_submit_params.FinancialReference,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReferenceSubmitResponse:
        """
        Submit the two business references and one financial reference for a DIR.

        The DIR's authorizer email must be verified first (see the email-verification
        endpoint). Until it is, this returns `409` and no references are stored.

        The request body carries exactly two business references plus one financial
        reference. On success the references are stored and the response echoes them in
        the same shape as the GET. Submitting again converges on the already-stored
        references rather than erroring.

        Args:
          business_references: Exactly two business references.

          financial_reference: One reference supplied at submit. The reference type is implied by the field
              that carries it (business_references vs financial_reference).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        return self._post(
            path_template("/dir/{dir_id}/references", dir_id=dir_id),
            body=maybe_transform(
                {
                    "business_references": business_references,
                    "financial_reference": financial_reference,
                },
                reference_submit_params.ReferenceSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReferenceSubmitResponse,
        )


class AsyncReferencesResource(AsyncAPIResource):
    """
    Submit and manage the two business references and one financial reference that vouch for a DIR. References are contacted to confirm the business identity during vetting.
    """

    @cached_property
    def with_raw_response(self) -> AsyncReferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncReferencesResourceWithStreamingResponse(self)

    async def update(
        self,
        slot: int,
        *,
        dir_id: str,
        ref_type: Literal["business", "financial"],
        email: str | Omit = omit,
        full_name: str | Omit = omit,
        job_title: Optional[str] | Omit = omit,
        organization: Optional[str] | Omit = omit,
        phone_e164: str | Omit = omit,
        relationship_to_registrant: Optional[str] | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReferenceUpdateResponse:
        """
        Partially update one reference, addressed by the DIR id plus the reference's
        type (business or financial) and slot.

        Cosmetic fields (full name, job title, organization, relationship, email) are
        always editable. The phone number and timezone may only be changed while a
        scheduled call has not yet been dialed; if a call is in progress or all attempts
        are complete, those fields are locked. Changing the timezone reschedules any
        pending call into the new local calling window.

        Args:
          email: Reference contact email address.

          full_name: Full name of the reference contact.

          job_title: Job title of the reference contact.

          organization: Organization the reference contact belongs to.

          phone_e164: Reference phone number in E.164 format.

          relationship_to_registrant: How the reference contact is related to the registering business.

          timezone: IANA timezone id for the reference.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        if not ref_type:
            raise ValueError(f"Expected a non-empty value for `ref_type` but received {ref_type!r}")
        return await self._patch(
            path_template("/dir/{dir_id}/references/{ref_type}/{slot}", dir_id=dir_id, ref_type=ref_type, slot=slot),
            body=await async_maybe_transform(
                {
                    "email": email,
                    "full_name": full_name,
                    "job_title": job_title,
                    "organization": organization,
                    "phone_e164": phone_e164,
                    "relationship_to_registrant": relationship_to_registrant,
                    "timezone": timezone,
                },
                reference_update_params.ReferenceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReferenceUpdateResponse,
        )

    async def list(
        self,
        dir_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReferenceListResponse:
        """
        List the business and financial references submitted for a DIR.

        Returns the two business references (slots 0 and 1) followed by the single
        financial reference. Each entry carries only the customer-supplied details
        (name, title, organization, relationship, phone, email, timezone). Returns an
        empty list when no references were submitted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        return await self._get(
            path_template("/dir/{dir_id}/references", dir_id=dir_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReferenceListResponse,
        )

    async def submit(
        self,
        dir_id: str,
        *,
        business_references: Iterable[reference_submit_params.BusinessReference],
        financial_reference: reference_submit_params.FinancialReference,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReferenceSubmitResponse:
        """
        Submit the two business references and one financial reference for a DIR.

        The DIR's authorizer email must be verified first (see the email-verification
        endpoint). Until it is, this returns `409` and no references are stored.

        The request body carries exactly two business references plus one financial
        reference. On success the references are stored and the response echoes them in
        the same shape as the GET. Submitting again converges on the already-stored
        references rather than erroring.

        Args:
          business_references: Exactly two business references.

          financial_reference: One reference supplied at submit. The reference type is implied by the field
              that carries it (business_references vs financial_reference).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        return await self._post(
            path_template("/dir/{dir_id}/references", dir_id=dir_id),
            body=await async_maybe_transform(
                {
                    "business_references": business_references,
                    "financial_reference": financial_reference,
                },
                reference_submit_params.ReferenceSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReferenceSubmitResponse,
        )


class ReferencesResourceWithRawResponse:
    def __init__(self, references: ReferencesResource) -> None:
        self._references = references

        self.update = to_raw_response_wrapper(
            references.update,
        )
        self.list = to_raw_response_wrapper(
            references.list,
        )
        self.submit = to_raw_response_wrapper(
            references.submit,
        )


class AsyncReferencesResourceWithRawResponse:
    def __init__(self, references: AsyncReferencesResource) -> None:
        self._references = references

        self.update = async_to_raw_response_wrapper(
            references.update,
        )
        self.list = async_to_raw_response_wrapper(
            references.list,
        )
        self.submit = async_to_raw_response_wrapper(
            references.submit,
        )


class ReferencesResourceWithStreamingResponse:
    def __init__(self, references: ReferencesResource) -> None:
        self._references = references

        self.update = to_streamed_response_wrapper(
            references.update,
        )
        self.list = to_streamed_response_wrapper(
            references.list,
        )
        self.submit = to_streamed_response_wrapper(
            references.submit,
        )


class AsyncReferencesResourceWithStreamingResponse:
    def __init__(self, references: AsyncReferencesResource) -> None:
        self._references = references

        self.update = async_to_streamed_response_wrapper(
            references.update,
        )
        self.list = async_to_streamed_response_wrapper(
            references.list,
        )
        self.submit = async_to_streamed_response_wrapper(
            references.submit,
        )
