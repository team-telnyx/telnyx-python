# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["UserTagListResponse", "Data"]


class Data(BaseModel):
    number_tags: Optional[List[str]] = None
    """A list of your tags on the given resource type.

    NOTE: The casing of the tags returned will not necessarily match the casing of
    the tags when they were added to a resource. This is because the tags will have
    the casing of the first time they were used within the Telnyx system regardless
    of source.
    """

    outbound_profile_tags: Optional[List[str]] = None
    """A list of your tags on the given resource type.

    NOTE: The casing of the tags returned will not necessarily match the casing of
    the tags when they were added to a resource. This is because the tags will have
    the casing of the first time they were used within the Telnyx system regardless
    of source.
    """


class UserTagListResponse(BaseModel):
    data: Optional[Data] = None
