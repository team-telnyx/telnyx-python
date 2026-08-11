# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .test_device_create_params import TestDeviceCreateParams as TestDeviceCreateParams
from .test_device_list_response import TestDeviceListResponse as TestDeviceListResponse

if TYPE_CHECKING:
    from .test_device_response import TestDeviceResponse as TestDeviceResponse


def __getattr__(name: str) -> Any:
    if name == "TestDeviceResponse":
        from .test_device_response import TestDeviceResponse

        return TestDeviceResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
