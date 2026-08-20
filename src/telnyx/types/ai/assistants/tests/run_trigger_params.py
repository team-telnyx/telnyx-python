# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["RunTriggerParams"]


class RunTriggerParams(TypedDict, total=False):
    destination_version_id: str
    """Optional assistant version ID to use for this test run.

    If provided, the version must exist or a 400 error will be returned. If not
    provided, test will run on main version
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
