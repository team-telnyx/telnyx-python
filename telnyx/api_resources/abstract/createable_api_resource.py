from __future__ import absolute_import, division, print_function

from telnyx import api_requestor, util
from telnyx.api_resources.abstract.api_resource import APIResource


class CreateableAPIResource(APIResource):
    @classmethod
    def create(cls, api_key=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        url = cls.class_url()
        params = util.rewrite_reserved_words(params)
        response, api_key = requestor.request("post", url, params)

        return util.convert_to_telnyx_object(response, api_key)
