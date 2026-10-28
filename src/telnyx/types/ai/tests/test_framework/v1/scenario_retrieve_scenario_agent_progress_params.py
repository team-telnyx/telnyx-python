# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ScenarioRetrieveScenarioAgentProgressParams"]


class ScenarioRetrieveScenarioAgentProgressParams(TypedDict, total=False):
    progress_id: Required[str]
    """Progress ID returned by the improve-evaluator-scenarios endpoint."""
