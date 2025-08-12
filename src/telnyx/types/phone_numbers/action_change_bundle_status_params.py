# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionChangeBundleStatusParams"]


class ActionChangeBundleStatusParams(TypedDict, total=False):
    bundle_id: Required[str]
    """The new bundle_id setting for the number.

    If you are assigning the number to a bundle, this is the unique ID of the bundle
    you wish to use. If you are removing the number from a bundle, this must be
    null. You cannot assign a number from one bundle to another directly. You must
    first remove it from a bundle, and then assign it to a new bundle.
    """
