from __future__ import absolute_import, division, print_function

import io
import logging
import os
import re
import sys

from six.moves.urllib.parse import parse_qsl

import telnyx
from telnyx import six

TELNYX_LOG = os.environ.get("TELNYX_LOG")

logger = logging.getLogger("telnyx")

__all__ = ["io", "parse_qsl", "utf8", "log_info", "log_debug", "logfmt"]

# Special valid characters in telnyx id's objects. Format: `=/$#`
telnyx_valid_id_parts = "=-"


def utf8(value):
    if six.PY2 and isinstance(value, six.text_type):
        return value.encode("utf-8")
    else:
        return value


def is_appengine_dev():
    return "APPENGINE_RUNTIME" in os.environ and "Dev" in os.environ.get(
        "SERVER_SOFTWARE", ""
    )


def _console_log_level():
    if telnyx.log in ["debug", "info"]:
        return telnyx.log
    elif TELNYX_LOG in ["debug", "info"]:
        return TELNYX_LOG
    else:
        return None


# Rewrites reserved word keyword arguments
# This makes Message.create(to="", from_="", text="") possible
def rewrite_reserved_words(kwargs, reverse=False):
    reserved = [("from_", "from")]

    for i in reserved:
        if not reverse:
            original, replacement = i
        else:
            replacement, original = i

        if kwargs.get(original, None) is not None:
            kwargs[replacement] = kwargs.pop(original)

    return kwargs


def log_debug(message, **params):
    msg = logfmt(dict(message=message, **params))
    if _console_log_level() == "debug":
        print(msg, file=sys.stderr)
    logger.debug(msg)


def log_info(message, **params):
    msg = logfmt(dict(message=message, **params))
    if _console_log_level() in ["debug", "info"]:
        print(msg, file=sys.stderr)
    logger.info(msg)


def logfmt(props):
    def fmt(key, val):
        # Handle case where val is a bytes or bytesarray
        if six.PY3 and hasattr(val, "decode"):
            val = val.decode("utf-8")
        # Check if val is already a string to avoid re-encoding into
        # ascii. Since the code is sent through 2to3, we can't just
        # use unicode(val, encoding='utf8') since it will be
        # translated incorrectly.
        if not isinstance(val, six.string_types):
            val = six.text_type(val)
        if re.search(r"\s", val):
            val = repr(val)
        # key should already be a string
        if re.search(r"\s", key):
            key = repr(key)
        return u"{key}={val}".format(key=key, val=val)

    return u" ".join([fmt(key, val) for key, val in sorted(props.items())])


OBJECT_CLASSES = {}


