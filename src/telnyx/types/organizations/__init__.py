# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .user_list_params import UserListParams as UserListParams
from .user_retrieve_params import UserRetrieveParams as UserRetrieveParams

if TYPE_CHECKING:
    from .organization_user import OrganizationUser as OrganizationUser
    from .user_group_reference import UserGroupReference as UserGroupReference
    from .user_retrieve_response import UserRetrieveResponse as UserRetrieveResponse
    from .user_get_groups_report_response import UserGetGroupsReportResponse as UserGetGroupsReportResponse


def __getattr__(name: str) -> Any:
    if name == "OrganizationUser":
        from .organization_user import OrganizationUser

        return OrganizationUser
    if name == "UserGroupReference":
        from .user_group_reference import UserGroupReference

        return UserGroupReference
    if name == "UserRetrieveResponse":
        from .user_retrieve_response import UserRetrieveResponse

        return UserRetrieveResponse
    if name == "UserGetGroupsReportResponse":
        from .user_get_groups_report_response import UserGetGroupsReportResponse

        return UserGetGroupsReportResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
