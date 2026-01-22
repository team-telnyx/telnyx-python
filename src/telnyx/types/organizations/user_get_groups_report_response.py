# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .user_group_reference import UserGroupReference

__all__ = ["UserGetGroupsReportResponse", "Data"]


class Data(BaseModel):
    """An organization user with their group memberships always included."""

    id: str
    """Identifies the specific resource."""

    created_at: str
    """ISO 8601 formatted date indicating when the resource was created."""

    email: str
    """The email address of the user."""

    groups: List[UserGroupReference]
    """The groups the user belongs to."""

    record_type: str
    """Identifies the type of the resource.

    Can be 'organization_owner' or 'organization_sub_user'.
    """

    user_status: Literal["enabled", "disabled", "blocked"]
    """The status of the account."""

    last_sign_in_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource last signed into the
    portal.

    Null if the user has never signed in.
    """

    organization_user_bypasses_sso: Optional[bool] = None
    """
    Indicates whether this user is allowed to bypass SSO and use password
    authentication.
    """


class UserGetGroupsReportResponse(BaseModel):
    data: Optional[List[Data]] = None
