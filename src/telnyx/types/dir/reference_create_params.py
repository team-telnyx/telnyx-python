# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .reference_input_param import ReferenceInputParam

__all__ = ["ReferenceCreateParams"]


class ReferenceCreateParams(TypedDict, total=False):
    business_references: Required[Iterable[ReferenceInputParam]]
    """Exactly two business references.

    Array order determines each one's slot: the first entry becomes slot 1 and the
    second becomes slot 2. Those slots are what you pass when updating a single
    reference later. Each should be a senior contact who can speak to your company's
    reputation and operations: a C-suite executive (CEO, CFO, CTO, COO), an owner or
    founder as reflected in your corporate records, or a senior manager, director,
    or executive at an organization you work with, such as a vendor, partner, or
    client.
    """

    financial_reference: Required[ReferenceInputParam]
    """One reference supplied at submit.

    The reference type is implied by the field that carries it (business_references
    vs financial_reference).
    """
