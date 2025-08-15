# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable

import httpx

from ...types import (
    porting_order_list_params,
    porting_order_create_params,
    porting_order_update_params,
    porting_order_retrieve_params,
    porting_order_retrieve_loa_template_params,
    porting_order_retrieve_requirements_params,
)
from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from .comments import (
    CommentsResource,
    AsyncCommentsResource,
    CommentsResourceWithRawResponse,
    AsyncCommentsResourceWithRawResponse,
    CommentsResourceWithStreamingResponse,
    AsyncCommentsResourceWithStreamingResponse,
)
from ..._compat import cached_property
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
from ..._base_client import make_request_options
from .activation_jobs import (
    ActivationJobsResource,
    AsyncActivationJobsResource,
    ActivationJobsResourceWithRawResponse,
    AsyncActivationJobsResourceWithRawResponse,
    ActivationJobsResourceWithStreamingResponse,
    AsyncActivationJobsResourceWithStreamingResponse,
)
from .verification_codes import (
    VerificationCodesResource,
    AsyncVerificationCodesResource,
    VerificationCodesResourceWithRawResponse,
    AsyncVerificationCodesResourceWithRawResponse,
    VerificationCodesResourceWithStreamingResponse,
    AsyncVerificationCodesResourceWithStreamingResponse,
)
from .action_requirements import (
    ActionRequirementsResource,
    AsyncActionRequirementsResource,
    ActionRequirementsResourceWithRawResponse,
    AsyncActionRequirementsResourceWithRawResponse,
    ActionRequirementsResourceWithStreamingResponse,
    AsyncActionRequirementsResourceWithStreamingResponse,
)
from .phone_number_blocks import (
    PhoneNumberBlocksResource,
    AsyncPhoneNumberBlocksResource,
    PhoneNumberBlocksResourceWithRawResponse,
    AsyncPhoneNumberBlocksResourceWithRawResponse,
    PhoneNumberBlocksResourceWithStreamingResponse,
    AsyncPhoneNumberBlocksResourceWithStreamingResponse,
)
from .additional_documents import (
    AdditionalDocumentsResource,
    AsyncAdditionalDocumentsResource,
    AdditionalDocumentsResourceWithRawResponse,
    AsyncAdditionalDocumentsResourceWithRawResponse,
    AdditionalDocumentsResourceWithStreamingResponse,
    AsyncAdditionalDocumentsResourceWithStreamingResponse,
)
from .phone_number_extensions import (
    PhoneNumberExtensionsResource,
    AsyncPhoneNumberExtensionsResource,
    PhoneNumberExtensionsResourceWithRawResponse,
    AsyncPhoneNumberExtensionsResourceWithRawResponse,
    PhoneNumberExtensionsResourceWithStreamingResponse,
    AsyncPhoneNumberExtensionsResourceWithStreamingResponse,
)
from .associated_phone_numbers import (
    AssociatedPhoneNumbersResource,
    AsyncAssociatedPhoneNumbersResource,
    AssociatedPhoneNumbersResourceWithRawResponse,
    AsyncAssociatedPhoneNumbersResourceWithRawResponse,
    AssociatedPhoneNumbersResourceWithStreamingResponse,
    AsyncAssociatedPhoneNumbersResourceWithStreamingResponse,
)
from .phone_number_configurations import (
    PhoneNumberConfigurationsResource,
    AsyncPhoneNumberConfigurationsResource,
    PhoneNumberConfigurationsResourceWithRawResponse,
    AsyncPhoneNumberConfigurationsResourceWithRawResponse,
    PhoneNumberConfigurationsResourceWithStreamingResponse,
    AsyncPhoneNumberConfigurationsResourceWithStreamingResponse,
)
from ...types.porting_order_misc_param import PortingOrderMiscParam
from ...types.porting_order_list_response import PortingOrderListResponse
from ...types.porting_order_end_user_param import PortingOrderEndUserParam
from ...types.porting_order_create_response import PortingOrderCreateResponse
from ...types.porting_order_documents_param import PortingOrderDocumentsParam
from ...types.porting_order_update_response import PortingOrderUpdateResponse
from ...types.porting_order_retrieve_response import PortingOrderRetrieveResponse
from ...types.porting_order_user_feedback_param import PortingOrderUserFeedbackParam
from ...types.porting_order_retrieve_sub_request_response import PortingOrderRetrieveSubRequestResponse
from ...types.porting_order_retrieve_requirements_response import PortingOrderRetrieveRequirementsResponse
from ...types.porting_order_phone_number_configuration_param import PortingOrderPhoneNumberConfigurationParam
from ...types.porting_order_retrieve_exception_types_response import PortingOrderRetrieveExceptionTypesResponse
from ...types.porting_order_retrieve_allowed_foc_windows_response import PortingOrderRetrieveAllowedFocWindowsResponse

