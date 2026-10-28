# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Iterable, ForwardRef
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ActionCreateParams",
    "NavigateAction",
    "ObserveAction",
    "ClickAction",
    "FillAction",
    "SelectAction",
    "PressAction",
    "ScrollAction",
    "ScreenshotAction",
    "WaitForAction",
    "WaitForActionCondition",
    "WaitForActionConditionUnionMember0",
    "WaitForActionConditionUnionMember1",
    "WaitForActionConditionUnionMember2",
    "WaitForActionConditionKind",
    "BatchAction",
    "BatchActionAction",
]


class NavigateAction(TypedDict, total=False):
    type: Required[Literal["navigate"]]

    url: Required[str]

    wait_seconds: int
    """
    Maximum seconds the submission request waits for completion, not an execution
    timeout. If still queued or running, returns 202 without cancelling execution;
    poll the returned action ID.
    """

    idempotency_key: str

    include_observation: bool

    wait_until: Literal["load", "dom_stable", "none"]


class ObserveAction(TypedDict, total=False):
    type: Required[Literal["observe"]]

    wait_seconds: int
    """
    Maximum seconds the submission request waits for completion, not an execution
    timeout. If still queued or running, returns 202 without cancelling execution;
    poll the returned action ID.
    """

    idempotency_key: str

    include_observation: bool


class ClickAction(TypedDict, total=False):
    observation_id: Required[str]

    ref: Required[str]

    type: Required[Literal["click"]]

    wait_seconds: int
    """
    Maximum seconds the submission request waits for completion, not an execution
    timeout. If still queued or running, returns 202 without cancelling execution;
    poll the returned action ID.
    """

    idempotency_key: str

    include_observation: bool

    timeout_ms: int

    wait: Literal["no_wait", "dom_stable", "url_change"]


class FillAction(TypedDict, total=False):
    observation_id: Required[str]

    ref: Required[str]

    type: Required[Literal["fill"]]

    value: Required[str]

    wait_seconds: int
    """
    Maximum seconds the submission request waits for completion, not an execution
    timeout. If still queued or running, returns 202 without cancelling execution;
    poll the returned action ID.
    """

    idempotency_key: str

    include_observation: bool


class SelectAction(TypedDict, total=False):
    observation_id: Required[str]

    ref: Required[str]

    type: Required[Literal["select"]]

    value: Required[str]

    wait_seconds: int
    """
    Maximum seconds the submission request waits for completion, not an execution
    timeout. If still queued or running, returns 202 without cancelling execution;
    poll the returned action ID.
    """

    idempotency_key: str

    include_observation: bool


class PressAction(TypedDict, total=False):
    key: Required[
        Literal[
            "Enter",
            "Tab",
            "Escape",
            "Backspace",
            "ArrowUp",
            "ArrowDown",
            "ArrowLeft",
            "ArrowRight",
            "PageUp",
            "PageDown",
            "Home",
            "End",
        ]
    ]

    type: Required[Literal["press"]]

    wait_seconds: int
    """
    Maximum seconds the submission request waits for completion, not an execution
    timeout. If still queued or running, returns 202 without cancelling execution;
    poll the returned action ID.
    """

    idempotency_key: str

    include_observation: bool


class ScrollAction(TypedDict, total=False):
    type: Required[Literal["scroll"]]

    wait_seconds: int
    """
    Maximum seconds the submission request waits for completion, not an execution
    timeout. If still queued or running, returns 202 without cancelling execution;
    poll the returned action ID.
    """

    delta_x: int

    delta_y: int

    idempotency_key: str

    include_observation: bool


class ScreenshotAction(TypedDict, total=False):
    type: Required[Literal["screenshot"]]

    wait_seconds: int
    """
    Maximum seconds the submission request waits for completion, not an execution
    timeout. If still queued or running, returns 202 without cancelling execution;
    poll the returned action ID.
    """

    idempotency_key: str

    include_observation: bool


class WaitForAction(TypedDict, total=False):
    condition: Required[WaitForActionCondition]

    type: Required[Literal["wait_for"]]

    wait_seconds: int
    """
    Maximum seconds the submission request waits for completion, not an execution
    timeout. If still queued or running, returns 202 without cancelling execution;
    poll the returned action ID.
    """

    idempotency_key: str

    include_observation: bool

    timeout_ms: int


class WaitForActionConditionUnionMember0(TypedDict, total=False):
    kind: Required[Literal["url_pattern"]]

    pattern: Required[str]


class WaitForActionConditionUnionMember1(TypedDict, total=False):
    kind: Required[Literal["ref"]]

    observation_id: Required[str]

    ref: Required[str]


class WaitForActionConditionUnionMember2(TypedDict, total=False):
    kind: Required[Literal["text"]]

    text: Required[str]


class WaitForActionConditionKind(TypedDict, total=False):
    kind: Required[Literal["dom_stable"]]


WaitForActionCondition: TypeAlias = Union[
    WaitForActionConditionUnionMember0,
    WaitForActionConditionUnionMember1,
    WaitForActionConditionUnionMember2,
    WaitForActionConditionKind,
]


class BatchAction(TypedDict, total=False):
    actions: Required[Iterable[BatchActionAction]]

    type: Required[Literal["batch"]]

    wait_seconds: int
    """
    Maximum seconds the submission request waits for completion, not an execution
    timeout. If still queued or running, returns 202 without cancelling execution;
    poll the returned action ID.
    """

    idempotency_key: str

    include_observation: bool


if TYPE_CHECKING:
    BatchActionAction: TypeAlias = Union[
        "NavigateActionParam",
        "ObserveActionParam",
        "ClickActionParam",
        "FillActionParam",
        "SelectActionParam",
        "PressActionParam",
        "ScrollActionParam",
        "ScreenshotActionParam",
        "WaitForActionParam",
    ]
else:
    BatchActionAction = Union[
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).NavigateActionParam"),
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).ObserveActionParam"),
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).ClickActionParam"),
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).FillActionParam"),
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).SelectActionParam"),
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).PressActionParam"),
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).ScrollActionParam"),
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).ScreenshotActionParam"),
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).WaitForActionParam"),
    ]

ActionCreateParams: TypeAlias = Union[
    NavigateAction,
    ObserveAction,
    ClickAction,
    FillAction,
    SelectAction,
    PressAction,
    ScrollAction,
    ScreenshotAction,
    WaitForAction,
    BatchAction,
]

from .fill_action_param import FillActionParam
from .click_action_param import ClickActionParam
from .press_action_param import PressActionParam
from .scroll_action_param import ScrollActionParam
from .select_action_param import SelectActionParam
from .observe_action_param import ObserveActionParam
from .navigate_action_param import NavigateActionParam
from .wait_for_action_param import WaitForActionParam
from .screenshot_action_param import ScreenshotActionParam
