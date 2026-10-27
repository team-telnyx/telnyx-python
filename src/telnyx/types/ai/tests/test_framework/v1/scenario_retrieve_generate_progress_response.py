# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional

from ......_models import BaseModel

__all__ = ["ScenarioRetrieveGenerateProgressResponse"]


class ScenarioRetrieveGenerateProgressResponse(BaseModel):
    completed_scenarios: Optional[int] = None

    failed_scenarios: Optional[int] = None

    scenarios_list: Optional[List[Dict[str, object]]] = None

    total_scenarios: Optional[int] = None
