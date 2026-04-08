# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import enterprise_list_params, enterprise_create_params, enterprise_update_params
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
from ...types.enterprise_list_response import EnterpriseListResponse
from ...types.enterprise_create_response import EnterpriseCreateResponse
from ...types.enterprise_update_response import EnterpriseUpdateResponse
from ...types.enterprise_retrieve_response import EnterpriseRetrieveResponse

__all__ = ["EnterprisesResource", "AsyncEnterprisesResource"]


class EnterprisesResource(SyncAPIResource):
    """Enterprise management for Branded Calling and Number Reputation services"""

    @cached_property
    def reputation(self) -> ReputationResource:
        """
        Manage Number Reputation enrollment and check frequency settings for an enterprise
        """
        return ReputationResource(self._client)

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
        billing_address: enterprise_create_params.BillingAddress,
        billing_contact: enterprise_create_params.BillingContact,
        country_code: str,
        doing_business_as: str,
        fein: str,
        industry: str,
        legal_name: str,
        number_of_employees: Literal["1-10", "11-50", "51-200", "201-500", "501-2000", "2001-10000", "10001+"],
        organization_contact: enterprise_create_params.OrganizationContact,
        organization_legal_type: Literal["corporation", "llc", "partnership", "nonprofit", "other"],
        organization_physical_address: enterprise_create_params.OrganizationPhysicalAddress,
        organization_type: Literal["commercial", "government", "non_profit"],
        website: str,
        corporate_registration_number: str | Omit = omit,
        customer_reference: str | Omit = omit,
        dun_bradstreet_number: str | Omit = omit,
        primary_business_domain_sic_code: str | Omit = omit,
        professional_license_number: str | Omit = omit,
        role_type: Literal["enterprise", "bpo"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnterpriseCreateResponse:
        """
        Create a new enterprise for Branded Calling / Number Reputation services.

        Registers the enterprise in the Branded Calling / Number Reputation services,
        enabling it to create Display Identity Records (DIRs) or enroll in Number
        Reputation monitoring.

        **Required Fields:** `legal_name`, `doing_business_as`, `organization_type`,
        `country_code`, `website`, `fein`, `industry`, `number_of_employees`,
        `organization_legal_type`, `organization_contact`, `billing_contact`,
        `organization_physical_address`, `billing_address`

        Args:
          country_code: Country code. Currently only 'US' is accepted.

          doing_business_as: Primary business name / DBA name

          fein: Federal Employer Identification Number. Format: XX-XXXXXXX or 9-digit number
              (minimum 9 digits).

          industry: Industry classification. Case-insensitive. Accepted values: accounting, finance,
              billing, collections, business, charity, nonprofit, communications, telecom,
              customer service, support, delivery, shipping, logistics, education, financial,
              banking, government, public, healthcare, health, pharmacy, medical, insurance,
              legal, law, notifications, scheduling, real estate, property, retail, ecommerce,
              sales, marketing, software, technology, tech, media, surveys, market research,
              travel, hospitality, hotel

          legal_name: Legal name of the enterprise

          number_of_employees: Employee count range

          organization_contact: Organization contact information. Note: the response returns this object with
              the phone field as 'phone' (not 'phone_number').

          organization_legal_type: Legal structure type

          organization_type: Type of organization

          website: Enterprise website URL. Accepts any string — no URL format validation enforced.

          corporate_registration_number: Corporate registration number (optional)

          customer_reference: Optional customer reference identifier for your own tracking

          dun_bradstreet_number: D-U-N-S Number (optional)

          primary_business_domain_sic_code: SIC Code (optional)

          professional_license_number: Professional license number (optional)

          role_type: Role type in Branded Calling / Number Reputation services

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
        """
        Retrieve details of a specific enterprise by ID.

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
        billing_address: enterprise_update_params.BillingAddress | Omit = omit,
        billing_contact: enterprise_update_params.BillingContact | Omit = omit,
        corporate_registration_number: str | Omit = omit,
        customer_reference: str | Omit = omit,
        doing_business_as: str | Omit = omit,
        dun_bradstreet_number: str | Omit = omit,
        fein: str | Omit = omit,
        industry: str | Omit = omit,
        legal_name: str | Omit = omit,
        number_of_employees: Literal["1-10", "11-50", "51-200", "201-500", "501-2000", "2001-10000", "10001+"]
        | Omit = omit,
        organization_contact: enterprise_update_params.OrganizationContact | Omit = omit,
        organization_legal_type: Literal["corporation", "llc", "partnership", "nonprofit", "other"] | Omit = omit,
        organization_physical_address: enterprise_update_params.OrganizationPhysicalAddress | Omit = omit,
        primary_business_domain_sic_code: str | Omit = omit,
        professional_license_number: str | Omit = omit,
        website: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnterpriseUpdateResponse:
        """Update enterprise information.

        All fields are optional — only the provided
        fields will be updated.

        Args:
          corporate_registration_number: Corporate registration number

          customer_reference: Customer reference identifier

          doing_business_as: DBA name

          dun_bradstreet_number: D-U-N-S Number

          fein: Federal Employer Identification Number. Format: XX-XXXXXXX or XXXXXXXXX

          industry: Industry classification

          legal_name: Legal name of the enterprise

          number_of_employees: Employee count range

          organization_contact: Organization contact information. Note: the response returns this object with
              the phone field as 'phone' (not 'phone_number').

          organization_legal_type: Legal structure type

          primary_business_domain_sic_code: SIC Code

          professional_license_number: Professional license number

          website: Company website URL

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
        legal_name: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[EnterpriseListResponse]:
        """
        Retrieve a paginated list of enterprises associated with your account.

        Args:
          legal_name: Filter by legal name (partial match)

          page_number: Page number (1-indexed)

          page_size: Number of items per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/enterprises",
            page=SyncDefaultFlatPagination[EnterpriseListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "legal_name": legal_name,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    enterprise_list_params.EnterpriseListParams,
                ),
            ),
            model=EnterpriseListResponse,
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
        """Delete an enterprise and all associated resources.

        This action is irreversible.

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


class AsyncEnterprisesResource(AsyncAPIResource):
    """Enterprise management for Branded Calling and Number Reputation services"""

    @cached_property
    def reputation(self) -> AsyncReputationResource:
        """
        Manage Number Reputation enrollment and check frequency settings for an enterprise
        """
        return AsyncReputationResource(self._client)

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
        billing_address: enterprise_create_params.BillingAddress,
        billing_contact: enterprise_create_params.BillingContact,
        country_code: str,
        doing_business_as: str,
        fein: str,
        industry: str,
        legal_name: str,
        number_of_employees: Literal["1-10", "11-50", "51-200", "201-500", "501-2000", "2001-10000", "10001+"],
        organization_contact: enterprise_create_params.OrganizationContact,
        organization_legal_type: Literal["corporation", "llc", "partnership", "nonprofit", "other"],
        organization_physical_address: enterprise_create_params.OrganizationPhysicalAddress,
        organization_type: Literal["commercial", "government", "non_profit"],
        website: str,
        corporate_registration_number: str | Omit = omit,
        customer_reference: str | Omit = omit,
        dun_bradstreet_number: str | Omit = omit,
        primary_business_domain_sic_code: str | Omit = omit,
        professional_license_number: str | Omit = omit,
        role_type: Literal["enterprise", "bpo"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnterpriseCreateResponse:
        """
        Create a new enterprise for Branded Calling / Number Reputation services.

        Registers the enterprise in the Branded Calling / Number Reputation services,
        enabling it to create Display Identity Records (DIRs) or enroll in Number
        Reputation monitoring.

        **Required Fields:** `legal_name`, `doing_business_as`, `organization_type`,
        `country_code`, `website`, `fein`, `industry`, `number_of_employees`,
        `organization_legal_type`, `organization_contact`, `billing_contact`,
        `organization_physical_address`, `billing_address`

        Args:
          country_code: Country code. Currently only 'US' is accepted.

          doing_business_as: Primary business name / DBA name

          fein: Federal Employer Identification Number. Format: XX-XXXXXXX or 9-digit number
              (minimum 9 digits).

          industry: Industry classification. Case-insensitive. Accepted values: accounting, finance,
              billing, collections, business, charity, nonprofit, communications, telecom,
              customer service, support, delivery, shipping, logistics, education, financial,
              banking, government, public, healthcare, health, pharmacy, medical, insurance,
              legal, law, notifications, scheduling, real estate, property, retail, ecommerce,
              sales, marketing, software, technology, tech, media, surveys, market research,
              travel, hospitality, hotel

          legal_name: Legal name of the enterprise

          number_of_employees: Employee count range

          organization_contact: Organization contact information. Note: the response returns this object with
              the phone field as 'phone' (not 'phone_number').

          organization_legal_type: Legal structure type

          organization_type: Type of organization

          website: Enterprise website URL. Accepts any string — no URL format validation enforced.

          corporate_registration_number: Corporate registration number (optional)

          customer_reference: Optional customer reference identifier for your own tracking

          dun_bradstreet_number: D-U-N-S Number (optional)

          primary_business_domain_sic_code: SIC Code (optional)

          professional_license_number: Professional license number (optional)

          role_type: Role type in Branded Calling / Number Reputation services

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
        """
        Retrieve details of a specific enterprise by ID.

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
        billing_address: enterprise_update_params.BillingAddress | Omit = omit,
        billing_contact: enterprise_update_params.BillingContact | Omit = omit,
        corporate_registration_number: str | Omit = omit,
        customer_reference: str | Omit = omit,
        doing_business_as: str | Omit = omit,
        dun_bradstreet_number: str | Omit = omit,
        fein: str | Omit = omit,
        industry: str | Omit = omit,
        legal_name: str | Omit = omit,
        number_of_employees: Literal["1-10", "11-50", "51-200", "201-500", "501-2000", "2001-10000", "10001+"]
        | Omit = omit,
        organization_contact: enterprise_update_params.OrganizationContact | Omit = omit,
        organization_legal_type: Literal["corporation", "llc", "partnership", "nonprofit", "other"] | Omit = omit,
        organization_physical_address: enterprise_update_params.OrganizationPhysicalAddress | Omit = omit,
        primary_business_domain_sic_code: str | Omit = omit,
        professional_license_number: str | Omit = omit,
        website: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnterpriseUpdateResponse:
        """Update enterprise information.

        All fields are optional — only the provided
        fields will be updated.

        Args:
          corporate_registration_number: Corporate registration number

          customer_reference: Customer reference identifier

          doing_business_as: DBA name

          dun_bradstreet_number: D-U-N-S Number

          fein: Federal Employer Identification Number. Format: XX-XXXXXXX or XXXXXXXXX

          industry: Industry classification

          legal_name: Legal name of the enterprise

          number_of_employees: Employee count range

          organization_contact: Organization contact information. Note: the response returns this object with
              the phone field as 'phone' (not 'phone_number').

          organization_legal_type: Legal structure type

          primary_business_domain_sic_code: SIC Code

          professional_license_number: Professional license number

          website: Company website URL

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
        legal_name: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[EnterpriseListResponse, AsyncDefaultFlatPagination[EnterpriseListResponse]]:
        """
        Retrieve a paginated list of enterprises associated with your account.

        Args:
          legal_name: Filter by legal name (partial match)

          page_number: Page number (1-indexed)

          page_size: Number of items per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/enterprises",
            page=AsyncDefaultFlatPagination[EnterpriseListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "legal_name": legal_name,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    enterprise_list_params.EnterpriseListParams,
                ),
            ),
            model=EnterpriseListResponse,
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
        """Delete an enterprise and all associated resources.

        This action is irreversible.

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

    @cached_property
    def reputation(self) -> ReputationResourceWithRawResponse:
        """
        Manage Number Reputation enrollment and check frequency settings for an enterprise
        """
        return ReputationResourceWithRawResponse(self._enterprises.reputation)


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

    @cached_property
    def reputation(self) -> AsyncReputationResourceWithRawResponse:
        """
        Manage Number Reputation enrollment and check frequency settings for an enterprise
        """
        return AsyncReputationResourceWithRawResponse(self._enterprises.reputation)


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

    @cached_property
    def reputation(self) -> ReputationResourceWithStreamingResponse:
        """
        Manage Number Reputation enrollment and check frequency settings for an enterprise
        """
        return ReputationResourceWithStreamingResponse(self._enterprises.reputation)


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

    @cached_property
    def reputation(self) -> AsyncReputationResourceWithStreamingResponse:
        """
        Manage Number Reputation enrollment and check frequency settings for an enterprise
        """
        return AsyncReputationResourceWithStreamingResponse(self._enterprises.reputation)
