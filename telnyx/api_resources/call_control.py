from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import CreateableAPIResource
from telnyx.api_resources.abstract import nested_resource_class_methods


@nested_resource_class_methods(
    "reject", path="actions/reject", operations=["create"], quote_params=False
)
@nested_resource_class_methods(
    "answer", path="actions/answer", operations=["create"], quote_params=False
)
@nested_resource_class_methods(
    "hangup", path="actions/hangup", operations=["create"], quote_params=False
)
@nested_resource_class_methods(
    "bridge", path="actions/bridge", operations=["create"], quote_params=False
)
@nested_resource_class_methods(
    "fork_start", path="actions/fork_start", operations=["create"], quote_params=False
)
@nested_resource_class_methods(
    "fork_stop", path="actions/fork_stop", operations=["create"], quote_params=False
)
@nested_resource_class_methods(
    "gather_using_audio",
    path="actions/gather_using_audio",
    operations=["create"],
    quote_params=False,
)
@nested_resource_class_methods(
    "gather_using_speak",
    path="actions/gather_using_speak",
    operations=["create"],
    quote_params=False,
)
@nested_resource_class_methods(
    "playback_start",
    path="actions/playback_start",
    operations=["create"],
    quote_params=False,
)
@nested_resource_class_methods(
    "playback_stop",
    path="actions/playback_stop",
    operations=["create"],
    quote_params=False,
)
@nested_resource_class_methods(
    "record_start",
    path="actions/record_start",
    operations=["create"],
    quote_params=False,
)
@nested_resource_class_methods(
    "record_stop", path="actions/record_stop", operations=["create"], quote_params=False
)
@nested_resource_class_methods(
    "send_dtmf", path="actions/send_dtmf", operations=["create"], quote_params=False
)
@nested_resource_class_methods(
    "speak", path="actions/speak", operations=["create"], quote_params=False
)
@nested_resource_class_methods(
    "transfer", path="actions/transfer", operations=["create"], quote_params=False
)
class CallControl(CreateableAPIResource):
    OBJECT_NAME = "call"

    def reject(self, **params):
        return CallControl.create_reject(self.call_control_id, **params)

    def answer(self, **params):
        return CallControl.create_answer(self.call_control_id, **params)

    def hangup(self, **params):
        return CallControl.create_hangup(self.call_control_id, **params)

    def bridge(self, **params):
        return CallControl.create_bridge(self.call_control_id, **params)

    def fork_start(self, **params):
        return CallControl.create_fork_start(self.call_control_id, **params)

    def fork_stop(self, **params):
        return CallControl.create_fork_stop(self.call_control_id, **params)

    def gather_using_audio(self, **params):
        return CallControl.create_gather_using_audio(self.call_control_id, **params)

    def gather_using_speak(self, **params):
        return CallControl.create_gather_using_speak(self.call_control_id, **params)

    def playback_start(self, **params):
        return CallControl.create_playback_start(self.call_control_id, **params)

    def playback_stop(self, **params):
        return CallControl.create_playback_stop(self.call_control_id, **params)

    def record_start(self, **params):
        return CallControl.create_record_start(self.call_control_id, **params)

    def record_stop(self, **params):
        return CallControl.create_record_stop(self.call_control_id, **params)

    def send_dtmf(self, **params):
        return CallControl.create_send_dtmf(self.call_control_id, **params)

    def speak(self, **params):
        return CallControl.create_speak(self.call_control_id, **params)

    def transfer(self, **params):
        return CallControl.create_transfer(self.call_control_id, **params)
