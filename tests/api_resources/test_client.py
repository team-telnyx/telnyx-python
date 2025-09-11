# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from telnyx import Telnyx, AsyncTelnyx
from tests.utils import assert_matches_type
from telnyx.types import (
    ListBucketsResponse,
    ListObjectsResponse,
)
from telnyx._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClient:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_bucket(self, client: Telnyx) -> None:
        client_ = client.create_bucket(
            bucket_name="mybucket",
        )
        assert client_ is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_bucket_with_all_params(self, client: Telnyx) -> None:
        client_ = client.create_bucket(
            bucket_name="mybucket",
            location_constraint="LocationConstraint",
        )
        assert client_ is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_bucket(self, client: Telnyx) -> None:
        response = client.with_raw_response.create_bucket(
            bucket_name="mybucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert client_ is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_bucket(self, client: Telnyx) -> None:
        with client.with_streaming_response.create_bucket(
            bucket_name="mybucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert client_ is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_bucket(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.with_raw_response.create_bucket(
                bucket_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_bucket(self, client: Telnyx) -> None:
        client_ = client.delete_bucket(
            "bucketName",
        )
        assert client_ is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_bucket(self, client: Telnyx) -> None:
        response = client.with_raw_response.delete_bucket(
            "bucketName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert client_ is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_bucket(self, client: Telnyx) -> None:
        with client.with_streaming_response.delete_bucket(
            "bucketName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert client_ is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_bucket(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.with_raw_response.delete_bucket(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_object(self, client: Telnyx) -> None:
        client_ = client.delete_object(
            object_name="x",
            bucket_name="bucketName",
        )
        assert client_ is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_object(self, client: Telnyx) -> None:
        response = client.with_raw_response.delete_object(
            object_name="x",
            bucket_name="bucketName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert client_ is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_object(self, client: Telnyx) -> None:
        with client.with_streaming_response.delete_object(
            object_name="x",
            bucket_name="bucketName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert client_ is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_object(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.with_raw_response.delete_object(
                object_name="x",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.with_raw_response.delete_object(
                object_name="",
                bucket_name="bucketName",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_objects(self, client: Telnyx) -> None:
        client_ = client.delete_objects(
            bucket_name="bucketName",
            delete=True,
            body=[{}],
        )
        assert_matches_type(object, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_objects(self, client: Telnyx) -> None:
        response = client.with_raw_response.delete_objects(
            bucket_name="bucketName",
            delete=True,
            body=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(object, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_objects(self, client: Telnyx) -> None:
        with client.with_streaming_response.delete_objects(
            bucket_name="bucketName",
            delete=True,
            body=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(object, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_objects(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.with_raw_response.delete_objects(
                bucket_name="",
                delete=True,
                body=[{}],
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_object(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/bucketName/x").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        client_ = client.get_object(
            object_name="x",
            bucket_name="bucketName",
        )
        assert client_.is_closed
        assert client_.json() == {"foo": "bar"}
        assert cast(Any, client_.is_closed) is True
        assert isinstance(client_, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_object_with_all_params(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/bucketName/x").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        client_ = client.get_object(
            object_name="x",
            bucket_name="bucketName",
            upload_id="uploadId",
        )
        assert client_.is_closed
        assert client_.json() == {"foo": "bar"}
        assert cast(Any, client_.is_closed) is True
        assert isinstance(client_, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_object(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/bucketName/x").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        client_ = client.with_raw_response.get_object(
            object_name="x",
            bucket_name="bucketName",
        )

        assert client_.is_closed is True
        assert client_.http_request.headers.get("X-Stainless-Lang") == "python"
        assert client_.json() == {"foo": "bar"}
        assert isinstance(client_, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_object(self, client: Telnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/bucketName/x").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.with_streaming_response.get_object(
            object_name="x",
            bucket_name="bucketName",
        ) as client_:
            assert not client_.is_closed
            assert client_.http_request.headers.get("X-Stainless-Lang") == "python"

            assert client_.json() == {"foo": "bar"}
            assert cast(Any, client_.is_closed) is True
            assert isinstance(client_, StreamedBinaryAPIResponse)

        assert cast(Any, client_.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get_object(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.with_raw_response.get_object(
                object_name="x",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.with_raw_response.get_object(
                object_name="",
                bucket_name="bucketName",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_buckets(self, client: Telnyx) -> None:
        client_ = client.list_buckets()
        assert_matches_type(ListBucketsResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_buckets(self, client: Telnyx) -> None:
        response = client.with_raw_response.list_buckets()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(ListBucketsResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_buckets(self, client: Telnyx) -> None:
        with client.with_streaming_response.list_buckets() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(ListBucketsResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_objects(self, client: Telnyx) -> None:
        client_ = client.list_objects(
            bucket_name="xxxx",
        )
        assert_matches_type(ListObjectsResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_objects_with_all_params(self, client: Telnyx) -> None:
        client_ = client.list_objects(
            bucket_name="xxxx",
            list_type=2,
        )
        assert_matches_type(ListObjectsResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_objects(self, client: Telnyx) -> None:
        response = client.with_raw_response.list_objects(
            bucket_name="xxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(ListObjectsResponse, client_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_objects(self, client: Telnyx) -> None:
        with client.with_streaming_response.list_objects(
            bucket_name="xxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(ListObjectsResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_objects(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.with_raw_response.list_objects(
                bucket_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_put_object(self, client: Telnyx) -> None:
        client_ = client.put_object(
            object_name="x",
            bucket_name="bucketName",
            body=b"raw file contents",
        )
        assert client_ is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_put_object_with_all_params(self, client: Telnyx) -> None:
        client_ = client.put_object(
            object_name="x",
            bucket_name="bucketName",
            body=b"raw file contents",
            part_number="partNumber",
            upload_id="uploadId",
        )
        assert client_ is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_put_object(self, client: Telnyx) -> None:
        response = client.with_raw_response.put_object(
            object_name="x",
            bucket_name="bucketName",
            body=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert client_ is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_put_object(self, client: Telnyx) -> None:
        with client.with_streaming_response.put_object(
            object_name="x",
            bucket_name="bucketName",
            body=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert client_ is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_put_object(self, client: Telnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.with_raw_response.put_object(
                object_name="x",
                bucket_name="",
                body=b"raw file contents",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            client.with_raw_response.put_object(
                object_name="",
                bucket_name="bucketName",
                body=b"raw file contents",
            )


class TestAsyncClient:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_bucket(self, async_client: AsyncTelnyx) -> None:
        client = await async_client.create_bucket(
            bucket_name="mybucket",
        )
        assert client is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_bucket_with_all_params(self, async_client: AsyncTelnyx) -> None:
        client = await async_client.create_bucket(
            bucket_name="mybucket",
            location_constraint="LocationConstraint",
        )
        assert client is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_bucket(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.with_raw_response.create_bucket(
            bucket_name="mybucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert client is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_bucket(self, async_client: AsyncTelnyx) -> None:
        async with async_client.with_streaming_response.create_bucket(
            bucket_name="mybucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert client is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_bucket(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.with_raw_response.create_bucket(
                bucket_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_bucket(self, async_client: AsyncTelnyx) -> None:
        client = await async_client.delete_bucket(
            "bucketName",
        )
        assert client is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_bucket(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.with_raw_response.delete_bucket(
            "bucketName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert client is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_bucket(self, async_client: AsyncTelnyx) -> None:
        async with async_client.with_streaming_response.delete_bucket(
            "bucketName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert client is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_bucket(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.with_raw_response.delete_bucket(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_object(self, async_client: AsyncTelnyx) -> None:
        client = await async_client.delete_object(
            object_name="x",
            bucket_name="bucketName",
        )
        assert client is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_object(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.with_raw_response.delete_object(
            object_name="x",
            bucket_name="bucketName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert client is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_object(self, async_client: AsyncTelnyx) -> None:
        async with async_client.with_streaming_response.delete_object(
            object_name="x",
            bucket_name="bucketName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert client is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_object(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.with_raw_response.delete_object(
                object_name="x",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.with_raw_response.delete_object(
                object_name="",
                bucket_name="bucketName",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_objects(self, async_client: AsyncTelnyx) -> None:
        client = await async_client.delete_objects(
            bucket_name="bucketName",
            delete=True,
            body=[{}],
        )
        assert_matches_type(object, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_objects(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.with_raw_response.delete_objects(
            bucket_name="bucketName",
            delete=True,
            body=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(object, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_objects(self, async_client: AsyncTelnyx) -> None:
        async with async_client.with_streaming_response.delete_objects(
            bucket_name="bucketName",
            delete=True,
            body=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(object, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_objects(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.with_raw_response.delete_objects(
                bucket_name="",
                delete=True,
                body=[{}],
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_object(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/bucketName/x").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        client = await async_client.get_object(
            object_name="x",
            bucket_name="bucketName",
        )
        assert client.is_closed
        assert await client.json() == {"foo": "bar"}
        assert cast(Any, client.is_closed) is True
        assert isinstance(client, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_object_with_all_params(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/bucketName/x").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        client = await async_client.get_object(
            object_name="x",
            bucket_name="bucketName",
            upload_id="uploadId",
        )
        assert client.is_closed
        assert await client.json() == {"foo": "bar"}
        assert cast(Any, client.is_closed) is True
        assert isinstance(client, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_object(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/bucketName/x").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        client = await async_client.with_raw_response.get_object(
            object_name="x",
            bucket_name="bucketName",
        )

        assert client.is_closed is True
        assert client.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await client.json() == {"foo": "bar"}
        assert isinstance(client, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_object(self, async_client: AsyncTelnyx, respx_mock: MockRouter) -> None:
        respx_mock.get("/bucketName/x").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.with_streaming_response.get_object(
            object_name="x",
            bucket_name="bucketName",
        ) as client:
            assert not client.is_closed
            assert client.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await client.json() == {"foo": "bar"}
            assert cast(Any, client.is_closed) is True
            assert isinstance(client, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, client.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get_object(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.with_raw_response.get_object(
                object_name="x",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.with_raw_response.get_object(
                object_name="",
                bucket_name="bucketName",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_buckets(self, async_client: AsyncTelnyx) -> None:
        client = await async_client.list_buckets()
        assert_matches_type(ListBucketsResponse, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_buckets(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.with_raw_response.list_buckets()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(ListBucketsResponse, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_buckets(self, async_client: AsyncTelnyx) -> None:
        async with async_client.with_streaming_response.list_buckets() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(ListBucketsResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_objects(self, async_client: AsyncTelnyx) -> None:
        client = await async_client.list_objects(
            bucket_name="xxxx",
        )
        assert_matches_type(ListObjectsResponse, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_objects_with_all_params(self, async_client: AsyncTelnyx) -> None:
        client = await async_client.list_objects(
            bucket_name="xxxx",
            list_type=2,
        )
        assert_matches_type(ListObjectsResponse, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_objects(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.with_raw_response.list_objects(
            bucket_name="xxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(ListObjectsResponse, client, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_objects(self, async_client: AsyncTelnyx) -> None:
        async with async_client.with_streaming_response.list_objects(
            bucket_name="xxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(ListObjectsResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_objects(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.with_raw_response.list_objects(
                bucket_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_put_object(self, async_client: AsyncTelnyx) -> None:
        client = await async_client.put_object(
            object_name="x",
            bucket_name="bucketName",
            body=b"raw file contents",
        )
        assert client is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_put_object_with_all_params(self, async_client: AsyncTelnyx) -> None:
        client = await async_client.put_object(
            object_name="x",
            bucket_name="bucketName",
            body=b"raw file contents",
            part_number="partNumber",
            upload_id="uploadId",
        )
        assert client is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_put_object(self, async_client: AsyncTelnyx) -> None:
        response = await async_client.with_raw_response.put_object(
            object_name="x",
            bucket_name="bucketName",
            body=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert client is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_put_object(self, async_client: AsyncTelnyx) -> None:
        async with async_client.with_streaming_response.put_object(
            object_name="x",
            bucket_name="bucketName",
            body=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert client is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_put_object(self, async_client: AsyncTelnyx) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.with_raw_response.put_object(
                object_name="x",
                bucket_name="",
                body=b"raw file contents",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_name` but received ''"):
            await async_client.with_raw_response.put_object(
                object_name="",
                bucket_name="bucketName",
                body=b"raw file contents",
            )
