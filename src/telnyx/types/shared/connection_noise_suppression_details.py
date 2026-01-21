# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ConnectionNoiseSuppressionDetails"]


class ConnectionNoiseSuppressionDetails(BaseModel):
    """Configuration options for noise suppression.

    These settings are stored regardless of the noise_suppression value, but only take effect when noise_suppression is not 'disabled'. If you disable noise suppression and later re-enable it, the previously configured settings will be used.
    """

    attenuation_limit: Optional[int] = None
    """The attenuation limit value for the selected engine.

    Default values vary by engine: 0 for 'denoiser', 80 for 'deep_filter_net',
    'deep_filter_net_large', and all Krisp engines ('krisp_viva_tel',
    'krisp_viva_tel_lite', 'krisp_viva_promodel', 'krisp_viva_ss').
    """

    engine: Optional[
        Literal[
            "denoiser",
            "deep_filter_net",
            "deep_filter_net_large",
            "krisp_viva_tel",
            "krisp_viva_tel_lite",
            "krisp_viva_promodel",
            "krisp_viva_ss",
        ]
    ] = None
    """The noise suppression engine to use.

    'denoiser' is the default engine. 'deep_filter_net' and 'deep_filter_net_large'
    are alternative engines with different performance characteristics. Krisp
    engines ('krisp_viva_tel', 'krisp_viva_tel_lite', 'krisp_viva_promodel',
    'krisp_viva_ss') provide advanced noise suppression capabilities.
    """
