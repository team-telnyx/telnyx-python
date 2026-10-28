# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IPPoolCreateParams"]


class IPPoolCreateParams(TypedDict, total=False):
    name: Required[str]
    """
    Pool name: 1-64 characters of lowercase letters, digits, `.`, `_`, and `-`,
    starting and ending with a letter or digit. Must be unique within the account
    and must not start with `dip_`.
    """

    domain_id: str
    """
    Scope the pool to one of the account's email domains; the pool then carries that
    domain's mail. Scope at most one pool to each domain.
    """

    is_default: bool
    """
    Make this the account's default pool, which carries mail for sending domains
    without a domain-scoped pool. An account can have one default pool. Defaults to
    `false`.
    """
