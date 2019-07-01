from __future__ import absolute_import, division, print_function

# flake8: noqa

from telnyx.api_resources.abstract.api_resource import APIResource
from telnyx.api_resources.abstract.singleton_api_resource import SingletonAPIResource

from telnyx.api_resources.abstract.createable_api_resource import CreateableAPIResource
from telnyx.api_resources.abstract.updateable_api_resource import UpdateableAPIResource
from telnyx.api_resources.abstract.deletable_api_resource import DeletableAPIResource
from telnyx.api_resources.abstract.listable_api_resource import ListableAPIResource
from telnyx.api_resources.abstract.nested_resource_class_methods import (
    nested_resource_class_methods,
)
