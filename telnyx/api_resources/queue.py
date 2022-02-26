from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import APIResource, nested_resource_class_methods


@nested_resource_class_methods(
    "queue_call", path="calls", operations=["list", "retrieve"]
)
class Queue(APIResource):
    OBJECT_NAME = "queue"

    def list_calls(self, **params):
        return Queue.list_queue_calls(self.name, **params)

    def retrieve_call(self, call_control_id, **params):
        return Queue.retrieve_queue_call(self.name, call_control_id, **params)


class QueueCall(APIResource):
    OBJECT_NAME = "queue_call"
