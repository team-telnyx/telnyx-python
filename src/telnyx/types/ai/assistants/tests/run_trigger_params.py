# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RunTriggerParams"]


class RunTriggerParams(TypedDict, total=False):
    destination_version_id: str
    """Optional assistant version ID to use for this test run.

    If provided, the version must exist or a 400 error will be returned. If not
    provided, test will run on main version
    """
