# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .metric_list_params import MetricListParams as MetricListParams
from .result_list_params import ResultListParams as ResultListParams
from .aiagent_list_params import AiagentListParams as AiagentListParams
from .metric_create_params import MetricCreateParams as MetricCreateParams
from .metric_list_response import MetricListResponse as MetricListResponse
from .metric_update_params import MetricUpdateParams as MetricUpdateParams
from .scenario_list_params import ScenarioListParams as ScenarioListParams
from .aiagent_create_params import AiagentCreateParams as AiagentCreateParams
from .aiagent_update_params import AiagentUpdateParams as AiagentUpdateParams
from .scenario_create_params import ScenarioCreateParams as ScenarioCreateParams
from .scenario_update_params import ScenarioUpdateParams as ScenarioUpdateParams
from .metric_bulk_create_params import MetricBulkCreateParams as MetricBulkCreateParams
from .metric_bulk_create_response import MetricBulkCreateResponse as MetricBulkCreateResponse
from .scenario_generate_bg_params import ScenarioGenerateBgParams as ScenarioGenerateBgParams
from .scenario_run_scenarios_params import ScenarioRunScenariosParams as ScenarioRunScenariosParams
from .metric_generate_metrics_params import MetricGenerateMetricsParams as MetricGenerateMetricsParams
from .scenario_scenario_agent_params import ScenarioScenarioAgentParams as ScenarioScenarioAgentParams
from .create_ai_test_metric_request_param import CreateAITestMetricRequestParam as CreateAITestMetricRequestParam
from .scenario_retrieve_export_scenarios_params import (
    ScenarioRetrieveExportScenariosParams as ScenarioRetrieveExportScenariosParams,
)
from .scenario_retrieve_generate_progress_params import (
    ScenarioRetrieveGenerateProgressParams as ScenarioRetrieveGenerateProgressParams,
)
from .metric_retrieve_generate_metrics_progress_params import (
    MetricRetrieveGenerateMetricsProgressParams as MetricRetrieveGenerateMetricsProgressParams,
)
from .scenario_retrieve_scenario_agent_progress_params import (
    ScenarioRetrieveScenarioAgentProgressParams as ScenarioRetrieveScenarioAgentProgressParams,
)

if TYPE_CHECKING:
    from .test_agent import TestAgent as TestAgent
    from .ai_test_metric import AITestMetric as AITestMetric
    from .test_run_result import TestRunResult as TestRunResult
    from .result_list_response import ResultListResponse as ResultListResponse
    from .aiagent_list_response import AiagentListResponse as AiagentListResponse
    from .scenario_list_response import ScenarioListResponse as ScenarioListResponse
    from .evaluator_scenario_detail import EvaluatorScenarioDetail as EvaluatorScenarioDetail
    from .scenario_generation_response import ScenarioGenerationResponse as ScenarioGenerationResponse
    from .scenario_run_scenarios_response import ScenarioRunScenariosResponse as ScenarioRunScenariosResponse
    from .scenario_scenario_agent_response import ScenarioScenarioAgentResponse as ScenarioScenarioAgentResponse
    from .scenario_retrieve_generate_progress_response import (
        ScenarioRetrieveGenerateProgressResponse as ScenarioRetrieveGenerateProgressResponse,
    )
    from .metric_retrieve_generate_metrics_progress_response import (
        MetricRetrieveGenerateMetricsProgressResponse as MetricRetrieveGenerateMetricsProgressResponse,
    )
    from .scenario_retrieve_scenario_agent_progress_response import (
        ScenarioRetrieveScenarioAgentProgressResponse as ScenarioRetrieveScenarioAgentProgressResponse,
    )


def __getattr__(name: str) -> Any:
    if name == "TestAgent":
        from .test_agent import TestAgent

        return TestAgent
    if name == "AiagentListResponse":
        from .aiagent_list_response import AiagentListResponse

        return AiagentListResponse
    if name == "AITestMetric":
        from .ai_test_metric import AITestMetric

        return AITestMetric
    if name == "ScenarioGenerationResponse":
        from .scenario_generation_response import ScenarioGenerationResponse

        return ScenarioGenerationResponse
    if name == "MetricRetrieveGenerateMetricsProgressResponse":
        from .metric_retrieve_generate_metrics_progress_response import MetricRetrieveGenerateMetricsProgressResponse

        return MetricRetrieveGenerateMetricsProgressResponse
    if name == "TestRunResult":
        from .test_run_result import TestRunResult

        return TestRunResult
    if name == "ResultListResponse":
        from .result_list_response import ResultListResponse

        return ResultListResponse
    if name == "EvaluatorScenarioDetail":
        from .evaluator_scenario_detail import EvaluatorScenarioDetail

        return EvaluatorScenarioDetail
    if name == "ScenarioListResponse":
        from .scenario_list_response import ScenarioListResponse

        return ScenarioListResponse
    if name == "ScenarioRetrieveGenerateProgressResponse":
        from .scenario_retrieve_generate_progress_response import ScenarioRetrieveGenerateProgressResponse

        return ScenarioRetrieveGenerateProgressResponse
    if name == "ScenarioRetrieveScenarioAgentProgressResponse":
        from .scenario_retrieve_scenario_agent_progress_response import ScenarioRetrieveScenarioAgentProgressResponse

        return ScenarioRetrieveScenarioAgentProgressResponse
    if name == "ScenarioRunScenariosResponse":
        from .scenario_run_scenarios_response import ScenarioRunScenariosResponse

        return ScenarioRunScenariosResponse
    if name == "ScenarioScenarioAgentResponse":
        from .scenario_scenario_agent_response import ScenarioScenarioAgentResponse

        return ScenarioScenarioAgentResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
