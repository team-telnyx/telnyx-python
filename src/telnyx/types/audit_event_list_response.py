# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AuditEventListResponse", "Data", "DataChange", "Meta"]


class DataChange(BaseModel):
    field: Optional[str] = None
    """The name of the field that was changed.

    May use the dot notation to indicate nested fields.
    """

    from_: Union[str, float, bool, Dict[str, object], List[object], None] = FieldInfo(alias="from", default=None)
    """The previous value of the field. Can be any JSON type."""

    to: Union[str, float, bool, Dict[str, object], List[object], None] = None
    """The new value of the field. Can be any JSON type."""


class Data(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the audit log entry."""

    alternate_resource_id: Optional[str] = None
    """
    An alternate identifier for a resource which may be considered unique enough to
    identify the resource but is not the primary identifier for the resource. For
    example, this field could be used to store the phone number value for a phone
    number when the primary database identifier is a separate distinct value.
    """

    change_made_by: Optional[Literal["telnyx", "account_manager", "account_owner", "organization_member"]] = None
    """
    Indicates if the change was made by Telnyx on your behalf, the organization
    owner, a member of your organization, or in the case of managed accounts, the
    account manager.
    """

    change_type: Optional[str] = None
    """The type of change that occurred."""

    changes: Optional[List[DataChange]] = None
    """Details of the changes made to the resource."""

    created_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the change occurred."""

    organization_id: Optional[str] = None
    """Unique identifier for the organization that owns the resource."""

    record_type: Optional[str] = None
    """The type of the resource being audited."""

    resource_id: Optional[str] = None
    """Unique identifier for the resource that was changed."""

    user_id: Optional[str] = None
    """Unique identifier for the user who made the change."""


class Meta(BaseModel):
    page_number: Optional[int] = None

    page_size: Optional[int] = None

    total_pages: Optional[int] = None

    total_results: Optional[int] = None


class AuditEventListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[Meta] = None
