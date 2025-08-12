# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SimCardDeleteParams"]


class SimCardDeleteParams(TypedDict, total=False):
    report_lost: bool
    """Enables deletion of disabled eSIMs that can't be uninstalled from a device.

    This is irreversible and the eSIM cannot be re-registered.
    """
