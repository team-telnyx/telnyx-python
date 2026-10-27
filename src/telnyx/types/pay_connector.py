# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PayConnector", "Config"]


class Config(BaseModel):
    """Redacted stored configuration.

    Generic connector fields are shown here. Unknown config keys are discarded. Password and token are never returned.
    """

    auth_type: Optional[Literal["none", "basic", "bearer"]] = None
    """Stored processor authentication selection.

    Omitted if it was not explicitly configured.
    """

    endpoint_url: Optional[str] = None
    """HTTP or HTTPS processor URL with a host.

    Use HTTPS to protect payment data in transit.
    """

    timeout: Optional[int] = None
    """Stored processor HTTP timeout in milliseconds.

    Omitted when no timeout was configured; the effective runtime default is 10000.
    """

    username: Optional[object] = None
    """Stored username, when supplied.

    Required to be a nonblank string for basic authentication.
    """


class PayConnector(BaseModel):
    """Organization-owned connector.

    Examples and config properties here describe generic connectors; listing is not restricted to that type unless filter[type]=generic is supplied. Passwords and bearer tokens are omitted, not masked. Defaults for auth_type and timeout need not appear in stored config.
    """

    id: Optional[str] = None
    """Connector identifier."""

    config: Optional[Config] = None
    """Redacted stored configuration.

    Generic connector fields are shown here. Unknown config keys are discarded.
    Password and token are never returned.
    """

    created_at: Optional[datetime] = None
    """Creation time."""

    mode: Optional[Literal["test", "live"]] = None
    """Configured mode."""

    name: Optional[str] = None
    """Connector name used for retrieval, update, deletion and Pay."""

    organization_id: Optional[str] = None
    """Owning organization; assigned from authentication, not request input."""

    record_type: Optional[Literal["pay_connector"]] = None
    """Resource type."""

    type: Optional[str] = None
    """Connector type; generic is covered by this reference.

    Other types may appear in unfiltered lists.
    """

    updated_at: Optional[datetime] = None
    """Last update time."""

    user_id: Optional[str] = None
    """Creating user; assigned from authentication, not request input."""
