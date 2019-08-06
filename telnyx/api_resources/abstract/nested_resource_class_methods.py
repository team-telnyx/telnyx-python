from __future__ import absolute_import, division, print_function

from telnyx import api_requestor, util
from telnyx.six.moves.urllib.parse import quote_plus


def nested_resource_class_methods(resource, path=None, operations=None):
    if path is None:
        path = "%ss" % resource
    if operations is None:
        raise ValueError("operations list required")

    def wrapper(cls):
        def nested_resource_url(cls, id, nested_id=None):
            parts = [cls.class_url()]
            if id is not None:
                parts.append(quote_plus(id, safe=util.telnyx_valid_id_parts))
            parts.append(quote_plus(path, safe="/"))
            if nested_id is not None:
                parts.append(quote_plus(nested_id, safe=util.telnyx_valid_id_parts))
            return "/".join(parts)

        resource_url_method = "%ss_url" % resource
        setattr(cls, resource_url_method, classmethod(nested_resource_url))

        def nested_resource_request(cls, method, url, api_key=None, **params):
            requestor = api_requestor.APIRequestor(api_key)
            response, api_key = requestor.request(method, url, params)
            return util.convert_to_telnyx_object(response, api_key)

        resource_request_method = "%ss_request" % resource
        setattr(cls, resource_request_method, classmethod(nested_resource_request))

        for operation in operations:
            if operation == "create":

                def create_nested_resource(cls, id, **params):
                    url = getattr(cls, resource_url_method)(id)
                    return getattr(cls, resource_request_method)("post", url, **params)

                create_method = "create_%s" % resource
                setattr(cls, create_method, classmethod(create_nested_resource))

            elif operation == "retrieve":

                def retrieve_nested_resource(cls, id, nested_id, **params):
                    url = getattr(cls, resource_url_method)(id, nested_id)
                    return getattr(cls, resource_request_method)("get", url, **params)

                retrieve_method = "retrieve_%s" % resource
                setattr(cls, retrieve_method, classmethod(retrieve_nested_resource))

            elif operation == "update":

                def modify_nested_resource(cls, id, nested_id, **params):
                    url = getattr(cls, resource_url_method)(id, nested_id)
                    return getattr(cls, resource_request_method)("post", url, **params)

                modify_method = "modify_%s" % resource
                setattr(cls, modify_method, classmethod(modify_nested_resource))

            elif operation == "delete":

                def delete_nested_resource(cls, id, nested_id, **params):
                    url = getattr(cls, resource_url_method)(id, nested_id)
                    return getattr(cls, resource_request_method)(
                        "delete", url, **params
                    )

                delete_method = "delete_%s" % resource
                setattr(cls, delete_method, classmethod(delete_nested_resource))

            elif operation == "list":

                def list_nested_resources(cls, id, **params):
                    url = getattr(cls, resource_url_method)(id)
                    return getattr(cls, resource_request_method)("get", url, **params)

                list_method = "list_%ss" % resource
                setattr(cls, list_method, classmethod(list_nested_resources))

            else:
                raise ValueError("Unknown operation: %s" % operation)

        return cls

    return wrapper
