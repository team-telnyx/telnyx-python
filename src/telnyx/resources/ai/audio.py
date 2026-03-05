# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Mapping, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from ..._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from ..._compat import cached_property
from ...types.ai import audio_transcribe_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.ai.audio_transcribe_response import AudioTranscribeResponse

__all__ = ["AudioResource", "AsyncAudioResource"]


class AudioResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AudioResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AudioResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AudioResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AudioResourceWithStreamingResponse(self)

    def transcribe(
        self,
        *,
        model: Literal["distil-whisper/distil-large-v2", "openai/whisper-large-v3-turbo", "deepgram/nova-3"],
        file: FileTypes | Omit = omit,
        file_url: str | Omit = omit,
        language: str | Omit = omit,
        model_config: Dict[str, object] | Omit = omit,
        response_format: Literal["json", "verbose_json"] | Omit = omit,
        timestamp_granularities: Literal["segment"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AudioTranscribeResponse:
        """Transcribe speech to text.

        This endpoint is consistent with the
        [OpenAI Transcription API](https://platform.openai.com/docs/api-reference/audio/createTranscription)
        and may be used with the OpenAI JS or Python SDK.

        Args:
          model: ID of the model to use. `distil-whisper/distil-large-v2` is lower latency but
              English-only. `openai/whisper-large-v3-turbo` is multi-lingual but slightly
              higher latency. `deepgram/nova-3` supports English variants (en, en-US, en-GB,
              en-AU, en-NZ, en-IN) and only accepts mp3/wav files.

          file: The audio file object to transcribe, in one of these formats: flac, mp3, mp4,
              mpeg, mpga, m4a, ogg, wav, or webm. File uploads are limited to 100 MB. Cannot
              be used together with `file_url`. Note: `deepgram/nova-3` only supports mp3 and
              wav formats.

          file_url: Link to audio file in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a,
              ogg, wav, or webm. Support for hosted files is limited to 100MB. Cannot be used
              together with `file`. Note: `deepgram/nova-3` only supports mp3 and wav formats.

          language: The language of the audio to be transcribed. For `deepgram/nova-3`, only English
              variants are supported: `en`, `en-US`, `en-GB`, `en-AU`, `en-NZ`, `en-IN`. For
              `openai/whisper-large-v3-turbo`, supports multiple languages.
              `distil-whisper/distil-large-v2` does not support language parameter.

          model_config: Additional model-specific configuration parameters. Only allowed with
              `deepgram/nova-3` model. Can include Deepgram-specific options such as
              `smart_format`, `punctuate`, `diarize`, `utterance`, `numerals`, and `language`.
              If `language` is provided both as a top-level parameter and in `model_config`,
              the top-level parameter takes precedence.

          response_format: The format of the transcript output. Use `verbose_json` to take advantage of
              timestamps.

          timestamp_granularities: The timestamp granularities to populate for this transcription.
              `response_format` must be set verbose_json to use timestamp granularities.
              Currently `segment` is supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "model": model,
                "file": file,
                "file_url": file_url,
                "language": language,
                "model_config": model_config,
                "response_format": response_format,
                "timestamp_granularities": timestamp_granularities,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/ai/audio/transcriptions",
            body=maybe_transform(body, audio_transcribe_params.AudioTranscribeParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AudioTranscribeResponse,
        )


class AsyncAudioResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAudioResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAudioResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAudioResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncAudioResourceWithStreamingResponse(self)

    async def transcribe(
        self,
        *,
        model: Literal["distil-whisper/distil-large-v2", "openai/whisper-large-v3-turbo", "deepgram/nova-3"],
        file: FileTypes | Omit = omit,
        file_url: str | Omit = omit,
        language: str | Omit = omit,
        model_config: Dict[str, object] | Omit = omit,
        response_format: Literal["json", "verbose_json"] | Omit = omit,
        timestamp_granularities: Literal["segment"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AudioTranscribeResponse:
        """Transcribe speech to text.

        This endpoint is consistent with the
        [OpenAI Transcription API](https://platform.openai.com/docs/api-reference/audio/createTranscription)
        and may be used with the OpenAI JS or Python SDK.

        Args:
          model: ID of the model to use. `distil-whisper/distil-large-v2` is lower latency but
              English-only. `openai/whisper-large-v3-turbo` is multi-lingual but slightly
              higher latency. `deepgram/nova-3` supports English variants (en, en-US, en-GB,
              en-AU, en-NZ, en-IN) and only accepts mp3/wav files.

          file: The audio file object to transcribe, in one of these formats: flac, mp3, mp4,
              mpeg, mpga, m4a, ogg, wav, or webm. File uploads are limited to 100 MB. Cannot
              be used together with `file_url`. Note: `deepgram/nova-3` only supports mp3 and
              wav formats.

          file_url: Link to audio file in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a,
              ogg, wav, or webm. Support for hosted files is limited to 100MB. Cannot be used
              together with `file`. Note: `deepgram/nova-3` only supports mp3 and wav formats.

          language: The language of the audio to be transcribed. For `deepgram/nova-3`, only English
              variants are supported: `en`, `en-US`, `en-GB`, `en-AU`, `en-NZ`, `en-IN`. For
              `openai/whisper-large-v3-turbo`, supports multiple languages.
              `distil-whisper/distil-large-v2` does not support language parameter.

          model_config: Additional model-specific configuration parameters. Only allowed with
              `deepgram/nova-3` model. Can include Deepgram-specific options such as
              `smart_format`, `punctuate`, `diarize`, `utterance`, `numerals`, and `language`.
              If `language` is provided both as a top-level parameter and in `model_config`,
              the top-level parameter takes precedence.

          response_format: The format of the transcript output. Use `verbose_json` to take advantage of
              timestamps.

          timestamp_granularities: The timestamp granularities to populate for this transcription.
              `response_format` must be set verbose_json to use timestamp granularities.
              Currently `segment` is supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "model": model,
                "file": file,
                "file_url": file_url,
                "language": language,
                "model_config": model_config,
                "response_format": response_format,
                "timestamp_granularities": timestamp_granularities,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/ai/audio/transcriptions",
            body=await async_maybe_transform(body, audio_transcribe_params.AudioTranscribeParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AudioTranscribeResponse,
        )


class AudioResourceWithRawResponse:
    def __init__(self, audio: AudioResource) -> None:
        self._audio = audio

        self.transcribe = to_raw_response_wrapper(
            audio.transcribe,
        )


class AsyncAudioResourceWithRawResponse:
    def __init__(self, audio: AsyncAudioResource) -> None:
        self._audio = audio

        self.transcribe = async_to_raw_response_wrapper(
            audio.transcribe,
        )


class AudioResourceWithStreamingResponse:
    def __init__(self, audio: AudioResource) -> None:
        self._audio = audio

        self.transcribe = to_streamed_response_wrapper(
            audio.transcribe,
        )


class AsyncAudioResourceWithStreamingResponse:
    def __init__(self, audio: AsyncAudioResource) -> None:
        self._audio = audio

        self.transcribe = async_to_streamed_response_wrapper(
            audio.transcribe,
        )
