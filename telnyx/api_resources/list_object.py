from __future__ import absolute_import, division, print_function

from telnyx import util
from telnyx.six.moves.urllib.parse import quote_plus
from telnyx.telnyx_object import TelnyxObject


class ListObject(TelnyxObject):
    def list(self, **params):
        r = self.request("get", self["url"], params)
        r["url"] = self["url"]

        return r

    @classmethod
    def empty_list(cls, params, url):
        list_object = ListObject()
        list_object.retrieve_params = params
        list_object.url = url
        list_object.data = []
        return list_object

    def auto_paging_iter(self):
        page = self
        params = dict(self._retrieve_params)

        while True:
            for item in page.data:
                yield item
            if page.empty():
                return

            page = page.next_page(**params)

    def auto_paging_iter_by_token(self):
        page = self
        params = dict(self._retrieve_params)

        while True:
            for item in page.data:
                yield item
            if page.empty():
                return

            page = page.next_page_by_token(**params)

    def empty(self):
        return len(self.data) == 0

    def next_page(self, **params):
        if not self.has_more():
            return ListObject.empty_list(params, self.url)

        next_page_number = self.page_number() + 1
        pagination = {"number": next_page_number, "size": self.page_size()}
        params["page"] = pagination

        return self.list(**params)

    def next_page_by_token(self, **params):
        if self.token() is None:
            return ListObject.empty_list(params, self.url)

        pagination = {"token": self.token()}
        params["page"] = pagination

        return self.list(**params)

    def previous_page(self, **params):
        prev_page_number = self.page_number() - 1
        prev_page_number = max(prev_page_number, 1)
        pagination = {"number": prev_page_number, "size": self.page_size()}
        params["page"] = pagination

        return self.list(**params)

    def has_more(self):
        return self.data != [] and self.get("meta", {}).get(
            "total_pages", 0
        ) > self.get("meta", {}).get("page_number", 0)

    def token(self):
        return self.get("meta", {}).get("next_page_token", None)

    def page_number(self):
        return self.get("meta", {}).get("page_number", 1)

    def page_size(self):
        return self.get("meta", {}).get("page_size", 20)

    def create(self, **params):
        return self.request("post", self["url"], params)

    def retrieve(self, id, **params):
        base = self.get("url")
        id = util.utf8(id)
        extn = quote_plus(id)
        url = "%s/%s" % (base, extn)

        return self.request("get", url, params)

    def __iter__(self):
        return getattr(self, "data", []).__iter__()

    def __len__(self):
        return getattr(self, "data", []).__len__()
