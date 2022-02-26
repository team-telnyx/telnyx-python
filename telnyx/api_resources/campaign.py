from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods("mno_metadata", path="mnoMetadata", operations=["list"])
@nested_resource_class_methods(
    "operation_status", path="operationStatus", operations=["list"]
)
class Campaign(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "campaign"

    @classmethod
    def class_url(cls):
        return "/10dlc/campaign"

    def mno_metadata(self, **params):
        return Campaign.list_mno_metadata(self.name, **params)

    def operation_status(self, **params):
        return Campaign.list_mno_metadata(self.name, **params)


class CampaignBuilder(CreateableAPIResource):
    OBJECT_NAME = "campaign_builder"


@nested_resource_class_methods("usecase", path="usecase", operations=["retrieve"])
class CampaignBuilderBrand(ListableAPIResource):
    OBJECT_NAME = "campaign_builder_brand"

    def download(self, **params):
        return Campaign.create_usecase(self.id, **params)
