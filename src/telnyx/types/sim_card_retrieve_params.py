# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SimCardRetrieveParams"]


class SimCardRetrieveParams(TypedDict, total=False):
    include_pin_puk_codes: bool
    """When set to true, includes the PIN and PUK codes in the response.

    These codes are used for SIM card security and unlocking purposes. Available for
    both physical SIM cards and eSIMs.
    """

    include_sim_card_group: bool
    """It includes the associated SIM card group object in the response when present."""
