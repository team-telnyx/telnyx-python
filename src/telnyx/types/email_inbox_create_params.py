# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["EmailInboxCreateParams"]


class EmailInboxCreateParams(TypedDict, total=False):
    domain_id: str
    """Account-owned, inbound-enabled domain UUID.

    The account's shared inbound subdomain is allocated when omitted.
    """

    username: str
    """Inbox local part.

    Trimmed and lowercased before validation; the normalized value must be 1-64
    characters, start and end with a letter or digit, and contain only letters,
    digits, dots, hyphens, and underscores. Generated when omitted.
    """
