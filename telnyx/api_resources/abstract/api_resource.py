from __future__ import absolute_import, division, print_function

from telnyx import error, six, util
from telnyx.six.moves.urllib.parse import quote_plus
from telnyx.telnyx_object import TelnyxObject


class APIResource(TelnyxObject):
    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        instance = cls(id, api_key, **params)
        response = instance.request("get", instance.instance_url())

        # It's not always the case that `cls.retrieve()` should return an
        # object of type `cls`, as the response's `record_type` might indicate
        # another `telnyx.api_resources.*` type.
        #
        # If this is the case, we simply return the already initialised
        # `response` instance.
        #
        # Otherwise, we will have an object of type `TelnyxObject`, the
        # default type returned by `util.convert_to_telnyx_object`, and we
        # promote the object back to an `APIResource`.
        if type(response) == TelnyxObject:
            instance.refresh_from(response)

            return instance
        else:
            return response

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
