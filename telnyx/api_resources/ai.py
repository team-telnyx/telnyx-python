from __future__ import absolute_import, division, print_function

from telnyx.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    nested_resource_class_methods,
)


@nested_resource_class_methods("generate", path="generate", operations=["create"])
@nested_resource_class_methods(
    "generate_stream", path="generate_stream", operations=["create"]
)
@nested_resource_class_methods("summarize", path="summarize", operations=["create"])
@nested_resource_class_methods("embeddings", path="embeddings", operations=["create"])
@nested_resource_class_methods(
    "similarity_search", path="embeddings/similarity-search", operations=["create"]
)
class AI(CreateableAPIResource, DeletableAPIResource, ListableAPIResource):
    OBJECT_NAME = "ai"

    def generate(self, **params):
        return AI.create_generate(**params)

    def generate_stream(self, **params):
        return AI.create_generate_stream(**params)

    def summarize(self, **params):
        return AI.create_summarize(**params)

    def embeddings(self, **params):
        return AI.create_embeddings(**params)

    def similarity_search(self, **params):
        return AI.create_simalarity_search
