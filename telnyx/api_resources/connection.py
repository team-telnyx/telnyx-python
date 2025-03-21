from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    ListableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods("active_call", path="active_calls", operations=["list"])
class Connection(ListableAPIResource):
    OBJECT_NAME = "connection"
    
    def active_calls(self, **params):
        """
        List all active calls for a given connection.

        Returns:
            A list of active calls for the connection.
        """
        return self.list_active_calls(self.id, **params)
