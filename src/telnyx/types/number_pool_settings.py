# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["NumberPoolSettings"]


class NumberPoolSettings(BaseModel):
    long_code_weight: float
    """
    Defines the probability weight for a Long Code number to be selected when
    sending a message. The higher the weight the higher the probability. The sum of
    the weights for all number types does not necessarily need to add to 100. Weight
    must be a non-negative number, and when equal to zero it will remove the number
    type from the pool.
    """

    skip_unhealthy: bool
    """
    If set to true all unhealthy numbers will be automatically excluded from the
    pool. Health metrics per number are calculated on a regular basis, taking into
    account the deliverability rate and the amount of messages marked as spam by
    upstream carriers. Numbers with a deliverability rate below 25% or spam ratio
    over 75% will be considered unhealthy.
    """

    toll_free_weight: float
    """
    Defines the probability weight for a Toll Free number to be selected when
    sending a message. The higher the weight the higher the probability. The sum of
    the weights for all number types does not necessarily need to add to 100. Weight
    must be a non-negative number, and when equal to zero it will remove the number
    type from the pool.
    """

    geomatch: Optional[bool] = None
    """
    If set to true, Number Pool will try to choose a sending number with the same
    area code as the destination number. If there are no such numbers available, a
    nunber with a different area code will be chosen. Currently only NANP numbers
    are supported.
    """

    sticky_sender: Optional[bool] = None
    """
    If set to true, Number Pool will try to choose the same sending number for all
    messages to a particular recipient. If the sending number becomes unhealthy and
    `skip_unhealthy` is set to true, a new number will be chosen.
    """
