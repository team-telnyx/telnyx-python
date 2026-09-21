# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["BotSignupCreateParams"]


class BotSignupCreateParams(TypedDict, total=False):
    bot_challenge_answer: Required[str]
    """Answer to the issued bot challenge."""

    bot_challenge_nonce: Required[str]
    """Nonce from a previously issued bot challenge."""

    privacy_policy_url: Required[str]
    """Must exactly match the privacy-policy URL returned by the challenge endpoint."""

    terms_and_conditions_url: Required[str]
    """
    Must exactly match the terms-and-conditions URL returned by the challenge
    endpoint.
    """

    terms_of_service: Required[Literal[True]]
    """Must be true to accept the terms of service."""

    email: str
    """Email address for the new account.

    The magic link is sent here. May only be omitted when placeholder-email
    registration is enabled server-side.
    """

    terms_and_conditions_eu_url: str
    """EU terms-and-conditions URL. Required when EU consent enforcement is enabled."""

    terms_of_service_eu: Literal[True]
    """EU terms-of-service acceptance.

    Required when EU consent enforcement is enabled.
    """
