# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, Iterable, cast

import httpx

from ..types import pronunciation_dict_list_params, pronunciation_dict_create_params, pronunciation_dict_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import extract_files, path_template, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.pronunciation_dict_list_response import PronunciationDictListResponse
from ..types.pronunciation_dict_create_response import PronunciationDictCreateResponse
from ..types.pronunciation_dict_update_response import PronunciationDictUpdateResponse
from ..types.pronunciation_dict_retrieve_response import PronunciationDictRetrieveResponse

__all__ = ["PronunciationDictsResource", "AsyncPronunciationDictsResource"]


class PronunciationDictsResource(SyncAPIResource):
    """Manage pronunciation dictionaries for text-to-speech synthesis.

    Dictionaries contain alias items (text replacement) and phoneme items (IPA pronunciation notation) that control how specific words are spoken.
    """

    @cached_property
    def with_raw_response(self) -> PronunciationDictsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return PronunciationDictsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PronunciationDictsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return PronunciationDictsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        items: Iterable[pronunciation_dict_create_params.Item],
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PronunciationDictCreateResponse:
        """Create a new pronunciation dictionary for the authenticated organization.

        Each
        dictionary contains a list of items that control how specific words are spoken.
        Items can be alias type (text replacement) or phoneme type (IPA pronunciation
        notation).

        As an alternative to providing items directly as JSON, you can upload a
        dictionary file (PLS/XML or plain text format, max 1MB) using
        multipart/form-data. PLS files use the standard W3C Pronunciation Lexicon
        Specification XML format. Text files use a line-based format: `word=alias` for
        aliases, `word:/phoneme/` for IPA phonemes.

        Limits:

        - Maximum 50 dictionaries per organization
        - Maximum 100 items per dictionary
        - Text: max 200 characters
        - Alias/phoneme value: max 500 characters
        - File upload: max 1MB (1,048,576 bytes)

        Args:
          items: List of pronunciation items (alias or phoneme type). At least one item is
              required.

          name: Human-readable name. Must be unique within the organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "items": items,
                "name": name,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/pronunciation_dicts",
            body=maybe_transform(body, pronunciation_dict_create_params.PronunciationDictCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PronunciationDictCreateResponse,
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
    ) -> PronunciationDictRetrieveResponse:
        """
        Retrieve a single pronunciation dictionary by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/pronunciation_dicts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PronunciationDictRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        items: Iterable[pronunciation_dict_update_params.Item] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PronunciationDictUpdateResponse:
        """Update the name and/or items of an existing pronunciation dictionary.

        Uses
        optimistic locking — if the dictionary was modified concurrently, the request
        returns 409 Conflict.

        Args:
          items: Updated list of pronunciation items (alias or phoneme type).

          name: Updated dictionary name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/pronunciation_dicts/{id}", id=id),
            body=maybe_transform(
                {
                    "items": items,
                    "name": name,
                },
                pronunciation_dict_update_params.PronunciationDictUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PronunciationDictUpdateResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[PronunciationDictListResponse]:
        """List all pronunciation dictionaries for the authenticated organization.

        Results
        are paginated using offset-based pagination.

        Args:
          page_number: Page number (1-based). Defaults to 1.

          page_size: Number of results per page. Defaults to 20, maximum 250.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/pronunciation_dicts",
            page=SyncDefaultFlatPagination[PronunciationDictListResponse],
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
                    pronunciation_dict_list_params.PronunciationDictListParams,
                ),
            ),
            model=PronunciationDictListResponse,
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
        Permanently delete a pronunciation dictionary.

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
            path_template("/pronunciation_dicts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncPronunciationDictsResource(AsyncAPIResource):
    """Manage pronunciation dictionaries for text-to-speech synthesis.

    Dictionaries contain alias items (text replacement) and phoneme items (IPA pronunciation notation) that control how specific words are spoken.
    """

    @cached_property
    def with_raw_response(self) -> AsyncPronunciationDictsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPronunciationDictsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPronunciationDictsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncPronunciationDictsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        items: Iterable[pronunciation_dict_create_params.Item],
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PronunciationDictCreateResponse:
        """Create a new pronunciation dictionary for the authenticated organization.

        Each
        dictionary contains a list of items that control how specific words are spoken.
        Items can be alias type (text replacement) or phoneme type (IPA pronunciation
        notation).

        As an alternative to providing items directly as JSON, you can upload a
        dictionary file (PLS/XML or plain text format, max 1MB) using
        multipart/form-data. PLS files use the standard W3C Pronunciation Lexicon
        Specification XML format. Text files use a line-based format: `word=alias` for
        aliases, `word:/phoneme/` for IPA phonemes.

        Limits:

        - Maximum 50 dictionaries per organization
        - Maximum 100 items per dictionary
        - Text: max 200 characters
        - Alias/phoneme value: max 500 characters
        - File upload: max 1MB (1,048,576 bytes)

        Args:
          items: List of pronunciation items (alias or phoneme type). At least one item is
              required.

          name: Human-readable name. Must be unique within the organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "items": items,
                "name": name,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/pronunciation_dicts",
            body=await async_maybe_transform(body, pronunciation_dict_create_params.PronunciationDictCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PronunciationDictCreateResponse,
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
    ) -> PronunciationDictRetrieveResponse:
        """
        Retrieve a single pronunciation dictionary by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/pronunciation_dicts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PronunciationDictRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        items: Iterable[pronunciation_dict_update_params.Item] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PronunciationDictUpdateResponse:
        """Update the name and/or items of an existing pronunciation dictionary.

        Uses
        optimistic locking — if the dictionary was modified concurrently, the request
        returns 409 Conflict.

        Args:
          items: Updated list of pronunciation items (alias or phoneme type).

          name: Updated dictionary name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/pronunciation_dicts/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "items": items,
                    "name": name,
                },
                pronunciation_dict_update_params.PronunciationDictUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PronunciationDictUpdateResponse,
        )

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PronunciationDictListResponse, AsyncDefaultFlatPagination[PronunciationDictListResponse]]:
        """List all pronunciation dictionaries for the authenticated organization.

        Results
        are paginated using offset-based pagination.

        Args:
          page_number: Page number (1-based). Defaults to 1.

          page_size: Number of results per page. Defaults to 20, maximum 250.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/pronunciation_dicts",
            page=AsyncDefaultFlatPagination[PronunciationDictListResponse],
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
                    pronunciation_dict_list_params.PronunciationDictListParams,
                ),
            ),
            model=PronunciationDictListResponse,
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
        Permanently delete a pronunciation dictionary.

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
            path_template("/pronunciation_dicts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class PronunciationDictsResourceWithRawResponse:
    def __init__(self, pronunciation_dicts: PronunciationDictsResource) -> None:
        self._pronunciation_dicts = pronunciation_dicts

        self.create = to_raw_response_wrapper(
            pronunciation_dicts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            pronunciation_dicts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            pronunciation_dicts.update,
        )
        self.list = to_raw_response_wrapper(
            pronunciation_dicts.list,
        )
        self.delete = to_raw_response_wrapper(
            pronunciation_dicts.delete,
        )


class AsyncPronunciationDictsResourceWithRawResponse:
    def __init__(self, pronunciation_dicts: AsyncPronunciationDictsResource) -> None:
        self._pronunciation_dicts = pronunciation_dicts

        self.create = async_to_raw_response_wrapper(
            pronunciation_dicts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            pronunciation_dicts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            pronunciation_dicts.update,
        )
        self.list = async_to_raw_response_wrapper(
            pronunciation_dicts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            pronunciation_dicts.delete,
        )


class PronunciationDictsResourceWithStreamingResponse:
    def __init__(self, pronunciation_dicts: PronunciationDictsResource) -> None:
        self._pronunciation_dicts = pronunciation_dicts

        self.create = to_streamed_response_wrapper(
            pronunciation_dicts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            pronunciation_dicts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            pronunciation_dicts.update,
        )
        self.list = to_streamed_response_wrapper(
            pronunciation_dicts.list,
        )
        self.delete = to_streamed_response_wrapper(
            pronunciation_dicts.delete,
        )


class AsyncPronunciationDictsResourceWithStreamingResponse:
    def __init__(self, pronunciation_dicts: AsyncPronunciationDictsResource) -> None:
        self._pronunciation_dicts = pronunciation_dicts

        self.create = async_to_streamed_response_wrapper(
            pronunciation_dicts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            pronunciation_dicts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            pronunciation_dicts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            pronunciation_dicts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            pronunciation_dicts.delete,
        )
