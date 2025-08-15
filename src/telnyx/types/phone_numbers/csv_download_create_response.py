# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .csv_download import CsvDownload

__all__ = ["CsvDownloadCreateResponse"]


class CsvDownloadCreateResponse(BaseModel):
    data: Optional[List[CsvDownload]] = None
