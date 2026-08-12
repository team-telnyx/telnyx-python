# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["TestDeviceResponse"]


class TestDeviceResponse(BaseModel):
    __test__ = False
    invite_status: Literal["PENDING", "ACCEPTED", "DECLINED"]

    phone_number: str

    test_device_id: str
