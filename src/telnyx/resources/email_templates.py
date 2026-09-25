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
from ..pagination import SyncEmailCursorPagination, AsyncEmailCursorPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.email_template import EmailTemplate
from ..types.email_template_response import EmailTemplateResponse
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
        autoescape: bool | Omit = omit,
        html_body: Optional[str] | Omit = omit,
        strict_variables: bool | Omit = omit,
        subject: Optional[str] | Omit = omit,
        text_body: Optional[str] | Omit = omit,
        variable_schema: Optional[Dict[str, email_template_create_params.VariableSchema]] | Omit = omit,
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

          autoescape: Per-template HTML autoescaping setting. Defaults to `false` for backward
              compatibility. When `true`, the rendered `html_body` HTML-escapes each Liquid
              expression's output at the output boundary (after its filters run, before
              concatenation with literal template markup). Input values are never mutated and
              `subject`/`text_body` are never autoescaped. The boundary escape is idempotent:
              HTML entities already present in the output (e.g. from an explicit `escape`
              filter) are preserved, so an explicit `escape`/`escape_once` is never
              double-escaped, and markup introduced by any later filter in the chain is still
              escaped.

          html_body: Liquid template HTML body.

          strict_variables: Per-template strict variable-validation setting. Defaults to `false` for
              backward compatibility. When `true`, a send or render that is missing a variable
              marked `required: true` in `variable_schema` fails with 422 naming the variable.
              Missing optional variables never fail; their schema `default` (when set) is
              applied to the render.

          subject: Liquid template subject.

          text_body: Liquid template text body.

          variable_schema: Structured variable requirements. Required variables cannot define defaults;
              invalid combinations return 422. This is independent of the legacy `variables`
              array. On render with `strict_variables` enabled: `required` variables must be
              supplied as non-empty values — absent, `null`, empty string, empty object `{}`,
              and empty array `[]` all fail with 422 naming the variable, while present values
              such as `false` and `0` pass (they are present, not empty). Optional variables
              fall back to their `default` when absent.

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
                    "autoescape": autoescape,
                    "html_body": html_body,
                    "strict_variables": strict_variables,
                    "subject": subject,
                    "text_body": text_body,
                    "variable_schema": variable_schema,
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
        Returns the account-owned template identified by ID, including its Liquid
        subject and bodies, declared variables, and timestamps.

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
        autoescape: bool | Omit = omit,
        html_body: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        strict_variables: bool | Omit = omit,
        subject: Optional[str] | Omit = omit,
        text_body: Optional[str] | Omit = omit,
        variable_schema: Optional[Dict[str, email_template_update_params.VariableSchema]] | Omit = omit,
        variables: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailTemplateResponse:
        """
        Updates one or more fields of the specified email template and returns the
        updated template.

        Args:
          autoescape: Per-template HTML autoescaping setting.

          html_body: Liquid template HTML body.

          strict_variables: Per-template strict variable-validation setting.

          subject: Liquid template subject.

          text_body: Liquid template text body.

          variable_schema: Structured variable requirements. Required variables cannot define defaults;
              invalid combinations return 422. Set to `null` to clear the schema.

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
                    "autoescape": autoescape,
                    "html_body": html_body,
                    "name": name,
                    "strict_variables": strict_variables,
                    "subject": subject,
                    "text_body": text_body,
                    "variable_schema": variable_schema,
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
    ) -> SyncEmailCursorPagination[EmailTemplate]:
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
        return self._get_api_list(
            "/email_templates",
            page=SyncEmailCursorPagination[EmailTemplate],
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
            model=EmailTemplate,
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
        """Deletes the account-owned template.

        The operation returns `204` with no body and
        prevents future sends or renders from using the deleted template ID.

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

        When the template has `strict_variables` enabled and a required variable (per
        `variable_schema`) is missing, returns 422 naming the variable. When the
        template has `autoescape` enabled, the rendered `html_body` expression output is
        HTML-escaped at the output boundary; `subject` and `text_body` are not
        autoescaped.

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
        autoescape: bool | Omit = omit,
        html_body: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        strict_variables: bool | Omit = omit,
        subject: Optional[str] | Omit = omit,
        text_body: Optional[str] | Omit = omit,
        variable_schema: Optional[Dict[str, email_template_replace_params.VariableSchema]] | Omit = omit,
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
          autoescape: Per-template HTML autoescaping setting.

          html_body: Liquid template HTML body.

          strict_variables: Per-template strict variable-validation setting.

          subject: Liquid template subject.

          text_body: Liquid template text body.

          variable_schema: Structured variable requirements. Required variables cannot define defaults;
              invalid combinations return 422. Set to `null` to clear the schema.

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
                    "autoescape": autoescape,
                    "html_body": html_body,
                    "name": name,
                    "strict_variables": strict_variables,
                    "subject": subject,
                    "text_body": text_body,
                    "variable_schema": variable_schema,
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
        autoescape: bool | Omit = omit,
        html_body: Optional[str] | Omit = omit,
        strict_variables: bool | Omit = omit,
        subject: Optional[str] | Omit = omit,
        text_body: Optional[str] | Omit = omit,
        variable_schema: Optional[Dict[str, email_template_create_params.VariableSchema]] | Omit = omit,
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

          autoescape: Per-template HTML autoescaping setting. Defaults to `false` for backward
              compatibility. When `true`, the rendered `html_body` HTML-escapes each Liquid
              expression's output at the output boundary (after its filters run, before
              concatenation with literal template markup). Input values are never mutated and
              `subject`/`text_body` are never autoescaped. The boundary escape is idempotent:
              HTML entities already present in the output (e.g. from an explicit `escape`
              filter) are preserved, so an explicit `escape`/`escape_once` is never
              double-escaped, and markup introduced by any later filter in the chain is still
              escaped.

          html_body: Liquid template HTML body.

          strict_variables: Per-template strict variable-validation setting. Defaults to `false` for
              backward compatibility. When `true`, a send or render that is missing a variable
              marked `required: true` in `variable_schema` fails with 422 naming the variable.
              Missing optional variables never fail; their schema `default` (when set) is
              applied to the render.

          subject: Liquid template subject.

          text_body: Liquid template text body.

          variable_schema: Structured variable requirements. Required variables cannot define defaults;
              invalid combinations return 422. This is independent of the legacy `variables`
              array. On render with `strict_variables` enabled: `required` variables must be
              supplied as non-empty values — absent, `null`, empty string, empty object `{}`,
              and empty array `[]` all fail with 422 naming the variable, while present values
              such as `false` and `0` pass (they are present, not empty). Optional variables
              fall back to their `default` when absent.

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
                    "autoescape": autoescape,
                    "html_body": html_body,
                    "strict_variables": strict_variables,
                    "subject": subject,
                    "text_body": text_body,
                    "variable_schema": variable_schema,
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
        Returns the account-owned template identified by ID, including its Liquid
        subject and bodies, declared variables, and timestamps.

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
        autoescape: bool | Omit = omit,
        html_body: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        strict_variables: bool | Omit = omit,
        subject: Optional[str] | Omit = omit,
        text_body: Optional[str] | Omit = omit,
        variable_schema: Optional[Dict[str, email_template_update_params.VariableSchema]] | Omit = omit,
        variables: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailTemplateResponse:
        """
        Updates one or more fields of the specified email template and returns the
        updated template.

        Args:
          autoescape: Per-template HTML autoescaping setting.

          html_body: Liquid template HTML body.

          strict_variables: Per-template strict variable-validation setting.

          subject: Liquid template subject.

          text_body: Liquid template text body.

          variable_schema: Structured variable requirements. Required variables cannot define defaults;
              invalid combinations return 422. Set to `null` to clear the schema.

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
                    "autoescape": autoescape,
                    "html_body": html_body,
                    "name": name,
                    "strict_variables": strict_variables,
                    "subject": subject,
                    "text_body": text_body,
                    "variable_schema": variable_schema,
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
    ) -> AsyncPaginator[EmailTemplate, AsyncEmailCursorPagination[EmailTemplate]]:
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
        return self._get_api_list(
            "/email_templates",
            page=AsyncEmailCursorPagination[EmailTemplate],
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
            model=EmailTemplate,
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
        """Deletes the account-owned template.

        The operation returns `204` with no body and
        prevents future sends or renders from using the deleted template ID.

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

        When the template has `strict_variables` enabled and a required variable (per
        `variable_schema`) is missing, returns 422 naming the variable. When the
        template has `autoescape` enabled, the rendered `html_body` expression output is
        HTML-escaped at the output boundary; `subject` and `text_body` are not
        autoescaped.

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
        autoescape: bool | Omit = omit,
        html_body: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        strict_variables: bool | Omit = omit,
        subject: Optional[str] | Omit = omit,
        text_body: Optional[str] | Omit = omit,
        variable_schema: Optional[Dict[str, email_template_replace_params.VariableSchema]] | Omit = omit,
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
          autoescape: Per-template HTML autoescaping setting.

          html_body: Liquid template HTML body.

          strict_variables: Per-template strict variable-validation setting.

          subject: Liquid template subject.

          text_body: Liquid template text body.

          variable_schema: Structured variable requirements. Required variables cannot define defaults;
              invalid combinations return 422. Set to `null` to clear the schema.

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
                    "autoescape": autoescape,
                    "html_body": html_body,
                    "name": name,
                    "strict_variables": strict_variables,
                    "subject": subject,
                    "text_body": text_body,
                    "variable_schema": variable_schema,
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
