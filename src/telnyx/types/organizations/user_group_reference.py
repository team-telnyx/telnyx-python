# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["UserGroupReference"]


class UserGroupReference(BaseModel):
    """A reference to a group that a user belongs to."""

    id: str
    """The unique identifier of the group."""

    name: str
    """The name of the group."""
