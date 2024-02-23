from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods(
    "refresh_client_token", path="actions/refresh_client_token", operations=["create"]
)
@nested_resource_class_methods(
    "generate_join_client_token",
    path="actions/generate_join_client_token",
    operations=["create"],
)
class RoomsClientToken(CreateableAPIResource):
    OBJECT_NAME = "rooms_client_token"

    def refresh_client_token(self, **params):
        return self.create_refresh_client_token(**params)

    def generate_join_client_token(self, **params):
        return self.create_generate_join_client_token(**params)
