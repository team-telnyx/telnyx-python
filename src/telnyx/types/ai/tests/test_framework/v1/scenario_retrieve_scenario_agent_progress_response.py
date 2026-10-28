# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional

from ......_models import BaseModel

__all__ = [
    "ScenarioRetrieveScenarioAgentProgressResponse",
    "Result",
    "ResultClarificationQuestion",
    "ResultConversationHistory",
]


class ResultClarificationQuestion(BaseModel):
    question: Optional[str] = None


class ResultConversationHistory(BaseModel):
    content: Optional[str] = None

    role: Optional[str] = None

    timestamp: Optional[str] = None


class Result(BaseModel):
    cancelled: Optional[bool] = None

    clarification_questions: Optional[List[ResultClarificationQuestion]] = None

    conversation_history: Optional[List[ResultConversationHistory]] = None

    message: Optional[str] = None

    needs_clarification: Optional[bool] = None

    session_id: Optional[int] = None

    success: Optional[bool] = None

    updated_scenarios: Optional[List[Dict[str, object]]] = None


class ScenarioRetrieveScenarioAgentProgressResponse(BaseModel):
    error: Optional[str] = None

    mode: Optional[str] = None

    progress_id: Optional[str] = None

    result: Optional[Result] = None

    session_id: Optional[int] = None

    status: Optional[str] = None
