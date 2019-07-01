from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import SingletonAPIResource


class PublicKey(SingletonAPIResource):
    OBJECT_NAME = "public_key"
