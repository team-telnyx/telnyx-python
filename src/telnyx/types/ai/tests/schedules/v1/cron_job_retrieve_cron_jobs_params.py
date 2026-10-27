# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CronJobRetrieveCronJobsParams"]


class CronJobRetrieveCronJobsParams(TypedDict, total=False):
    agent_id: int
    """Filter jobs belonging to the specified test agent."""
