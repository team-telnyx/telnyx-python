# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BpoAuthorizationInputParam"]


class BpoAuthorizationInputParam(TypedDict, total=False):
    """
    One authorization to include when creating or updating a DIR: an approved BPO (Business Process Outsourcer) account plus the signed Letter of Authorization the Brand Owner granted it.
    """

    bpo_enterprise_id: Required[str]
    """
    Enterprise id of an approved BPO (Business Process Outsourcer) account on your
    organization to authorize for this DIR.
    """

    loa_document_id: Required[str]
    """
    Id of the signed Letter of Authorization document (uploaded via the Telnyx
    Documents API) in which the Brand Owner authorizes this BPO.
    """
