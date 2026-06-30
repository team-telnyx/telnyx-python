# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .tos_product_type import TosProductType as TosProductType
from .agreement_list_params import AgreementListParams as AgreementListParams

if TYPE_CHECKING:
    from .tos_agreement import TosAgreement as TosAgreement
    from .tos_agreement_wrapped import TosAgreementWrapped as TosAgreementWrapped


def __getattr__(name: str) -> Any:
    if name == "TosAgreement":
        from .tos_agreement import TosAgreement

        return TosAgreement
    if name == "TosAgreementWrapped":
        from .tos_agreement_wrapped import TosAgreementWrapped

        return TosAgreementWrapped
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
