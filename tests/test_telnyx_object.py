from __future__ import absolute_import, division, print_function

import datetime
import json
import pickle
from copy import copy, deepcopy

import pytest

import telnyx
from telnyx import six

SAMPLE_FOO = json.loads(
    """
{
  "record_type": "foo",
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "organization_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "name": "New Messaging Profile",
  "created_at": "2019-01-23T18:10:02.574Z",
  "updated_at": "2019-01-23T18:10:02.574Z",
  "calls": {
    "outbound": [],
    "inbound": [
        {
            "record_type": "call",
            "started_at": "2019-01-23T18:10:02.574Z",
            "ended_at": "2019-01-23T18:10:02.574Z",
            "metadata": {
                "foo": "bar"
            }
        }
    ],
    "on_net": []
    }
}
"""
)


class TestTelnyxObject(object):
    def test_initializes_with_parameters(self):
        obj = telnyx.telnyx_object.TelnyxObject(
            "foo", "bar", myparam=5, yourparam="boo"
        )

        assert obj.id == "foo"
        assert obj.api_key == "bar"

    def test_access(self):
        obj = telnyx.telnyx_object.TelnyxObject("myid", "mykey", myparam=5)

        # Empty
        with pytest.raises(AttributeError):
            obj.myattr
        with pytest.raises(KeyError):
            obj["myattr"]
        assert obj.get("myattr", "def") == "def"
        assert obj.get("myattr") is None

        # Setters
        obj.myattr = "myval"
        obj["myitem"] = "itval"
        assert obj.setdefault("mydef", "sdef") == "sdef"

        # Getters
        assert obj.setdefault("myattr", "sdef") == "myval"
        assert obj.myattr == "myval"
        assert obj["myattr"] == "myval"
        assert obj.get("myattr") == "myval"

        assert sorted(obj.keys()) == ["id", "myattr", "mydef", "myitem"]

        assert sorted(obj.values()) == ["itval", "myid", "myval", "sdef"]

        # Illegal operations
        with pytest.raises(ValueError):
            obj.foo = ""

    def test_refresh_from(self, mocker):
        obj = telnyx.telnyx_object.TelnyxObject.construct_from(
            {"foo": "bar", "trans": "me"}, "mykey"
        )

        assert obj.api_key == "mykey"
        assert obj.foo == "bar"
        assert obj["trans"] == "me"
        assert obj.last_response is None

        last_response = mocker.Mock()
        obj.refresh_from(
            {"foo": "baz", "johnny": 5}, "key2", last_response=last_response
        )

        assert obj.johnny == 5
        assert obj.foo == "baz"
        with pytest.raises(AttributeError):
            obj.trans
        assert obj.api_key == "key2"
        assert obj.last_response == last_response

        obj.refresh_from({"trans": 4, "metadata": {"amount": 42}}, "key2", True)

        assert obj.foo == "baz"
        assert obj.trans == 4

    def test_passing_nested_refresh(self):
        obj = telnyx.telnyx_object.TelnyxObject.construct_from(
            {"foos": {"type": "list", "data": [{"id": "nested"}]}}, "key"
        )

        nested = obj.foos.data[0]

        assert obj.api_key == "key"
        assert nested.id == "nested"
        assert nested.api_key == "key"

    def test_refresh_from_nested_object(self):
        obj = telnyx.telnyx_object.TelnyxObject.construct_from(SAMPLE_FOO, "key")

        assert len(obj.calls.inbound) == 1
        assert isinstance(obj.calls.inbound[0], telnyx.telnyx_object.TelnyxObject)
        assert obj.calls.inbound[0].metadata.foo == "bar"

    def test_to_json(self):
        obj = telnyx.telnyx_object.TelnyxObject.construct_from(SAMPLE_FOO, "key")

        self.check_data(json.loads(str(obj)))

    def check_data(self, data):
        # Check rough structure
        assert len(list(data.keys())) == 7
        assert len(list(data["calls"].keys())) == 3
        assert len(data["calls"]["inbound"]) == 1
        assert len(data["calls"]["outbound"]) == 0
        assert len(data["calls"]["on_net"]) == 0

    def test_repr(self):
        obj = telnyx.telnyx_object.TelnyxObject("foo", "bar", myparam=5)

        obj["record_type"] = u"\u4e00boo\u1f00"
        obj.date = datetime.datetime.fromtimestamp(1511136000)

        res = repr(obj)

        if six.PY2:
            res = six.text_type(repr(obj), "utf-8")

        assert u"<TelnyxObject \u4e00boo\u1f00" in res
        assert u"id=foo" in res
        assert u'"date": 1511136000' in res

    def test_pickling(self):
        obj = telnyx.telnyx_object.TelnyxObject("foo", "bar", myparam=5)

        obj["object"] = "boo"
        obj.refresh_from(
            {
                "fala": "lalala",
                # ensures that empty strings are correctly unpickled in Py3
                "emptystring": "",
            },
            api_key="bar",
            partial=True,
        )

        assert obj.fala == "lalala"

        pickled = pickle.dumps(obj)
        newobj = pickle.loads(pickled)

        assert newobj.id == "foo"
        assert newobj.api_key == "bar"
        assert newobj["object"] == "boo"
        assert newobj.fala == "lalala"
        assert newobj.emptystring == ""

    def test_deletion(self):
        obj = telnyx.telnyx_object.TelnyxObject("id", "key")

        obj.coupon = "foo"
        assert obj.coupon == "foo"

        del obj.coupon
        with pytest.raises(AttributeError):
            obj.coupon

        obj.refresh_from({"coupon": "foo"}, api_key="bar", partial=True)
        assert obj.coupon == "foo"

    def test_copy(self):
        nested = telnyx.telnyx_object.TelnyxObject.construct_from(
            {"value": "bar"}, "mykey"
        )
        obj = telnyx.telnyx_object.TelnyxObject.construct_from(
            {"empty": "", "value": "foo", "nested": nested}, "mykey"
        )

        copied = copy(obj)

        assert copied.empty == ""
        assert copied.value == "foo"
        assert copied.nested.value == "bar"

        assert copied.api_key == "mykey"

        # Verify that we're not deep copying nested values.
        assert id(nested) == id(copied.nested)

    def test_deepcopy(self):
        nested = telnyx.telnyx_object.TelnyxObject.construct_from(
            {"value": "bar"}, "mykey"
        )
        obj = telnyx.telnyx_object.TelnyxObject.construct_from(
            {"empty": "", "value": "foo", "nested": nested}, "mykey"
        )

        copied = deepcopy(obj)

        assert copied.empty == ""
        assert copied.value == "foo"
        assert copied.nested.value == "bar"

        assert copied.api_key == "mykey"

        # Verify that we're actually deep copying nested values.
        assert id(nested) != id(copied.nested)

    def test_serialize_empty_string_unsets(self):
        class SerializeToEmptyString(telnyx.telnyx_object.TelnyxObject):
            def serialize(self, previous):
                return ""

        nested = SerializeToEmptyString.construct_from({"value": "bar"}, "mykey")
        obj = telnyx.telnyx_object.TelnyxObject.construct_from(
            {"nested": nested}, "mykey"
        )

        assert obj.serialize(None) == {"nested": ""}
