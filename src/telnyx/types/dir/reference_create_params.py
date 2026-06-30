# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .reference_input_param import ReferenceInputParam

__all__ = ["ReferenceCreateParams"]


class ReferenceCreateParams(TypedDict, total=False):
    business_references: Required[Iterable[ReferenceInputParam]]
    """Exactly two business references."""

    financial_reference: Required[ReferenceInputParam]
    """One reference supplied at submit.

    The reference type is implied by the field that carries it (business_references
    vs financial_reference).
    """
