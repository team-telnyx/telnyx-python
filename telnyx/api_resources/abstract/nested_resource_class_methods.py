from __future__ import absolute_import, division, print_function

from six.moves.urllib.parse import quote_plus

from telnyx import api_requestor, util


def nested_resource_class_methods(
    resource, path=None, operations=None, pluralize_path=True
):
    def make_path(v):
        if pluralize_path:
            return "%ss" % v
        else:
            return v

    if path is None:
        path = make_path(resource)
    if operations is None:
        raise ValueError("operations list required")

    def wrapper(cls):
        def nested_resource_url(cls, id, nested_id=None):
            parts = []
            if not path.startswith("/"):
                parts.append(cls.class_url())
            if id is not None and "phone_number" not in path:
                parts.append(quote_plus(id, safe=util.telnyx_valid_id_parts))
            if id is not None:
                if "phone_number" in path:
                    parts.append(path.format(phone_number=quote_plus(id, safe=util.telnyx_valid_id_parts + '+')))
                elif "verification_id" in path:
                    parts.append(path.format(verification_id=quote_plus(id, safe=util.telnyx_valid_id_parts)))
                else:
                    parts.append(path)
            else:
                parts.append(path)
            if nested_id is not None:
                parts.append(quote_plus(nested_id, safe=util.telnyx_valid_id_parts))
            return "/".join(parts)

        resource_url_method = "%s_url" % make_path(resource)
        setattr(cls, resource_url_method, classmethod(nested_resource_url))

        def nested_resource_request(cls, method, url, api_key=None, **params):
            requestor = api_requestor.APIRequestor(api_key)
            params = util.rewrite_reserved_words(params)
            response, api_key = requestor.request(method, url, params)
            return util.convert_to_telnyx_object(response, api_key)

        resource_request_method = "%s_request" % make_path(resource)
        setattr(cls, resource_request_method, classmethod(nested_resource_request))

        for operation in operations:
            if operation == "create":

                def create_nested_resource(cls, id, **params):
                    url = getattr(cls, resource_url_method)(id)
                    return getattr(cls, resource_request_method)("post", url, **params)

                create_method = "create_%s" % resource
                setattr(cls, create_method, classmethod(create_nested_resource))

            elif operation == "retrieve":

                def retrieve_nested_resource(cls, id, nested_id=None, **params):
                    url = getattr(cls, resource_url_method)(id, nested_id=nested_id)
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

                list_method = "list_%s" % make_path(resource)
                setattr(cls, list_method, classmethod(list_nested_resources))

            elif operation == "put":

                def update_nested_resource(cls, id, nested_id, **params):
                    url = getattr(cls, resource_url_method)(id, nested_id)
                    return getattr(cls, resource_request_method)("put", url, **params)

                update_method = "update_%s" % resource
                setattr(cls, update_method, classmethod(update_nested_resource))

            else:
                raise ValueError("Unknown operation: %s" % operation)

        return cls

    return wrapper
