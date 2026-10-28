# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["MetricBulkCreateParams"]


class MetricBulkCreateParams(TypedDict, total=False):
    body: Required[Iterable["CreateAITestMetricRequestParam"]]


from .create_ai_test_metric_request_param import CreateAITestMetricRequestParam
