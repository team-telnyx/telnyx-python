# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["VideoRegion"]


class VideoRegion(BaseModel):
    height: Optional[int] = None
    """Height of the video region"""

    max_columns: Optional[int] = None
    """Maximum number of columns of the region's placement grid.

    By default, the region has as many columns as needed to layout all the specified
    video sources.
    """

    max_rows: Optional[int] = None
    """Maximum number of rows of the region's placement grid.

    By default, the region has as many rows as needed to layout all the specified
    video sources.
    """

    video_sources: Optional[List[str]] = None
    """Array of video recording ids to be composed in the region.

    Can be "\\**" to specify all video recordings in the session
    """

    width: Optional[int] = None
    """Width of the video region"""

    x_pos: Optional[int] = None
    """
    X axis value (in pixels) of the region's upper left corner relative to the upper
    left corner of the whole room composition viewport.
    """

    y_pos: Optional[int] = None
    """
    Y axis value (in pixels) of the region's upper left corner relative to the upper
    left corner of the whole room composition viewport.
    """

    z_pos: Optional[int] = None
    """
    Regions with higher z_pos values are stacked on top of regions with lower z_pos
    values
    """
