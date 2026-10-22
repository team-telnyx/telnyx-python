# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["FuncListResponse", "Binding"]


class Binding(BaseModel):
    """A function-scoped binding persisted at ship time.

    For binding_type=actor, actor_type is the referenced Stateful Actor type and env_name is the binding name exposed to the function.
    """

    actor_type: Optional[str] = None

    binding_id: Optional[str] = None

    binding_type: Optional[str] = None

    bucket_id: Optional[str] = None

    created_at: Optional[str] = None

    env_name: Optional[str] = None

    func_id: Optional[str] = None

    kv_id: Optional[str] = None

    record_type: Optional[str] = None

    secret_name: Optional[str] = None

    sqldb_id: Optional[str] = None

    status: Optional[str] = None

    updated_at: Optional[str] = None


class FuncListResponse(BaseModel):
    id: Optional[str] = None

    bindings: Optional[List[Binding]] = None
    """Always present; empty when the function has no bindings."""

    created_at: Optional[str] = None

    invoke_url: Optional[str] = None

    message: Optional[str] = None

    name: Optional[str] = None

    record_type: Optional[str] = None

    status: Optional[str] = None

    status_detail: Optional[str] = None

    updated_at: Optional[str] = None
