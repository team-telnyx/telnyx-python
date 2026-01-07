# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TranscriptionSettingsConfig"]


class TranscriptionSettingsConfig(BaseModel):
    eager_eot_threshold: Optional[float] = None
    """Available only for deepgram/flux.

    Confidence threshold for eager end of turn detection. Must be lower than or
    equal to eot_threshold. Setting this equal to eot_threshold effectively disables
    eager end of turn.
    """

    eot_threshold: Optional[float] = None
    """Available only for deepgram/flux.

    Confidence required to trigger an end of turn. Higher values = more reliable
    turn detection but slightly increased latency.
    """

    eot_timeout_ms: Optional[int] = None
    """Available only for deepgram/flux.

    Maximum milliseconds of silence before forcing an end of turn, regardless of
    confidence.
    """

    numerals: Optional[bool] = None

    smart_format: Optional[bool] = None
