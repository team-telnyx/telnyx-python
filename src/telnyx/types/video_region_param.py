# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["VideoRegionParam"]


class VideoRegionParam(TypedDict, total=False):
    height: int
    """Height of the video region"""

    max_columns: int
    """Maximum number of columns of the region's placement grid.

    By default, the region has as many columns as needed to layout all the specified
    video sources.
    """

    max_rows: int
    """Maximum number of rows of the region's placement grid.

    By default, the region has as many rows as needed to layout all the specified
    video sources.
    """

    video_sources: SequenceNotStr[str]
    """Array of video recording ids to be composed in the region.

    Can be "\\**" to specify all video recordings in the session
    """

    width: int
    """Width of the video region"""

    x_pos: int
    """
    X axis value (in pixels) of the region's upper left corner relative to the upper
    left corner of the whole room composition viewport.
    """

    y_pos: int
    """
    Y axis value (in pixels) of the region's upper left corner relative to the upper
    left corner of the whole room composition viewport.
    """

    z_pos: int
    """
    Regions with higher z_pos values are stacked on top of regions with lower z_pos
    values
    """
