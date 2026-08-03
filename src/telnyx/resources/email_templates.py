# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..types import (
    email_template_list_params,
    email_template_create_params,
    email_template_render_params,
    email_template_update_params,
    email_template_replace_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.email_template_response import EmailTemplateResponse
from ..types.email_template_list_response import EmailTemplateListResponse
from ..types.email_template_render_response import EmailTemplateRenderResponse

__all__ = ["EmailTemplatesResource", "AsyncEmailTemplatesResource"]


class EmailTemplatesResource(SyncAPIResource):
    """Create, list, retrieve, update, delete, and render Liquid email templates."""

    @cached_property
    def with_raw_response(self) -> EmailTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return EmailTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return EmailTemplatesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        html_body: Optional[str] | Omit = omit,
        subject: Optional[str] | Omit = omit,
        text_body: Optional[str] | Omit = omit,
        variables: SequenceNotStr[str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailTemplateResponse:
        """Creates a Liquid email template.

        Variables are auto-extracted when omitted.

        Args:
          name: Letters, numbers, spaces, hyphens, and underscores only.

          html_body: Liquid template HTML body.

          subject: Liquid template subject.

          text_body: Liquid template text body.

          variables: Template variables. Auto-extracted from subject/body fields when absent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/email_templates",
            body=maybe_transform(
                {
                    "name": name,
                    "html_body": html_body,
                    "subject": subject,
                    "text_body": text_body,
                    "variables": variables,
                },
                email_template_create_params.EmailTemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailTemplateResponse,
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
    ) -> EmailTemplateResponse:
        """
        Get an email template

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/email_templates/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailTemplateResponse,
        )

    def update(
        self,
        id: str,
        *,
        html_body: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        subject: Optional[str] | Omit = omit,
        text_body: Optional[str] | Omit = omit,
        variables: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailTemplateResponse:
        """
        Updates one or more template fields.

        Args:
          html_body: Liquid template HTML body.

          subject: Liquid template subject.

          text_body: Liquid template text body.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/email_templates/{id}", id=id),
            body=maybe_transform(
                {
                    "html_body": html_body,
                    "name": name,
                    "subject": subject,
                    "text_body": text_body,
                    "variables": variables,
                },
                email_template_update_params.EmailTemplateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailTemplateResponse,
        )

    def list(
        self,
        *,
        page_cursor: str | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailTemplateListResponse:
        """
        Lists templates sorted newest first by `created_at desc, id desc`.

        Args:
          page_cursor: Opaque URL-safe Base64 cursor returned by a previous list response.

          page_size: Number of results to return. Defaults to 25; maximum is 100. Invalid values are
              clamped to the valid range.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/email_templates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_cursor": page_cursor,
                        "page_size": page_size,
                    },
                    email_template_list_params.EmailTemplateListParams,
                ),
            ),
            cast_to=EmailTemplateListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an email template

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
            path_template("/email_templates/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def render(
        self,
        id: str,
        *,
        template_variables: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailTemplateRenderResponse:
        """Renders a template using the provided Liquid variables.

        Missing
        `template_variables` defaults to `{}`.

        Args:
          template_variables: Variables for Liquid template rendering. Non-object values are silently treated
              as an empty object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/email_templates/{id}/render", id=id),
            body=maybe_transform(
                {"template_variables": template_variables}, email_template_render_params.EmailTemplateRenderParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailTemplateRenderResponse,
        )

    def replace(
        self,
        id: str,
        *,
        html_body: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        subject: Optional[str] | Omit = omit,
        text_body: Optional[str] | Omit = omit,
        variables: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailTemplateResponse:
        """Replaces template fields.

        Behaves identically to PATCH; provided for
        compatibility with Phoenix resource routes.

        Args:
          html_body: Liquid template HTML body.

          subject: Liquid template subject.

          text_body: Liquid template text body.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            path_template("/email_templates/{id}", id=id),
            body=maybe_transform(
                {
                    "html_body": html_body,
                    "name": name,
                    "subject": subject,
                    "text_body": text_body,
                    "variables": variables,
                },
                email_template_replace_params.EmailTemplateReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailTemplateResponse,
        )


class AsyncEmailTemplatesResource(AsyncAPIResource):
    """Create, list, retrieve, update, delete, and render Liquid email templates."""

    @cached_property
    def with_raw_response(self) -> AsyncEmailTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncEmailTemplatesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        html_body: Optional[str] | Omit = omit,
        subject: Optional[str] | Omit = omit,
        text_body: Optional[str] | Omit = omit,
        variables: SequenceNotStr[str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailTemplateResponse:
        """Creates a Liquid email template.

        Variables are auto-extracted when omitted.

        Args:
          name: Letters, numbers, spaces, hyphens, and underscores only.

          html_body: Liquid template HTML body.

          subject: Liquid template subject.

          text_body: Liquid template text body.

          variables: Template variables. Auto-extracted from subject/body fields when absent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/email_templates",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "html_body": html_body,
                    "subject": subject,
                    "text_body": text_body,
                    "variables": variables,
                },
                email_template_create_params.EmailTemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailTemplateResponse,
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
    ) -> EmailTemplateResponse:
        """
        Get an email template

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/email_templates/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailTemplateResponse,
        )

    async def update(
        self,
        id: str,
        *,
        html_body: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        subject: Optional[str] | Omit = omit,
        text_body: Optional[str] | Omit = omit,
        variables: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailTemplateResponse:
        """
        Updates one or more template fields.

        Args:
          html_body: Liquid template HTML body.

          subject: Liquid template subject.

          text_body: Liquid template text body.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/email_templates/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "html_body": html_body,
                    "name": name,
                    "subject": subject,
                    "text_body": text_body,
                    "variables": variables,
                },
                email_template_update_params.EmailTemplateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailTemplateResponse,
        )

    async def list(
        self,
        *,
        page_cursor: str | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailTemplateListResponse:
        """
        Lists templates sorted newest first by `created_at desc, id desc`.

        Args:
          page_cursor: Opaque URL-safe Base64 cursor returned by a previous list response.

          page_size: Number of results to return. Defaults to 25; maximum is 100. Invalid values are
              clamped to the valid range.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/email_templates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page_cursor": page_cursor,
                        "page_size": page_size,
                    },
                    email_template_list_params.EmailTemplateListParams,
                ),
            ),
            cast_to=EmailTemplateListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an email template

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
            path_template("/email_templates/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def render(
        self,
        id: str,
        *,
        template_variables: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailTemplateRenderResponse:
        """Renders a template using the provided Liquid variables.

        Missing
        `template_variables` defaults to `{}`.

        Args:
          template_variables: Variables for Liquid template rendering. Non-object values are silently treated
              as an empty object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/email_templates/{id}/render", id=id),
            body=await async_maybe_transform(
                {"template_variables": template_variables}, email_template_render_params.EmailTemplateRenderParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailTemplateRenderResponse,
        )

    async def replace(
        self,
        id: str,
        *,
        html_body: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        subject: Optional[str] | Omit = omit,
        text_body: Optional[str] | Omit = omit,
        variables: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailTemplateResponse:
        """Replaces template fields.

        Behaves identically to PATCH; provided for
        compatibility with Phoenix resource routes.

        Args:
          html_body: Liquid template HTML body.

          subject: Liquid template subject.

          text_body: Liquid template text body.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            path_template("/email_templates/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "html_body": html_body,
                    "name": name,
                    "subject": subject,
                    "text_body": text_body,
                    "variables": variables,
                },
                email_template_replace_params.EmailTemplateReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailTemplateResponse,
        )


