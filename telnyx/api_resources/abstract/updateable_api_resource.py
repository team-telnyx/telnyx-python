from __future__ import absolute_import, division, print_function

from telnyx import api_requestor, util
from telnyx.api_resources.abstract.api_resource import APIResource
from telnyx.six.moves.urllib.parse import quote_plus


class UpdateableAPIResource(APIResource):
    @classmethod
    def _modify(cls, url, api_key=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        params = util.rewrite_reserved_words(params)
        response, api_key = requestor.request("patch", url, params)
        return util.convert_to_telnyx_object(response, api_key)

    @classmethod
    def modify(cls, sid, **params):
        url = "%s/%s" % (cls.class_url(), quote_plus(util.utf8(sid)))
        return cls._modify(url, **params)

    @classmethod
    def _putify(cls, url, api_key=None, **params):
        requestor = api_requestor.APIRequestor(api_key)
        params = util.rewrite_reserved_words(params)
        response, api_key = requestor.request("put", url, params)
        return util.convert_to_telnyx_object(response, api_key)

    @classmethod
    def putify(cls, sid, **params):
        url = "%s/%s" % (cls.class_url(), quote_plus(util.utf8(sid)))
        return cls._putify(url, **params)

    def save(self):
        updated_params = self.serialize(None)

        if updated_params:
            self.refresh_from(
                self.request(self.save_method(), self.instance_url(), updated_params)
            )
        else:
            util.logger.debug("Trying to save already saved object %r", self)
        return self

    def save_method(self):
        if self.id is None:
            return "post"
        else:
            return "patch"
