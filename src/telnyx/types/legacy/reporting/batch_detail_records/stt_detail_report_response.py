# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["SttDetailReportResponse"]


class SttDetailReportResponse(BaseModel):
    id: Optional[str] = None
    """Identifies the resource"""

    created_at: Optional[datetime] = None

    download_link: Optional[str] = None
    """URL to download the report"""

    end_date: Optional[datetime] = None

    record_type: Optional[str] = None

    start_date: Optional[datetime] = None

    status: Optional[Literal["PENDING", "COMPLETE", "FAILED", "EXPIRED"]] = None
