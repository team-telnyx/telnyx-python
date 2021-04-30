from __future__ import absolute_import, division, print_function

from telnyx import error, six, util
from telnyx.api_resources.abstract import (
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)
from telnyx.six.moves.urllib.parse import quote_plus


@nested_resource_class_methods(
    "voice", operations=["list", "update"], pluralize_path=False
)
@nested_resource_class_methods(
    "enable_emergency", path="actions/enable_emergency", operations=["create"]
)
@nested_resource_class_methods(
    "messaging", path="messaging", operations=["list", "update"], pluralize_path=False
)
class PhoneNumber(DeletableAPIResource, ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME = "phone_number"

    @classmethod
    def all_voice(cls, **params):
        """Returns the voice settings for /all/ numbers owned by the user.

        This method breaks the naming convention of helper methods by adding
        an `all_` prefix, which might be confusing at first. The reason for
        this prefix is the `voice()` method name is already taken. The
        Telnyx API supports these two endpoints:

        - /v2/phone_numbers/{id}/voice
        - /v2/phone_numbers/voice

        The `/{id}/voice` endpoint is taken by the instance method `voice()`.
        As we can't nicely re-use this method for two different endpoints,
        we have this `all_voice()` endpoint to support the `/voice` endpoint.
        """

        return PhoneNumber.list_voice(None, **params)

    def voice(self, **params):
        """Returns the voice settings for the instantiated phone number."""

        return PhoneNumber.list_voice(self.id, **params)

    def enable_emergency(self, **params):
        return PhoneNumber.create_enable_emergency(self.id, **params)

    @classmethod
    def all_messaging(cls, **params):
        """Returns the messaging settings for /all/ numbers owned by the
        user.

        See the documentation for `all_voice()` for an explanation on the
        difference between `all_messaging()` and `messaging()`.
        """

        return PhoneNumber.list_messaging(None, **params)

    def messaging(self, **params):
        """Returns the messaging settings for the instantiated phone
        number.
        """

        return PhoneNumber.list_messaging(self.id, **params)


class VoiceSettings(ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME = "voice_settings"

    @classmethod
    def class_url(cls):
        return "/v2/phone_numbers/voice"

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
        extn = quote_plus(id)
        return "/v2/phone_numbers/%s/voice" % extn

    @classmethod
    def modify(cls, sid, **params):
        url = "/v2/phone_numbers/%s/voice" % quote_plus(util.utf8(sid))
        return cls._modify(url, **params)


class MessagingSettings(ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME = "messaging_settings"

    @classmethod
    def class_url(cls):
        return "/v2/phone_numbers/messaging"

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
        extn = quote_plus(id)
        return "/v2/phone_numbers/%s/messaging" % extn

    @classmethod
    def modify(cls, sid, **params):
        url = "/v2/phone_numbers/%s/messaging" % quote_plus(util.utf8(sid))
        return cls._modify(url, **params)
