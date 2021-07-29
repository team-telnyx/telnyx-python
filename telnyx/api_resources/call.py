from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods("reject", path="actions/reject", operations=["create"])
@nested_resource_class_methods("answer", path="actions/answer", operations=["create"])
@nested_resource_class_methods("hangup", path="actions/hangup", operations=["create"])
@nested_resource_class_methods("bridge", path="actions/bridge", operations=["create"])
@nested_resource_class_methods("speak", path="actions/speak", operations=["create"])
@nested_resource_class_methods(
    "fork_start", path="actions/fork_start", operations=["create"]
)
@nested_resource_class_methods(
    "fork_stop", path="actions/fork_stop", operations=["create"]
)
@nested_resource_class_methods(
    "gather_using_audio", path="actions/gather_using_audio", operations=["create"]
)
@nested_resource_class_methods(
    "gather_using_speak", path="actions/gather_using_speak", operations=["create"]
)
@nested_resource_class_methods(
    "gather_stop", path="actions/gather_stop", operations=["create"]
)
@nested_resource_class_methods(
    "playback_start", path="actions/playback_start", operations=["create"]
)
@nested_resource_class_methods(
    "playback_stop", path="actions/playback_stop", operations=["create"]
)
@nested_resource_class_methods(
    "record_pause", path="actions/record_pause", operations=["create"]
)
@nested_resource_class_methods(
    "record_resume", path="actions/record_resume", operations=["create"]
)
@nested_resource_class_methods(
    "record_start", path="actions/record_start", operations=["create"]
)
@nested_resource_class_methods(
    "record_stop", path="actions/record_stop", operations=["create"]
)
@nested_resource_class_methods("refer", path="actions/refer", operations=["create"])
@nested_resource_class_methods(
    "send_dtmf", path="actions/send_dtmf", operations=["create"]
)
@nested_resource_class_methods(
    "transcription_start", path="actions/transcription_start", operations=["create"]
)
@nested_resource_class_methods(
    "transcription_stop", path="actions/transcription_stop", operations=["create"]
)
@nested_resource_class_methods(
    "transfer", path="actions/transfer", operations=["create"]
)
@nested_resource_class_methods("enqueue", path="actions/enqueue", operations=["create"])
@nested_resource_class_methods(
    "leave_queue", path="actions/leave_queue", operations=["create"]
)
class Call(CreateableAPIResource):
    OBJECT_NAME = "call"

    def reject(self, **params):
        return Call.create_reject(self.call_control_id, **params)

    def answer(self, **params):
        return Call.create_answer(self.call_control_id, **params)

    def hangup(self, **params):
        return Call.create_hangup(self.call_control_id, **params)

    def bridge(self, **params):
        return Call.create_bridge(self.call_control_id, **params)

    def fork_start(self, **params):
        return Call.create_fork_start(self.call_control_id, **params)

    def fork_stop(self, **params):
        return Call.create_fork_stop(self.call_control_id, **params)

    def gather_using_audio(self, **params):
        return Call.create_gather_using_audio(self.call_control_id, **params)

    def gather_using_speak(self, **params):
        return Call.create_gather_using_speak(self.call_control_id, **params)

    def gather_stop(self, **params):
        return Call.create_gather_stop(self.call_control_id, **params)

    def playback_start(self, **params):
        return Call.create_playback_start(self.call_control_id, **params)

    def playback_stop(self, **params):
        return Call.create_playback_stop(self.call_control_id, **params)

    def record_pause(self, **params):
        return Call.create_record_pause(self.call_control_id, **params)

    def record_resume(self, **params):
        return Call.create_record_resume(self.call_control_id, **params)

    def record_start(self, **params):
        return Call.create_record_start(self.call_control_id, **params)

    def record_stop(self, **params):
        return Call.create_record_stop(self.call_control_id, **params)

    def refer(self, **params):
        return Call.create_refer(self.call_control_id, **params)

    def send_dtmf(self, **params):
        return Call.create_send_dtmf(self.call_control_id, **params)

    def speak(self, **params):
        return Call.create_speak(self.call_control_id, **params)

    def transcription_start(self, **params):
        return Call.create_transcription_start(self.call_control_id, **params)

    def transcription_stop(self, **params):
        return Call.create_transcription_stop(self.call_control_id, **params)

    def transfer(self, **params):
        return Call.create_transfer(self.call_control_id, **params)

    def enqueue(self, queue_name, **params):
        params["queue_name"] = queue_name
        return Call.create_enqueue(self.call_control_id, **params)

    def leave_queue(self, **params):
        return Call.create_leave_queue(self.call_control_id, **params)
