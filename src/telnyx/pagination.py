# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Any, List, Type, Generic, Mapping, TypeVar, Optional, cast
from typing_extensions import override

from httpx import Response
from pydantic import Field as FieldInfo

from ._utils import is_mapping
from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "DefaultFlatPaginationMeta",
    "SyncDefaultFlatPagination",
    "AsyncDefaultFlatPagination",
    "SyncDefaultFlatPaginationTopLevelArray",
    "AsyncDefaultFlatPaginationTopLevelArray",
    "DefaultPaginationForLogMessagesMeta",
    "SyncDefaultPaginationForLogMessages",
    "AsyncDefaultPaginationForLogMessages",
    "SyncDefaultPaginationForMessagingTollfree",
    "AsyncDefaultPaginationForMessagingTollfree",
    "SyncDefaultPaginationForQueues",
    "AsyncDefaultPaginationForQueues",
    "DefaultFlatPaginationForInexplicitNumberOrdersMeta",
    "SyncDefaultFlatPaginationForInexplicitNumberOrders",
    "AsyncDefaultFlatPaginationForInexplicitNumberOrders",
    "PerPagePaginationMeta",
    "SyncPerPagePagination",
    "AsyncPerPagePagination",
    "SyncPerPagePaginationV2",
    "AsyncPerPagePaginationV2",
]

_BaseModelT = TypeVar("_BaseModelT", bound=BaseModel)

_T = TypeVar("_T")


class DefaultFlatPaginationMeta(BaseModel):
    page_number: int

    total_pages: int


class SyncDefaultFlatPagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    meta: Optional[DefaultFlatPaginationMeta] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = None
        if self.meta is not None:
            if self.meta.page_number is not None:  # pyright: ignore[reportUnnecessaryComparison]
                current_page = self.meta.page_number
        if current_page is None:
            current_page = 1

        total_pages = None
        if self.meta is not None:
            if self.meta.total_pages is not None:  # pyright: ignore[reportUnnecessaryComparison]
                total_pages = self.meta.total_pages
        if total_pages is not None and current_page >= total_pages:
            return None

        return PageInfo(params={"page[number]": current_page + 1})


class AsyncDefaultFlatPagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    meta: Optional[DefaultFlatPaginationMeta] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = None
        if self.meta is not None:
            if self.meta.page_number is not None:  # pyright: ignore[reportUnnecessaryComparison]
                current_page = self.meta.page_number
        if current_page is None:
            current_page = 1

        total_pages = None
        if self.meta is not None:
            if self.meta.total_pages is not None:  # pyright: ignore[reportUnnecessaryComparison]
                total_pages = self.meta.total_pages
        if total_pages is not None and current_page >= total_pages:
            return None

        return PageInfo(params={"page[number]": current_page + 1})


class SyncDefaultFlatPaginationTopLevelArray(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page[number]")) or 1

        return PageInfo(params={"page[number]": last_page + 1})

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:  # noqa: ARG003
        return cls.construct(
            None,
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
            },
        )


class AsyncDefaultFlatPaginationTopLevelArray(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page[number]")) or 1

        return PageInfo(params={"page[number]": last_page + 1})

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:  # noqa: ARG003
        return cls.construct(
            None,
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
            },
        )


class DefaultPaginationForLogMessagesMeta(BaseModel):
    page_number: int

    total_pages: int