class EmailTemplatesResourceWithRawResponse:
    def __init__(self, email_templates: EmailTemplatesResource) -> None:
        self._email_templates = email_templates

        self.create = to_raw_response_wrapper(
            email_templates.create,
        )
        self.retrieve = to_raw_response_wrapper(
            email_templates.retrieve,
        )
        self.update = to_raw_response_wrapper(
            email_templates.update,
        )
        self.list = to_raw_response_wrapper(
            email_templates.list,
        )
        self.delete = to_raw_response_wrapper(
            email_templates.delete,
        )
        self.render = to_raw_response_wrapper(
            email_templates.render,
        )
        self.replace = to_raw_response_wrapper(
            email_templates.replace,
        )


class AsyncEmailTemplatesResourceWithRawResponse:
    def __init__(self, email_templates: AsyncEmailTemplatesResource) -> None:
        self._email_templates = email_templates

        self.create = async_to_raw_response_wrapper(
            email_templates.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            email_templates.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            email_templates.update,
        )
        self.list = async_to_raw_response_wrapper(
            email_templates.list,
        )
        self.delete = async_to_raw_response_wrapper(
            email_templates.delete,
        )
        self.render = async_to_raw_response_wrapper(
            email_templates.render,
        )
        self.replace = async_to_raw_response_wrapper(
            email_templates.replace,
        )


class EmailTemplatesResourceWithStreamingResponse:
    def __init__(self, email_templates: EmailTemplatesResource) -> None:
        self._email_templates = email_templates

        self.create = to_streamed_response_wrapper(
            email_templates.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            email_templates.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            email_templates.update,
        )
        self.list = to_streamed_response_wrapper(
            email_templates.list,
        )
        self.delete = to_streamed_response_wrapper(
            email_templates.delete,
        )
        self.render = to_streamed_response_wrapper(
            email_templates.render,
        )
        self.replace = to_streamed_response_wrapper(
            email_templates.replace,
        )


class AsyncEmailTemplatesResourceWithStreamingResponse:
    def __init__(self, email_templates: AsyncEmailTemplatesResource) -> None:
        self._email_templates = email_templates

        self.create = async_to_streamed_response_wrapper(
            email_templates.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            email_templates.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            email_templates.update,
        )
        self.list = async_to_streamed_response_wrapper(
            email_templates.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            email_templates.delete,
        )
        self.render = async_to_streamed_response_wrapper(
            email_templates.render,
        )
        self.replace = async_to_streamed_response_wrapper(
            email_templates.replace,
        )
