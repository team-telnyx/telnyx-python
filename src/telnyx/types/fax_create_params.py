# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FaxCreateParams"]


class FaxCreateParams(TypedDict, total=False):
    connection_id: Required[str]
    """The connection ID to send the fax with."""

    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """The phone number, in E.164 format, the fax will be sent from."""

    to: Required[str]
    """The phone number, in E.164 format, the fax will be sent to or SIP URI"""

    client_state: str
    """Use this field to add state to every subsequent webhook.

    It must be a valid Base-64 encoded string.
    """

    from_display_name: str
    """
    The `from_display_name` string to be used as the caller id name (SIP From
    Display Name) presented to the destination (`to` number). The string should have
    a maximum of 128 characters, containing only letters, numbers, spaces, and
    -\\__~!.+ special characters. If ommited, the display name will be the same as the
    number in the `from` field.
    """

    media_name: str
    """The media_name used for the fax's media.

    Must point to a file previously uploaded to api.telnyx.com/v2/media by the same
    user/organization. media_name and media_url/contents can't be submitted
    together.
    """

    media_url: str
    """The URL (or list of URLs) to the PDF used for the fax's media.

    media_url and media_name/contents can't be submitted together.
    """

    monochrome: bool
    """The flag to enable monochrome, true black and white fax results."""

    preview_format: Literal["pdf", "tiff"]
    """The format for the preview file in case the `store_preview` is `true`."""

    quality: Literal["normal", "high", "very_high", "ultra_light", "ultra_dark"]
    """The quality of the fax.

    The `ultra` settings provides the highest quality available, but also present
    longer fax processing times. `ultra_light` is best suited for images, wihle
    `ultra_dark` is best suited for text.
    """

    store_media: bool
    """Should fax media be stored on temporary URL.

    It does not support media_name, they can't be submitted together.
    """

    store_preview: bool
    """Should fax preview be stored on temporary URL."""

    t38_enabled: bool
    """The flag to disable the T.38 protocol."""

    webhook_url: str
    """
    Use this field to override the URL to which Telnyx will send subsequent webhooks
    for this fax.
    """
