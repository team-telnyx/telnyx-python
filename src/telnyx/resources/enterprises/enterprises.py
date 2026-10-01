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
from .verify_email import (
    VerifyEmailResource,
    AsyncVerifyEmailResource,
    VerifyEmailResourceWithRawResponse,
    AsyncVerifyEmailResourceWithRawResponse,
    VerifyEmailResourceWithStreamingResponse,
    AsyncVerifyEmailResourceWithStreamingResponse,
)
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
from ...types.billing_contact_param import BillingContactParam
from ...types.physical_address_param import PhysicalAddressParam
from ...types.enterprise_public_wrapped import EnterprisePublicWrapped
from ...types.organization_contact_param import OrganizationContactParam

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
    def verify_email(self) -> VerifyEmailResource:
        """Verify ownership of a DIR's authorizer email.

        A short code is emailed and confirmed; the email must be verified before references can be submitted.
        """
        return VerifyEmailResource(self._client)

    @cached_property
    def with_raw_response(self) -> EnterprisesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return EnterprisesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnterprisesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return EnterprisesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        billing_address: PhysicalAddressParam,
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
    ) -> EnterprisePublicWrapped:
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

          doing_business_as: The trade name your business operates under if it is different from your legal
              name, also called a Doing Business As (DBA) name. Leave blank if you only use
              your legal name.

          fein: US Federal Employer Identification Number (`NN-NNNNNNN`) or Canadian equivalent.

          industry: The industry your business operates in. Choose the closest match from the list;
              if your value is not accepted, pick the nearest category.

          jurisdiction_of_incorporation: The state, province, or country where your business was legally incorporated,
              for example Delaware.

          legal_name: Your business's full registered legal name, exactly as it appears on your
              incorporation or tax documents, 3 to 64 characters.

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

          website: Your business's public website address, including https://. Leave blank if your
              business has no website.

          corporate_registration_number: The official number your company received when it was legally registered or
              incorporated (for example from your state or national business registry). It is
              on your certificate of incorporation.

          customer_reference: Your own label for this account. Enter any reference that helps you find it in
              your records. Telnyx does not use it during vetting.

          dun_bradstreet_number: Your optional 9-digit D-U-N-S Number issued by Dun & Bradstreet, a unique
              identifier for your business. Leave blank if you do not have one.

          primary_business_domain_sic_code: The 4-digit Standard Industrial Classification code for your main line of
              business, which tells us what industry you operate in. Look it up in the SIC
              code directory if you are unsure.

          professional_license_number: If your business operates under a professional license (for example legal,
              medical, or financial services), enter the license number issued by the
              licensing authority. Leave blank if it does not apply.

          role_type: `enterprise` for an organization registering its own DIRs (the default, and the
              right choice when the calls display your own brand). `bpo` for a Business
              Process Outsourcer: a call center that places calls on behalf of other
              enterprises and displays their brand. A `bpo` enterprise describes the call
              center itself and cannot own a DIR. Each client the call center calls for gets
              its own `enterprise` in the same account, with the client's DIR under it; that
              DIR is then linked to the `bpo` enterprise through `bpo_authorizations`. Fixed
              at creation.

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
            cast_to=EnterprisePublicWrapped,
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
    ) -> EnterprisePublicWrapped:
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
            cast_to=EnterprisePublicWrapped,
        )

    def update(
        self,
        enterprise_id: str,
        *,
        billing_address: PhysicalAddressParam | Omit = omit,
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
    ) -> EnterprisePublicWrapped:
        """Replace the enterprise's mutable fields.

        Only mutable fields may be sent.
        Server-assigned and immutable fields (`id`, `record_type`, `created_at`,
        `updated_at`, status fields, `organization_type`, `country_code`, `role_type`)
        cannot be changed: including any of them in the body is rejected with
        `400 Bad Request` (`Field 'X' is not allowed in this request`).

        For an approved BPO enterprise (`role_type` `bpo`), changing any identity field
        (legal name, DBA, website, FEIN, industry, number of employees, physical
        address, organization contact, D-U-N-S number, legal type, SIC code, corporate
        registration number, professional license number, or jurisdiction of
        incorporation) resets `bpo_verification_status` to `pending` for re-approval and
        sets every DIR authorization for that BPO to `rejected`. After re-approval, link
        it again with a newly signed LOA (a new `loa_document_id`); resending the old
        one keeps the authorization `rejected`. Re-sending an unchanged value does not
        reset anything.

        If Number Reputation is enabled on the enterprise, `legal_name`,
        `doing_business_as`, `website`, `fein`, `industry`, `number_of_employees`,
        `organization_physical_address`, `organization_contact`, and
        `dun_bradstreet_number` cannot be changed: the request is rejected with `400`.

        Args:
          corporate_registration_number: The official number your company received when it was legally registered or
              incorporated (for example from your state or national business registry). It is
              on your certificate of incorporation.

          customer_reference: Your own label for this account. Enter any reference that helps you find it in
              your records. Telnyx does not use it during vetting.

          doing_business_as: The trade name your business operates under if it is different from your legal
              name, also called a Doing Business As (DBA) name. Leave blank if you only use
              your legal name.

          dun_bradstreet_number: Your optional 9-digit D-U-N-S Number issued by Dun & Bradstreet, a unique
              identifier for your business. Leave blank if you do not have one.

          fein: US Federal Employer Identification Number (`NN-NNNNNNN`) or Canadian equivalent.

          industry: The industry your business operates in. Choose the closest match from the list;
              if your value is not accepted, pick the nearest category.

          jurisdiction_of_incorporation: The state, province, or country where your business was legally incorporated,
              for example Delaware.

          legal_name: Your business's full registered legal name, exactly as it appears on your
              incorporation or tax documents, 3 to 64 characters.

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

          primary_business_domain_sic_code: The 4-digit Standard Industrial Classification code for your main line of
              business, which tells us what industry you operate in. Look it up in the SIC
              code directory if you are unsure.

          professional_license_number: If your business operates under a professional license (for example legal,
              medical, or financial services), enter the license number issued by the
              licensing authority. Leave blank if it does not apply.

          website: Your business's public website address, including https://. Leave blank if your
              business has no website.

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
            cast_to=EnterprisePublicWrapped,
        )

    def list(
        self,
        *,
        filter_legal_name_contains: str | Omit = omit,
        filter_role_type: Literal["enterprise", "bpo"] | Omit = omit,
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

          filter_role_type: Only return enterprises of this type: `bpo` for call-center (BPO) enterprises,
              `enterprise` for normal enterprises. Omit to return both.

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
                        "filter_role_type": filter_role_type,
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

    def branded_calling(
        self,
        enterprise_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnterprisePublicWrapped:
        """Branded Calling must be activated on each enterprise.

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

        - `400` - the account has no available credit. Add funds and retry.
        - `400` - the enterprise is not in the United States. Branded Calling is
          currently available only to US enterprises.
        - `403` - Branded Calling Terms of Service not accepted.
        - `404` - enterprise does not exist or does not belong to your account.

        **Pricing:** Activation itself is free, but the account must have available
        credit. Branded Calling fees are charged per DIR and per branded call. See
        https://telnyx.com/pricing/branded-calling for current pricing.

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
            cast_to=EnterprisePublicWrapped,
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
    def verify_email(self) -> AsyncVerifyEmailResource:
        """Verify ownership of a DIR's authorizer email.

        A short code is emailed and confirmed; the email must be verified before references can be submitted.
        """
        return AsyncVerifyEmailResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEnterprisesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnterprisesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnterprisesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncEnterprisesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        billing_address: PhysicalAddressParam,
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
    ) -> EnterprisePublicWrapped:
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

          doing_business_as: The trade name your business operates under if it is different from your legal
              name, also called a Doing Business As (DBA) name. Leave blank if you only use
              your legal name.

          fein: US Federal Employer Identification Number (`NN-NNNNNNN`) or Canadian equivalent.

          industry: The industry your business operates in. Choose the closest match from the list;
              if your value is not accepted, pick the nearest category.

          jurisdiction_of_incorporation: The state, province, or country where your business was legally incorporated,
              for example Delaware.

          legal_name: Your business's full registered legal name, exactly as it appears on your
              incorporation or tax documents, 3 to 64 characters.

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

          website: Your business's public website address, including https://. Leave blank if your
              business has no website.

          corporate_registration_number: The official number your company received when it was legally registered or
              incorporated (for example from your state or national business registry). It is
              on your certificate of incorporation.

          customer_reference: Your own label for this account. Enter any reference that helps you find it in
              your records. Telnyx does not use it during vetting.

          dun_bradstreet_number: Your optional 9-digit D-U-N-S Number issued by Dun & Bradstreet, a unique
              identifier for your business. Leave blank if you do not have one.

          primary_business_domain_sic_code: The 4-digit Standard Industrial Classification code for your main line of
              business, which tells us what industry you operate in. Look it up in the SIC
              code directory if you are unsure.

          professional_license_number: If your business operates under a professional license (for example legal,
              medical, or financial services), enter the license number issued by the
              licensing authority. Leave blank if it does not apply.

          role_type: `enterprise` for an organization registering its own DIRs (the default, and the
              right choice when the calls display your own brand). `bpo` for a Business
              Process Outsourcer: a call center that places calls on behalf of other
              enterprises and displays their brand. A `bpo` enterprise describes the call
              center itself and cannot own a DIR. Each client the call center calls for gets
              its own `enterprise` in the same account, with the client's DIR under it; that
              DIR is then linked to the `bpo` enterprise through `bpo_authorizations`. Fixed
              at creation.

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
            cast_to=EnterprisePublicWrapped,
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
    ) -> EnterprisePublicWrapped:
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
            cast_to=EnterprisePublicWrapped,
        )

    async def update(
        self,
        enterprise_id: str,
        *,
        billing_address: PhysicalAddressParam | Omit = omit,
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
    ) -> EnterprisePublicWrapped:
        """Replace the enterprise's mutable fields.

        Only mutable fields may be sent.
        Server-assigned and immutable fields (`id`, `record_type`, `created_at`,
        `updated_at`, status fields, `organization_type`, `country_code`, `role_type`)
        cannot be changed: including any of them in the body is rejected with
        `400 Bad Request` (`Field 'X' is not allowed in this request`).

        For an approved BPO enterprise (`role_type` `bpo`), changing any identity field
        (legal name, DBA, website, FEIN, industry, number of employees, physical
        address, organization contact, D-U-N-S number, legal type, SIC code, corporate
        registration number, professional license number, or jurisdiction of
        incorporation) resets `bpo_verification_status` to `pending` for re-approval and
        sets every DIR authorization for that BPO to `rejected`. After re-approval, link
        it again with a newly signed LOA (a new `loa_document_id`); resending the old
        one keeps the authorization `rejected`. Re-sending an unchanged value does not
        reset anything.

        If Number Reputation is enabled on the enterprise, `legal_name`,
        `doing_business_as`, `website`, `fein`, `industry`, `number_of_employees`,
        `organization_physical_address`, `organization_contact`, and
        `dun_bradstreet_number` cannot be changed: the request is rejected with `400`.

        Args:
          corporate_registration_number: The official number your company received when it was legally registered or
              incorporated (for example from your state or national business registry). It is
              on your certificate of incorporation.

          customer_reference: Your own label for this account. Enter any reference that helps you find it in
              your records. Telnyx does not use it during vetting.

          doing_business_as: The trade name your business operates under if it is different from your legal
              name, also called a Doing Business As (DBA) name. Leave blank if you only use
              your legal name.

          dun_bradstreet_number: Your optional 9-digit D-U-N-S Number issued by Dun & Bradstreet, a unique
              identifier for your business. Leave blank if you do not have one.

          fein: US Federal Employer Identification Number (`NN-NNNNNNN`) or Canadian equivalent.

          industry: The industry your business operates in. Choose the closest match from the list;
              if your value is not accepted, pick the nearest category.

          jurisdiction_of_incorporation: The state, province, or country where your business was legally incorporated,
              for example Delaware.

          legal_name: Your business's full registered legal name, exactly as it appears on your
              incorporation or tax documents, 3 to 64 characters.

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

          primary_business_domain_sic_code: The 4-digit Standard Industrial Classification code for your main line of
              business, which tells us what industry you operate in. Look it up in the SIC
              code directory if you are unsure.

          professional_license_number: If your business operates under a professional license (for example legal,
              medical, or financial services), enter the license number issued by the
              licensing authority. Leave blank if it does not apply.

          website: Your business's public website address, including https://. Leave blank if your
              business has no website.

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
            cast_to=EnterprisePublicWrapped,
        )

    def list(
        self,
        *,
        filter_legal_name_contains: str | Omit = omit,
        filter_role_type: Literal["enterprise", "bpo"] | Omit = omit,
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

          filter_role_type: Only return enterprises of this type: `bpo` for call-center (BPO) enterprises,
              `enterprise` for normal enterprises. Omit to return both.

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
                        "filter_role_type": filter_role_type,
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

    async def branded_calling(
        self,
        enterprise_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnterprisePublicWrapped:
        """Branded Calling must be activated on each enterprise.

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

        - `400` - the account has no available credit. Add funds and retry.
        - `400` - the enterprise is not in the United States. Branded Calling is
          currently available only to US enterprises.
        - `403` - Branded Calling Terms of Service not accepted.
        - `404` - enterprise does not exist or does not belong to your account.

        **Pricing:** Activation itself is free, but the account must have available
        credit. Branded Calling fees are charged per DIR and per branded call. See
        https://telnyx.com/pricing/branded-calling for current pricing.

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
            cast_to=EnterprisePublicWrapped,
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
        self.branded_calling = to_raw_response_wrapper(
            enterprises.branded_calling,
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

    @cached_property
    def verify_email(self) -> VerifyEmailResourceWithRawResponse:
        """Verify ownership of a DIR's authorizer email.

        A short code is emailed and confirmed; the email must be verified before references can be submitted.
        """
        return VerifyEmailResourceWithRawResponse(self._enterprises.verify_email)


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
        self.branded_calling = async_to_raw_response_wrapper(
            enterprises.branded_calling,
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

    @cached_property
    def verify_email(self) -> AsyncVerifyEmailResourceWithRawResponse:
        """Verify ownership of a DIR's authorizer email.

        A short code is emailed and confirmed; the email must be verified before references can be submitted.
        """
        return AsyncVerifyEmailResourceWithRawResponse(self._enterprises.verify_email)


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
        self.branded_calling = to_streamed_response_wrapper(
            enterprises.branded_calling,
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

    @cached_property
    def verify_email(self) -> VerifyEmailResourceWithStreamingResponse:
        """Verify ownership of a DIR's authorizer email.

        A short code is emailed and confirmed; the email must be verified before references can be submitted.
        """
        return VerifyEmailResourceWithStreamingResponse(self._enterprises.verify_email)


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
        self.branded_calling = async_to_streamed_response_wrapper(
            enterprises.branded_calling,
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

    @cached_property
    def verify_email(self) -> AsyncVerifyEmailResourceWithStreamingResponse:
        """Verify ownership of a DIR's authorizer email.

        A short code is emailed and confirmed; the email must be verified before references can be submitted.
        """
        return AsyncVerifyEmailResourceWithStreamingResponse(self._enterprises.verify_email)