__all__ = ["PortingOrdersResource", "AsyncPortingOrdersResource"]


class PortingOrdersResource(SyncAPIResource):
    @cached_property
    def phone_number_configurations(self) -> PhoneNumberConfigurationsResource:
        return PhoneNumberConfigurationsResource(self._client)

    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def activation_jobs(self) -> ActivationJobsResource:
        return ActivationJobsResource(self._client)

    @cached_property
    def additional_documents(self) -> AdditionalDocumentsResource:
        return AdditionalDocumentsResource(self._client)

    @cached_property
    def comments(self) -> CommentsResource:
        return CommentsResource(self._client)

    @cached_property
    def verification_codes(self) -> VerificationCodesResource:
        return VerificationCodesResource(self._client)

    @cached_property
    def action_requirements(self) -> ActionRequirementsResource:
        return ActionRequirementsResource(self._client)

    @cached_property
    def associated_phone_numbers(self) -> AssociatedPhoneNumbersResource:
        return AssociatedPhoneNumbersResource(self._client)

    @cached_property
    def phone_number_blocks(self) -> PhoneNumberBlocksResource:
        return PhoneNumberBlocksResource(self._client)

    @cached_property
    def phone_number_extensions(self) -> PhoneNumberExtensionsResource:
        return PhoneNumberExtensionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PortingOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return PortingOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PortingOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return PortingOrdersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        phone_numbers: List[str],
        customer_reference: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortingOrderCreateResponse:
        """
        Creates a new porting order object.

        Args:
          phone_numbers: The list of +E.164 formatted phone numbers

          customer_reference: A customer-specified reference number for customer bookkeeping purposes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/porting_orders",
            body=maybe_transform(
                {
                    "phone_numbers": phone_numbers,
                    "customer_reference": customer_reference,
                },
                porting_order_create_params.PortingOrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortingOrderCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        include_phone_numbers: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortingOrderRetrieveResponse:
        """
        Retrieves the details of an existing porting order.

        Args:
          include_phone_numbers: Include the first 50 phone number objects in the results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/porting_orders/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_phone_numbers": include_phone_numbers},
                    porting_order_retrieve_params.PortingOrderRetrieveParams,
                ),
            ),
            cast_to=PortingOrderRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        activation_settings: porting_order_update_params.ActivationSettings | NotGiven = NOT_GIVEN,
        customer_reference: str | NotGiven = NOT_GIVEN,
        documents: PortingOrderDocumentsParam | NotGiven = NOT_GIVEN,
        end_user: PortingOrderEndUserParam | NotGiven = NOT_GIVEN,
        messaging: porting_order_update_params.Messaging | NotGiven = NOT_GIVEN,
        misc: PortingOrderMiscParam | NotGiven = NOT_GIVEN,
        phone_number_configuration: PortingOrderPhoneNumberConfigurationParam | NotGiven = NOT_GIVEN,
        requirement_group_id: str | NotGiven = NOT_GIVEN,
        requirements: Iterable[porting_order_update_params.Requirement] | NotGiven = NOT_GIVEN,
        user_feedback: PortingOrderUserFeedbackParam | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortingOrderUpdateResponse:
        """
        Edits the details of an existing porting order.

        Any or all of a porting orders attributes may be included in the resource object
        included in a PATCH request.

        If a request does not include all of the attributes for a resource, the system
        will interpret the missing attributes as if they were included with their
        current values. To explicitly set something to null, it must be included in the
        request with a null value.

        Args:
          documents: Can be specified directly or via the `requirement_group_id` parameter.

          requirement_group_id: If present, we will read the current values from the specified Requirement Group
              into the Documents and Requirements for this Porting Order. Note that any future
              changes in the Requirement Group would have no impact on this Porting Order. We
              will return an error if a specified Requirement Group conflicts with documents
              or requirements in the same request.

          requirements: List of requirements for porting numbers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/porting_orders/{id}",
            body=maybe_transform(
                {
                    "activation_settings": activation_settings,
                    "customer_reference": customer_reference,
                    "documents": documents,
                    "end_user": end_user,
                    "messaging": messaging,
                    "misc": misc,
                    "phone_number_configuration": phone_number_configuration,
                    "requirement_group_id": requirement_group_id,
                    "requirements": requirements,
                    "user_feedback": user_feedback,
                    "webhook_url": webhook_url,
                },
                porting_order_update_params.PortingOrderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortingOrderUpdateResponse,
        )

    def list(
        self,
        *,
        filter: porting_order_list_params.Filter | NotGiven = NOT_GIVEN,
        include_phone_numbers: bool | NotGiven = NOT_GIVEN,
        page: porting_order_list_params.Page | NotGiven = NOT_GIVEN,
        sort: porting_order_list_params.Sort | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortingOrderListResponse:
        """
        Returns a list of your porting order.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[customer_reference], filter[parent_support_key],
              filter[phone_numbers.country_code], filter[phone_numbers.carrier_name],
              filter[misc.type], filter[end_user.admin.entity_name],
              filter[end_user.admin.auth_person_name],
              filter[activation_settings.fast_port_eligible],
              filter[activation_settings.foc_datetime_requested][gt],
              filter[activation_settings.foc_datetime_requested][lt],
              filter[phone_numbers.phone_number][contains]

          include_phone_numbers: Include the first 50 phone number objects in the results

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          sort: Consolidated sort parameter (deepObject style). Originally: sort[value]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/porting_orders",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "include_phone_numbers": include_phone_numbers,
                        "page": page,
                        "sort": sort,
                    },
                    porting_order_list_params.PortingOrderListParams,
                ),
            ),
            cast_to=PortingOrderListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Deletes an existing porting order.

        This operation is restrict to porting orders
        in draft state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/porting_orders/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve_allowed_foc_windows(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortingOrderRetrieveAllowedFocWindowsResponse:
        """
        Returns a list of allowed FOC dates for a porting order.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/porting_orders/{id}/allowed_foc_windows",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortingOrderRetrieveAllowedFocWindowsResponse,
        )

    def retrieve_exception_types(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortingOrderRetrieveExceptionTypesResponse:
        """Returns a list of all possible exception types for a porting order."""
        return self._get(
            "/porting_orders/exception_types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortingOrderRetrieveExceptionTypesResponse,
        )

    def retrieve_loa_template(
        self,
        id: str,
        *,
        loa_configuration_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Download a porting order loa template

        Args:
          loa_configuration_id: The identifier of the LOA configuration to use for the template. If not
              provided, the default LOA configuration will be used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/pdf", **(extra_headers or {})}
        return self._get(
            f"/porting_orders/{id}/loa_template",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"loa_configuration_id": loa_configuration_id},
                    porting_order_retrieve_loa_template_params.PortingOrderRetrieveLoaTemplateParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def retrieve_requirements(
        self,
        id: str,
        *,
        page: porting_order_retrieve_requirements_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortingOrderRetrieveRequirementsResponse:
        """
        Returns a list of all requirements based on country/number type for this porting
        order.

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/porting_orders/{id}/requirements",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"page": page}, porting_order_retrieve_requirements_params.PortingOrderRetrieveRequirementsParams
                ),
            ),
            cast_to=PortingOrderRetrieveRequirementsResponse,
        )

    def retrieve_sub_request(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortingOrderRetrieveSubRequestResponse:
        """
        Retrieve the associated V1 sub_request_id and port_request_id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/porting_orders/{id}/sub_request",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortingOrderRetrieveSubRequestResponse,
        )


class AsyncPortingOrdersResource(AsyncAPIResource):
    @cached_property
    def phone_number_configurations(self) -> AsyncPhoneNumberConfigurationsResource:
        return AsyncPhoneNumberConfigurationsResource(self._client)

    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def activation_jobs(self) -> AsyncActivationJobsResource:
        return AsyncActivationJobsResource(self._client)

    @cached_property
    def additional_documents(self) -> AsyncAdditionalDocumentsResource:
        return AsyncAdditionalDocumentsResource(self._client)

    @cached_property
    def comments(self) -> AsyncCommentsResource:
        return AsyncCommentsResource(self._client)

    @cached_property
    def verification_codes(self) -> AsyncVerificationCodesResource:
        return AsyncVerificationCodesResource(self._client)

    @cached_property
    def action_requirements(self) -> AsyncActionRequirementsResource:
        return AsyncActionRequirementsResource(self._client)

    @cached_property
    def associated_phone_numbers(self) -> AsyncAssociatedPhoneNumbersResource:
        return AsyncAssociatedPhoneNumbersResource(self._client)

    @cached_property
    def phone_number_blocks(self) -> AsyncPhoneNumberBlocksResource:
        return AsyncPhoneNumberBlocksResource(self._client)

    @cached_property
    def phone_number_extensions(self) -> AsyncPhoneNumberExtensionsResource:
        return AsyncPhoneNumberExtensionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPortingOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPortingOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPortingOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncPortingOrdersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        phone_numbers: List[str],
        customer_reference: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortingOrderCreateResponse:
        """
        Creates a new porting order object.

        Args:
          phone_numbers: The list of +E.164 formatted phone numbers

          customer_reference: A customer-specified reference number for customer bookkeeping purposes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/porting_orders",
            body=await async_maybe_transform(
                {
                    "phone_numbers": phone_numbers,
                    "customer_reference": customer_reference,
                },
                porting_order_create_params.PortingOrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortingOrderCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        include_phone_numbers: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortingOrderRetrieveResponse:
        """
        Retrieves the details of an existing porting order.

        Args:
          include_phone_numbers: Include the first 50 phone number objects in the results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/porting_orders/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_phone_numbers": include_phone_numbers},
                    porting_order_retrieve_params.PortingOrderRetrieveParams,
                ),
            ),
            cast_to=PortingOrderRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        activation_settings: porting_order_update_params.ActivationSettings | NotGiven = NOT_GIVEN,
        customer_reference: str | NotGiven = NOT_GIVEN,
        documents: PortingOrderDocumentsParam | NotGiven = NOT_GIVEN,
        end_user: PortingOrderEndUserParam | NotGiven = NOT_GIVEN,
        messaging: porting_order_update_params.Messaging | NotGiven = NOT_GIVEN,
        misc: PortingOrderMiscParam | NotGiven = NOT_GIVEN,
        phone_number_configuration: PortingOrderPhoneNumberConfigurationParam | NotGiven = NOT_GIVEN,
        requirement_group_id: str | NotGiven = NOT_GIVEN,
        requirements: Iterable[porting_order_update_params.Requirement] | NotGiven = NOT_GIVEN,
        user_feedback: PortingOrderUserFeedbackParam | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortingOrderUpdateResponse:
        """
        Edits the details of an existing porting order.

        Any or all of a porting orders attributes may be included in the resource object
        included in a PATCH request.

        If a request does not include all of the attributes for a resource, the system
        will interpret the missing attributes as if they were included with their
        current values. To explicitly set something to null, it must be included in the
        request with a null value.

        Args:
          documents: Can be specified directly or via the `requirement_group_id` parameter.

          requirement_group_id: If present, we will read the current values from the specified Requirement Group
              into the Documents and Requirements for this Porting Order. Note that any future
              changes in the Requirement Group would have no impact on this Porting Order. We
              will return an error if a specified Requirement Group conflicts with documents
              or requirements in the same request.

          requirements: List of requirements for porting numbers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/porting_orders/{id}",
            body=await async_maybe_transform(
                {
                    "activation_settings": activation_settings,
                    "customer_reference": customer_reference,
                    "documents": documents,
                    "end_user": end_user,
                    "messaging": messaging,
                    "misc": misc,
                    "phone_number_configuration": phone_number_configuration,
                    "requirement_group_id": requirement_group_id,
                    "requirements": requirements,
                    "user_feedback": user_feedback,
                    "webhook_url": webhook_url,
                },
                porting_order_update_params.PortingOrderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortingOrderUpdateResponse,
        )

    async def list(
        self,
        *,
        filter: porting_order_list_params.Filter | NotGiven = NOT_GIVEN,
        include_phone_numbers: bool | NotGiven = NOT_GIVEN,
        page: porting_order_list_params.Page | NotGiven = NOT_GIVEN,
        sort: porting_order_list_params.Sort | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortingOrderListResponse:
        """
        Returns a list of your porting order.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[customer_reference], filter[parent_support_key],
              filter[phone_numbers.country_code], filter[phone_numbers.carrier_name],
              filter[misc.type], filter[end_user.admin.entity_name],
              filter[end_user.admin.auth_person_name],
              filter[activation_settings.fast_port_eligible],
              filter[activation_settings.foc_datetime_requested][gt],
              filter[activation_settings.foc_datetime_requested][lt],
              filter[phone_numbers.phone_number][contains]

          include_phone_numbers: Include the first 50 phone number objects in the results

          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          sort: Consolidated sort parameter (deepObject style). Originally: sort[value]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/porting_orders",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "include_phone_numbers": include_phone_numbers,
                        "page": page,
                        "sort": sort,
                    },
                    porting_order_list_params.PortingOrderListParams,
                ),
            ),
            cast_to=PortingOrderListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Deletes an existing porting order.

        This operation is restrict to porting orders
        in draft state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/porting_orders/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve_allowed_foc_windows(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortingOrderRetrieveAllowedFocWindowsResponse:
        """
        Returns a list of allowed FOC dates for a porting order.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/porting_orders/{id}/allowed_foc_windows",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortingOrderRetrieveAllowedFocWindowsResponse,
        )

    async def retrieve_exception_types(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortingOrderRetrieveExceptionTypesResponse:
        """Returns a list of all possible exception types for a porting order."""
        return await self._get(
            "/porting_orders/exception_types",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortingOrderRetrieveExceptionTypesResponse,
        )

    async def retrieve_loa_template(
        self,
        id: str,
        *,
        loa_configuration_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Download a porting order loa template

        Args:
          loa_configuration_id: The identifier of the LOA configuration to use for the template. If not
              provided, the default LOA configuration will be used.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/pdf", **(extra_headers or {})}
        return await self._get(
            f"/porting_orders/{id}/loa_template",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"loa_configuration_id": loa_configuration_id},
                    porting_order_retrieve_loa_template_params.PortingOrderRetrieveLoaTemplateParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def retrieve_requirements(
        self,
        id: str,
        *,
        page: porting_order_retrieve_requirements_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortingOrderRetrieveRequirementsResponse:
        """
        Returns a list of all requirements based on country/number type for this porting
        order.

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/porting_orders/{id}/requirements",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"page": page}, porting_order_retrieve_requirements_params.PortingOrderRetrieveRequirementsParams
                ),
            ),
            cast_to=PortingOrderRetrieveRequirementsResponse,
        )

    async def retrieve_sub_request(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortingOrderRetrieveSubRequestResponse:
        """
        Retrieve the associated V1 sub_request_id and port_request_id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/porting_orders/{id}/sub_request",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortingOrderRetrieveSubRequestResponse,
        )


class PortingOrdersResourceWithRawResponse:
    def __init__(self, porting_orders: PortingOrdersResource) -> None:
        self._porting_orders = porting_orders

        self.create = to_raw_response_wrapper(
            porting_orders.create,
        )
        self.retrieve = to_raw_response_wrapper(
            porting_orders.retrieve,
        )
        self.update = to_raw_response_wrapper(
            porting_orders.update,
        )
        self.list = to_raw_response_wrapper(
            porting_orders.list,
        )
        self.delete = to_raw_response_wrapper(
            porting_orders.delete,
        )
        self.retrieve_allowed_foc_windows = to_raw_response_wrapper(
            porting_orders.retrieve_allowed_foc_windows,
        )
        self.retrieve_exception_types = to_raw_response_wrapper(
            porting_orders.retrieve_exception_types,
        )
        self.retrieve_loa_template = to_custom_raw_response_wrapper(
            porting_orders.retrieve_loa_template,
            BinaryAPIResponse,
        )
        self.retrieve_requirements = to_raw_response_wrapper(
            porting_orders.retrieve_requirements,
        )
        self.retrieve_sub_request = to_raw_response_wrapper(
            porting_orders.retrieve_sub_request,
        )

    @cached_property
    def phone_number_configurations(self) -> PhoneNumberConfigurationsResourceWithRawResponse:
        return PhoneNumberConfigurationsResourceWithRawResponse(self._porting_orders.phone_number_configurations)

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._porting_orders.actions)

    @cached_property
    def activation_jobs(self) -> ActivationJobsResourceWithRawResponse:
        return ActivationJobsResourceWithRawResponse(self._porting_orders.activation_jobs)

    @cached_property
    def additional_documents(self) -> AdditionalDocumentsResourceWithRawResponse:
        return AdditionalDocumentsResourceWithRawResponse(self._porting_orders.additional_documents)

    @cached_property
    def comments(self) -> CommentsResourceWithRawResponse:
        return CommentsResourceWithRawResponse(self._porting_orders.comments)

    @cached_property
    def verification_codes(self) -> VerificationCodesResourceWithRawResponse:
        return VerificationCodesResourceWithRawResponse(self._porting_orders.verification_codes)

    @cached_property
    def action_requirements(self) -> ActionRequirementsResourceWithRawResponse:
        return ActionRequirementsResourceWithRawResponse(self._porting_orders.action_requirements)

    @cached_property
    def associated_phone_numbers(self) -> AssociatedPhoneNumbersResourceWithRawResponse:
        return AssociatedPhoneNumbersResourceWithRawResponse(self._porting_orders.associated_phone_numbers)

    @cached_property
    def phone_number_blocks(self) -> PhoneNumberBlocksResourceWithRawResponse:
        return PhoneNumberBlocksResourceWithRawResponse(self._porting_orders.phone_number_blocks)

    @cached_property
    def phone_number_extensions(self) -> PhoneNumberExtensionsResourceWithRawResponse:
        return PhoneNumberExtensionsResourceWithRawResponse(self._porting_orders.phone_number_extensions)


class AsyncPortingOrdersResourceWithRawResponse:
    def __init__(self, porting_orders: AsyncPortingOrdersResource) -> None:
        self._porting_orders = porting_orders

        self.create = async_to_raw_response_wrapper(
            porting_orders.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            porting_orders.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            porting_orders.update,
        )
        self.list = async_to_raw_response_wrapper(
            porting_orders.list,
        )
        self.delete = async_to_raw_response_wrapper(
            porting_orders.delete,
        )
        self.retrieve_allowed_foc_windows = async_to_raw_response_wrapper(
            porting_orders.retrieve_allowed_foc_windows,
        )
        self.retrieve_exception_types = async_to_raw_response_wrapper(
            porting_orders.retrieve_exception_types,
        )
        self.retrieve_loa_template = async_to_custom_raw_response_wrapper(
            porting_orders.retrieve_loa_template,
            AsyncBinaryAPIResponse,
        )
        self.retrieve_requirements = async_to_raw_response_wrapper(
            porting_orders.retrieve_requirements,
        )
        self.retrieve_sub_request = async_to_raw_response_wrapper(
            porting_orders.retrieve_sub_request,
        )

    @cached_property
    def phone_number_configurations(self) -> AsyncPhoneNumberConfigurationsResourceWithRawResponse:
        return AsyncPhoneNumberConfigurationsResourceWithRawResponse(self._porting_orders.phone_number_configurations)

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._porting_orders.actions)

    @cached_property
    def activation_jobs(self) -> AsyncActivationJobsResourceWithRawResponse:
        return AsyncActivationJobsResourceWithRawResponse(self._porting_orders.activation_jobs)

    @cached_property
    def additional_documents(self) -> AsyncAdditionalDocumentsResourceWithRawResponse:
        return AsyncAdditionalDocumentsResourceWithRawResponse(self._porting_orders.additional_documents)

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithRawResponse:
        return AsyncCommentsResourceWithRawResponse(self._porting_orders.comments)

    @cached_property
    def verification_codes(self) -> AsyncVerificationCodesResourceWithRawResponse:
        return AsyncVerificationCodesResourceWithRawResponse(self._porting_orders.verification_codes)

    @cached_property
    def action_requirements(self) -> AsyncActionRequirementsResourceWithRawResponse:
        return AsyncActionRequirementsResourceWithRawResponse(self._porting_orders.action_requirements)

    @cached_property
    def associated_phone_numbers(self) -> AsyncAssociatedPhoneNumbersResourceWithRawResponse:
        return AsyncAssociatedPhoneNumbersResourceWithRawResponse(self._porting_orders.associated_phone_numbers)

    @cached_property
    def phone_number_blocks(self) -> AsyncPhoneNumberBlocksResourceWithRawResponse:
        return AsyncPhoneNumberBlocksResourceWithRawResponse(self._porting_orders.phone_number_blocks)

    @cached_property
    def phone_number_extensions(self) -> AsyncPhoneNumberExtensionsResourceWithRawResponse:
        return AsyncPhoneNumberExtensionsResourceWithRawResponse(self._porting_orders.phone_number_extensions)


class PortingOrdersResourceWithStreamingResponse:
    def __init__(self, porting_orders: PortingOrdersResource) -> None:
        self._porting_orders = porting_orders

        self.create = to_streamed_response_wrapper(
            porting_orders.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            porting_orders.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            porting_orders.update,
        )
        self.list = to_streamed_response_wrapper(
            porting_orders.list,
        )
        self.delete = to_streamed_response_wrapper(
            porting_orders.delete,
        )
        self.retrieve_allowed_foc_windows = to_streamed_response_wrapper(
            porting_orders.retrieve_allowed_foc_windows,
        )
        self.retrieve_exception_types = to_streamed_response_wrapper(
            porting_orders.retrieve_exception_types,
        )
        self.retrieve_loa_template = to_custom_streamed_response_wrapper(
            porting_orders.retrieve_loa_template,
            StreamedBinaryAPIResponse,
        )
        self.retrieve_requirements = to_streamed_response_wrapper(
            porting_orders.retrieve_requirements,
        )
        self.retrieve_sub_request = to_streamed_response_wrapper(
            porting_orders.retrieve_sub_request,
        )

    @cached_property
    def phone_number_configurations(self) -> PhoneNumberConfigurationsResourceWithStreamingResponse:
        return PhoneNumberConfigurationsResourceWithStreamingResponse(self._porting_orders.phone_number_configurations)

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._porting_orders.actions)

    @cached_property
    def activation_jobs(self) -> ActivationJobsResourceWithStreamingResponse:
        return ActivationJobsResourceWithStreamingResponse(self._porting_orders.activation_jobs)

    @cached_property
    def additional_documents(self) -> AdditionalDocumentsResourceWithStreamingResponse:
        return AdditionalDocumentsResourceWithStreamingResponse(self._porting_orders.additional_documents)

    @cached_property
    def comments(self) -> CommentsResourceWithStreamingResponse:
        return CommentsResourceWithStreamingResponse(self._porting_orders.comments)

    @cached_property
    def verification_codes(self) -> VerificationCodesResourceWithStreamingResponse:
        return VerificationCodesResourceWithStreamingResponse(self._porting_orders.verification_codes)

    @cached_property
    def action_requirements(self) -> ActionRequirementsResourceWithStreamingResponse:
        return ActionRequirementsResourceWithStreamingResponse(self._porting_orders.action_requirements)

    @cached_property
    def associated_phone_numbers(self) -> AssociatedPhoneNumbersResourceWithStreamingResponse:
        return AssociatedPhoneNumbersResourceWithStreamingResponse(self._porting_orders.associated_phone_numbers)

    @cached_property
    def phone_number_blocks(self) -> PhoneNumberBlocksResourceWithStreamingResponse:
        return PhoneNumberBlocksResourceWithStreamingResponse(self._porting_orders.phone_number_blocks)

    @cached_property
    def phone_number_extensions(self) -> PhoneNumberExtensionsResourceWithStreamingResponse:
        return PhoneNumberExtensionsResourceWithStreamingResponse(self._porting_orders.phone_number_extensions)


class AsyncPortingOrdersResourceWithStreamingResponse:
    def __init__(self, porting_orders: AsyncPortingOrdersResource) -> None:
        self._porting_orders = porting_orders

        self.create = async_to_streamed_response_wrapper(
            porting_orders.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            porting_orders.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            porting_orders.update,
        )
        self.list = async_to_streamed_response_wrapper(
            porting_orders.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            porting_orders.delete,
        )
        self.retrieve_allowed_foc_windows = async_to_streamed_response_wrapper(
            porting_orders.retrieve_allowed_foc_windows,
        )
        self.retrieve_exception_types = async_to_streamed_response_wrapper(
            porting_orders.retrieve_exception_types,
        )
        self.retrieve_loa_template = async_to_custom_streamed_response_wrapper(
            porting_orders.retrieve_loa_template,
            AsyncStreamedBinaryAPIResponse,
        )
        self.retrieve_requirements = async_to_streamed_response_wrapper(
            porting_orders.retrieve_requirements,
        )
        self.retrieve_sub_request = async_to_streamed_response_wrapper(
            porting_orders.retrieve_sub_request,
        )

    @cached_property
    def phone_number_configurations(self) -> AsyncPhoneNumberConfigurationsResourceWithStreamingResponse:
        return AsyncPhoneNumberConfigurationsResourceWithStreamingResponse(
            self._porting_orders.phone_number_configurations
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._porting_orders.actions)

    @cached_property
    def activation_jobs(self) -> AsyncActivationJobsResourceWithStreamingResponse:
        return AsyncActivationJobsResourceWithStreamingResponse(self._porting_orders.activation_jobs)

    @cached_property
    def additional_documents(self) -> AsyncAdditionalDocumentsResourceWithStreamingResponse:
        return AsyncAdditionalDocumentsResourceWithStreamingResponse(self._porting_orders.additional_documents)

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithStreamingResponse:
        return AsyncCommentsResourceWithStreamingResponse(self._porting_orders.comments)

    @cached_property
    def verification_codes(self) -> AsyncVerificationCodesResourceWithStreamingResponse:
        return AsyncVerificationCodesResourceWithStreamingResponse(self._porting_orders.verification_codes)

    @cached_property
    def action_requirements(self) -> AsyncActionRequirementsResourceWithStreamingResponse:
        return AsyncActionRequirementsResourceWithStreamingResponse(self._porting_orders.action_requirements)

    @cached_property
    def associated_phone_numbers(self) -> AsyncAssociatedPhoneNumbersResourceWithStreamingResponse:
        return AsyncAssociatedPhoneNumbersResourceWithStreamingResponse(self._porting_orders.associated_phone_numbers)

    @cached_property
    def phone_number_blocks(self) -> AsyncPhoneNumberBlocksResourceWithStreamingResponse:
        return AsyncPhoneNumberBlocksResourceWithStreamingResponse(self._porting_orders.phone_number_blocks)

    @cached_property
    def phone_number_extensions(self) -> AsyncPhoneNumberExtensionsResourceWithStreamingResponse:
        return AsyncPhoneNumberExtensionsResourceWithStreamingResponse(self._porting_orders.phone_number_extensions)
