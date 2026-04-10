# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["BookAppointmentToolParams"]


class BookAppointmentToolParams(BaseModel):
    api_key_ref: str
    """Reference to an integration secret that contains your Cal.com API key.

    You would pass the `identifier` for an integration secret
    [/v2/integration_secrets](https://developers.telnyx.com/api/secrets-manager/integration-secrets/create-integration-secret)
    that refers to your Cal.com API key.
    """

    event_type_id: int
    """Event Type ID for which slots are being fetched.

    [cal.com](https://cal.com/docs/api-reference/v2/bookings/create-a-booking#body-event-type-id)
    """

    attendee_name: Optional[str] = None
    """
    The name of the attendee
    [cal.com](https://cal.com/docs/api-reference/v2/bookings/create-a-booking#body-attendee-name).
    If not provided, the assistant will ask for the attendee's name.
    """

    attendee_timezone: Optional[str] = None
    """
    The timezone of the attendee
    [cal.com](https://cal.com/docs/api-reference/v2/bookings/create-a-booking#body-attendee-timezone).
    If not provided, the assistant will ask for the attendee's timezone.
    """
