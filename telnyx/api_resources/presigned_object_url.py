from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import CreateableAPIResource


class PresignedObjectUrl(CreateableAPIResource):
    OBJECT_NAME = "presigned_object_url"