def load_object_classes():
    # This is here to avoid a circular dependency
    from telnyx import api_resources

    global OBJECT_CLASSES

    OBJECT_CLASSES = {
        # business objects
        api_resources.Address.OBJECT_NAME: api_resources.Address,
        api_resources.APIKey.OBJECT_NAME: api_resources.APIKey,
        api_resources.AvailablePhoneNumber.OBJECT_NAME: api_resources.AvailablePhoneNumber,
        api_resources.Balance.OBJECT_NAME: api_resources.Balance,
        api_resources.BillingGroup.OBJECT_NAME: api_resources.BillingGroup,
        api_resources.Call.OBJECT_NAME: api_resources.Call,
        api_resources.CallControlApplication.OBJECT_NAME: api_resources.CallControlApplication,
        api_resources.Conference.OBJECT_NAME: api_resources.Conference,
        api_resources.Connection.OBJECT_NAME: api_resources.Connection,
        api_resources.CredentialConnection.OBJECT_NAME: api_resources.CredentialConnection,
        api_resources.DetailRecordsReport.OBJECT_NAME: api_resources.DetailRecordsReport,
        api_resources.Fax.OBJECT_NAME: api_resources.Fax,
        api_resources.FaxApplication.OBJECT_NAME: api_resources.FaxApplication,
        api_resources.FQDN.OBJECT_NAME: api_resources.FQDN,
        api_resources.FQDNConnection.OBJECT_NAME: api_resources.FQDNConnection,
        api_resources.InboundChannel.OBJECT_NAME: api_resources.InboundChannel,
        api_resources.IP.OBJECT_NAME: api_resources.IP,
        api_resources.IPConnection.OBJECT_NAME: api_resources.IPConnection,
        api_resources.Message.OBJECT_NAME: api_resources.Message,
        api_resources.MessagingHostedNumber.OBJECT_NAME: api_resources.MessagingHostedNumber,
        api_resources.MessagingHostedNumberOrder.OBJECT_NAME: api_resources.MessagingHostedNumberOrder,
        api_resources.MessagingPhoneNumber.OBJECT_NAME: api_resources.MessagingPhoneNumber,
        api_resources.MessagingProfile.OBJECT_NAME: api_resources.MessagingProfile,
        api_resources.MessagingSettings.OBJECT_NAME: api_resources.MessagingSettings,
        api_resources.NumberLookup.OBJECT_NAME: api_resources.NumberLookup,
        api_resources.NumberOrder.OBJECT_NAME: api_resources.NumberOrder,
        api_resources.NumberOrderPhoneNumber.OBJECT_NAME: api_resources.NumberOrderPhoneNumber,
        api_resources.NumberReservation.OBJECT_NAME: api_resources.NumberReservation,
        api_resources.OutboundVoiceProfile.OBJECT_NAME: api_resources.OutboundVoiceProfile,
        api_resources.PhoneNumber.OBJECT_NAME: api_resources.PhoneNumber,
        api_resources.PhoneNumberRegulatoryRequirement.OBJECT_NAME: api_resources.PhoneNumberRegulatoryRequirement,
        api_resources.PublicKey.OBJECT_NAME: api_resources.PublicKey,
        api_resources.Queue.OBJECT_NAME: api_resources.Queue,
        api_resources.QueueCall.OBJECT_NAME: api_resources.QueueCall,
        api_resources.RegulatoryRequirement.OBJECT_NAME: api_resources.RegulatoryRequirement,
        api_resources.SIMCard.OBJECT_NAME: api_resources.SIMCard,
        api_resources.ShortCode.OBJECT_NAME: api_resources.ShortCode,
        api_resources.TelephonyCredential.OBJECT_NAME: api_resources.TelephonyCredential,
        api_resources.TelephonyCredential.API_RECORD_TYPE_NAME: api_resources.TelephonyCredential,
        api_resources.VoiceSettings.OBJECT_NAME: api_resources.VoiceSettings,
        api_resources.Verification.OBJECT_NAME: api_resources.Verification,
        api_resources.VerifyProfile.OBJECT_NAME: api_resources.VerifyProfile,
    }


def convert_to_telnyx_object(resp, api_key=None):
    global OBJECT_CLASSES

    if len(OBJECT_CLASSES) == 0:
        load_object_classes()
    types = OBJECT_CLASSES.copy()

    # If we get a TelnyxResponse, we'll want to return a
    # TelnyxObject with the last_response field filled out with
    # the raw API response information
    telnyx_response = None

    if isinstance(resp, telnyx.telnyx_response.TelnyxResponse):
        telnyx_response = resp
        resp = telnyx_response.data

    if isinstance(resp, list):
        return [convert_to_telnyx_object(i, api_key) for i in resp]
    elif isinstance(resp, dict) and not isinstance(
        resp, telnyx.telnyx_object.TelnyxObject
    ):
        resp = resp.copy()
        resp = rewrite_reserved_words(resp, reverse=True)
        data = resp.get("data", None)
        if data:
            if isinstance(data, list):
                return telnyx.api_resources.ListObject.construct_from(
                    resp, api_key, last_response=telnyx_response
                )

            record_type = data.get("record_type", None)
            if record_type:
                klass = types.get(record_type, telnyx.telnyx_object.TelnyxObject)
                return klass.construct_from(
                    data, api_key, last_response=telnyx_response
                )

        record_type = resp.get("record_type", None)
        if record_type:
            klass = types.get(record_type, telnyx.telnyx_object.TelnyxObject)
            return klass.construct_from(resp, api_key, last_response=telnyx_response)
        else:
            klass = telnyx.telnyx_object.TelnyxObject
            return klass.construct_from(resp, api_key, last_response=telnyx_response)
    else:
        return resp
