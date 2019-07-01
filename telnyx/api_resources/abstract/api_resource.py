from __future__ import absolute_import, division, print_function

from telnyx import error, util, six
from telnyx.telnyx_object import TelnyxObject
from telnyx.six.moves.urllib.parse import quote_plus


class APIResource(TelnyxObject):
    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    def refresh(self):
        self.refresh_from(self.request("get", self.instance_url()))
        return self

    @classmethod
    def class_url(cls):
        if cls == APIResource:
            raise NotImplementedError(
                "APIResource is an abstract class.  You should perform "
                "actions on its subclasses (e.g. MessagingProfile)"
            )
        # Namespaces are separated in object names with periods (.) and in URLs
        # with forward slashes (/), so replace the former with the latter.
        base = cls.OBJECT_NAME.replace(".", "/")
        return "/v2/%ss" % (base,)

    def instance_url(self):
        id = self.get("id")

        if not isinstance(id, six.string_types):
            raise error.InvalidRequestError(
                "Could not determine which URL to request: %s instance "
                "has invalid ID: %r, %s. ID should be of type `str` (or"
                " `unicode`)" % (type(self).__name__, id, type(id)),
                "id",
            )

        id = util.utf8(id)
        base = self.class_url()
        extn = quote_plus(id)
        return "%s/%s" % (base, extn)
