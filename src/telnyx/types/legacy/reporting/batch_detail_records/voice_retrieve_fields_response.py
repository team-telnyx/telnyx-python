# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["VoiceRetrieveFieldsResponse"]


class VoiceRetrieveFieldsResponse(BaseModel):
    """Available CDR report fields grouped by category"""

    billing: Optional[List[str]] = FieldInfo(alias="Billing", default=None)
    """Cost and billing related information"""

    interaction_data: Optional[List[str]] = FieldInfo(alias="Interaction Data", default=None)
    """Fields related to call interaction and basic call information"""

    number_information: Optional[List[str]] = FieldInfo(alias="Number Information", default=None)
    """Geographic and routing information for phone numbers"""

    telephony_data: Optional[List[str]] = FieldInfo(alias="Telephony Data", default=None)
    """Technical telephony and call control information"""
