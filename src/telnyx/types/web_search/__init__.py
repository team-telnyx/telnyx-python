# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .research_create_params import ResearchCreateParams as ResearchCreateParams

if TYPE_CHECKING:
    from .research_citation import ResearchCitation as ResearchCitation
    from .research_create_response import ResearchCreateResponse as ResearchCreateResponse
    from .research_retrieve_response import ResearchRetrieveResponse as ResearchRetrieveResponse


def __getattr__(name: str) -> Any:
    if name == "ResearchCitation":
        from .research_citation import ResearchCitation

        return ResearchCitation
    if name == "ResearchCreateResponse":
        from .research_create_response import ResearchCreateResponse

        return ResearchCreateResponse
    if name == "ResearchRetrieveResponse":
        from .research_retrieve_response import ResearchRetrieveResponse

        return ResearchRetrieveResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
