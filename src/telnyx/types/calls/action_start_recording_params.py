# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ActionStartRecordingParams"]


class ActionStartRecordingParams(TypedDict, total=False):
    channels: Required[Literal["single", "dual"]]
    """
    When `dual`, final audio file will be stereo recorded with the first leg on
    channel A, and the rest on channel B.
    """

    format: Required[Literal["wav", "mp3"]]
    """The audio file format used when storing the call recording.

    Can be either `mp3` or `wav`.
    """

    client_state: str
    """Use this field to add state to every subsequent webhook.

    It must be a valid Base-64 encoded string.
    """

    command_id: str
    """Use this field to avoid duplicate commands.

    Telnyx will ignore any command with the same `command_id` for the same
    `call_control_id`.
    """

    custom_file_name: str
    """The custom recording file name to be used instead of the default `call_leg_id`.

    Telnyx will still add a Unix timestamp suffix.
    """

    max_length: int
    """Defines the maximum length for the recording in seconds.

    The minimum value is 0. The maximum value is 14400. The default value is 0
    (infinite)
    """

    play_beep: bool
    """If enabled, a beep sound will be played at the start of a recording."""

    recording_track: Literal["both", "inbound", "outbound"]
    """The audio track to be recorded.

    Can be either `both`, `inbound` or `outbound`. If only single track is specified
    (`inbound`, `outbound`), `channels` configuration is ignored and it will be
    recorded as mono (single channel).
    """

    timeout_secs: int
    """
    The number of seconds that Telnyx will wait for the recording to be stopped if
    silence is detected. The timer only starts when the speech is detected. Please
    note that call transcription is used to detect silence and the related charge
    will be applied. The minimum value is 0. The default value is 0 (infinite)
    """

    transcription: bool
    """Enable post recording transcription. The default value is false."""

    transcription_engine: Literal["A", "B", "deepgram/nova-3"]
    """Engine to use for speech recognition.

    `A` - `Google`, `B` - `Telnyx`, `deepgram/nova-3` - `Deepgram Nova-3`. Note:
    `deepgram/nova-3` supports only `en` and `en-{Region}` languages.
    """

    transcription_language: Literal[
        "af",
        "af-ZA",
        "am",
        "am-ET",
        "ar",
        "ar-AE",
        "ar-BH",
        "ar-DZ",
        "ar-EG",
        "ar-IL",
        "ar-IQ",
        "ar-JO",
        "ar-KW",
        "ar-LB",
        "ar-MA",
        "ar-MR",
        "ar-OM",
        "ar-PS",
        "ar-QA",
        "ar-SA",
        "ar-TN",
        "ar-YE",
        "as",
        "auto_detect",
        "az",
        "az-AZ",
        "ba",
        "be",
        "bg",
        "bg-BG",
        "bn",
        "bn-BD",
        "bn-IN",
        "bo",
        "br",
        "bs",
        "bs-BA",
        "ca",
        "ca-ES",
        "cs",
        "cs-CZ",
        "cy",
        "da",
        "da-DK",
        "de",
        "de-AT",
        "de-CH",
        "de-DE",
        "el",
        "el-GR",
        "en",
        "en-AU",
        "en-CA",
        "en-GB",
        "en-GH",
        "en-HK",
        "en-IE",
        "en-IN",
        "en-KE",
        "en-NG",
        "en-NZ",
        "en-PH",
        "en-PK",
        "en-SG",
        "en-TZ",
        "en-US",
        "en-ZA",
        "es",
        "es-419",
        "es-AR",
        "es-BO",
        "es-CL",
        "es-CO",
        "es-CR",
        "es-DO",
        "es-EC",
        "es-ES",
        "es-GT",
        "es-HN",
        "es-MX",
        "es-NI",
        "es-PA",
        "es-PE",
        "es-PR",
        "es-PY",
        "es-SV",
        "es-US",
        "es-UY",
        "es-VE",
        "et",
        "et-EE",
        "eu",
        "eu-ES",
        "fa",
        "fa-IR",
        "fi",
        "fi-FI",
        "fil-PH",
        "fo",
        "fr",
        "fr-BE",
        "fr-CA",
        "fr-CH",
        "fr-FR",
        "gl",
        "gl-ES",
        "gu",
        "gu-IN",
        "ha",
        "haw",
        "he",
        "hi",
        "hi-IN",
        "hr",
        "hr-HR",
        "ht",
        "hu",
        "hu-HU",
        "hy",
        "hy-AM",
        "id",
        "id-ID",
        "is",
        "is-IS",
        "it",
        "it-CH",
        "it-IT",
        "iw-IL",
        "ja",
        "ja-JP",
        "jv-ID",
        "jw",
        "ka",
        "ka-GE",
        "kk",
        "kk-KZ",
        "km",
        "km-KH",
        "kn",
        "kn-IN",
        "ko",
        "ko-KR",
        "la",
        "lb",
        "ln",
        "lo",
        "lo-LA",
        "lt",
        "lt-LT",
        "lv",
        "lv-LV",
        "mg",
        "mi",
        "mk",
        "mk-MK",
        "ml",
        "ml-IN",
        "mn",
        "mn-MN",
        "mr",
        "mr-IN",
        "ms",
        "ms-MY",
        "mt",
        "my",
        "my-MM",
        "ne",
        "ne-NP",
        "nl",
        "nl-BE",
        "nl-NL",
        "nn",
        "no",
        "no-NO",
        "oc",
        "pa",
        "pa-Guru-IN",
        "pl",
        "pl-PL",
        "ps",
        "pt",
        "pt-BR",
        "pt-PT",
        "ro",
        "ro-RO",
        "ru",
        "ru-RU",
        "rw-RW",
        "sa",
        "sd",
        "si",
        "si-LK",
        "sk",
        "sk-SK",
        "sl",
        "sl-SI",
        "sn",
        "so",
        "sq",
        "sq-AL",
        "sr",
        "sr-RS",
        "ss-latn-za",
        "st-ZA",
        "su",
        "su-ID",
        "sv",
        "sv-SE",
        "sw",
        "sw-KE",
        "sw-TZ",
        "ta",
        "ta-IN",
        "ta-LK",
        "ta-MY",
        "ta-SG",
        "te",
        "te-IN",
        "tg",
        "th",
        "th-TH",
        "tk",
        "tl",
        "tn-latn-za",
        "tr",
        "tr-TR",
        "ts-ZA",
        "tt",
        "uk",
        "uk-UA",
        "ur",
        "ur-IN",
        "ur-PK",
        "uz",
        "uz-UZ",
        "ve-ZA",
        "vi",
        "vi-VN",
        "xh-ZA",
        "yi",
        "yo",
        "yue-Hant-HK",
        "zh",
        "zh-TW",
        "zu-ZA",
    ]
    """Language code for transcription.

    Note: Not all languages are supported by all transcription engines (google,
    telnyx, deepgram). See engine-specific documentation for supported values.
    """

    transcription_max_speaker_count: int
    """Defines maximum number of speakers in the conversation.

    Applies to `google` engine only.
    """

    transcription_min_speaker_count: int
    """Defines minimum number of speakers in the conversation.

    Applies to `google` engine only.
    """

    transcription_profanity_filter: bool
    """Enables profanity_filter. Applies to `google` engine only."""

    transcription_speaker_diarization: bool
    """Enables speaker diarization. Applies to `google` engine only."""

    trim: Literal["trim-silence"]
    """
    When set to `trim-silence`, silence will be removed from the beginning and end
    of the recording.
    """
