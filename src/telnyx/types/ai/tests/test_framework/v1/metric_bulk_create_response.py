# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypeAlias

from .ai_test_metric import AITestMetric

__all__ = ["MetricBulkCreateResponse"]

MetricBulkCreateResponse: TypeAlias = List[AITestMetric]
