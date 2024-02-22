from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
)


class SslCertificate(CreateableAPIResource, DeletableAPIResource, ListableAPIResource):
    OBJECT_NAME = "ssl_certificate"
