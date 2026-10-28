# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ScenarioRetrieveExportScenariosParams"]


class ScenarioRetrieveExportScenariosParams(TypedDict, total=False):
    export_type: Required[Literal["csv", "xlsx"]]
    """File format of the export."""

    scenario_ids: Required[str]
    """Comma-separated scenario IDs to export."""

    agent_id: int
    """Export scenarios belonging to the specified test agent."""
