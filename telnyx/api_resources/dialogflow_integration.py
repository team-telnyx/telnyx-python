from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)


class DialogflowIntegration(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "dialogflow_integration"
