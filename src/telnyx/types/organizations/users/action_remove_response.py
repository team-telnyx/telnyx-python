# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel
from ..user_group_reference import UserGroupReference

__all__ = ["ActionRemoveResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the specific resource."""

    created_at: Optional[str] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    email: Optional[str] = None
    """The email address of the user."""

    groups: Optional[List[UserGroupReference]] = None
    """The groups the user belongs to.

    Only included when include_groups parameter is true.
    """

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

    record_type: Optional[str] = None
    """Identifies the type of the resource.

    Can be 'organization_owner' or 'organization_sub_user'.
    """

    user_status: Optional[Literal["enabled", "disabled", "blocked"]] = None
    """The status of the account."""


class ActionRemoveResponse(BaseModel):
    data: Optional[Data] = None
