from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import CreateableAPIResource


class PortabilityCheck(CreateableAPIResource):
    OBJECT_NAME = "portability_check"
