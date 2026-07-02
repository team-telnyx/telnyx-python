# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from .dir import (
    DirResource,
    AsyncDirResource,
    DirResourceWithRawResponse,
    AsyncDirResourceWithRawResponse,
    DirResourceWithStreamingResponse,
    AsyncDirResourceWithStreamingResponse,
)
from ...types import (
    enterprise_list_params,
    enterprise_create_params,
    enterprise_update_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from .reputation.reputation import (
    ReputationResource,
    AsyncReputationResource,
    ReputationResourceWithRawResponse,
    AsyncReputationResourceWithRawResponse,
    ReputationResourceWithStreamingResponse,
    AsyncReputationResourceWithStreamingResponse,
)
from ...types.enterprise_public import EnterprisePublic
from ...types.billing_address_param import BillingAddressParam
from ...types.billing_contact_param import BillingContactParam
from ...types.physical_address_param import PhysicalAddressParam
from ...types.enterprise_create_response import EnterpriseCreateResponse
from ...types.enterprise_update_response import EnterpriseUpdateResponse
from ...types.organization_contact_param import OrganizationContactParam
from ...types.enterprise_retrieve_response import EnterpriseRetrieveResponse
from ...types.enterprise_activate_branded_calling_response import EnterpriseActivateBrandedCallingResponse

__all__ = ["EnterprisesResource", "AsyncEnterprisesResource"]


class EnterprisesResource(SyncAPIResource):
    """Manage the legal-entity record that owns your DIRs and phone numbers."""

    @cached_property
    def reputation(self) -> ReputationResource:
        """Phone-number reputation monitoring (spam-score lookup and tracking)."""
        return ReputationResource(self._client)

    @cached_property
    def dir(self) -> DirResource:
        """
        A Display Identity Record (DIR) is the verified calling identity (display name, logo, call reasons) shown to recipients on outbound calls.
        """
        return DirResource(self._client)

    @cached_property
    def with_raw_response(self) -> EnterprisesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return EnterprisesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnterprisesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#with_streaming_response
        """
        return EnterprisesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        billing_address: BillingAddressParam,
        billing_contact: BillingContactParam,
        country_code: str,
        doing_business_as: str,
        fein: str,
        industry: Literal[
            "accounting",
            "finance",
            "billing",
            "collections",
            "business",
            "charity",
            "nonprofit",
            "communications",
            "telecom",
            "customer service",
            "support",
            "delivery",
            "shipping",
            "logistics",
            "education",
            "financial",
            "banking",
            "government",
            "public",
            "healthcare",
            "health",
            "pharmacy",
            "medical",
            "insurance",
            "legal",
            "law",
            "notifications",
            "scheduling",
            "real estate",
            "property",
            "retail",
            "ecommerce",
            "sales",
            "marketing",
            "software",
            "technology",
            "tech",
            "media",
            "surveys",
            "market research",
            "travel",
            "hospitality",
            "hotel",
        ],
        jurisdiction_of_incorporation: str,
        legal_name: str,
        number_of_employees: Literal["1-10", "11-50", "51-200", "201-500", "501-2000", "2001-10000", "10001+"],
        organization_contact: OrganizationContactParam,
        organization_legal_type: Literal["corporation", "llc", "partnership", "nonprofit", "other"],
        organization_physical_address: PhysicalAddressParam,
        organization_type: Literal["commercial", "government", "non_profit"],
        website: str,
        corporate_registration_number: Optional[str] | Omit = omit,
        customer_reference: str | Omit = omit,
        dun_bradstreet_number: Optional[str] | Omit = omit,
        primary_business_domain_sic_code: Optional[str] | Omit = omit,
        professional_license_number: Optional[str] | Omit = omit,
        role_type: Literal["enterprise", "bpo"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnterpriseCreateResponse:
        """
        Create the legal entity (enterprise) that represents your business on the Telnyx
        platform.

        The response carries a server-assigned `id` you use for every subsequent call.
        An enterprise is created once and reused; the API collects all required fields
        up front.

        Common failure modes:

        - `422` - a required field is missing or malformed (the response
          `errors[].source.pointer` names the field).
        - `409` - an enterprise with the same identifying details already exists under
          your account.

        Args:
          country_code: ISO 3166-1 alpha-2 country code. Currently `US` and `CA` are supported.

          fein: US Federal Employer Identification Number (`NN-NNNNNNN`) or Canadian equivalent.

          industry: Industry classification.

          legal_name: Legal name of the enterprise.

          number_of_employees: Approximate headcount range. Used for vetting heuristics; pick the bucket that
              contains your current employee count.

          organization_legal_type:
              Legal-entity form. Pick the form that matches your incorporation documents:

              - `corporation` - C-corp or S-corp.
              - `llc` - limited liability company.
              - `partnership` - general/limited partnership.
              - `nonprofit` - non-profit corporation, charitable trust, or
                501(c)(3)/equivalent.
              - `other` - anything else (sole proprietorships, government bodies, DBAs, etc.).
                You may be asked for additional documents during vetting.

          organization_type:
              Organization category for vetting purposes:

              - `commercial` - for-profit business entities (LLC, corp, partnership, sole
                proprietorship). Most callers fall here.
              - `government` - federal/state/local government bodies.
              - `non_profit` - registered 501(c)(3)/equivalent (incl. educational
                institutions, charities, religious organisations).

          corporate_registration_number: Optional corporate-registration / company-number identifier.

          customer_reference: Optional free-form string the caller can attach for their own bookkeeping.
              Telnyx does not interpret it.

          dun_bradstreet_number: Optional D-U-N-S Number.

          primary_business_domain_sic_code: Optional SIC code for the primary line of business.

          professional_license_number: Optional professional-license number for regulated industries.

          role_type: `enterprise` for an organization registering its own DIRs; `bpo` for a Business
              Process Outsourcer placing calls on behalf of one or more enterprises.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/enterprises",
            body=maybe_transform(
                {
                    "billing_address": billing_address,
                    "billing_contact": billing_contact,
                    "country_code": country_code,
                    "doing_business_as": doing_business_as,
                    "fein": fein,
                    "industry": industry,
                    "jurisdiction_of_incorporation": jurisdiction_of_incorporation,
                    "legal_name": legal_name,
                    "number_of_employees": number_of_employees,
                    "organization_contact": organization_contact,
                    "organization_legal_type": organization_legal_type,
                    "organization_physical_address": organization_physical_address,
                    "organization_type": organization_type,
                    "website": website,
                    "corporate_registration_number": corporate_registration_number,
                    "customer_reference": customer_reference,
                    "dun_bradstreet_number": dun_bradstreet_number,
                    "primary_business_domain_sic_code": primary_business_domain_sic_code,
                    "professional_license_number": professional_license_number,
                    "role_type": role_type,
                },
                enterprise_create_params.EnterpriseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnterpriseCreateResponse,
        )

    def retrieve(
        self,
        enterprise_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnterpriseRetrieveResponse:
        """Retrieve a single enterprise by id.

        Returns `404` if the id does not exist or
        does not belong to your account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return self._get(
            path_template("/enterprises/{enterprise_id}", enterprise_id=enterprise_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnterpriseRetrieveResponse,
        )

    def update(
        self,
        enterprise_id: str,
        *,
        billing_address: BillingAddressParam | Omit = omit,
        billing_contact: BillingContactParam | Omit = omit,
        corporate_registration_number: Optional[str] | Omit = omit,
        customer_reference: str | Omit = omit,
        doing_business_as: str | Omit = omit,
        dun_bradstreet_number: Optional[str] | Omit = omit,
        fein: str | Omit = omit,
        industry: Literal[
            "accounting",
            "finance",
            "billing",
            "collections",
            "business",
            "charity",
            "nonprofit",
            "communications",
            "telecom",
            "customer service",
            "support",
            "delivery",
            "shipping",
            "logistics",
            "education",
            "financial",
            "banking",
            "government",
            "public",
            "healthcare",
            "health",
            "pharmacy",
            "medical",
            "insurance",
            "legal",
            "law",
            "notifications",
            "scheduling",
            "real estate",
            "property",
            "retail",
            "ecommerce",
            "sales",
            "marketing",
            "software",
            "technology",
            "tech",
            "media",
            "surveys",
            "market research",
            "travel",
            "hospitality",
            "hotel",
        ]
        | Omit = omit,
        jurisdiction_of_incorporation: str | Omit = omit,
        legal_name: str | Omit = omit,
        number_of_employees: str | Omit = omit,
        organization_contact: OrganizationContactParam | Omit = omit,
        organization_legal_type: str | Omit = omit,
        organization_physical_address: PhysicalAddressParam | Omit = omit,
        primary_business_domain_sic_code: Optional[str] | Omit = omit,
        professional_license_number: Optional[str] | Omit = omit,
        website: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnterpriseUpdateResponse:
        """Replace the enterprise's mutable fields.

        Only mutable fields may be sent.
        Server-assigned and immutable fields (`id`, `record_type`, `created_at`,
        `updated_at`, status fields, `organization_type`, `country_code`, `role_type`)
        cannot be changed: including any of them in the body is rejected with
        `400 Bad Request` (`Field 'X' is not allowed in this request`).

        Args:
          jurisdiction_of_incorporation: Updated state/province/country of incorporation. Optional on update.

          legal_name: Legal name of the enterprise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return self._put(
            path_template("/enterprises/{enterprise_id}", enterprise_id=enterprise_id),
            body=maybe_transform(
                {
                    "billing_address": billing_address,
                    "billing_contact": billing_contact,
                    "corporate_registration_number": corporate_registration_number,
                    "customer_reference": customer_reference,
                    "doing_business_as": doing_business_as,
                    "dun_bradstreet_number": dun_bradstreet_number,
                    "fein": fein,
                    "industry": industry,
                    "jurisdiction_of_incorporation": jurisdiction_of_incorporation,
                    "legal_name": legal_name,
                    "number_of_employees": number_of_employees,
                    "organization_contact": organization_contact,
                    "organization_legal_type": organization_legal_type,
                    "organization_physical_address": organization_physical_address,
                    "primary_business_domain_sic_code": primary_business_domain_sic_code,
                    "professional_license_number": professional_license_number,
                    "website": website,
                },
                enterprise_update_params.EnterpriseUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnterpriseUpdateResponse,
        )

    def list(
        self,
        *,
        filter_legal_name_contains: str | Omit = omit,
        legal_name: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[EnterprisePublic]:
        """Return the enterprises you own, paginated.

        The default page size is 20; the
        maximum is 250.

        Args:
          filter_legal_name_contains: Case-insensitive partial match on legal name.

          legal_name: Filter by legal name (partial match).

          page_number: 1-based page number. Out-of-range values return an empty page with correct meta.

          page_size: Items per page. Default 10. Maximum 250; values above are clamped to 250.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/enterprises",
            page=SyncDefaultFlatPagination[EnterprisePublic],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_legal_name_contains": filter_legal_name_contains,
                        "legal_name": legal_name,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    enterprise_list_params.EnterpriseListParams,
                ),
            ),
            model=EnterprisePublic,
        )

    def delete(
        self,
        enterprise_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Soft-delete an enterprise.

        Failure modes:

        - `400` - the enterprise still has dependent resources in a non-deletable state.
          Remove those first; the response `detail` identifies what is blocking the
          delete.
        - `409` - the enterprise has a dependent resource with an unresolved claim.
          Resolve it before deleting.
        - `404` - the enterprise does not exist or does not belong to your account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/enterprises/{enterprise_id}", enterprise_id=enterprise_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def activate_branded_calling(
        self,
        enterprise_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnterpriseActivateBrandedCallingResponse:
        """
        Branded Calling is a paid product that must be activated on each enterprise.
        Activation is idempotent:

        - First call: marks the enterprise as activated and begins onboarding it with
          the Branded Calling platform asynchronously. Returns `200` with
          `branded_calling_enabled: true`.
        - Re-call after success: no-op, returns the same enterprise body.
        - Re-call after a prior failure: re-queues onboarding, returns `200`.

        Prerequisite: the calling user must have agreed to the Branded Calling Terms of
        Service (`POST /terms_of_service/branded_calling/agree`). Without that, this
        endpoint returns `403 terms_of_service_not_accepted`.

        Failure modes:

        - `403` - Branded Calling Terms of Service not accepted.
        - `404` - enterprise does not exist or does not belong to your account.

        **Pricing:** This is a billable action. See https://telnyx.com/pricing/numbers
        for current pricing.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return self._post(
            path_template("/enterprises/{enterprise_id}/branded_calling", enterprise_id=enterprise_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnterpriseActivateBrandedCallingResponse,
        )


class AsyncEnterprisesResource(AsyncAPIResource):
    """Manage the legal-entity record that owns your DIRs and phone numbers."""

    @cached_property
    def reputation(self) -> AsyncReputationResource:
        """Phone-number reputation monitoring (spam-score lookup and tracking)."""
        return AsyncReputationResource(self._client)

    @cached_property
    def dir(self) -> AsyncDirResource:
        """
        A Display Identity Record (DIR) is the verified calling identity (display name, logo, call reasons) shown to recipients on outbound calls.
        """
        return AsyncDirResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEnterprisesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnterprisesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnterprisesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/telnyx-python#with_streaming_response
        """
        return AsyncEnterprisesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        billing_address: BillingAddressParam,
        billing_contact: BillingContactParam,
        country_code: str,
        doing_business_as: str,
        fein: str,
        industry: Literal[
            "accounting",
            "finance",
            "billing",
            "collections",
            "business",
            "charity",
            "nonprofit",
            "communications",
            "telecom",
            "customer service",
            "support",
            "delivery",
            "shipping",
            "logistics",
            "education",
            "financial",
            "banking",
            "government",
            "public",
            "healthcare",
            "health",
            "pharmacy",
            "medical",
            "insurance",
            "legal",
            "law",
            "notifications",
            "scheduling",
            "real estate",
            "property",
            "retail",
            "ecommerce",
            "sales",
            "marketing",
            "software",
            "technology",
            "tech",
            "media",
            "surveys",
            "market research",
            "travel",
            "hospitality",
            "hotel",
        ],
        jurisdiction_of_incorporation: str,
        legal_name: str,
        number_of_employees: Literal["1-10", "11-50", "51-200", "201-500", "501-2000", "2001-10000", "10001+"],
        organization_contact: OrganizationContactParam,
        organization_legal_type: Literal["corporation", "llc", "partnership", "nonprofit", "other"],
        organization_physical_address: PhysicalAddressParam,
        organization_type: Literal["commercial", "government", "non_profit"],
        website: str,
        corporate_registration_number: Optional[str] | Omit = omit,
        customer_reference: str | Omit = omit,
        dun_bradstreet_number: Optional[str] | Omit = omit,
        primary_business_domain_sic_code: Optional[str] | Omit = omit,
        professional_license_number: Optional[str] | Omit = omit,
        role_type: Literal["enterprise", "bpo"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnterpriseCreateResponse:
        """
        Create the legal entity (enterprise) that represents your business on the Telnyx
        platform.

        The response carries a server-assigned `id` you use for every subsequent call.
        An enterprise is created once and reused; the API collects all required fields
        up front.

        Common failure modes:

        - `422` - a required field is missing or malformed (the response
          `errors[].source.pointer` names the field).
        - `409` - an enterprise with the same identifying details already exists under
          your account.

        Args:
          country_code: ISO 3166-1 alpha-2 country code. Currently `US` and `CA` are supported.

          fein: US Federal Employer Identification Number (`NN-NNNNNNN`) or Canadian equivalent.

          industry: Industry classification.

          legal_name: Legal name of the enterprise.

          number_of_employees: Approximate headcount range. Used for vetting heuristics; pick the bucket that
              contains your current employee count.

          organization_legal_type:
              Legal-entity form. Pick the form that matches your incorporation documents:

              - `corporation` - C-corp or S-corp.
              - `llc` - limited liability company.
              - `partnership` - general/limited partnership.
              - `nonprofit` - non-profit corporation, charitable trust, or
                501(c)(3)/equivalent.
              - `other` - anything else (sole proprietorships, government bodies, DBAs, etc.).
                You may be asked for additional documents during vetting.

          organization_type:
              Organization category for vetting purposes:

              - `commercial` - for-profit business entities (LLC, corp, partnership, sole
                proprietorship). Most callers fall here.
              - `government` - federal/state/local government bodies.
              - `non_profit` - registered 501(c)(3)/equivalent (incl. educational
                institutions, charities, religious organisations).

          corporate_registration_number: Optional corporate-registration / company-number identifier.

          customer_reference: Optional free-form string the caller can attach for their own bookkeeping.
              Telnyx does not interpret it.

          dun_bradstreet_number: Optional D-U-N-S Number.

          primary_business_domain_sic_code: Optional SIC code for the primary line of business.

          professional_license_number: Optional professional-license number for regulated industries.

          role_type: `enterprise` for an organization registering its own DIRs; `bpo` for a Business
              Process Outsourcer placing calls on behalf of one or more enterprises.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/enterprises",
            body=await async_maybe_transform(
                {
                    "billing_address": billing_address,
                    "billing_contact": billing_contact,
                    "country_code": country_code,
                    "doing_business_as": doing_business_as,
                    "fein": fein,
                    "industry": industry,
                    "jurisdiction_of_incorporation": jurisdiction_of_incorporation,
                    "legal_name": legal_name,
                    "number_of_employees": number_of_employees,
                    "organization_contact": organization_contact,
                    "organization_legal_type": organization_legal_type,
                    "organization_physical_address": organization_physical_address,
                    "organization_type": organization_type,
                    "website": website,
                    "corporate_registration_number": corporate_registration_number,
                    "customer_reference": customer_reference,
                    "dun_bradstreet_number": dun_bradstreet_number,
                    "primary_business_domain_sic_code": primary_business_domain_sic_code,
                    "professional_license_number": professional_license_number,
                    "role_type": role_type,
                },
                enterprise_create_params.EnterpriseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnterpriseCreateResponse,
        )

    async def retrieve(
        self,
        enterprise_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnterpriseRetrieveResponse:
        """Retrieve a single enterprise by id.

        Returns `404` if the id does not exist or
        does not belong to your account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return await self._get(
            path_template("/enterprises/{enterprise_id}", enterprise_id=enterprise_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnterpriseRetrieveResponse,
        )

    async def update(
        self,
        enterprise_id: str,
        *,
        billing_address: BillingAddressParam | Omit = omit,
        billing_contact: BillingContactParam | Omit = omit,
        corporate_registration_number: Optional[str] | Omit = omit,
        customer_reference: str | Omit = omit,
        doing_business_as: str | Omit = omit,
        dun_bradstreet_number: Optional[str] | Omit = omit,
        fein: str | Omit = omit,
        industry: Literal[
            "accounting",
            "finance",
            "billing",
            "collections",
            "business",
            "charity",
            "nonprofit",
            "communications",
            "telecom",
            "customer service",
            "support",
            "delivery",
            "shipping",
            "logistics",
            "education",
            "financial",
            "banking",
            "government",
            "public",
            "healthcare",
            "health",
            "pharmacy",
            "medical",
            "insurance",
            "legal",
            "law",
            "notifications",
            "scheduling",
            "real estate",
            "property",
            "retail",
            "ecommerce",
            "sales",
            "marketing",
            "software",
            "technology",
            "tech",
            "media",
            "surveys",
            "market research",
            "travel",
            "hospitality",
            "hotel",
        ]
        | Omit = omit,
        jurisdiction_of_incorporation: str | Omit = omit,
        legal_name: str | Omit = omit,
        number_of_employees: str | Omit = omit,
        organization_contact: OrganizationContactParam | Omit = omit,
        organization_legal_type: str | Omit = omit,
        organization_physical_address: PhysicalAddressParam | Omit = omit,
        primary_business_domain_sic_code: Optional[str] | Omit = omit,
        professional_license_number: Optional[str] | Omit = omit,
        website: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnterpriseUpdateResponse:
        """Replace the enterprise's mutable fields.

        Only mutable fields may be sent.
        Server-assigned and immutable fields (`id`, `record_type`, `created_at`,
        `updated_at`, status fields, `organization_type`, `country_code`, `role_type`)
        cannot be changed: including any of them in the body is rejected with
        `400 Bad Request` (`Field 'X' is not allowed in this request`).

        Args:
          jurisdiction_of_incorporation: Updated state/province/country of incorporation. Optional on update.

          legal_name: Legal name of the enterprise.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return await self._put(
            path_template("/enterprises/{enterprise_id}", enterprise_id=enterprise_id),
            body=await async_maybe_transform(
                {
                    "billing_address": billing_address,
                    "billing_contact": billing_contact,
                    "corporate_registration_number": corporate_registration_number,
                    "customer_reference": customer_reference,
                    "doing_business_as": doing_business_as,
                    "dun_bradstreet_number": dun_bradstreet_number,
                    "fein": fein,
                    "industry": industry,
                    "jurisdiction_of_incorporation": jurisdiction_of_incorporation,
                    "legal_name": legal_name,
                    "number_of_employees": number_of_employees,
                    "organization_contact": organization_contact,
                    "organization_legal_type": organization_legal_type,
                    "organization_physical_address": organization_physical_address,
                    "primary_business_domain_sic_code": primary_business_domain_sic_code,
                    "professional_license_number": professional_license_number,
                    "website": website,
                },
                enterprise_update_params.EnterpriseUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnterpriseUpdateResponse,
        )

    def list(
        self,
        *,
        filter_legal_name_contains: str | Omit = omit,
        legal_name: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[EnterprisePublic, AsyncDefaultFlatPagination[EnterprisePublic]]:
        """Return the enterprises you own, paginated.

        The default page size is 20; the
        maximum is 250.

        Args:
          filter_legal_name_contains: Case-insensitive partial match on legal name.

          legal_name: Filter by legal name (partial match).

          page_number: 1-based page number. Out-of-range values return an empty page with correct meta.

          page_size: Items per page. Default 10. Maximum 250; values above are clamped to 250.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/enterprises",
            page=AsyncDefaultFlatPagination[EnterprisePublic],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_legal_name_contains": filter_legal_name_contains,
                        "legal_name": legal_name,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    enterprise_list_params.EnterpriseListParams,
                ),
            ),
            model=EnterprisePublic,
        )

    async def delete(
        self,
        enterprise_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Soft-delete an enterprise.

        Failure modes:

        - `400` - the enterprise still has dependent resources in a non-deletable state.
          Remove those first; the response `detail` identifies what is blocking the
          delete.
        - `409` - the enterprise has a dependent resource with an unresolved claim.
          Resolve it before deleting.
        - `404` - the enterprise does not exist or does not belong to your account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/enterprises/{enterprise_id}", enterprise_id=enterprise_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def activate_branded_calling(
        self,
        enterprise_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnterpriseActivateBrandedCallingResponse:
        """
        Branded Calling is a paid product that must be activated on each enterprise.
        Activation is idempotent:

        - First call: marks the enterprise as activated and begins onboarding it with
          the Branded Calling platform asynchronously. Returns `200` with
          `branded_calling_enabled: true`.
        - Re-call after success: no-op, returns the same enterprise body.
        - Re-call after a prior failure: re-queues onboarding, returns `200`.

        Prerequisite: the calling user must have agreed to the Branded Calling Terms of
        Service (`POST /terms_of_service/branded_calling/agree`). Without that, this
        endpoint returns `403 terms_of_service_not_accepted`.

        Failure modes:

        - `403` - Branded Calling Terms of Service not accepted.
        - `404` - enterprise does not exist or does not belong to your account.

        **Pricing:** This is a billable action. See https://telnyx.com/pricing/numbers
        for current pricing.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not enterprise_id:
            raise ValueError(f"Expected a non-empty value for `enterprise_id` but received {enterprise_id!r}")
        return await self._post(
            path_template("/enterprises/{enterprise_id}/branded_calling", enterprise_id=enterprise_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnterpriseActivateBrandedCallingResponse,
        )


class EnterprisesResourceWithRawResponse:
    def __init__(self, enterprises: EnterprisesResource) -> None:
        self._enterprises = enterprises

        self.create = to_raw_response_wrapper(
            enterprises.create,
        )
        self.retrieve = to_raw_response_wrapper(
            enterprises.retrieve,
        )
        self.update = to_raw_response_wrapper(
            enterprises.update,
        )
        self.list = to_raw_response_wrapper(
            enterprises.list,
        )
        self.delete = to_raw_response_wrapper(
            enterprises.delete,
        )
        self.activate_branded_calling = to_raw_response_wrapper(
            enterprises.activate_branded_calling,
        )

    @cached_property
    def reputation(self) -> ReputationResourceWithRawResponse:
        """Phone-number reputation monitoring (spam-score lookup and tracking)."""
        return ReputationResourceWithRawResponse(self._enterprises.reputation)

    @cached_property
    def dir(self) -> DirResourceWithRawResponse:
        """
        A Display Identity Record (DIR) is the verified calling identity (display name, logo, call reasons) shown to recipients on outbound calls.
        """
        return DirResourceWithRawResponse(self._enterprises.dir)


class AsyncEnterprisesResourceWithRawResponse:
    def __init__(self, enterprises: AsyncEnterprisesResource) -> None:
        self._enterprises = enterprises

        self.create = async_to_raw_response_wrapper(
            enterprises.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            enterprises.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            enterprises.update,
        )
        self.list = async_to_raw_response_wrapper(
            enterprises.list,
        )
        self.delete = async_to_raw_response_wrapper(
            enterprises.delete,
        )
        self.activate_branded_calling = async_to_raw_response_wrapper(
            enterprises.activate_branded_calling,
        )

    @cached_property
    def reputation(self) -> AsyncReputationResourceWithRawResponse:
        """Phone-number reputation monitoring (spam-score lookup and tracking)."""
        return AsyncReputationResourceWithRawResponse(self._enterprises.reputation)

    @cached_property
    def dir(self) -> AsyncDirResourceWithRawResponse:
        """
        A Display Identity Record (DIR) is the verified calling identity (display name, logo, call reasons) shown to recipients on outbound calls.
        """
        return AsyncDirResourceWithRawResponse(self._enterprises.dir)


class EnterprisesResourceWithStreamingResponse:
    def __init__(self, enterprises: EnterprisesResource) -> None:
        self._enterprises = enterprises

        self.create = to_streamed_response_wrapper(
            enterprises.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            enterprises.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            enterprises.update,
        )
        self.list = to_streamed_response_wrapper(
            enterprises.list,
        )
        self.delete = to_streamed_response_wrapper(
            enterprises.delete,
        )
        self.activate_branded_calling = to_streamed_response_wrapper(
            enterprises.activate_branded_calling,
        )

    @cached_property
    def reputation(self) -> ReputationResourceWithStreamingResponse:
        """Phone-number reputation monitoring (spam-score lookup and tracking)."""
        return ReputationResourceWithStreamingResponse(self._enterprises.reputation)

    @cached_property
    def dir(self) -> DirResourceWithStreamingResponse:
        """
        A Display Identity Record (DIR) is the verified calling identity (display name, logo, call reasons) shown to recipients on outbound calls.
        """
        return DirResourceWithStreamingResponse(self._enterprises.dir)


class AsyncEnterprisesResourceWithStreamingResponse:
    def __init__(self, enterprises: AsyncEnterprisesResource) -> None:
        self._enterprises = enterprises

        self.create = async_to_streamed_response_wrapper(
            enterprises.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            enterprises.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            enterprises.update,
        )
        self.list = async_to_streamed_response_wrapper(
            enterprises.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            enterprises.delete,
        )
        self.activate_branded_calling = async_to_streamed_response_wrapper(
            enterprises.activate_branded_calling,
        )

    @cached_property
    def reputation(self) -> AsyncReputationResourceWithStreamingResponse:
        """Phone-number reputation monitoring (spam-score lookup and tracking)."""
        return AsyncReputationResourceWithStreamingResponse(self._enterprises.reputation)

    @cached_property
    def dir(self) -> AsyncDirResourceWithStreamingResponse:
        """
        A Display Identity Record (DIR) is the verified calling identity (display name, logo, call reasons) shown to recipients on outbound calls.
        """
        return AsyncDirResourceWithStreamingResponse(self._enterprises.dir)
