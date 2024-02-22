from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import CreateableAPIResource


class AccessToken(CreateableAPIResource):
    OBJECT_NAME = "access_token"
