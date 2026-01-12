# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import time
import threading
from typing import Any
from typing_extensions import Generator, AsyncGenerator, override

import anyio
import httpx

from ._utils import lru_cache


class OAuth2ClientCredentials(httpx.Auth):
    """OAuth2 client credentials authentication flow"""

    requires_response_body: bool = True

    def __init__(
        self,
        *,
        token_url: httpx.URL,
        client_id: str,
        client_secret: str,
        header: str,
    ) -> None:
        self._token_url = token_url
        self._header = header
        self._client_id = client_id
        self._client_secret = client_secret

        self._token: dict[str, Any] | None = None
        self._token_expires_at: float | None = None
        self._token_async_lock = anyio.Lock()
        self._token_sync_lock = threading.Lock()

    @override
    def sync_auth_flow(self, request: httpx.Request) -> Generator[httpx.Request, httpx.Response, None]:
        with self._token_sync_lock:
            if self._token and not self.token_is_expired():
                request.headers[self._header] = f"Bearer {self._token['access_token']}"
                yield request
                return

            token_response = yield self._build_token_request()
            if token_response.status_code == 200:
                token_response.read()
                self._token = token_response.json()
                assert self._token is not None

                self._token_expires_at = time.time() + self._token.get("expires_in", 3600)
                request.headers[self._header] = f"Bearer {self._token['access_token']}"

            yield request

    @override
    def auth_flow(self, request: httpx.Request) -> Generator[httpx.Request, httpx.Response, None]:
        return self.sync_auth_flow(request)

    @override
    async def async_auth_flow(self, request: httpx.Request) -> AsyncGenerator[httpx.Request, httpx.Response]:
        async with self._token_async_lock:
            if self._token is not None and not self.token_is_expired():
                request.headers[self._header] = f"Bearer {self._token['access_token']}"
                yield request
                return

            token_response = yield self._build_token_request()
            if token_response.status_code == 200:
                await token_response.aread()
                self._token = token_response.json()
                assert self._token is not None

                self._token_expires_at = time.time() + self._token.get("expires_in", 3600)
                request.headers[self._header] = f"Bearer {self._token['access_token']}"

            yield request

    def _build_token_request(self) -> httpx.Request:
        import base64

        credentials = f"{self._client_id}:{self._client_secret}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()

        return httpx.Request(
            "POST",
            self._token_url,
            params={"grant_type": "client_credentials"},
            headers={"Authorization": f"Basic {encoded_credentials}"},
        )

    def token_is_expired(self) -> bool:
        if self._token_expires_at is None or self._token is None:
            return True

        return time.time() > self._token_expires_at - 10

    def invalidate_token(self) -> None:
        """Invalidate the cached token, forcing a refresh on the next request"""
        self._token = None
        self._token_expires_at = None


@lru_cache(maxsize=None)
def make_oauth2(
    token_url: httpx.URL,
    client_id: str,
    client_secret: str,
    header: str,
) -> OAuth2ClientCredentials:
    return OAuth2ClientCredentials(
        token_url=token_url,
        client_id=client_id,
        client_secret=client_secret,
        header=header,
    )