class SyncDefaultPaginationForLogMessages(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    log_messages: List[_T]
    meta: Optional[DefaultPaginationForLogMessagesMeta] = None

    @override
    def _get_page_items(self) -> List[_T]:
        log_messages = self.log_messages
        if not log_messages:
            return []
        return log_messages

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = None
        if self.meta is not None:
            if self.meta.page_number is not None:  # pyright: ignore[reportUnnecessaryComparison]
                current_page = self.meta.page_number
        if current_page is None:
            current_page = 1

        total_pages = None
        if self.meta is not None:
            if self.meta.total_pages is not None:  # pyright: ignore[reportUnnecessaryComparison]
                total_pages = self.meta.total_pages
        if total_pages is not None and current_page >= total_pages:
            return None

        return PageInfo(params={"page[number]": current_page + 1})


class AsyncDefaultPaginationForLogMessages(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    log_messages: List[_T]
    meta: Optional[DefaultPaginationForLogMessagesMeta] = None

    @override
    def _get_page_items(self) -> List[_T]:
        log_messages = self.log_messages
        if not log_messages:
            return []
        return log_messages

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = None
        if self.meta is not None:
            if self.meta.page_number is not None:  # pyright: ignore[reportUnnecessaryComparison]
                current_page = self.meta.page_number
        if current_page is None:
            current_page = 1

        total_pages = None
        if self.meta is not None:
            if self.meta.total_pages is not None:  # pyright: ignore[reportUnnecessaryComparison]
                total_pages = self.meta.total_pages
        if total_pages is not None and current_page >= total_pages:
            return None

        return PageInfo(params={"page[number]": current_page + 1})


class SyncDefaultPaginationForMessagingTollfree(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    records: List[_T]
    total_records: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        records = self.records
        if not records:
            return []
        return records

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page")) or 1

        total_pages = self.total_records
        if total_pages is not None and last_page >= total_pages:
            return None

        return PageInfo(params={"page": last_page + 1})


class AsyncDefaultPaginationForMessagingTollfree(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    records: List[_T]
    total_records: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        records = self.records
        if not records:
            return []
        return records

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page")) or 1

        total_pages = self.total_records
        if total_pages is not None and last_page >= total_pages:
            return None

        return PageInfo(params={"page": last_page + 1})


class SyncDefaultPaginationForQueues(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    queues: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        queues = self.queues
        if not queues:
            return []
        return queues

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("Page")) or 1

        return PageInfo(params={"Page": last_page + 1})


class AsyncDefaultPaginationForQueues(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    queues: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        queues = self.queues
        if not queues:
            return []
        return queues

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("Page")) or 1

        return PageInfo(params={"Page": last_page + 1})


class DefaultFlatPaginationForInexplicitNumberOrdersMeta(BaseModel):
    page_number: int

    total_pages: int


class SyncDefaultFlatPaginationForInexplicitNumberOrders(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    meta: Optional[DefaultFlatPaginationForInexplicitNumberOrdersMeta] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = None
        if self.meta is not None:
            if self.meta.page_number is not None:  # pyright: ignore[reportUnnecessaryComparison]
                current_page = self.meta.page_number
        if current_page is None:
            current_page = 1

        total_pages = None
        if self.meta is not None:
            if self.meta.total_pages is not None:  # pyright: ignore[reportUnnecessaryComparison]
                total_pages = self.meta.total_pages
        if total_pages is not None and current_page >= total_pages:
            return None

        return PageInfo(params={"page_number": current_page + 1})


class AsyncDefaultFlatPaginationForInexplicitNumberOrders(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    meta: Optional[DefaultFlatPaginationForInexplicitNumberOrdersMeta] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = None
        if self.meta is not None:
            if self.meta.page_number is not None:  # pyright: ignore[reportUnnecessaryComparison]
                current_page = self.meta.page_number
        if current_page is None:
            current_page = 1

        total_pages = None
        if self.meta is not None:
            if self.meta.total_pages is not None:  # pyright: ignore[reportUnnecessaryComparison]
                total_pages = self.meta.total_pages
        if total_pages is not None and current_page >= total_pages:
            return None

        return PageInfo(params={"page_number": current_page + 1})


class PerPagePaginationMeta(BaseModel):
    page_number: int

    total_pages: int


class SyncPerPagePagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    meta: Optional[PerPagePaginationMeta] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = None
        if self.meta is not None:
            if self.meta.page_number is not None:  # pyright: ignore[reportUnnecessaryComparison]
                current_page = self.meta.page_number
        if current_page is None:
            current_page = 1

        total_pages = None
        if self.meta is not None:
            if self.meta.total_pages is not None:  # pyright: ignore[reportUnnecessaryComparison]
                total_pages = self.meta.total_pages
        if total_pages is not None and current_page >= total_pages:
            return None

        return PageInfo(params={"page": current_page + 1})


class AsyncPerPagePagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    meta: Optional[PerPagePaginationMeta] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = None
        if self.meta is not None:
            if self.meta.page_number is not None:  # pyright: ignore[reportUnnecessaryComparison]
                current_page = self.meta.page_number
        if current_page is None:
            current_page = 1

        total_pages = None
        if self.meta is not None:
            if self.meta.total_pages is not None:  # pyright: ignore[reportUnnecessaryComparison]
                total_pages = self.meta.total_pages
        if total_pages is not None and current_page >= total_pages:
            return None

        return PageInfo(params={"page": current_page + 1})


class SyncPerPagePaginationV2(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    records: List[_T]
    page: int
    total_records: int = FieldInfo(alias="totalRecords")

    @override
    def _get_page_items(self) -> List[_T]:
        records = self.records
        if not records:
            return []
        return records

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = self.page

        total_pages = self.total_records
        if current_page >= total_pages:
            return None

        return PageInfo(params={"page": current_page + 1})


class AsyncPerPagePaginationV2(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    records: List[_T]
    page: int
    total_records: int = FieldInfo(alias="totalRecords")

    @override
    def _get_page_items(self) -> List[_T]:
        records = self.records
        if not records:
            return []
        return records

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = self.page

        total_pages = self.total_records
        if current_page >= total_pages:
            return None

        return PageInfo(params={"page": current_page + 1})
