# Shared Types

```python
from telnyx.types import (
    ConnectionsPaginationMeta,
    DocReqsRequirementType,
    HostedNumber,
    MessagingFeatureSet,
    MessagingHostedNumberOrder,
    Metadata,
    NumberHealthMetrics,
    PhoneNumberWithMessagingSettings,
    PortingOrderStatus,
    PortingOrdersExceptionType,
    RoomParticipant,
    ShortCode,
    SimCardStatus,
    SimpleSimCard,
    SubNumberOrderRegulatoryRequirementWithValue,
)
```

# Telnyx

Types:

```python
from telnyx.types import ListBucketsResponse, ListObjectsResponse
```

Methods:

- <code title="put /{bucketName}">client.<a href="./src/telnyx/_client.py">create_bucket</a>(bucket_name, \*\*<a href="src/telnyx/types/client_create_bucket_params.py">params</a>) -> None</code>
- <code title="delete /{bucketName}">client.<a href="./src/telnyx/_client.py">delete_bucket</a>(bucket_name) -> None</code>
- <code title="delete /{bucketName}/{objectName}">client.<a href="./src/telnyx/_client.py">delete_object</a>(object_name, \*, bucket_name) -> None</code>
- <code title="post /{bucketName}">client.<a href="./src/telnyx/_client.py">delete_objects</a>(bucket_name, \*\*<a href="src/telnyx/types/client_delete_objects_params.py">params</a>) -> object</code>
- <code title="get /{bucketName}/{objectName}">client.<a href="./src/telnyx/_client.py">get_object</a>(object_name, \*, bucket_name, \*\*<a href="src/telnyx/types/client_get_object_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /">client.<a href="./src/telnyx/_client.py">list_buckets</a>() -> <a href="./src/telnyx/types/list_buckets_response.py">ListBucketsResponse</a></code>
- <code title="get /{bucketName}">client.<a href="./src/telnyx/_client.py">list_objects</a>(bucket_name, \*\*<a href="src/telnyx/types/client_list_objects_params.py">params</a>) -> <a href="./src/telnyx/types/list_objects_response.py">ListObjectsResponse</a></code>
- <code title="put /{bucketName}/{objectName}">client.<a href="./src/telnyx/_client.py">put_object</a>(object_name, \*, bucket_name, \*\*<a href="src/telnyx/types/client_put_object_params.py">params</a>) -> None</code>

# AccessIPAddress

Types:

```python
from telnyx.types import AccessIPAddressResponse, CloudflareSyncStatus, AccessIPAddressListResponse
```

Methods:

- <code title="post /access_ip_address">client.access_ip_address.<a href="./src/telnyx/resources/access_ip_address.py">create</a>(\*\*<a href="src/telnyx/types/access_ip_address_create_params.py">params</a>) -> <a href="./src/telnyx/types/access_ip_address_response.py">AccessIPAddressResponse</a></code>
- <code title="get /access_ip_address/{access_ip_address_id}">client.access_ip_address.<a href="./src/telnyx/resources/access_ip_address.py">retrieve</a>(access_ip_address_id) -> <a href="./src/telnyx/types/access_ip_address_response.py">AccessIPAddressResponse</a></code>
- <code title="get /access_ip_address">client.access_ip_address.<a href="./src/telnyx/resources/access_ip_address.py">list</a>(\*\*<a href="src/telnyx/types/access_ip_address_list_params.py">params</a>) -> <a href="./src/telnyx/types/access_ip_address_list_response.py">AccessIPAddressListResponse</a></code>
- <code title="delete /access_ip_address/{access_ip_address_id}">client.access_ip_address.<a href="./src/telnyx/resources/access_ip_address.py">delete</a>(access_ip_address_id) -> <a href="./src/telnyx/types/access_ip_address_response.py">AccessIPAddressResponse</a></code>

# AccessIPRanges

Types:

```python
from telnyx.types import AccessIPRange, AccessIPRangeListResponse
```

Methods:

- <code title="post /access_ip_ranges">client.access_ip_ranges.<a href="./src/telnyx/resources/access_ip_ranges.py">create</a>(\*\*<a href="src/telnyx/types/access_ip_range_create_params.py">params</a>) -> <a href="./src/telnyx/types/access_ip_range.py">AccessIPRange</a></code>
- <code title="get /access_ip_ranges">client.access_ip_ranges.<a href="./src/telnyx/resources/access_ip_ranges.py">list</a>(\*\*<a href="src/telnyx/types/access_ip_range_list_params.py">params</a>) -> <a href="./src/telnyx/types/access_ip_range_list_response.py">AccessIPRangeListResponse</a></code>
- <code title="delete /access_ip_ranges/{access_ip_range_id}">client.access_ip_ranges.<a href="./src/telnyx/resources/access_ip_ranges.py">delete</a>(access_ip_range_id) -> <a href="./src/telnyx/types/access_ip_range.py">AccessIPRange</a></code>

# Actions

## Purchase

Types:

```python
from telnyx.types.actions import PurchaseCreateResponse
```

Methods:

- <code title="post /actions/purchase/esims">client.actions.purchase.<a href="./src/telnyx/resources/actions/purchase.py">create</a>(\*\*<a href="src/telnyx/types/actions/purchase_create_params.py">params</a>) -> <a href="./src/telnyx/types/actions/purchase_create_response.py">PurchaseCreateResponse</a></code>

## Register

Types:

```python
from telnyx.types.actions import RegisterCreateResponse
```

Methods:

- <code title="post /actions/register/sim_cards">client.actions.register.<a href="./src/telnyx/resources/actions/register.py">create</a>(\*\*<a href="src/telnyx/types/actions/register_create_params.py">params</a>) -> <a href="./src/telnyx/types/actions/register_create_response.py">RegisterCreateResponse</a></code>

# Addresses

Types:

```python
from telnyx.types import (
    Address,
    AddressCreateResponse,
    AddressRetrieveResponse,
    AddressListResponse,
    AddressDeleteResponse,
)
```

Methods:

- <code title="post /addresses">client.addresses.<a href="./src/telnyx/resources/addresses/addresses.py">create</a>(\*\*<a href="src/telnyx/types/address_create_params.py">params</a>) -> <a href="./src/telnyx/types/address_create_response.py">AddressCreateResponse</a></code>
- <code title="get /addresses/{id}">client.addresses.<a href="./src/telnyx/resources/addresses/addresses.py">retrieve</a>(id) -> <a href="./src/telnyx/types/address_retrieve_response.py">AddressRetrieveResponse</a></code>
- <code title="get /addresses">client.addresses.<a href="./src/telnyx/resources/addresses/addresses.py">list</a>(\*\*<a href="src/telnyx/types/address_list_params.py">params</a>) -> <a href="./src/telnyx/types/address_list_response.py">AddressListResponse</a></code>
- <code title="delete /addresses/{id}">client.addresses.<a href="./src/telnyx/resources/addresses/addresses.py">delete</a>(id) -> <a href="./src/telnyx/types/address_delete_response.py">AddressDeleteResponse</a></code>

## Actions

Types:

```python
from telnyx.types.addresses import ActionAcceptSuggestionsResponse, ActionValidateResponse
```

Methods:

- <code title="post /addresses/{id}/actions/accept_suggestions">client.addresses.actions.<a href="./src/telnyx/resources/addresses/actions.py">accept_suggestions</a>(path_id, \*\*<a href="src/telnyx/types/addresses/action_accept_suggestions_params.py">params</a>) -> <a href="./src/telnyx/types/addresses/action_accept_suggestions_response.py">ActionAcceptSuggestionsResponse</a></code>
- <code title="post /addresses/actions/validate">client.addresses.actions.<a href="./src/telnyx/resources/addresses/actions.py">validate</a>(\*\*<a href="src/telnyx/types/addresses/action_validate_params.py">params</a>) -> <a href="./src/telnyx/types/addresses/action_validate_response.py">ActionValidateResponse</a></code>

# AdvancedOrders

Methods:

- <code title="post /advanced_orders">client.advanced_orders.<a href="./src/telnyx/resources/advanced_orders.py">create</a>(\*\*<a href="src/telnyx/types/advanced_order_create_params.py">params</a>) -> object</code>
- <code title="get /advanced_orders/{order_id}">client.advanced_orders.<a href="./src/telnyx/resources/advanced_orders.py">retrieve</a>(order_id) -> object</code>
- <code title="get /advanced_orders">client.advanced_orders.<a href="./src/telnyx/resources/advanced_orders.py">list</a>() -> object</code>

# AI

Types:

```python
from telnyx.types import AIRetrieveModelsResponse, AISummarizeResponse
```

Methods:

- <code title="get /ai/models">client.ai.<a href="./src/telnyx/resources/ai/ai.py">retrieve_models</a>() -> <a href="./src/telnyx/types/ai_retrieve_models_response.py">AIRetrieveModelsResponse</a></code>
- <code title="post /ai/summarize">client.ai.<a href="./src/telnyx/resources/ai/ai.py">summarize</a>(\*\*<a href="src/telnyx/types/ai_summarize_params.py">params</a>) -> <a href="./src/telnyx/types/ai_summarize_response.py">AISummarizeResponse</a></code>

## Assistants

Types:

```python
from telnyx.types.ai import (
    Assistant,
    AssistantTool,
    AssistantsList,
    EnabledFeatures,
    HangupTool,
    HangupToolParams,
    ImportMetadata,
    InferenceEmbeddingBucketIDs,
    InferenceEmbeddingTransferToolParams,
    InferenceEmbeddingWebhookToolParams,
    InsightSettings,
    MessagingSettings,
    PrivacySettings,
    RetrievalTool,
    TelephonySettings,
    TranscriptionSettings,
    TransferTool,
    VoiceSettings,
    WebhookTool,
    AssistantCreateResponse,
    AssistantRetrieveResponse,
    AssistantDeleteResponse,
    AssistantChatResponse,
    AssistantCloneResponse,
    AssistantGetTexmlResponse,
)
```

Methods:

- <code title="post /ai/assistants">client.ai.assistants.<a href="./src/telnyx/resources/ai/assistants/assistants.py">create</a>(\*\*<a href="src/telnyx/types/ai/assistant_create_params.py">params</a>) -> <a href="./src/telnyx/types/ai/assistant_create_response.py">AssistantCreateResponse</a></code>
- <code title="get /ai/assistants/{assistant_id}">client.ai.assistants.<a href="./src/telnyx/resources/ai/assistants/assistants.py">retrieve</a>(assistant_id, \*\*<a href="src/telnyx/types/ai/assistant_retrieve_params.py">params</a>) -> <a href="./src/telnyx/types/ai/assistant_retrieve_response.py">AssistantRetrieveResponse</a></code>
- <code title="post /ai/assistants/{assistant_id}">client.ai.assistants.<a href="./src/telnyx/resources/ai/assistants/assistants.py">update</a>(assistant_id, \*\*<a href="src/telnyx/types/ai/assistant_update_params.py">params</a>) -> object</code>
- <code title="get /ai/assistants">client.ai.assistants.<a href="./src/telnyx/resources/ai/assistants/assistants.py">list</a>() -> <a href="./src/telnyx/types/ai/assistants_list.py">AssistantsList</a></code>
- <code title="delete /ai/assistants/{assistant_id}">client.ai.assistants.<a href="./src/telnyx/resources/ai/assistants/assistants.py">delete</a>(assistant_id) -> <a href="./src/telnyx/types/ai/assistant_delete_response.py">AssistantDeleteResponse</a></code>
- <code title="post /ai/assistants/{assistant_id}/chat">client.ai.assistants.<a href="./src/telnyx/resources/ai/assistants/assistants.py">chat</a>(assistant_id, \*\*<a href="src/telnyx/types/ai/assistant_chat_params.py">params</a>) -> <a href="./src/telnyx/types/ai/assistant_chat_response.py">AssistantChatResponse</a></code>
- <code title="post /ai/assistants/{assistant_id}/clone">client.ai.assistants.<a href="./src/telnyx/resources/ai/assistants/assistants.py">clone</a>(assistant_id) -> <a href="./src/telnyx/types/ai/assistant_clone_response.py">AssistantCloneResponse</a></code>
- <code title="get /ai/assistants/{assistant_id}/texml">client.ai.assistants.<a href="./src/telnyx/resources/ai/assistants/assistants.py">get_texml</a>(assistant_id) -> str</code>
- <code title="post /ai/assistants/import">client.ai.assistants.<a href="./src/telnyx/resources/ai/assistants/assistants.py">import\_</a>(\*\*<a href="src/telnyx/types/ai/assistant_import_params.py">params</a>) -> <a href="./src/telnyx/types/ai/assistants_list.py">AssistantsList</a></code>

### Tests

Types:

```python
from telnyx.types.ai.assistants import AssistantTest, TelnyxConversationChannel, TestListResponse
```

Methods:

- <code title="post /ai/assistants/tests">client.ai.assistants.tests.<a href="./src/telnyx/resources/ai/assistants/tests/tests.py">create</a>(\*\*<a href="src/telnyx/types/ai/assistants/test_create_params.py">params</a>) -> <a href="./src/telnyx/types/ai/assistants/assistant_test.py">AssistantTest</a></code>
- <code title="get /ai/assistants/tests/{test_id}">client.ai.assistants.tests.<a href="./src/telnyx/resources/ai/assistants/tests/tests.py">retrieve</a>(test_id) -> <a href="./src/telnyx/types/ai/assistants/assistant_test.py">AssistantTest</a></code>
- <code title="put /ai/assistants/tests/{test_id}">client.ai.assistants.tests.<a href="./src/telnyx/resources/ai/assistants/tests/tests.py">update</a>(test_id, \*\*<a href="src/telnyx/types/ai/assistants/test_update_params.py">params</a>) -> <a href="./src/telnyx/types/ai/assistants/assistant_test.py">AssistantTest</a></code>
- <code title="get /ai/assistants/tests">client.ai.assistants.tests.<a href="./src/telnyx/resources/ai/assistants/tests/tests.py">list</a>(\*\*<a href="src/telnyx/types/ai/assistants/test_list_params.py">params</a>) -> <a href="./src/telnyx/types/ai/assistants/test_list_response.py">TestListResponse</a></code>
- <code title="delete /ai/assistants/tests/{test_id}">client.ai.assistants.tests.<a href="./src/telnyx/resources/ai/assistants/tests/tests.py">delete</a>(test_id) -> object</code>

#### TestSuites

Types:

```python
from telnyx.types.ai.assistants.tests import TestSuiteListResponse
```

Methods:

- <code title="get /ai/assistants/tests/test-suites">client.ai.assistants.tests.test_suites.<a href="./src/telnyx/resources/ai/assistants/tests/test_suites/test_suites.py">list</a>() -> <a href="./src/telnyx/types/ai/assistants/tests/test_suite_list_response.py">TestSuiteListResponse</a></code>

##### Runs

Types:

```python
from telnyx.types.ai.assistants.tests.test_suites import (
    Meta,
    PaginatedTestRunList,
    RunTriggerResponse,
)
```

Methods:

- <code title="get /ai/assistants/tests/test-suites/{suite_name}/runs">client.ai.assistants.tests.test_suites.runs.<a href="./src/telnyx/resources/ai/assistants/tests/test_suites/runs.py">list</a>(suite_name, \*\*<a href="src/telnyx/types/ai/assistants/tests/test_suites/run_list_params.py">params</a>) -> <a href="./src/telnyx/types/ai/assistants/tests/test_suites/paginated_test_run_list.py">PaginatedTestRunList</a></code>
- <code title="post /ai/assistants/tests/test-suites/{suite_name}/runs">client.ai.assistants.tests.test_suites.runs.<a href="./src/telnyx/resources/ai/assistants/tests/test_suites/runs.py">trigger</a>(suite_name, \*\*<a href="src/telnyx/types/ai/assistants/tests/test_suites/run_trigger_params.py">params</a>) -> <a href="./src/telnyx/types/ai/assistants/tests/test_suites/run_trigger_response.py">RunTriggerResponse</a></code>

#### Runs

Types:

```python
from telnyx.types.ai.assistants.tests import TestRunResponse, TestStatus
```

Methods:

- <code title="get /ai/assistants/tests/{test_id}/runs/{run_id}">client.ai.assistants.tests.runs.<a href="./src/telnyx/resources/ai/assistants/tests/runs.py">retrieve</a>(run_id, \*, test_id) -> <a href="./src/telnyx/types/ai/assistants/tests/test_run_response.py">TestRunResponse</a></code>
- <code title="get /ai/assistants/tests/{test_id}/runs">client.ai.assistants.tests.runs.<a href="./src/telnyx/resources/ai/assistants/tests/runs.py">list</a>(test_id, \*\*<a href="src/telnyx/types/ai/assistants/tests/run_list_params.py">params</a>) -> <a href="./src/telnyx/types/ai/assistants/tests/test_suites/paginated_test_run_list.py">PaginatedTestRunList</a></code>
- <code title="post /ai/assistants/tests/{test_id}/runs">client.ai.assistants.tests.runs.<a href="./src/telnyx/resources/ai/assistants/tests/runs.py">trigger</a>(test_id, \*\*<a href="src/telnyx/types/ai/assistants/tests/run_trigger_params.py">params</a>) -> <a href="./src/telnyx/types/ai/assistants/tests/test_run_response.py">TestRunResponse</a></code>

### CanaryDeploys

Types:

```python
from telnyx.types.ai.assistants import CanaryDeploy, CanaryDeployResponse, VersionConfig
```

Methods:

- <code title="post /ai/assistants/{assistant_id}/canary-deploys">client.ai.assistants.canary_deploys.<a href="./src/telnyx/resources/ai/assistants/canary_deploys.py">create</a>(assistant_id, \*\*<a href="src/telnyx/types/ai/assistants/canary_deploy_create_params.py">params</a>) -> <a href="./src/telnyx/types/ai/assistants/canary_deploy_response.py">CanaryDeployResponse</a></code>
- <code title="get /ai/assistants/{assistant_id}/canary-deploys">client.ai.assistants.canary_deploys.<a href="./src/telnyx/resources/ai/assistants/canary_deploys.py">retrieve</a>(assistant_id) -> <a href="./src/telnyx/types/ai/assistants/canary_deploy_response.py">CanaryDeployResponse</a></code>
- <code title="put /ai/assistants/{assistant_id}/canary-deploys">client.ai.assistants.canary_deploys.<a href="./src/telnyx/resources/ai/assistants/canary_deploys.py">update</a>(assistant_id, \*\*<a href="src/telnyx/types/ai/assistants/canary_deploy_update_params.py">params</a>) -> <a href="./src/telnyx/types/ai/assistants/canary_deploy_response.py">CanaryDeployResponse</a></code>
- <code title="delete /ai/assistants/{assistant_id}/canary-deploys">client.ai.assistants.canary_deploys.<a href="./src/telnyx/resources/ai/assistants/canary_deploys.py">delete</a>(assistant_id) -> None</code>

### ScheduledEvents

Types:

```python
from telnyx.types.ai.assistants import (
    ConversationChannelType,
    EventStatus,
    ScheduledEventResponse,
    ScheduledPhoneCallEventResponse,
    ScheduledSMSEventResponse,
    ScheduledEventListResponse,
)
```

Methods:

- <code title="post /ai/assistants/{assistant_id}/scheduled_events">client.ai.assistants.scheduled_events.<a href="./src/telnyx/resources/ai/assistants/scheduled_events.py">create</a>(assistant_id, \*\*<a href="src/telnyx/types/ai/assistants/scheduled_event_create_params.py">params</a>) -> <a href="./src/telnyx/types/ai/assistants/scheduled_event_response.py">ScheduledEventResponse</a></code>
- <code title="get /ai/assistants/{assistant_id}/scheduled_events/{event_id}">client.ai.assistants.scheduled_events.<a href="./src/telnyx/resources/ai/assistants/scheduled_events.py">retrieve</a>(event_id, \*, assistant_id) -> <a href="./src/telnyx/types/ai/assistants/scheduled_event_response.py">ScheduledEventResponse</a></code>
- <code title="get /ai/assistants/{assistant_id}/scheduled_events">client.ai.assistants.scheduled_events.<a href="./src/telnyx/resources/ai/assistants/scheduled_events.py">list</a>(assistant_id, \*\*<a href="src/telnyx/types/ai/assistants/scheduled_event_list_params.py">params</a>) -> <a href="./src/telnyx/types/ai/assistants/scheduled_event_list_response.py">ScheduledEventListResponse</a></code>
- <code title="delete /ai/assistants/{assistant_id}/scheduled_events/{event_id}">client.ai.assistants.scheduled_events.<a href="./src/telnyx/resources/ai/assistants/scheduled_events.py">delete</a>(event_id, \*, assistant_id) -> object</code>

### Tools

Types:

```python
from telnyx.types.ai.assistants import ToolTestResponse
```

Methods:

- <code title="post /ai/assistants/{assistant_id}/tools/{tool_id}/test">client.ai.assistants.tools.<a href="./src/telnyx/resources/ai/assistants/tools.py">test</a>(tool_id, \*, assistant_id, \*\*<a href="src/telnyx/types/ai/assistants/tool_test_params.py">params</a>) -> <a href="./src/telnyx/types/ai/assistants/tool_test_response.py">ToolTestResponse</a></code>

### Versions

Types:

```python
from telnyx.types.ai.assistants import (
    UpdateAssistant,
    VersionRetrieveResponse,
    VersionUpdateResponse,
    VersionPromoteResponse,
)
```

Methods:

- <code title="get /ai/assistants/{assistant_id}/versions/{version_id}">client.ai.assistants.versions.<a href="./src/telnyx/resources/ai/assistants/versions.py">retrieve</a>(version_id, \*, assistant_id, \*\*<a href="src/telnyx/types/ai/assistants/version_retrieve_params.py">params</a>) -> <a href="./src/telnyx/types/ai/assistants/version_retrieve_response.py">VersionRetrieveResponse</a></code>
- <code title="post /ai/assistants/{assistant_id}/versions/{version_id}">client.ai.assistants.versions.<a href="./src/telnyx/resources/ai/assistants/versions.py">update</a>(version_id, \*, assistant_id, \*\*<a href="src/telnyx/types/ai/assistants/version_update_params.py">params</a>) -> <a href="./src/telnyx/types/ai/assistants/version_update_response.py">VersionUpdateResponse</a></code>
- <code title="get /ai/assistants/{assistant_id}/versions">client.ai.assistants.versions.<a href="./src/telnyx/resources/ai/assistants/versions.py">list</a>(assistant_id) -> <a href="./src/telnyx/types/ai/assistants_list.py">AssistantsList</a></code>
- <code title="delete /ai/assistants/{assistant_id}/versions/{version_id}">client.ai.assistants.versions.<a href="./src/telnyx/resources/ai/assistants/versions.py">delete</a>(version_id, \*, assistant_id) -> None</code>
- <code title="post /ai/assistants/{assistant_id}/versions/{version_id}/promote">client.ai.assistants.versions.<a href="./src/telnyx/resources/ai/assistants/versions.py">promote</a>(version_id, \*, assistant_id) -> <a href="./src/telnyx/types/ai/assistants/version_promote_response.py">VersionPromoteResponse</a></code>

## Audio

Types:

```python
from telnyx.types.ai import AudioTranscribeResponse
```

Methods:

- <code title="post /ai/audio/transcriptions">client.ai.audio.<a href="./src/telnyx/resources/ai/audio.py">transcribe</a>(\*\*<a href="src/telnyx/types/ai/audio_transcribe_params.py">params</a>) -> <a href="./src/telnyx/types/ai/audio_transcribe_response.py">AudioTranscribeResponse</a></code>

## Chat

Types:

```python
from telnyx.types.ai import BucketIDs
```

Methods:

- <code title="post /ai/chat/completions">client.ai.chat.<a href="./src/telnyx/resources/ai/chat.py">create_completion</a>(\*\*<a href="src/telnyx/types/ai/chat_create_completion_params.py">params</a>) -> object</code>

## Clusters

Types:

```python
from telnyx.types.ai import (
    RecursiveCluster,
    ClusterRetrieveResponse,
    ClusterListResponse,
    ClusterComputeResponse,
)
```

Methods:

- <code title="get /ai/clusters/{task_id}">client.ai.clusters.<a href="./src/telnyx/resources/ai/clusters.py">retrieve</a>(task_id, \*\*<a href="src/telnyx/types/ai/cluster_retrieve_params.py">params</a>) -> <a href="./src/telnyx/types/ai/cluster_retrieve_response.py">ClusterRetrieveResponse</a></code>
- <code title="get /ai/clusters">client.ai.clusters.<a href="./src/telnyx/resources/ai/clusters.py">list</a>(\*\*<a href="src/telnyx/types/ai/cluster_list_params.py">params</a>) -> <a href="./src/telnyx/types/ai/cluster_list_response.py">ClusterListResponse</a></code>
- <code title="delete /ai/clusters/{task_id}">client.ai.clusters.<a href="./src/telnyx/resources/ai/clusters.py">delete</a>(task_id) -> None</code>
- <code title="post /ai/clusters">client.ai.clusters.<a href="./src/telnyx/resources/ai/clusters.py">compute</a>(\*\*<a href="src/telnyx/types/ai/cluster_compute_params.py">params</a>) -> <a href="./src/telnyx/types/ai/cluster_compute_response.py">ClusterComputeResponse</a></code>
- <code title="get /ai/clusters/{task_id}/graph">client.ai.clusters.<a href="./src/telnyx/resources/ai/clusters.py">fetch_graph</a>(task_id, \*\*<a href="src/telnyx/types/ai/cluster_fetch_graph_params.py">params</a>) -> object</code>

## Conversations

Types:

```python
from telnyx.types.ai import (
    Conversation,
    ConversationRetrieveResponse,
    ConversationUpdateResponse,
    ConversationListResponse,
    ConversationRetrieveConversationsInsightsResponse,
)
```

Methods:

- <code title="post /ai/conversations">client.ai.conversations.<a href="./src/telnyx/resources/ai/conversations/conversations.py">create</a>(\*\*<a href="src/telnyx/types/ai/conversation_create_params.py">params</a>) -> <a href="./src/telnyx/types/ai/conversation.py">Conversation</a></code>
- <code title="get /ai/conversations/{conversation_id}">client.ai.conversations.<a href="./src/telnyx/resources/ai/conversations/conversations.py">retrieve</a>(conversation_id) -> <a href="./src/telnyx/types/ai/conversation_retrieve_response.py">ConversationRetrieveResponse</a></code>
- <code title="put /ai/conversations/{conversation_id}">client.ai.conversations.<a href="./src/telnyx/resources/ai/conversations/conversations.py">update</a>(conversation_id, \*\*<a href="src/telnyx/types/ai/conversation_update_params.py">params</a>) -> <a href="./src/telnyx/types/ai/conversation_update_response.py">ConversationUpdateResponse</a></code>
- <code title="get /ai/conversations">client.ai.conversations.<a href="./src/telnyx/resources/ai/conversations/conversations.py">list</a>(\*\*<a href="src/telnyx/types/ai/conversation_list_params.py">params</a>) -> <a href="./src/telnyx/types/ai/conversation_list_response.py">ConversationListResponse</a></code>
- <code title="delete /ai/conversations/{conversation_id}">client.ai.conversations.<a href="./src/telnyx/resources/ai/conversations/conversations.py">delete</a>(conversation_id) -> None</code>
- <code title="get /ai/conversations/{conversation_id}/conversations-insights">client.ai.conversations.<a href="./src/telnyx/resources/ai/conversations/conversations.py">retrieve_conversations_insights</a>(conversation_id) -> <a href="./src/telnyx/types/ai/conversation_retrieve_conversations_insights_response.py">ConversationRetrieveConversationsInsightsResponse</a></code>

### InsightGroups

Types:

```python
from telnyx.types.ai.conversations import (
    InsightTemplateGroup,
    InsightTemplateGroupDetail,
    InsightGroupRetrieveInsightGroupsResponse,
)
```

Methods:

- <code title="get /ai/conversations/insight-groups/{group_id}">client.ai.conversations.insight_groups.<a href="./src/telnyx/resources/ai/conversations/insight_groups/insight_groups.py">retrieve</a>(group_id) -> <a href="./src/telnyx/types/ai/conversations/insight_template_group_detail.py">InsightTemplateGroupDetail</a></code>
- <code title="put /ai/conversations/insight-groups/{group_id}">client.ai.conversations.insight_groups.<a href="./src/telnyx/resources/ai/conversations/insight_groups/insight_groups.py">update</a>(group_id, \*\*<a href="src/telnyx/types/ai/conversations/insight_group_update_params.py">params</a>) -> <a href="./src/telnyx/types/ai/conversations/insight_template_group_detail.py">InsightTemplateGroupDetail</a></code>
- <code title="delete /ai/conversations/insight-groups/{group_id}">client.ai.conversations.insight_groups.<a href="./src/telnyx/resources/ai/conversations/insight_groups/insight_groups.py">delete</a>(group_id) -> object</code>
- <code title="post /ai/conversations/insight-groups">client.ai.conversations.insight_groups.<a href="./src/telnyx/resources/ai/conversations/insight_groups/insight_groups.py">insight_groups</a>(\*\*<a href="src/telnyx/types/ai/conversations/insight_group_insight_groups_params.py">params</a>) -> <a href="./src/telnyx/types/ai/conversations/insight_template_group_detail.py">InsightTemplateGroupDetail</a></code>
- <code title="get /ai/conversations/insight-groups">client.ai.conversations.insight_groups.<a href="./src/telnyx/resources/ai/conversations/insight_groups/insight_groups.py">retrieve_insight_groups</a>(\*\*<a href="src/telnyx/types/ai/conversations/insight_group_retrieve_insight_groups_params.py">params</a>) -> <a href="./src/telnyx/types/ai/conversations/insight_group_retrieve_insight_groups_response.py">InsightGroupRetrieveInsightGroupsResponse</a></code>

#### Insights

Methods:

- <code title="post /ai/conversations/insight-groups/{group_id}/insights/{insight_id}/assign">client.ai.conversations.insight_groups.insights.<a href="./src/telnyx/resources/ai/conversations/insight_groups/insights.py">assign</a>(insight_id, \*, group_id) -> object</code>
- <code title="delete /ai/conversations/insight-groups/{group_id}/insights/{insight_id}/unassign">client.ai.conversations.insight_groups.insights.<a href="./src/telnyx/resources/ai/conversations/insight_groups/insights.py">delete_unassign</a>(insight_id, \*, group_id) -> object</code>

### Insights

Types:

```python
from telnyx.types.ai.conversations import (
    InsightTemplate,
    InsightTemplateDetail,
    InsightListResponse,
)
```

Methods:

- <code title="post /ai/conversations/insights">client.ai.conversations.insights.<a href="./src/telnyx/resources/ai/conversations/insights.py">create</a>(\*\*<a href="src/telnyx/types/ai/conversations/insight_create_params.py">params</a>) -> <a href="./src/telnyx/types/ai/conversations/insight_template_detail.py">InsightTemplateDetail</a></code>
- <code title="get /ai/conversations/insights/{insight_id}">client.ai.conversations.insights.<a href="./src/telnyx/resources/ai/conversations/insights.py">retrieve</a>(insight_id) -> <a href="./src/telnyx/types/ai/conversations/insight_template_detail.py">InsightTemplateDetail</a></code>
- <code title="put /ai/conversations/insights/{insight_id}">client.ai.conversations.insights.<a href="./src/telnyx/resources/ai/conversations/insights.py">update</a>(insight_id, \*\*<a href="src/telnyx/types/ai/conversations/insight_update_params.py">params</a>) -> <a href="./src/telnyx/types/ai/conversations/insight_template_detail.py">InsightTemplateDetail</a></code>
- <code title="get /ai/conversations/insights">client.ai.conversations.insights.<a href="./src/telnyx/resources/ai/conversations/insights.py">list</a>(\*\*<a href="src/telnyx/types/ai/conversations/insight_list_params.py">params</a>) -> <a href="./src/telnyx/types/ai/conversations/insight_list_response.py">InsightListResponse</a></code>
- <code title="delete /ai/conversations/insights/{insight_id}">client.ai.conversations.insights.<a href="./src/telnyx/resources/ai/conversations/insights.py">delete</a>(insight_id) -> object</code>

### Messages

Types:

```python
from telnyx.types.ai.conversations import MessageListResponse
```

Methods:

- <code title="post /ai/conversations/{conversation_id}/messages">client.ai.conversations.messages.<a href="./src/telnyx/resources/ai/conversations/messages.py">create</a>(conversation_id, \*\*<a href="src/telnyx/types/ai/conversations/message_create_params.py">params</a>) -> object</code>
- <code title="get /ai/conversations/{conversation_id}/messages">client.ai.conversations.messages.<a href="./src/telnyx/resources/ai/conversations/messages.py">list</a>(conversation_id) -> <a href="./src/telnyx/types/ai/conversations/message_list_response.py">MessageListResponse</a></code>

## Embeddings

Types:

```python
from telnyx.types.ai import (
    BackgroundTaskStatus,
    EmbeddingResponse,
    EmbeddingRetrieveResponse,
    EmbeddingListResponse,
    EmbeddingSimilaritySearchResponse,
)
```

Methods:

- <code title="post /ai/embeddings">client.ai.embeddings.<a href="./src/telnyx/resources/ai/embeddings/embeddings.py">create</a>(\*\*<a href="src/telnyx/types/ai/embedding_create_params.py">params</a>) -> <a href="./src/telnyx/types/ai/embedding_response.py">EmbeddingResponse</a></code>
- <code title="get /ai/embeddings/{task_id}">client.ai.embeddings.<a href="./src/telnyx/resources/ai/embeddings/embeddings.py">retrieve</a>(task_id) -> <a href="./src/telnyx/types/ai/embedding_retrieve_response.py">EmbeddingRetrieveResponse</a></code>
- <code title="get /ai/embeddings">client.ai.embeddings.<a href="./src/telnyx/resources/ai/embeddings/embeddings.py">list</a>(\*\*<a href="src/telnyx/types/ai/embedding_list_params.py">params</a>) -> <a href="./src/telnyx/types/ai/embedding_list_response.py">EmbeddingListResponse</a></code>
- <code title="post /ai/embeddings/similarity-search">client.ai.embeddings.<a href="./src/telnyx/resources/ai/embeddings/embeddings.py">similarity_search</a>(\*\*<a href="src/telnyx/types/ai/embedding_similarity_search_params.py">params</a>) -> <a href="./src/telnyx/types/ai/embedding_similarity_search_response.py">EmbeddingSimilaritySearchResponse</a></code>
- <code title="post /ai/embeddings/url">client.ai.embeddings.<a href="./src/telnyx/resources/ai/embeddings/embeddings.py">url</a>(\*\*<a href="src/telnyx/types/ai/embedding_url_params.py">params</a>) -> <a href="./src/telnyx/types/ai/embedding_response.py">EmbeddingResponse</a></code>

### Buckets

Types:

```python
from telnyx.types.ai.embeddings import BucketRetrieveResponse, BucketListResponse
```

Methods:

- <code title="get /ai/embeddings/buckets/{bucket_name}">client.ai.embeddings.buckets.<a href="./src/telnyx/resources/ai/embeddings/buckets.py">retrieve</a>(bucket_name) -> <a href="./src/telnyx/types/ai/embeddings/bucket_retrieve_response.py">BucketRetrieveResponse</a></code>
- <code title="get /ai/embeddings/buckets">client.ai.embeddings.buckets.<a href="./src/telnyx/resources/ai/embeddings/buckets.py">list</a>() -> <a href="./src/telnyx/types/ai/embeddings/bucket_list_response.py">BucketListResponse</a></code>
- <code title="delete /ai/embeddings/buckets/{bucket_name}">client.ai.embeddings.buckets.<a href="./src/telnyx/resources/ai/embeddings/buckets.py">delete</a>(bucket_name) -> None</code>

## FineTuning

### Jobs

Types:

```python
from telnyx.types.ai.fine_tuning import FineTuningJob, JobListResponse
```

Methods:

- <code title="post /ai/fine_tuning/jobs">client.ai.fine_tuning.jobs.<a href="./src/telnyx/resources/ai/fine_tuning/jobs.py">create</a>(\*\*<a href="src/telnyx/types/ai/fine_tuning/job_create_params.py">params</a>) -> <a href="./src/telnyx/types/ai/fine_tuning/fine_tuning_job.py">FineTuningJob</a></code>
- <code title="get /ai/fine_tuning/jobs/{job_id}">client.ai.fine_tuning.jobs.<a href="./src/telnyx/resources/ai/fine_tuning/jobs.py">retrieve</a>(job_id) -> <a href="./src/telnyx/types/ai/fine_tuning/fine_tuning_job.py">FineTuningJob</a></code>
- <code title="get /ai/fine_tuning/jobs">client.ai.fine_tuning.jobs.<a href="./src/telnyx/resources/ai/fine_tuning/jobs.py">list</a>() -> <a href="./src/telnyx/types/ai/fine_tuning/job_list_response.py">JobListResponse</a></code>
- <code title="post /ai/fine_tuning/jobs/{job_id}/cancel">client.ai.fine_tuning.jobs.<a href="./src/telnyx/resources/ai/fine_tuning/jobs.py">cancel</a>(job_id) -> <a href="./src/telnyx/types/ai/fine_tuning/fine_tuning_job.py">FineTuningJob</a></code>

# AuditEvents

Types:

```python
from telnyx.types import AuditEventListResponse
```

Methods:

- <code title="get /audit_events">client.audit_events.<a href="./src/telnyx/resources/audit_events.py">list</a>(\*\*<a href="src/telnyx/types/audit_event_list_params.py">params</a>) -> <a href="./src/telnyx/types/audit_event_list_response.py">AuditEventListResponse</a></code>

# AuthenticationProviders

Types:

```python
from telnyx.types import (
    AuthenticationProvider,
    PaginationMeta,
    Settings,
    AuthenticationProviderCreateResponse,
    AuthenticationProviderRetrieveResponse,
    AuthenticationProviderUpdateResponse,
    AuthenticationProviderListResponse,
    AuthenticationProviderDeleteResponse,
)
```

Methods:

- <code title="post /authentication_providers">client.authentication_providers.<a href="./src/telnyx/resources/authentication_providers.py">create</a>(\*\*<a href="src/telnyx/types/authentication_provider_create_params.py">params</a>) -> <a href="./src/telnyx/types/authentication_provider_create_response.py">AuthenticationProviderCreateResponse</a></code>
- <code title="get /authentication_providers/{id}">client.authentication_providers.<a href="./src/telnyx/resources/authentication_providers.py">retrieve</a>(id) -> <a href="./src/telnyx/types/authentication_provider_retrieve_response.py">AuthenticationProviderRetrieveResponse</a></code>
- <code title="patch /authentication_providers/{id}">client.authentication_providers.<a href="./src/telnyx/resources/authentication_providers.py">update</a>(id, \*\*<a href="src/telnyx/types/authentication_provider_update_params.py">params</a>) -> <a href="./src/telnyx/types/authentication_provider_update_response.py">AuthenticationProviderUpdateResponse</a></code>
- <code title="get /authentication_providers">client.authentication_providers.<a href="./src/telnyx/resources/authentication_providers.py">list</a>(\*\*<a href="src/telnyx/types/authentication_provider_list_params.py">params</a>) -> <a href="./src/telnyx/types/authentication_provider_list_response.py">AuthenticationProviderListResponse</a></code>
- <code title="delete /authentication_providers/{id}">client.authentication_providers.<a href="./src/telnyx/resources/authentication_providers.py">delete</a>(id) -> <a href="./src/telnyx/types/authentication_provider_delete_response.py">AuthenticationProviderDeleteResponse</a></code>

# AvailablePhoneNumberBlocks

Types:

```python
from telnyx.types import AvailablePhoneNumberBlockListResponse
```

Methods:

- <code title="get /available_phone_number_blocks">client.available_phone_number_blocks.<a href="./src/telnyx/resources/available_phone_number_blocks.py">list</a>(\*\*<a href="src/telnyx/types/available_phone_number_block_list_params.py">params</a>) -> <a href="./src/telnyx/types/available_phone_number_block_list_response.py">AvailablePhoneNumberBlockListResponse</a></code>

# AvailablePhoneNumbers

Types:

```python
from telnyx.types import AvailablePhoneNumberListResponse
```

Methods:

- <code title="get /available_phone_numbers">client.available_phone_numbers.<a href="./src/telnyx/resources/available_phone_numbers.py">list</a>(\*\*<a href="src/telnyx/types/available_phone_number_list_params.py">params</a>) -> <a href="./src/telnyx/types/available_phone_number_list_response.py">AvailablePhoneNumberListResponse</a></code>

# Balance

Types:

```python
from telnyx.types import BalanceRetrieveResponse
```

Methods:

- <code title="get /balance">client.balance.<a href="./src/telnyx/resources/balance.py">retrieve</a>() -> <a href="./src/telnyx/types/balance_retrieve_response.py">BalanceRetrieveResponse</a></code>

# BillingGroups

Types:

```python
from telnyx.types import (
    BillingGroup,
    BillingGroupCreateResponse,
    BillingGroupRetrieveResponse,
    BillingGroupUpdateResponse,
    BillingGroupListResponse,
    BillingGroupDeleteResponse,
)
```

Methods:

- <code title="post /billing_groups">client.billing_groups.<a href="./src/telnyx/resources/billing_groups.py">create</a>(\*\*<a href="src/telnyx/types/billing_group_create_params.py">params</a>) -> <a href="./src/telnyx/types/billing_group_create_response.py">BillingGroupCreateResponse</a></code>
- <code title="get /billing_groups/{id}">client.billing_groups.<a href="./src/telnyx/resources/billing_groups.py">retrieve</a>(id) -> <a href="./src/telnyx/types/billing_group_retrieve_response.py">BillingGroupRetrieveResponse</a></code>
- <code title="patch /billing_groups/{id}">client.billing_groups.<a href="./src/telnyx/resources/billing_groups.py">update</a>(id, \*\*<a href="src/telnyx/types/billing_group_update_params.py">params</a>) -> <a href="./src/telnyx/types/billing_group_update_response.py">BillingGroupUpdateResponse</a></code>
- <code title="get /billing_groups">client.billing_groups.<a href="./src/telnyx/resources/billing_groups.py">list</a>(\*\*<a href="src/telnyx/types/billing_group_list_params.py">params</a>) -> <a href="./src/telnyx/types/billing_group_list_response.py">BillingGroupListResponse</a></code>
- <code title="delete /billing_groups/{id}">client.billing_groups.<a href="./src/telnyx/resources/billing_groups.py">delete</a>(id) -> <a href="./src/telnyx/types/billing_group_delete_response.py">BillingGroupDeleteResponse</a></code>

# Brand

Types:

```python
from telnyx.types import (
    AltBusinessIDType,
    BrandIdentityStatus,
    EntityType,
    StockExchange,
    TelnyxBrand,
    Vertical,
    BrandRetrieveResponse,
    BrandListResponse,
    BrandGetFeedbackResponse,
)
```

Methods:

- <code title="post /brand">client.brand.<a href="./src/telnyx/resources/brand/brand.py">create</a>(\*\*<a href="src/telnyx/types/brand_create_params.py">params</a>) -> <a href="./src/telnyx/types/telnyx_brand.py">TelnyxBrand</a></code>
- <code title="get /brand/{brandId}">client.brand.<a href="./src/telnyx/resources/brand/brand.py">retrieve</a>(brand_id) -> <a href="./src/telnyx/types/brand_retrieve_response.py">BrandRetrieveResponse</a></code>
- <code title="put /brand/{brandId}">client.brand.<a href="./src/telnyx/resources/brand/brand.py">update</a>(brand_id, \*\*<a href="src/telnyx/types/brand_update_params.py">params</a>) -> <a href="./src/telnyx/types/telnyx_brand.py">TelnyxBrand</a></code>
- <code title="get /brand">client.brand.<a href="./src/telnyx/resources/brand/brand.py">list</a>(\*\*<a href="src/telnyx/types/brand_list_params.py">params</a>) -> <a href="./src/telnyx/types/brand_list_response.py">BrandListResponse</a></code>
- <code title="delete /brand/{brandId}">client.brand.<a href="./src/telnyx/resources/brand/brand.py">delete</a>(brand_id) -> object</code>
- <code title="get /brand/feedback/{brandId}">client.brand.<a href="./src/telnyx/resources/brand/brand.py">get_feedback</a>(brand_id) -> <a href="./src/telnyx/types/brand_get_feedback_response.py">BrandGetFeedbackResponse</a></code>
- <code title="post /brand/{brandId}/2faEmail">client.brand.<a href="./src/telnyx/resources/brand/brand.py">resend_2fa_email</a>(brand_id) -> None</code>
- <code title="put /brand/{brandId}/revet">client.brand.<a href="./src/telnyx/resources/brand/brand.py">revet</a>(brand_id) -> object</code>

## ExternalVetting

Types:

```python
from telnyx.types.brand import ExternalVettingImportResponse
```

Methods:

- <code title="get /brand/{brandId}/externalVetting">client.brand.external_vetting.<a href="./src/telnyx/resources/brand/external_vetting.py">list</a>(brand_id) -> object</code>
- <code title="put /brand/{brandId}/externalVetting">client.brand.external*vetting.<a href="./src/telnyx/resources/brand/external_vetting.py">import*</a>(brand_id, \*\*<a href="src/telnyx/types/brand/external_vetting_import_params.py">params</a>) -> <a href="./src/telnyx/types/brand/external_vetting_import_response.py">ExternalVettingImportResponse</a></code>
- <code title="post /brand/{brandId}/externalVetting">client.brand.external_vetting.<a href="./src/telnyx/resources/brand/external_vetting.py">order</a>(brand_id, \*\*<a href="src/telnyx/types/brand/external_vetting_order_params.py">params</a>) -> object</code>

# BulkSimCardActions

Types:

```python
from telnyx.types import BulkSimCardActionRetrieveResponse, BulkSimCardActionListResponse
```

Methods:

- <code title="get /bulk_sim_card_actions/{id}">client.bulk_sim_card_actions.<a href="./src/telnyx/resources/bulk_sim_card_actions.py">retrieve</a>(id) -> <a href="./src/telnyx/types/bulk_sim_card_action_retrieve_response.py">BulkSimCardActionRetrieveResponse</a></code>
- <code title="get /bulk_sim_card_actions">client.bulk_sim_card_actions.<a href="./src/telnyx/resources/bulk_sim_card_actions.py">list</a>(\*\*<a href="src/telnyx/types/bulk_sim_card_action_list_params.py">params</a>) -> <a href="./src/telnyx/types/bulk_sim_card_action_list_response.py">BulkSimCardActionListResponse</a></code>

# BundlePricing

## BillingBundles

Types:

```python
from telnyx.types.bundle_pricing import (
    BillingBundleSummary,
    PaginationResponse,
    BillingBundleRetrieveResponse,
    BillingBundleListResponse,
)
```

Methods:

- <code title="get /bundle_pricing/billing_bundles/{bundle_id}">client.bundle_pricing.billing_bundles.<a href="./src/telnyx/resources/bundle_pricing/billing_bundles.py">retrieve</a>(bundle_id) -> <a href="./src/telnyx/types/bundle_pricing/billing_bundle_retrieve_response.py">BillingBundleRetrieveResponse</a></code>
- <code title="get /bundle_pricing/billing_bundles">client.bundle_pricing.billing_bundles.<a href="./src/telnyx/resources/bundle_pricing/billing_bundles.py">list</a>(\*\*<a href="src/telnyx/types/bundle_pricing/billing_bundle_list_params.py">params</a>) -> <a href="./src/telnyx/types/bundle_pricing/billing_bundle_list_response.py">BillingBundleListResponse</a></code>

## UserBundles

Types:

```python
from telnyx.types.bundle_pricing import (
    UserBundle,
    UserBundleResource,
    UserBundleCreateResponse,
    UserBundleRetrieveResponse,
    UserBundleListResponse,
    UserBundleDeactivateResponse,
    UserBundleListResourcesResponse,
    UserBundleListUnusedResponse,
)
```

Methods:

- <code title="post /bundle_pricing/user_bundles/bulk">client.bundle_pricing.user_bundles.<a href="./src/telnyx/resources/bundle_pricing/user_bundles.py">create</a>(\*\*<a href="src/telnyx/types/bundle_pricing/user_bundle_create_params.py">params</a>) -> <a href="./src/telnyx/types/bundle_pricing/user_bundle_create_response.py">UserBundleCreateResponse</a></code>
- <code title="get /bundle_pricing/user_bundles/{user_bundle_id}">client.bundle_pricing.user_bundles.<a href="./src/telnyx/resources/bundle_pricing/user_bundles.py">retrieve</a>(user_bundle_id) -> <a href="./src/telnyx/types/bundle_pricing/user_bundle_retrieve_response.py">UserBundleRetrieveResponse</a></code>
- <code title="get /bundle_pricing/user_bundles">client.bundle_pricing.user_bundles.<a href="./src/telnyx/resources/bundle_pricing/user_bundles.py">list</a>(\*\*<a href="src/telnyx/types/bundle_pricing/user_bundle_list_params.py">params</a>) -> <a href="./src/telnyx/types/bundle_pricing/user_bundle_list_response.py">UserBundleListResponse</a></code>
- <code title="delete /bundle_pricing/user_bundles/{user_bundle_id}">client.bundle_pricing.user_bundles.<a href="./src/telnyx/resources/bundle_pricing/user_bundles.py">deactivate</a>(user_bundle_id) -> <a href="./src/telnyx/types/bundle_pricing/user_bundle_deactivate_response.py">UserBundleDeactivateResponse</a></code>
- <code title="get /bundle_pricing/user_bundles/{user_bundle_id}/resources">client.bundle_pricing.user_bundles.<a href="./src/telnyx/resources/bundle_pricing/user_bundles.py">list_resources</a>(user_bundle_id) -> <a href="./src/telnyx/types/bundle_pricing/user_bundle_list_resources_response.py">UserBundleListResourcesResponse</a></code>
- <code title="get /bundle_pricing/user_bundles/unused">client.bundle_pricing.user_bundles.<a href="./src/telnyx/resources/bundle_pricing/user_bundles.py">list_unused</a>(\*\*<a href="src/telnyx/types/bundle_pricing/user_bundle_list_unused_params.py">params</a>) -> <a href="./src/telnyx/types/bundle_pricing/user_bundle_list_unused_response.py">UserBundleListUnusedResponse</a></code>

# CallControlApplications

Types:

```python
from telnyx.types import (
    CallControlApplication,
    CallControlApplicationInbound,
    CallControlApplicationOutbound,
    CallControlApplicationCreateResponse,
    CallControlApplicationRetrieveResponse,
    CallControlApplicationUpdateResponse,
    CallControlApplicationListResponse,
    CallControlApplicationDeleteResponse,
)
```

Methods:

- <code title="post /call_control_applications">client.call_control_applications.<a href="./src/telnyx/resources/call_control_applications.py">create</a>(\*\*<a href="src/telnyx/types/call_control_application_create_params.py">params</a>) -> <a href="./src/telnyx/types/call_control_application_create_response.py">CallControlApplicationCreateResponse</a></code>
- <code title="get /call_control_applications/{id}">client.call_control_applications.<a href="./src/telnyx/resources/call_control_applications.py">retrieve</a>(id) -> <a href="./src/telnyx/types/call_control_application_retrieve_response.py">CallControlApplicationRetrieveResponse</a></code>
- <code title="patch /call_control_applications/{id}">client.call_control_applications.<a href="./src/telnyx/resources/call_control_applications.py">update</a>(id, \*\*<a href="src/telnyx/types/call_control_application_update_params.py">params</a>) -> <a href="./src/telnyx/types/call_control_application_update_response.py">CallControlApplicationUpdateResponse</a></code>
- <code title="get /call_control_applications">client.call_control_applications.<a href="./src/telnyx/resources/call_control_applications.py">list</a>(\*\*<a href="src/telnyx/types/call_control_application_list_params.py">params</a>) -> <a href="./src/telnyx/types/call_control_application_list_response.py">CallControlApplicationListResponse</a></code>
- <code title="delete /call_control_applications/{id}">client.call_control_applications.<a href="./src/telnyx/resources/call_control_applications.py">delete</a>(id) -> <a href="./src/telnyx/types/call_control_application_delete_response.py">CallControlApplicationDeleteResponse</a></code>

# CallEvents

Types:

```python
from telnyx.types import CallEventListResponse
```

Methods:

- <code title="get /call_events">client.call_events.<a href="./src/telnyx/resources/call_events.py">list</a>(\*\*<a href="src/telnyx/types/call_event_list_params.py">params</a>) -> <a href="./src/telnyx/types/call_event_list_response.py">CallEventListResponse</a></code>

# Calls

Types:

```python
from telnyx.types import (
    CustomSipHeader,
    DialogflowConfig,
    SipHeader,
    SoundModifications,
    StreamBidirectionalCodec,
    StreamBidirectionalMode,
    StreamBidirectionalTargetLegs,
    StreamCodec,
    CallDialResponse,
    CallRetrieveStatusResponse,
)
```

Methods:

- <code title="post /calls">client.calls.<a href="./src/telnyx/resources/calls/calls.py">dial</a>(\*\*<a href="src/telnyx/types/call_dial_params.py">params</a>) -> <a href="./src/telnyx/types/call_dial_response.py">CallDialResponse</a></code>
- <code title="get /calls/{call_control_id}">client.calls.<a href="./src/telnyx/resources/calls/calls.py">retrieve_status</a>(call_control_id) -> <a href="./src/telnyx/types/call_retrieve_status_response.py">CallRetrieveStatusResponse</a></code>

## Actions

Types:

```python
from telnyx.types.calls import (
    AwsVoiceSettings,
    CallControlCommandResult,
    ElevenLabsVoiceSettings,
    GoogleTranscriptionLanguage,
    InterruptionSettings,
    Loopcount,
    StopRecordingRequest,
    TelnyxVoiceSettings,
    TranscriptionConfig,
    TranscriptionEngineAConfig,
    TranscriptionEngineBConfig,
    TranscriptionStartRequest,
    ActionAnswerResponse,
    ActionBridgeResponse,
    ActionEnqueueResponse,
    ActionGatherResponse,
    ActionGatherUsingAIResponse,
    ActionGatherUsingAudioResponse,
    ActionGatherUsingSpeakResponse,
    ActionHangupResponse,
    ActionLeaveQueueResponse,
    ActionPauseRecordingResponse,
    ActionReferResponse,
    ActionRejectResponse,
    ActionResumeRecordingResponse,
    ActionSendDtmfResponse,
    ActionSendSipInfoResponse,
    ActionSpeakResponse,
    ActionStartAIAssistantResponse,
    ActionStartForkingResponse,
    ActionStartNoiseSuppressionResponse,
    ActionStartPlaybackResponse,
    ActionStartRecordingResponse,
    ActionStartSiprecResponse,
    ActionStartStreamingResponse,
    ActionStartTranscriptionResponse,
    ActionStopAIAssistantResponse,
    ActionStopForkingResponse,
    ActionStopGatherResponse,
    ActionStopNoiseSuppressionResponse,
    ActionStopPlaybackResponse,
    ActionStopRecordingResponse,
    ActionStopSiprecResponse,
    ActionStopStreamingResponse,
    ActionStopTranscriptionResponse,
    ActionSwitchSupervisorRoleResponse,
    ActionTransferResponse,
    ActionUpdateClientStateResponse,
)
```

Methods:

- <code title="post /calls/{call_control_id}/actions/answer">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">answer</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_answer_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_answer_response.py">ActionAnswerResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/bridge">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">bridge</a>(path_call_control_id, \*\*<a href="src/telnyx/types/calls/action_bridge_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_bridge_response.py">ActionBridgeResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/enqueue">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">enqueue</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_enqueue_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_enqueue_response.py">ActionEnqueueResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/gather">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">gather</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_gather_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_gather_response.py">ActionGatherResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/gather_using_ai">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">gather_using_ai</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_gather_using_ai_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_gather_using_ai_response.py">ActionGatherUsingAIResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/gather_using_audio">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">gather_using_audio</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_gather_using_audio_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_gather_using_audio_response.py">ActionGatherUsingAudioResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/gather_using_speak">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">gather_using_speak</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_gather_using_speak_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_gather_using_speak_response.py">ActionGatherUsingSpeakResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/hangup">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">hangup</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_hangup_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_hangup_response.py">ActionHangupResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/leave_queue">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">leave_queue</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_leave_queue_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_leave_queue_response.py">ActionLeaveQueueResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/record_pause">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">pause_recording</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_pause_recording_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_pause_recording_response.py">ActionPauseRecordingResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/refer">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">refer</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_refer_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_refer_response.py">ActionReferResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/reject">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">reject</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_reject_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_reject_response.py">ActionRejectResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/record_resume">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">resume_recording</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_resume_recording_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_resume_recording_response.py">ActionResumeRecordingResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/send_dtmf">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">send_dtmf</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_send_dtmf_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_send_dtmf_response.py">ActionSendDtmfResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/send_sip_info">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">send_sip_info</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_send_sip_info_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_send_sip_info_response.py">ActionSendSipInfoResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/speak">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">speak</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_speak_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_speak_response.py">ActionSpeakResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/ai_assistant_start">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">start_ai_assistant</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_start_ai_assistant_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_start_ai_assistant_response.py">ActionStartAIAssistantResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/fork_start">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">start_forking</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_start_forking_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_start_forking_response.py">ActionStartForkingResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/suppression_start">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">start_noise_suppression</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_start_noise_suppression_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_start_noise_suppression_response.py">ActionStartNoiseSuppressionResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/playback_start">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">start_playback</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_start_playback_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_start_playback_response.py">ActionStartPlaybackResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/record_start">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">start_recording</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_start_recording_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_start_recording_response.py">ActionStartRecordingResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/siprec_start">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">start_siprec</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_start_siprec_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_start_siprec_response.py">ActionStartSiprecResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/streaming_start">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">start_streaming</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_start_streaming_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_start_streaming_response.py">ActionStartStreamingResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/transcription_start">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">start_transcription</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_start_transcription_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_start_transcription_response.py">ActionStartTranscriptionResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/ai_assistant_stop">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">stop_ai_assistant</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_stop_ai_assistant_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_stop_ai_assistant_response.py">ActionStopAIAssistantResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/fork_stop">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">stop_forking</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_stop_forking_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_stop_forking_response.py">ActionStopForkingResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/gather_stop">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">stop_gather</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_stop_gather_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_stop_gather_response.py">ActionStopGatherResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/suppression_stop">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">stop_noise_suppression</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_stop_noise_suppression_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_stop_noise_suppression_response.py">ActionStopNoiseSuppressionResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/playback_stop">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">stop_playback</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_stop_playback_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_stop_playback_response.py">ActionStopPlaybackResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/record_stop">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">stop_recording</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_stop_recording_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_stop_recording_response.py">ActionStopRecordingResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/siprec_stop">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">stop_siprec</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_stop_siprec_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_stop_siprec_response.py">ActionStopSiprecResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/streaming_stop">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">stop_streaming</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_stop_streaming_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_stop_streaming_response.py">ActionStopStreamingResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/transcription_stop">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">stop_transcription</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_stop_transcription_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_stop_transcription_response.py">ActionStopTranscriptionResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/switch_supervisor_role">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">switch_supervisor_role</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_switch_supervisor_role_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_switch_supervisor_role_response.py">ActionSwitchSupervisorRoleResponse</a></code>
- <code title="post /calls/{call_control_id}/actions/transfer">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">transfer</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_transfer_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_transfer_response.py">ActionTransferResponse</a></code>
- <code title="put /calls/{call_control_id}/actions/client_state_update">client.calls.actions.<a href="./src/telnyx/resources/calls/actions.py">update_client_state</a>(call_control_id, \*\*<a href="src/telnyx/types/calls/action_update_client_state_params.py">params</a>) -> <a href="./src/telnyx/types/calls/action_update_client_state_response.py">ActionUpdateClientStateResponse</a></code>

# Campaign

Types:

```python
from telnyx.types import (
    CampaignSharingStatus,
    TelnyxCampaignCsp,
    CampaignListResponse,
    CampaignDeactivateResponse,
    CampaignGetMnoMetadataResponse,
    CampaignGetSharingStatusResponse,
    CampaignSubmitAppealResponse,
)
```

Methods:

- <code title="get /campaign/{campaignId}">client.campaign.<a href="./src/telnyx/resources/campaign/campaign.py">retrieve</a>(campaign_id) -> <a href="./src/telnyx/types/telnyx_campaign_csp.py">TelnyxCampaignCsp</a></code>
- <code title="put /campaign/{campaignId}">client.campaign.<a href="./src/telnyx/resources/campaign/campaign.py">update</a>(campaign_id, \*\*<a href="src/telnyx/types/campaign_update_params.py">params</a>) -> <a href="./src/telnyx/types/telnyx_campaign_csp.py">TelnyxCampaignCsp</a></code>
- <code title="get /campaign">client.campaign.<a href="./src/telnyx/resources/campaign/campaign.py">list</a>(\*\*<a href="src/telnyx/types/campaign_list_params.py">params</a>) -> <a href="./src/telnyx/types/campaign_list_response.py">CampaignListResponse</a></code>
- <code title="post /campaign/acceptSharing/{campaignId}">client.campaign.<a href="./src/telnyx/resources/campaign/campaign.py">accept_sharing</a>(campaign_id) -> object</code>
- <code title="delete /campaign/{campaignId}">client.campaign.<a href="./src/telnyx/resources/campaign/campaign.py">deactivate</a>(campaign_id) -> <a href="./src/telnyx/types/campaign_deactivate_response.py">CampaignDeactivateResponse</a></code>
- <code title="get /campaign/{campaignId}/mnoMetadata">client.campaign.<a href="./src/telnyx/resources/campaign/campaign.py">get_mno_metadata</a>(campaign_id) -> <a href="./src/telnyx/types/campaign_get_mno_metadata_response.py">CampaignGetMnoMetadataResponse</a></code>
- <code title="get /campaign/{campaignId}/operationStatus">client.campaign.<a href="./src/telnyx/resources/campaign/campaign.py">get_operation_status</a>(campaign_id) -> object</code>
- <code title="get /campaign/{campaignId}/sharing">client.campaign.<a href="./src/telnyx/resources/campaign/campaign.py">get_sharing_status</a>(campaign_id) -> <a href="./src/telnyx/types/campaign_get_sharing_status_response.py">CampaignGetSharingStatusResponse</a></code>
- <code title="post /campaign/{campaignId}/appeal">client.campaign.<a href="./src/telnyx/resources/campaign/campaign.py">submit_appeal</a>(campaign_id, \*\*<a href="src/telnyx/types/campaign_submit_appeal_params.py">params</a>) -> <a href="./src/telnyx/types/campaign_submit_appeal_response.py">CampaignSubmitAppealResponse</a></code>

## Usecase

Types:

```python
from telnyx.types.campaign import UsecaseGetCostResponse
```

Methods:

- <code title="get /campaign/usecase/cost">client.campaign.usecase.<a href="./src/telnyx/resources/campaign/usecase.py">get_cost</a>(\*\*<a href="src/telnyx/types/campaign/usecase_get_cost_params.py">params</a>) -> <a href="./src/telnyx/types/campaign/usecase_get_cost_response.py">UsecaseGetCostResponse</a></code>

## Osr

Methods:

- <code title="get /campaign/{campaignId}/osr/attributes">client.campaign.osr.<a href="./src/telnyx/resources/campaign/osr.py">get_attributes</a>(campaign_id) -> object</code>

# CampaignBuilder

Types:

```python
from telnyx.types import CampaignBuilderCreateResponse
```

Methods:

- <code title="post /campaignBuilder">client.campaign_builder.<a href="./src/telnyx/resources/campaign_builder/campaign_builder.py">create</a>(\*\*<a href="src/telnyx/types/campaign_builder_create_params.py">params</a>) -> <a href="./src/telnyx/types/campaign_builder_create_response.py">CampaignBuilderCreateResponse</a></code>

## Brand

Types:

```python
from telnyx.types.campaign_builder import BrandQualifyByUsecaseResponse
```

Methods:

- <code title="get /campaignBuilder/brand/{brandId}/usecase/{usecase}">client.campaign_builder.brand.<a href="./src/telnyx/resources/campaign_builder/brand.py">qualify_by_usecase</a>(usecase, \*, brand_id) -> <a href="./src/telnyx/types/campaign_builder/brand_qualify_by_usecase_response.py">BrandQualifyByUsecaseResponse</a></code>

# ChannelZones

Types:

```python
from telnyx.types import ChannelZoneUpdateResponse, ChannelZoneListResponse
```

Methods:

- <code title="put /channel_zones/{channel_zone_id}">client.channel_zones.<a href="./src/telnyx/resources/channel_zones.py">update</a>(channel_zone_id, \*\*<a href="src/telnyx/types/channel_zone_update_params.py">params</a>) -> <a href="./src/telnyx/types/channel_zone_update_response.py">ChannelZoneUpdateResponse</a></code>
- <code title="get /channel_zones">client.channel_zones.<a href="./src/telnyx/resources/channel_zones.py">list</a>(\*\*<a href="src/telnyx/types/channel_zone_list_params.py">params</a>) -> <a href="./src/telnyx/types/channel_zone_list_response.py">ChannelZoneListResponse</a></code>

# ChargesBreakdown

Types:

```python
from telnyx.types import ChargesBreakdownRetrieveResponse
```

Methods:

- <code title="get /charges_breakdown">client.charges_breakdown.<a href="./src/telnyx/resources/charges_breakdown.py">retrieve</a>(\*\*<a href="src/telnyx/types/charges_breakdown_retrieve_params.py">params</a>) -> <a href="./src/telnyx/types/charges_breakdown_retrieve_response.py">ChargesBreakdownRetrieveResponse</a></code>

# ChargesSummary

Types:

```python
from telnyx.types import MonthDetail, ChargesSummaryRetrieveResponse
```

Methods:

- <code title="get /charges_summary">client.charges_summary.<a href="./src/telnyx/resources/charges_summary.py">retrieve</a>(\*\*<a href="src/telnyx/types/charges_summary_retrieve_params.py">params</a>) -> <a href="./src/telnyx/types/charges_summary_retrieve_response.py">ChargesSummaryRetrieveResponse</a></code>

# Comments

Types:

```python
from telnyx.types import (
    CommentCreateResponse,
    CommentRetrieveResponse,
    CommentListResponse,
    CommentMarkAsReadResponse,
)
```

Methods:

- <code title="post /comments">client.comments.<a href="./src/telnyx/resources/comments.py">create</a>(\*\*<a href="src/telnyx/types/comment_create_params.py">params</a>) -> <a href="./src/telnyx/types/comment_create_response.py">CommentCreateResponse</a></code>
- <code title="get /comments/{id}">client.comments.<a href="./src/telnyx/resources/comments.py">retrieve</a>(id) -> <a href="./src/telnyx/types/comment_retrieve_response.py">CommentRetrieveResponse</a></code>
- <code title="get /comments">client.comments.<a href="./src/telnyx/resources/comments.py">list</a>(\*\*<a href="src/telnyx/types/comment_list_params.py">params</a>) -> <a href="./src/telnyx/types/comment_list_response.py">CommentListResponse</a></code>
- <code title="patch /comments/{id}/read">client.comments.<a href="./src/telnyx/resources/comments.py">mark_as_read</a>(id) -> <a href="./src/telnyx/types/comment_mark_as_read_response.py">CommentMarkAsReadResponse</a></code>

# Conferences

Types:

```python
from telnyx.types import (
    Conference,
    ConferenceCreateResponse,
    ConferenceRetrieveResponse,
    ConferenceListResponse,
    ConferenceListParticipantsResponse,
)
```

Methods:

- <code title="post /conferences">client.conferences.<a href="./src/telnyx/resources/conferences/conferences.py">create</a>(\*\*<a href="src/telnyx/types/conference_create_params.py">params</a>) -> <a href="./src/telnyx/types/conference_create_response.py">ConferenceCreateResponse</a></code>
- <code title="get /conferences/{id}">client.conferences.<a href="./src/telnyx/resources/conferences/conferences.py">retrieve</a>(id) -> <a href="./src/telnyx/types/conference_retrieve_response.py">ConferenceRetrieveResponse</a></code>
- <code title="get /conferences">client.conferences.<a href="./src/telnyx/resources/conferences/conferences.py">list</a>(\*\*<a href="src/telnyx/types/conference_list_params.py">params</a>) -> <a href="./src/telnyx/types/conference_list_response.py">ConferenceListResponse</a></code>
- <code title="get /conferences/{conference_id}/participants">client.conferences.<a href="./src/telnyx/resources/conferences/conferences.py">list_participants</a>(conference_id, \*\*<a href="src/telnyx/types/conference_list_participants_params.py">params</a>) -> <a href="./src/telnyx/types/conference_list_participants_response.py">ConferenceListParticipantsResponse</a></code>

## Actions

Types:

```python
from telnyx.types.conferences import (
    ConferenceCommandResult,
    UpdateConference,
    ActionUpdateResponse,
    ActionHoldResponse,
    ActionJoinResponse,
    ActionLeaveResponse,
    ActionMuteResponse,
    ActionPlayResponse,
    ActionRecordPauseResponse,
    ActionRecordResumeResponse,
    ActionRecordStartResponse,
    ActionRecordStopResponse,
    ActionSpeakResponse,
    ActionStopResponse,
    ActionUnholdResponse,
    ActionUnmuteResponse,
)
```

Methods:

- <code title="post /conferences/{id}/actions/update">client.conferences.actions.<a href="./src/telnyx/resources/conferences/actions.py">update</a>(id, \*\*<a href="src/telnyx/types/conferences/action_update_params.py">params</a>) -> <a href="./src/telnyx/types/conferences/action_update_response.py">ActionUpdateResponse</a></code>
- <code title="post /conferences/{id}/actions/hold">client.conferences.actions.<a href="./src/telnyx/resources/conferences/actions.py">hold</a>(id, \*\*<a href="src/telnyx/types/conferences/action_hold_params.py">params</a>) -> <a href="./src/telnyx/types/conferences/action_hold_response.py">ActionHoldResponse</a></code>
- <code title="post /conferences/{id}/actions/join">client.conferences.actions.<a href="./src/telnyx/resources/conferences/actions.py">join</a>(id, \*\*<a href="src/telnyx/types/conferences/action_join_params.py">params</a>) -> <a href="./src/telnyx/types/conferences/action_join_response.py">ActionJoinResponse</a></code>
- <code title="post /conferences/{id}/actions/leave">client.conferences.actions.<a href="./src/telnyx/resources/conferences/actions.py">leave</a>(id, \*\*<a href="src/telnyx/types/conferences/action_leave_params.py">params</a>) -> <a href="./src/telnyx/types/conferences/action_leave_response.py">ActionLeaveResponse</a></code>
- <code title="post /conferences/{id}/actions/mute">client.conferences.actions.<a href="./src/telnyx/resources/conferences/actions.py">mute</a>(id, \*\*<a href="src/telnyx/types/conferences/action_mute_params.py">params</a>) -> <a href="./src/telnyx/types/conferences/action_mute_response.py">ActionMuteResponse</a></code>
- <code title="post /conferences/{id}/actions/play">client.conferences.actions.<a href="./src/telnyx/resources/conferences/actions.py">play</a>(id, \*\*<a href="src/telnyx/types/conferences/action_play_params.py">params</a>) -> <a href="./src/telnyx/types/conferences/action_play_response.py">ActionPlayResponse</a></code>
- <code title="post /conferences/{id}/actions/record_pause">client.conferences.actions.<a href="./src/telnyx/resources/conferences/actions.py">record_pause</a>(id, \*\*<a href="src/telnyx/types/conferences/action_record_pause_params.py">params</a>) -> <a href="./src/telnyx/types/conferences/action_record_pause_response.py">ActionRecordPauseResponse</a></code>
- <code title="post /conferences/{id}/actions/record_resume">client.conferences.actions.<a href="./src/telnyx/resources/conferences/actions.py">record_resume</a>(id, \*\*<a href="src/telnyx/types/conferences/action_record_resume_params.py">params</a>) -> <a href="./src/telnyx/types/conferences/action_record_resume_response.py">ActionRecordResumeResponse</a></code>
- <code title="post /conferences/{id}/actions/record_start">client.conferences.actions.<a href="./src/telnyx/resources/conferences/actions.py">record_start</a>(id, \*\*<a href="src/telnyx/types/conferences/action_record_start_params.py">params</a>) -> <a href="./src/telnyx/types/conferences/action_record_start_response.py">ActionRecordStartResponse</a></code>
- <code title="post /conferences/{id}/actions/record_stop">client.conferences.actions.<a href="./src/telnyx/resources/conferences/actions.py">record_stop</a>(id, \*\*<a href="src/telnyx/types/conferences/action_record_stop_params.py">params</a>) -> <a href="./src/telnyx/types/conferences/action_record_stop_response.py">ActionRecordStopResponse</a></code>
- <code title="post /conferences/{id}/actions/speak">client.conferences.actions.<a href="./src/telnyx/resources/conferences/actions.py">speak</a>(id, \*\*<a href="src/telnyx/types/conferences/action_speak_params.py">params</a>) -> <a href="./src/telnyx/types/conferences/action_speak_response.py">ActionSpeakResponse</a></code>
- <code title="post /conferences/{id}/actions/stop">client.conferences.actions.<a href="./src/telnyx/resources/conferences/actions.py">stop</a>(id, \*\*<a href="src/telnyx/types/conferences/action_stop_params.py">params</a>) -> <a href="./src/telnyx/types/conferences/action_stop_response.py">ActionStopResponse</a></code>
- <code title="post /conferences/{id}/actions/unhold">client.conferences.actions.<a href="./src/telnyx/resources/conferences/actions.py">unhold</a>(id, \*\*<a href="src/telnyx/types/conferences/action_unhold_params.py">params</a>) -> <a href="./src/telnyx/types/conferences/action_unhold_response.py">ActionUnholdResponse</a></code>
- <code title="post /conferences/{id}/actions/unmute">client.conferences.actions.<a href="./src/telnyx/resources/conferences/actions.py">unmute</a>(id, \*\*<a href="src/telnyx/types/conferences/action_unmute_params.py">params</a>) -> <a href="./src/telnyx/types/conferences/action_unmute_response.py">ActionUnmuteResponse</a></code>

# Connections

Types:

```python
from telnyx.types import (
    ConnectionRetrieveResponse,
    ConnectionListResponse,
    ConnectionListActiveCallsResponse,
)
```

Methods:

- <code title="get /connections/{id}">client.connections.<a href="./src/telnyx/resources/connections.py">retrieve</a>(id) -> <a href="./src/telnyx/types/connection_retrieve_response.py">ConnectionRetrieveResponse</a></code>
- <code title="get /connections">client.connections.<a href="./src/telnyx/resources/connections.py">list</a>(\*\*<a href="src/telnyx/types/connection_list_params.py">params</a>) -> <a href="./src/telnyx/types/connection_list_response.py">ConnectionListResponse</a></code>
- <code title="get /connections/{connection_id}/active_calls">client.connections.<a href="./src/telnyx/resources/connections.py">list_active_calls</a>(connection_id, \*\*<a href="src/telnyx/types/connection_list_active_calls_params.py">params</a>) -> <a href="./src/telnyx/types/connection_list_active_calls_response.py">ConnectionListActiveCallsResponse</a></code>

# CountryCoverage

Types:

```python
from telnyx.types import CountryCoverageRetrieveResponse, CountryCoverageRetrieveCountryResponse
```

Methods:

- <code title="get /country_coverage">client.country_coverage.<a href="./src/telnyx/resources/country_coverage.py">retrieve</a>() -> <a href="./src/telnyx/types/country_coverage_retrieve_response.py">CountryCoverageRetrieveResponse</a></code>
- <code title="get /country_coverage/countries/{country_code}">client.country_coverage.<a href="./src/telnyx/resources/country_coverage.py">retrieve_country</a>(country_code) -> <a href="./src/telnyx/types/country_coverage_retrieve_country_response.py">CountryCoverageRetrieveCountryResponse</a></code>

# CredentialConnections

Types:

```python
from telnyx.types import (
    AnchorsiteOverride,
    ConnectionRtcpSettings,
    CredentialConnection,
    CredentialInbound,
    CredentialOutbound,
    DtmfType,
    EncryptedMedia,
    CredentialConnectionCreateResponse,
    CredentialConnectionRetrieveResponse,
    CredentialConnectionUpdateResponse,
    CredentialConnectionListResponse,
    CredentialConnectionDeleteResponse,
)
```

Methods:

- <code title="post /credential_connections">client.credential_connections.<a href="./src/telnyx/resources/credential_connections/credential_connections.py">create</a>(\*\*<a href="src/telnyx/types/credential_connection_create_params.py">params</a>) -> <a href="./src/telnyx/types/credential_connection_create_response.py">CredentialConnectionCreateResponse</a></code>
- <code title="get /credential_connections/{id}">client.credential_connections.<a href="./src/telnyx/resources/credential_connections/credential_connections.py">retrieve</a>(id) -> <a href="./src/telnyx/types/credential_connection_retrieve_response.py">CredentialConnectionRetrieveResponse</a></code>
- <code title="patch /credential_connections/{id}">client.credential_connections.<a href="./src/telnyx/resources/credential_connections/credential_connections.py">update</a>(id, \*\*<a href="src/telnyx/types/credential_connection_update_params.py">params</a>) -> <a href="./src/telnyx/types/credential_connection_update_response.py">CredentialConnectionUpdateResponse</a></code>
- <code title="get /credential_connections">client.credential_connections.<a href="./src/telnyx/resources/credential_connections/credential_connections.py">list</a>(\*\*<a href="src/telnyx/types/credential_connection_list_params.py">params</a>) -> <a href="./src/telnyx/types/credential_connection_list_response.py">CredentialConnectionListResponse</a></code>
- <code title="delete /credential_connections/{id}">client.credential_connections.<a href="./src/telnyx/resources/credential_connections/credential_connections.py">delete</a>(id) -> <a href="./src/telnyx/types/credential_connection_delete_response.py">CredentialConnectionDeleteResponse</a></code>

## Actions

Types:

```python
from telnyx.types.credential_connections import ActionCheckRegistrationStatusResponse
```

Methods:

- <code title="post /credential_connections/{id}/actions/check_registration_status">client.credential_connections.actions.<a href="./src/telnyx/resources/credential_connections/actions.py">check_registration_status</a>(id) -> <a href="./src/telnyx/types/credential_connections/action_check_registration_status_response.py">ActionCheckRegistrationStatusResponse</a></code>

# CustomStorageCredentials

Types:

```python
from telnyx.types import (
    AzureConfigurationData,
    CustomStorageConfiguration,
    GcsConfigurationData,
    S3ConfigurationData,
    CustomStorageCredentialCreateResponse,
    CustomStorageCredentialRetrieveResponse,
    CustomStorageCredentialUpdateResponse,
)
```

Methods:

- <code title="post /custom_storage_credentials/{connection_id}">client.custom_storage_credentials.<a href="./src/telnyx/resources/custom_storage_credentials.py">create</a>(connection_id, \*\*<a href="src/telnyx/types/custom_storage_credential_create_params.py">params</a>) -> <a href="./src/telnyx/types/custom_storage_credential_create_response.py">CustomStorageCredentialCreateResponse</a></code>
- <code title="get /custom_storage_credentials/{connection_id}">client.custom_storage_credentials.<a href="./src/telnyx/resources/custom_storage_credentials.py">retrieve</a>(connection_id) -> <a href="./src/telnyx/types/custom_storage_credential_retrieve_response.py">CustomStorageCredentialRetrieveResponse</a></code>
- <code title="put /custom_storage_credentials/{connection_id}">client.custom_storage_credentials.<a href="./src/telnyx/resources/custom_storage_credentials.py">update</a>(connection_id, \*\*<a href="src/telnyx/types/custom_storage_credential_update_params.py">params</a>) -> <a href="./src/telnyx/types/custom_storage_credential_update_response.py">CustomStorageCredentialUpdateResponse</a></code>
- <code title="delete /custom_storage_credentials/{connection_id}">client.custom_storage_credentials.<a href="./src/telnyx/resources/custom_storage_credentials.py">delete</a>(connection_id) -> None</code>

# CustomerServiceRecords

Types:

```python
from telnyx.types import (
    CustomerServiceRecord,
    CustomerServiceRecordCreateResponse,
    CustomerServiceRecordRetrieveResponse,
    CustomerServiceRecordListResponse,
    CustomerServiceRecordVerifyPhoneNumberCoverageResponse,
)
```

Methods:

- <code title="post /customer_service_records">client.customer_service_records.<a href="./src/telnyx/resources/customer_service_records.py">create</a>(\*\*<a href="src/telnyx/types/customer_service_record_create_params.py">params</a>) -> <a href="./src/telnyx/types/customer_service_record_create_response.py">CustomerServiceRecordCreateResponse</a></code>
- <code title="get /customer_service_records/{customer_service_record_id}">client.customer_service_records.<a href="./src/telnyx/resources/customer_service_records.py">retrieve</a>(customer_service_record_id) -> <a href="./src/telnyx/types/customer_service_record_retrieve_response.py">CustomerServiceRecordRetrieveResponse</a></code>
- <code title="get /customer_service_records">client.customer_service_records.<a href="./src/telnyx/resources/customer_service_records.py">list</a>(\*\*<a href="src/telnyx/types/customer_service_record_list_params.py">params</a>) -> <a href="./src/telnyx/types/customer_service_record_list_response.py">CustomerServiceRecordListResponse</a></code>
- <code title="post /customer_service_records/phone_number_coverages">client.customer_service_records.<a href="./src/telnyx/resources/customer_service_records.py">verify_phone_number_coverage</a>(\*\*<a href="src/telnyx/types/customer_service_record_verify_phone_number_coverage_params.py">params</a>) -> <a href="./src/telnyx/types/customer_service_record_verify_phone_number_coverage_response.py">CustomerServiceRecordVerifyPhoneNumberCoverageResponse</a></code>

# DetailRecords

Types:

```python
from telnyx.types import DetailRecordListResponse
```

Methods:

- <code title="get /detail_records">client.detail_records.<a href="./src/telnyx/resources/detail_records.py">list</a>(\*\*<a href="src/telnyx/types/detail_record_list_params.py">params</a>) -> <a href="./src/telnyx/types/detail_record_list_response.py">DetailRecordListResponse</a></code>

# DialogflowConnections

Types:

```python
from telnyx.types import (
    DialogflowConnectionCreateResponse,
    DialogflowConnectionRetrieveResponse,
    DialogflowConnectionUpdateResponse,
)
```

Methods:

- <code title="post /dialogflow_connections/{connection_id}">client.dialogflow_connections.<a href="./src/telnyx/resources/dialogflow_connections.py">create</a>(connection_id, \*\*<a href="src/telnyx/types/dialogflow_connection_create_params.py">params</a>) -> <a href="./src/telnyx/types/dialogflow_connection_create_response.py">DialogflowConnectionCreateResponse</a></code>
- <code title="get /dialogflow_connections/{connection_id}">client.dialogflow_connections.<a href="./src/telnyx/resources/dialogflow_connections.py">retrieve</a>(connection_id) -> <a href="./src/telnyx/types/dialogflow_connection_retrieve_response.py">DialogflowConnectionRetrieveResponse</a></code>
- <code title="put /dialogflow_connections/{connection_id}">client.dialogflow_connections.<a href="./src/telnyx/resources/dialogflow_connections.py">update</a>(connection_id, \*\*<a href="src/telnyx/types/dialogflow_connection_update_params.py">params</a>) -> <a href="./src/telnyx/types/dialogflow_connection_update_response.py">DialogflowConnectionUpdateResponse</a></code>
- <code title="delete /dialogflow_connections/{connection_id}">client.dialogflow_connections.<a href="./src/telnyx/resources/dialogflow_connections.py">delete</a>(connection_id) -> None</code>

# DocumentLinks

Types:

```python
from telnyx.types import DocumentLinkListResponse
```

Methods:

- <code title="get /document_links">client.document_links.<a href="./src/telnyx/resources/document_links.py">list</a>(\*\*<a href="src/telnyx/types/document_link_list_params.py">params</a>) -> <a href="./src/telnyx/types/document_link_list_response.py">DocumentLinkListResponse</a></code>

# Documents

Types:

```python
from telnyx.types import (
    DocServiceDocument,
    DocumentRetrieveResponse,
    DocumentUpdateResponse,
    DocumentListResponse,
    DocumentDeleteResponse,
    DocumentUploadResponse,
)
```

Methods:

- <code title="get /documents/{id}">client.documents.<a href="./src/telnyx/resources/documents.py">retrieve</a>(id) -> <a href="./src/telnyx/types/document_retrieve_response.py">DocumentRetrieveResponse</a></code>
- <code title="patch /documents/{id}">client.documents.<a href="./src/telnyx/resources/documents.py">update</a>(id, \*\*<a href="src/telnyx/types/document_update_params.py">params</a>) -> <a href="./src/telnyx/types/document_update_response.py">DocumentUpdateResponse</a></code>
- <code title="get /documents">client.documents.<a href="./src/telnyx/resources/documents.py">list</a>(\*\*<a href="src/telnyx/types/document_list_params.py">params</a>) -> <a href="./src/telnyx/types/document_list_response.py">DocumentListResponse</a></code>
- <code title="delete /documents/{id}">client.documents.<a href="./src/telnyx/resources/documents.py">delete</a>(id) -> <a href="./src/telnyx/types/document_delete_response.py">DocumentDeleteResponse</a></code>
- <code title="get /documents/{id}/download">client.documents.<a href="./src/telnyx/resources/documents.py">download</a>(id) -> BinaryAPIResponse</code>
- <code title="post /documents">client.documents.<a href="./src/telnyx/resources/documents.py">upload</a>(\*\*<a href="src/telnyx/types/document_upload_params.py">params</a>) -> <a href="./src/telnyx/types/document_upload_response.py">DocumentUploadResponse</a></code>

# DynamicEmergencyAddresses

Types:

```python
from telnyx.types import (
    DynamicEmergencyAddress,
    DynamicEmergencyAddressCreateResponse,
    DynamicEmergencyAddressRetrieveResponse,
    DynamicEmergencyAddressListResponse,
    DynamicEmergencyAddressDeleteResponse,
)
```

Methods:

- <code title="post /dynamic_emergency_addresses">client.dynamic_emergency_addresses.<a href="./src/telnyx/resources/dynamic_emergency_addresses.py">create</a>(\*\*<a href="src/telnyx/types/dynamic_emergency_address_create_params.py">params</a>) -> <a href="./src/telnyx/types/dynamic_emergency_address_create_response.py">DynamicEmergencyAddressCreateResponse</a></code>
- <code title="get /dynamic_emergency_addresses/{id}">client.dynamic_emergency_addresses.<a href="./src/telnyx/resources/dynamic_emergency_addresses.py">retrieve</a>(id) -> <a href="./src/telnyx/types/dynamic_emergency_address_retrieve_response.py">DynamicEmergencyAddressRetrieveResponse</a></code>
- <code title="get /dynamic_emergency_addresses">client.dynamic_emergency_addresses.<a href="./src/telnyx/resources/dynamic_emergency_addresses.py">list</a>(\*\*<a href="src/telnyx/types/dynamic_emergency_address_list_params.py">params</a>) -> <a href="./src/telnyx/types/dynamic_emergency_address_list_response.py">DynamicEmergencyAddressListResponse</a></code>
- <code title="delete /dynamic_emergency_addresses/{id}">client.dynamic_emergency_addresses.<a href="./src/telnyx/resources/dynamic_emergency_addresses.py">delete</a>(id) -> <a href="./src/telnyx/types/dynamic_emergency_address_delete_response.py">DynamicEmergencyAddressDeleteResponse</a></code>

# DynamicEmergencyEndpoints

Types:

```python
from telnyx.types import (
    DynamicEmergencyEndpoint,
    DynamicEmergencyEndpointCreateResponse,
    DynamicEmergencyEndpointRetrieveResponse,
    DynamicEmergencyEndpointListResponse,
    DynamicEmergencyEndpointDeleteResponse,
)
```

Methods:

- <code title="post /dynamic_emergency_endpoints">client.dynamic_emergency_endpoints.<a href="./src/telnyx/resources/dynamic_emergency_endpoints.py">create</a>(\*\*<a href="src/telnyx/types/dynamic_emergency_endpoint_create_params.py">params</a>) -> <a href="./src/telnyx/types/dynamic_emergency_endpoint_create_response.py">DynamicEmergencyEndpointCreateResponse</a></code>
- <code title="get /dynamic_emergency_endpoints/{id}">client.dynamic_emergency_endpoints.<a href="./src/telnyx/resources/dynamic_emergency_endpoints.py">retrieve</a>(id) -> <a href="./src/telnyx/types/dynamic_emergency_endpoint_retrieve_response.py">DynamicEmergencyEndpointRetrieveResponse</a></code>
- <code title="get /dynamic_emergency_endpoints">client.dynamic_emergency_endpoints.<a href="./src/telnyx/resources/dynamic_emergency_endpoints.py">list</a>(\*\*<a href="src/telnyx/types/dynamic_emergency_endpoint_list_params.py">params</a>) -> <a href="./src/telnyx/types/dynamic_emergency_endpoint_list_response.py">DynamicEmergencyEndpointListResponse</a></code>
- <code title="delete /dynamic_emergency_endpoints/{id}">client.dynamic_emergency_endpoints.<a href="./src/telnyx/resources/dynamic_emergency_endpoints.py">delete</a>(id) -> <a href="./src/telnyx/types/dynamic_emergency_endpoint_delete_response.py">DynamicEmergencyEndpointDeleteResponse</a></code>

# Enum

Types:

```python
from telnyx.types import EnumRetrieveResponse
```

Methods:

- <code title="get /enum/{endpoint}">client.enum.<a href="./src/telnyx/resources/enum.py">retrieve</a>(endpoint) -> <a href="./src/telnyx/types/enum_retrieve_response.py">EnumRetrieveResponse</a></code>

# ExternalConnections

Types:

```python
from telnyx.types import (
    ExternalConnection,
    ExternalVoiceIntegrationsPaginationMeta,
    ExternalConnectionCreateResponse,
    ExternalConnectionRetrieveResponse,
    ExternalConnectionUpdateResponse,
    ExternalConnectionListResponse,
    ExternalConnectionDeleteResponse,
    ExternalConnectionUpdateLocationResponse,
)
```

Methods:

- <code title="post /external_connections">client.external_connections.<a href="./src/telnyx/resources/external_connections/external_connections.py">create</a>(\*\*<a href="src/telnyx/types/external_connection_create_params.py">params</a>) -> <a href="./src/telnyx/types/external_connection_create_response.py">ExternalConnectionCreateResponse</a></code>
- <code title="get /external_connections/{id}">client.external_connections.<a href="./src/telnyx/resources/external_connections/external_connections.py">retrieve</a>(id) -> <a href="./src/telnyx/types/external_connection_retrieve_response.py">ExternalConnectionRetrieveResponse</a></code>
- <code title="patch /external_connections/{id}">client.external_connections.<a href="./src/telnyx/resources/external_connections/external_connections.py">update</a>(id, \*\*<a href="src/telnyx/types/external_connection_update_params.py">params</a>) -> <a href="./src/telnyx/types/external_connection_update_response.py">ExternalConnectionUpdateResponse</a></code>
- <code title="get /external_connections">client.external_connections.<a href="./src/telnyx/resources/external_connections/external_connections.py">list</a>(\*\*<a href="src/telnyx/types/external_connection_list_params.py">params</a>) -> <a href="./src/telnyx/types/external_connection_list_response.py">ExternalConnectionListResponse</a></code>
- <code title="delete /external_connections/{id}">client.external_connections.<a href="./src/telnyx/resources/external_connections/external_connections.py">delete</a>(id) -> <a href="./src/telnyx/types/external_connection_delete_response.py">ExternalConnectionDeleteResponse</a></code>
- <code title="patch /external_connections/{id}/locations/{location_id}">client.external_connections.<a href="./src/telnyx/resources/external_connections/external_connections.py">update_location</a>(location_id, \*, id, \*\*<a href="src/telnyx/types/external_connection_update_location_params.py">params</a>) -> <a href="./src/telnyx/types/external_connection_update_location_response.py">ExternalConnectionUpdateLocationResponse</a></code>

## LogMessages

Types:

```python
from telnyx.types.external_connections import (
    LogMessageRetrieveResponse,
    LogMessageListResponse,
    LogMessageDismissResponse,
)
```

Methods:

- <code title="get /external_connections/log_messages/{id}">client.external_connections.log_messages.<a href="./src/telnyx/resources/external_connections/log_messages.py">retrieve</a>(id) -> <a href="./src/telnyx/types/external_connections/log_message_retrieve_response.py">LogMessageRetrieveResponse</a></code>
- <code title="get /external_connections/log_messages">client.external_connections.log_messages.<a href="./src/telnyx/resources/external_connections/log_messages.py">list</a>(\*\*<a href="src/telnyx/types/external_connections/log_message_list_params.py">params</a>) -> <a href="./src/telnyx/types/external_connections/log_message_list_response.py">LogMessageListResponse</a></code>
- <code title="delete /external_connections/log_messages/{id}">client.external_connections.log_messages.<a href="./src/telnyx/resources/external_connections/log_messages.py">dismiss</a>(id) -> <a href="./src/telnyx/types/external_connections/log_message_dismiss_response.py">LogMessageDismissResponse</a></code>

## CivicAddresses

Types:

```python
from telnyx.types.external_connections import CivicAddressRetrieveResponse, CivicAddressListResponse
```

Methods:

- <code title="get /external_connections/{id}/civic_addresses/{address_id}">client.external_connections.civic_addresses.<a href="./src/telnyx/resources/external_connections/civic_addresses.py">retrieve</a>(address_id, \*, id) -> <a href="./src/telnyx/types/external_connections/civic_address_retrieve_response.py">CivicAddressRetrieveResponse</a></code>
- <code title="get /external_connections/{id}/civic_addresses">client.external_connections.civic_addresses.<a href="./src/telnyx/resources/external_connections/civic_addresses.py">list</a>(id, \*\*<a href="src/telnyx/types/external_connections/civic_address_list_params.py">params</a>) -> <a href="./src/telnyx/types/external_connections/civic_address_list_response.py">CivicAddressListResponse</a></code>

## PhoneNumbers

Types:

```python
from telnyx.types.external_connections import (
    ExternalConnectionPhoneNumber,
    PhoneNumberRetrieveResponse,
    PhoneNumberUpdateResponse,
    PhoneNumberListResponse,
)
```

Methods:

- <code title="get /external_connections/{id}/phone_numbers/{phone_number_id}">client.external_connections.phone_numbers.<a href="./src/telnyx/resources/external_connections/phone_numbers.py">retrieve</a>(phone_number_id, \*, id) -> <a href="./src/telnyx/types/external_connections/phone_number_retrieve_response.py">PhoneNumberRetrieveResponse</a></code>
- <code title="patch /external_connections/{id}/phone_numbers/{phone_number_id}">client.external_connections.phone_numbers.<a href="./src/telnyx/resources/external_connections/phone_numbers.py">update</a>(phone_number_id, \*, id, \*\*<a href="src/telnyx/types/external_connections/phone_number_update_params.py">params</a>) -> <a href="./src/telnyx/types/external_connections/phone_number_update_response.py">PhoneNumberUpdateResponse</a></code>
- <code title="get /external_connections/{id}/phone_numbers">client.external_connections.phone_numbers.<a href="./src/telnyx/resources/external_connections/phone_numbers.py">list</a>(id, \*\*<a href="src/telnyx/types/external_connections/phone_number_list_params.py">params</a>) -> <a href="./src/telnyx/types/external_connections/phone_number_list_response.py">PhoneNumberListResponse</a></code>

## Releases

Types:

```python
from telnyx.types.external_connections import ReleaseRetrieveResponse, ReleaseListResponse
```

Methods:

- <code title="get /external_connections/{id}/releases/{release_id}">client.external_connections.releases.<a href="./src/telnyx/resources/external_connections/releases.py">retrieve</a>(release_id, \*, id) -> <a href="./src/telnyx/types/external_connections/release_retrieve_response.py">ReleaseRetrieveResponse</a></code>
- <code title="get /external_connections/{id}/releases">client.external_connections.releases.<a href="./src/telnyx/resources/external_connections/releases.py">list</a>(id, \*\*<a href="src/telnyx/types/external_connections/release_list_params.py">params</a>) -> <a href="./src/telnyx/types/external_connections/release_list_response.py">ReleaseListResponse</a></code>

## Uploads

Types:

```python
from telnyx.types.external_connections import (
    TnUploadEntry,
    Upload,
    UploadCreateResponse,
    UploadRetrieveResponse,
    UploadListResponse,
    UploadPendingCountResponse,
    UploadRefreshStatusResponse,
    UploadRetryResponse,
)
```

Methods:

- <code title="post /external_connections/{id}/uploads">client.external_connections.uploads.<a href="./src/telnyx/resources/external_connections/uploads.py">create</a>(id, \*\*<a href="src/telnyx/types/external_connections/upload_create_params.py">params</a>) -> <a href="./src/telnyx/types/external_connections/upload_create_response.py">UploadCreateResponse</a></code>
- <code title="get /external_connections/{id}/uploads/{ticket_id}">client.external_connections.uploads.<a href="./src/telnyx/resources/external_connections/uploads.py">retrieve</a>(ticket_id, \*, id) -> <a href="./src/telnyx/types/external_connections/upload_retrieve_response.py">UploadRetrieveResponse</a></code>
- <code title="get /external_connections/{id}/uploads">client.external_connections.uploads.<a href="./src/telnyx/resources/external_connections/uploads.py">list</a>(id, \*\*<a href="src/telnyx/types/external_connections/upload_list_params.py">params</a>) -> <a href="./src/telnyx/types/external_connections/upload_list_response.py">UploadListResponse</a></code>
- <code title="get /external_connections/{id}/uploads/status">client.external_connections.uploads.<a href="./src/telnyx/resources/external_connections/uploads.py">pending_count</a>(id) -> <a href="./src/telnyx/types/external_connections/upload_pending_count_response.py">UploadPendingCountResponse</a></code>
- <code title="post /external_connections/{id}/uploads/refresh">client.external_connections.uploads.<a href="./src/telnyx/resources/external_connections/uploads.py">refresh_status</a>(id) -> <a href="./src/telnyx/types/external_connections/upload_refresh_status_response.py">UploadRefreshStatusResponse</a></code>
- <code title="post /external_connections/{id}/uploads/{ticket_id}/retry">client.external_connections.uploads.<a href="./src/telnyx/resources/external_connections/uploads.py">retry</a>(ticket_id, \*, id) -> <a href="./src/telnyx/types/external_connections/upload_retry_response.py">UploadRetryResponse</a></code>

# FaxApplications

Types:

```python
from telnyx.types import (
    FaxApplication,
    FaxApplicationCreateResponse,
    FaxApplicationRetrieveResponse,
    FaxApplicationUpdateResponse,
    FaxApplicationListResponse,
    FaxApplicationDeleteResponse,
)
```

Methods:

- <code title="post /fax_applications">client.fax_applications.<a href="./src/telnyx/resources/fax_applications.py">create</a>(\*\*<a href="src/telnyx/types/fax_application_create_params.py">params</a>) -> <a href="./src/telnyx/types/fax_application_create_response.py">FaxApplicationCreateResponse</a></code>
- <code title="get /fax_applications/{id}">client.fax_applications.<a href="./src/telnyx/resources/fax_applications.py">retrieve</a>(id) -> <a href="./src/telnyx/types/fax_application_retrieve_response.py">FaxApplicationRetrieveResponse</a></code>
- <code title="patch /fax_applications/{id}">client.fax_applications.<a href="./src/telnyx/resources/fax_applications.py">update</a>(id, \*\*<a href="src/telnyx/types/fax_application_update_params.py">params</a>) -> <a href="./src/telnyx/types/fax_application_update_response.py">FaxApplicationUpdateResponse</a></code>
- <code title="get /fax_applications">client.fax_applications.<a href="./src/telnyx/resources/fax_applications.py">list</a>(\*\*<a href="src/telnyx/types/fax_application_list_params.py">params</a>) -> <a href="./src/telnyx/types/fax_application_list_response.py">FaxApplicationListResponse</a></code>
- <code title="delete /fax_applications/{id}">client.fax_applications.<a href="./src/telnyx/resources/fax_applications.py">delete</a>(id) -> <a href="./src/telnyx/types/fax_application_delete_response.py">FaxApplicationDeleteResponse</a></code>

# Faxes

Types:

```python
from telnyx.types import Fax, FaxCreateResponse, FaxRetrieveResponse, FaxListResponse
```

Methods:

- <code title="post /faxes">client.faxes.<a href="./src/telnyx/resources/faxes/faxes.py">create</a>(\*\*<a href="src/telnyx/types/fax_create_params.py">params</a>) -> <a href="./src/telnyx/types/fax_create_response.py">FaxCreateResponse</a></code>
- <code title="get /faxes/{id}">client.faxes.<a href="./src/telnyx/resources/faxes/faxes.py">retrieve</a>(id) -> <a href="./src/telnyx/types/fax_retrieve_response.py">FaxRetrieveResponse</a></code>
- <code title="get /faxes">client.faxes.<a href="./src/telnyx/resources/faxes/faxes.py">list</a>(\*\*<a href="src/telnyx/types/fax_list_params.py">params</a>) -> <a href="./src/telnyx/types/fax_list_response.py">FaxListResponse</a></code>
- <code title="delete /faxes/{id}">client.faxes.<a href="./src/telnyx/resources/faxes/faxes.py">delete</a>(id) -> None</code>

## Actions

Types:

```python
from telnyx.types.faxes import ActionCancelResponse, ActionRefreshResponse
```

Methods:

- <code title="post /faxes/{id}/actions/cancel">client.faxes.actions.<a href="./src/telnyx/resources/faxes/actions.py">cancel</a>(id) -> <a href="./src/telnyx/types/faxes/action_cancel_response.py">ActionCancelResponse</a></code>
- <code title="post /faxes/{id}/actions/refresh">client.faxes.actions.<a href="./src/telnyx/resources/faxes/actions.py">refresh</a>(id) -> <a href="./src/telnyx/types/faxes/action_refresh_response.py">ActionRefreshResponse</a></code>

# FqdnConnections

Types:

```python
from telnyx.types import (
    FqdnConnection,
    InboundFqdn,
    OutboundFqdn,
    TransportProtocol,
    WebhookAPIVersion,
    FqdnConnectionCreateResponse,
    FqdnConnectionRetrieveResponse,
    FqdnConnectionUpdateResponse,
    FqdnConnectionListResponse,
    FqdnConnectionDeleteResponse,
)
```

Methods:

- <code title="post /fqdn_connections">client.fqdn_connections.<a href="./src/telnyx/resources/fqdn_connections.py">create</a>(\*\*<a href="src/telnyx/types/fqdn_connection_create_params.py">params</a>) -> <a href="./src/telnyx/types/fqdn_connection_create_response.py">FqdnConnectionCreateResponse</a></code>
- <code title="get /fqdn_connections/{id}">client.fqdn_connections.<a href="./src/telnyx/resources/fqdn_connections.py">retrieve</a>(id) -> <a href="./src/telnyx/types/fqdn_connection_retrieve_response.py">FqdnConnectionRetrieveResponse</a></code>
- <code title="patch /fqdn_connections/{id}">client.fqdn_connections.<a href="./src/telnyx/resources/fqdn_connections.py">update</a>(id, \*\*<a href="src/telnyx/types/fqdn_connection_update_params.py">params</a>) -> <a href="./src/telnyx/types/fqdn_connection_update_response.py">FqdnConnectionUpdateResponse</a></code>
- <code title="get /fqdn_connections">client.fqdn_connections.<a href="./src/telnyx/resources/fqdn_connections.py">list</a>(\*\*<a href="src/telnyx/types/fqdn_connection_list_params.py">params</a>) -> <a href="./src/telnyx/types/fqdn_connection_list_response.py">FqdnConnectionListResponse</a></code>
- <code title="delete /fqdn_connections/{id}">client.fqdn_connections.<a href="./src/telnyx/resources/fqdn_connections.py">delete</a>(id) -> <a href="./src/telnyx/types/fqdn_connection_delete_response.py">FqdnConnectionDeleteResponse</a></code>

# Fqdns

Types:

```python
from telnyx.types import (
    Fqdn,
    FqdnCreateResponse,
    FqdnRetrieveResponse,
    FqdnUpdateResponse,
    FqdnListResponse,
    FqdnDeleteResponse,
)
```

Methods:

- <code title="post /fqdns">client.fqdns.<a href="./src/telnyx/resources/fqdns.py">create</a>(\*\*<a href="src/telnyx/types/fqdn_create_params.py">params</a>) -> <a href="./src/telnyx/types/fqdn_create_response.py">FqdnCreateResponse</a></code>
- <code title="get /fqdns/{id}">client.fqdns.<a href="./src/telnyx/resources/fqdns.py">retrieve</a>(id) -> <a href="./src/telnyx/types/fqdn_retrieve_response.py">FqdnRetrieveResponse</a></code>
- <code title="patch /fqdns/{id}">client.fqdns.<a href="./src/telnyx/resources/fqdns.py">update</a>(id, \*\*<a href="src/telnyx/types/fqdn_update_params.py">params</a>) -> <a href="./src/telnyx/types/fqdn_update_response.py">FqdnUpdateResponse</a></code>
- <code title="get /fqdns">client.fqdns.<a href="./src/telnyx/resources/fqdns.py">list</a>(\*\*<a href="src/telnyx/types/fqdn_list_params.py">params</a>) -> <a href="./src/telnyx/types/fqdn_list_response.py">FqdnListResponse</a></code>
- <code title="delete /fqdns/{id}">client.fqdns.<a href="./src/telnyx/resources/fqdns.py">delete</a>(id) -> <a href="./src/telnyx/types/fqdn_delete_response.py">FqdnDeleteResponse</a></code>

# GlobalIPAllowedPorts

Types:

```python
from telnyx.types import GlobalIPAllowedPortListResponse
```

Methods:

- <code title="get /global_ip_allowed_ports">client.global_ip_allowed_ports.<a href="./src/telnyx/resources/global_ip_allowed_ports.py">list</a>() -> <a href="./src/telnyx/types/global_ip_allowed_port_list_response.py">GlobalIPAllowedPortListResponse</a></code>

# GlobalIPAssignmentHealth

Types:

```python
from telnyx.types import GlobalIPAssignmentHealthRetrieveResponse
```

Methods:

- <code title="get /global_ip_assignment_health">client.global_ip_assignment_health.<a href="./src/telnyx/resources/global_ip_assignment_health.py">retrieve</a>(\*\*<a href="src/telnyx/types/global_ip_assignment_health_retrieve_params.py">params</a>) -> <a href="./src/telnyx/types/global_ip_assignment_health_retrieve_response.py">GlobalIPAssignmentHealthRetrieveResponse</a></code>

# GlobalIPAssignments

Types:

```python
from telnyx.types import (
    GlobalIPAssignment,
    Record,
    GlobalIPAssignmentCreateResponse,
    GlobalIPAssignmentRetrieveResponse,
    GlobalIPAssignmentUpdateResponse,
    GlobalIPAssignmentListResponse,
    GlobalIPAssignmentDeleteResponse,
)
```

Methods:

- <code title="post /global_ip_assignments">client.global_ip_assignments.<a href="./src/telnyx/resources/global_ip_assignments.py">create</a>(\*\*<a href="src/telnyx/types/global_ip_assignment_create_params.py">params</a>) -> <a href="./src/telnyx/types/global_ip_assignment_create_response.py">GlobalIPAssignmentCreateResponse</a></code>
- <code title="get /global_ip_assignments/{id}">client.global_ip_assignments.<a href="./src/telnyx/resources/global_ip_assignments.py">retrieve</a>(id) -> <a href="./src/telnyx/types/global_ip_assignment_retrieve_response.py">GlobalIPAssignmentRetrieveResponse</a></code>
- <code title="patch /global_ip_assignments/{id}">client.global_ip_assignments.<a href="./src/telnyx/resources/global_ip_assignments.py">update</a>(id, \*\*<a href="src/telnyx/types/global_ip_assignment_update_params.py">params</a>) -> <a href="./src/telnyx/types/global_ip_assignment_update_response.py">GlobalIPAssignmentUpdateResponse</a></code>
- <code title="get /global_ip_assignments">client.global_ip_assignments.<a href="./src/telnyx/resources/global_ip_assignments.py">list</a>(\*\*<a href="src/telnyx/types/global_ip_assignment_list_params.py">params</a>) -> <a href="./src/telnyx/types/global_ip_assignment_list_response.py">GlobalIPAssignmentListResponse</a></code>
- <code title="delete /global_ip_assignments/{id}">client.global_ip_assignments.<a href="./src/telnyx/resources/global_ip_assignments.py">delete</a>(id) -> <a href="./src/telnyx/types/global_ip_assignment_delete_response.py">GlobalIPAssignmentDeleteResponse</a></code>

# GlobalIPAssignmentsUsage

Types:

```python
from telnyx.types import GlobalIPAssignmentsUsageRetrieveResponse
```

Methods:

- <code title="get /global_ip_assignments_usage">client.global_ip_assignments_usage.<a href="./src/telnyx/resources/global_ip_assignments_usage.py">retrieve</a>(\*\*<a href="src/telnyx/types/global_ip_assignments_usage_retrieve_params.py">params</a>) -> <a href="./src/telnyx/types/global_ip_assignments_usage_retrieve_response.py">GlobalIPAssignmentsUsageRetrieveResponse</a></code>

# GlobalIPHealthCheckTypes

Types:

```python
from telnyx.types import GlobalIPHealthCheckTypeListResponse
```

Methods:

- <code title="get /global_ip_health_check_types">client.global_ip_health_check_types.<a href="./src/telnyx/resources/global_ip_health_check_types.py">list</a>() -> <a href="./src/telnyx/types/global_ip_health_check_type_list_response.py">GlobalIPHealthCheckTypeListResponse</a></code>

# GlobalIPHealthChecks

Types:

```python
from telnyx.types import (
    GlobalIPHealthCheckCreateResponse,
    GlobalIPHealthCheckRetrieveResponse,
    GlobalIPHealthCheckListResponse,
    GlobalIPHealthCheckDeleteResponse,
)
```

Methods:

- <code title="post /global_ip_health_checks">client.global_ip_health_checks.<a href="./src/telnyx/resources/global_ip_health_checks.py">create</a>(\*\*<a href="src/telnyx/types/global_ip_health_check_create_params.py">params</a>) -> <a href="./src/telnyx/types/global_ip_health_check_create_response.py">GlobalIPHealthCheckCreateResponse</a></code>
- <code title="get /global_ip_health_checks/{id}">client.global_ip_health_checks.<a href="./src/telnyx/resources/global_ip_health_checks.py">retrieve</a>(id) -> <a href="./src/telnyx/types/global_ip_health_check_retrieve_response.py">GlobalIPHealthCheckRetrieveResponse</a></code>
- <code title="get /global_ip_health_checks">client.global_ip_health_checks.<a href="./src/telnyx/resources/global_ip_health_checks.py">list</a>(\*\*<a href="src/telnyx/types/global_ip_health_check_list_params.py">params</a>) -> <a href="./src/telnyx/types/global_ip_health_check_list_response.py">GlobalIPHealthCheckListResponse</a></code>
- <code title="delete /global_ip_health_checks/{id}">client.global_ip_health_checks.<a href="./src/telnyx/resources/global_ip_health_checks.py">delete</a>(id) -> <a href="./src/telnyx/types/global_ip_health_check_delete_response.py">GlobalIPHealthCheckDeleteResponse</a></code>

# GlobalIPLatency

Types:

```python
from telnyx.types import GlobalIPLatencyRetrieveResponse
```

Methods:

- <code title="get /global_ip_latency">client.global_ip_latency.<a href="./src/telnyx/resources/global_ip_latency.py">retrieve</a>(\*\*<a href="src/telnyx/types/global_ip_latency_retrieve_params.py">params</a>) -> <a href="./src/telnyx/types/global_ip_latency_retrieve_response.py">GlobalIPLatencyRetrieveResponse</a></code>

# GlobalIPProtocols

Types:

```python
from telnyx.types import GlobalIPProtocolListResponse
```

Methods:

- <code title="get /global_ip_protocols">client.global_ip_protocols.<a href="./src/telnyx/resources/global_ip_protocols.py">list</a>() -> <a href="./src/telnyx/types/global_ip_protocol_list_response.py">GlobalIPProtocolListResponse</a></code>

# GlobalIPUsage

Types:

```python
from telnyx.types import GlobalIPUsageRetrieveResponse
```

Methods:

- <code title="get /global_ip_usage">client.global_ip_usage.<a href="./src/telnyx/resources/global_ip_usage.py">retrieve</a>(\*\*<a href="src/telnyx/types/global_ip_usage_retrieve_params.py">params</a>) -> <a href="./src/telnyx/types/global_ip_usage_retrieve_response.py">GlobalIPUsageRetrieveResponse</a></code>

# GlobalIPs

Types:

```python
from telnyx.types import (
    GlobalIPCreateResponse,
    GlobalIPRetrieveResponse,
    GlobalIPListResponse,
    GlobalIPDeleteResponse,
)
```

Methods:

- <code title="post /global_ips">client.global_ips.<a href="./src/telnyx/resources/global_ips.py">create</a>(\*\*<a href="src/telnyx/types/global_ip_create_params.py">params</a>) -> <a href="./src/telnyx/types/global_ip_create_response.py">GlobalIPCreateResponse</a></code>
- <code title="get /global_ips/{id}">client.global_ips.<a href="./src/telnyx/resources/global_ips.py">retrieve</a>(id) -> <a href="./src/telnyx/types/global_ip_retrieve_response.py">GlobalIPRetrieveResponse</a></code>
- <code title="get /global_ips">client.global_ips.<a href="./src/telnyx/resources/global_ips.py">list</a>(\*\*<a href="src/telnyx/types/global_ip_list_params.py">params</a>) -> <a href="./src/telnyx/types/global_ip_list_response.py">GlobalIPListResponse</a></code>
- <code title="delete /global_ips/{id}">client.global_ips.<a href="./src/telnyx/resources/global_ips.py">delete</a>(id) -> <a href="./src/telnyx/types/global_ip_delete_response.py">GlobalIPDeleteResponse</a></code>

# InboundChannels

Types:

```python
from telnyx.types import InboundChannelUpdateResponse, InboundChannelListResponse
```

Methods:

- <code title="patch /inbound_channels">client.inbound_channels.<a href="./src/telnyx/resources/inbound_channels.py">update</a>(\*\*<a href="src/telnyx/types/inbound_channel_update_params.py">params</a>) -> <a href="./src/telnyx/types/inbound_channel_update_response.py">InboundChannelUpdateResponse</a></code>
- <code title="get /inbound_channels">client.inbound_channels.<a href="./src/telnyx/resources/inbound_channels.py">list</a>() -> <a href="./src/telnyx/types/inbound_channel_list_response.py">InboundChannelListResponse</a></code>

# IntegrationSecrets

Types:

```python
from telnyx.types import (
    IntegrationSecret,
    IntegrationSecretCreateResponse,
    IntegrationSecretListResponse,
)
```

Methods:

- <code title="post /integration_secrets">client.integration_secrets.<a href="./src/telnyx/resources/integration_secrets.py">create</a>(\*\*<a href="src/telnyx/types/integration_secret_create_params.py">params</a>) -> <a href="./src/telnyx/types/integration_secret_create_response.py">IntegrationSecretCreateResponse</a></code>
- <code title="get /integration_secrets">client.integration_secrets.<a href="./src/telnyx/resources/integration_secrets.py">list</a>(\*\*<a href="src/telnyx/types/integration_secret_list_params.py">params</a>) -> <a href="./src/telnyx/types/integration_secret_list_response.py">IntegrationSecretListResponse</a></code>
- <code title="delete /integration_secrets/{id}">client.integration_secrets.<a href="./src/telnyx/resources/integration_secrets.py">delete</a>(id) -> None</code>

# InventoryCoverage

Types:

```python
from telnyx.types import InventoryCoverageListResponse
```

Methods:

- <code title="get /inventory_coverage">client.inventory_coverage.<a href="./src/telnyx/resources/inventory_coverage.py">list</a>(\*\*<a href="src/telnyx/types/inventory_coverage_list_params.py">params</a>) -> <a href="./src/telnyx/types/inventory_coverage_list_response.py">InventoryCoverageListResponse</a></code>

# Invoices

Types:

```python
from telnyx.types import InvoiceRetrieveResponse, InvoiceListResponse
```

Methods:

- <code title="get /invoices/{id}">client.invoices.<a href="./src/telnyx/resources/invoices.py">retrieve</a>(id, \*\*<a href="src/telnyx/types/invoice_retrieve_params.py">params</a>) -> <a href="./src/telnyx/types/invoice_retrieve_response.py">InvoiceRetrieveResponse</a></code>
- <code title="get /invoices">client.invoices.<a href="./src/telnyx/resources/invoices.py">list</a>(\*\*<a href="src/telnyx/types/invoice_list_params.py">params</a>) -> <a href="./src/telnyx/types/invoice_list_response.py">InvoiceListResponse</a></code>

# IPConnections

Types:

```python
from telnyx.types import (
    InboundIP,
    IPConnection,
    OutboundIP,
    IPConnectionCreateResponse,
    IPConnectionRetrieveResponse,
    IPConnectionUpdateResponse,
    IPConnectionListResponse,
    IPConnectionDeleteResponse,
)
```

Methods:

- <code title="post /ip_connections">client.ip_connections.<a href="./src/telnyx/resources/ip_connections.py">create</a>(\*\*<a href="src/telnyx/types/ip_connection_create_params.py">params</a>) -> <a href="./src/telnyx/types/ip_connection_create_response.py">IPConnectionCreateResponse</a></code>
- <code title="get /ip_connections/{id}">client.ip_connections.<a href="./src/telnyx/resources/ip_connections.py">retrieve</a>(id) -> <a href="./src/telnyx/types/ip_connection_retrieve_response.py">IPConnectionRetrieveResponse</a></code>
- <code title="patch /ip_connections/{id}">client.ip_connections.<a href="./src/telnyx/resources/ip_connections.py">update</a>(id, \*\*<a href="src/telnyx/types/ip_connection_update_params.py">params</a>) -> <a href="./src/telnyx/types/ip_connection_update_response.py">IPConnectionUpdateResponse</a></code>
- <code title="get /ip_connections">client.ip_connections.<a href="./src/telnyx/resources/ip_connections.py">list</a>(\*\*<a href="src/telnyx/types/ip_connection_list_params.py">params</a>) -> <a href="./src/telnyx/types/ip_connection_list_response.py">IPConnectionListResponse</a></code>
- <code title="delete /ip_connections/{id}">client.ip_connections.<a href="./src/telnyx/resources/ip_connections.py">delete</a>(id) -> <a href="./src/telnyx/types/ip_connection_delete_response.py">IPConnectionDeleteResponse</a></code>

# IPs

Types:

```python
from telnyx.types import (
    IP,
    IPCreateResponse,
    IPRetrieveResponse,
    IPUpdateResponse,
    IPListResponse,
    IPDeleteResponse,
)
```

Methods:

- <code title="post /ips">client.ips.<a href="./src/telnyx/resources/ips.py">create</a>(\*\*<a href="src/telnyx/types/ip_create_params.py">params</a>) -> <a href="./src/telnyx/types/ip_create_response.py">IPCreateResponse</a></code>
- <code title="get /ips/{id}">client.ips.<a href="./src/telnyx/resources/ips.py">retrieve</a>(id) -> <a href="./src/telnyx/types/ip_retrieve_response.py">IPRetrieveResponse</a></code>
- <code title="patch /ips/{id}">client.ips.<a href="./src/telnyx/resources/ips.py">update</a>(id, \*\*<a href="src/telnyx/types/ip_update_params.py">params</a>) -> <a href="./src/telnyx/types/ip_update_response.py">IPUpdateResponse</a></code>
- <code title="get /ips">client.ips.<a href="./src/telnyx/resources/ips.py">list</a>(\*\*<a href="src/telnyx/types/ip_list_params.py">params</a>) -> <a href="./src/telnyx/types/ip_list_response.py">IPListResponse</a></code>
- <code title="delete /ips/{id}">client.ips.<a href="./src/telnyx/resources/ips.py">delete</a>(id) -> <a href="./src/telnyx/types/ip_delete_response.py">IPDeleteResponse</a></code>

# LedgerBillingGroupReports

Types:

```python
from telnyx.types import (
    LedgerBillingGroupReport,
    LedgerBillingGroupReportCreateResponse,
    LedgerBillingGroupReportRetrieveResponse,
)
```

Methods:

- <code title="post /ledger_billing_group_reports">client.ledger_billing_group_reports.<a href="./src/telnyx/resources/ledger_billing_group_reports.py">create</a>(\*\*<a href="src/telnyx/types/ledger_billing_group_report_create_params.py">params</a>) -> <a href="./src/telnyx/types/ledger_billing_group_report_create_response.py">LedgerBillingGroupReportCreateResponse</a></code>
- <code title="get /ledger_billing_group_reports/{id}">client.ledger_billing_group_reports.<a href="./src/telnyx/resources/ledger_billing_group_reports.py">retrieve</a>(id) -> <a href="./src/telnyx/types/ledger_billing_group_report_retrieve_response.py">LedgerBillingGroupReportRetrieveResponse</a></code>

# List

Types:

```python
from telnyx.types import ListRetrieveAllResponse, ListRetrieveByZoneResponse
```

Methods:

- <code title="get /list">client.list.<a href="./src/telnyx/resources/list.py">retrieve_all</a>() -> <a href="./src/telnyx/types/list_retrieve_all_response.py">ListRetrieveAllResponse</a></code>
- <code title="get /list/{channel_zone_id}">client.list.<a href="./src/telnyx/resources/list.py">retrieve_by_zone</a>(channel_zone_id) -> <a href="./src/telnyx/types/list_retrieve_by_zone_response.py">ListRetrieveByZoneResponse</a></code>

# ManagedAccounts

Types:

```python
from telnyx.types import (
    ManagedAccount,
    ManagedAccountBalance,
    ManagedAccountCreateResponse,
    ManagedAccountRetrieveResponse,
    ManagedAccountUpdateResponse,
    ManagedAccountListResponse,
    ManagedAccountGetAllocatableGlobalOutboundChannelsResponse,
    ManagedAccountUpdateGlobalChannelLimitResponse,
)
```

Methods:

- <code title="post /managed_accounts">client.managed_accounts.<a href="./src/telnyx/resources/managed_accounts/managed_accounts.py">create</a>(\*\*<a href="src/telnyx/types/managed_account_create_params.py">params</a>) -> <a href="./src/telnyx/types/managed_account_create_response.py">ManagedAccountCreateResponse</a></code>
- <code title="get /managed_accounts/{id}">client.managed_accounts.<a href="./src/telnyx/resources/managed_accounts/managed_accounts.py">retrieve</a>(id) -> <a href="./src/telnyx/types/managed_account_retrieve_response.py">ManagedAccountRetrieveResponse</a></code>
- <code title="patch /managed_accounts/{id}">client.managed_accounts.<a href="./src/telnyx/resources/managed_accounts/managed_accounts.py">update</a>(id, \*\*<a href="src/telnyx/types/managed_account_update_params.py">params</a>) -> <a href="./src/telnyx/types/managed_account_update_response.py">ManagedAccountUpdateResponse</a></code>
- <code title="get /managed_accounts">client.managed_accounts.<a href="./src/telnyx/resources/managed_accounts/managed_accounts.py">list</a>(\*\*<a href="src/telnyx/types/managed_account_list_params.py">params</a>) -> <a href="./src/telnyx/types/managed_account_list_response.py">ManagedAccountListResponse</a></code>
- <code title="get /managed_accounts/allocatable_global_outbound_channels">client.managed_accounts.<a href="./src/telnyx/resources/managed_accounts/managed_accounts.py">get_allocatable_global_outbound_channels</a>() -> <a href="./src/telnyx/types/managed_account_get_allocatable_global_outbound_channels_response.py">ManagedAccountGetAllocatableGlobalOutboundChannelsResponse</a></code>
- <code title="patch /managed_accounts/{id}/update_global_channel_limit">client.managed_accounts.<a href="./src/telnyx/resources/managed_accounts/managed_accounts.py">update_global_channel_limit</a>(id, \*\*<a href="src/telnyx/types/managed_account_update_global_channel_limit_params.py">params</a>) -> <a href="./src/telnyx/types/managed_account_update_global_channel_limit_response.py">ManagedAccountUpdateGlobalChannelLimitResponse</a></code>

## Actions

Types:

```python
from telnyx.types.managed_accounts import ActionDisableResponse, ActionEnableResponse
```

Methods:

- <code title="post /managed_accounts/{id}/actions/disable">client.managed_accounts.actions.<a href="./src/telnyx/resources/managed_accounts/actions.py">disable</a>(id) -> <a href="./src/telnyx/types/managed_accounts/action_disable_response.py">ActionDisableResponse</a></code>
- <code title="post /managed_accounts/{id}/actions/enable">client.managed_accounts.actions.<a href="./src/telnyx/resources/managed_accounts/actions.py">enable</a>(id, \*\*<a href="src/telnyx/types/managed_accounts/action_enable_params.py">params</a>) -> <a href="./src/telnyx/types/managed_accounts/action_enable_response.py">ActionEnableResponse</a></code>

# Media

Types:

```python
from telnyx.types import (
    MediaResource,
    MediaRetrieveResponse,
    MediaUpdateResponse,
    MediaListResponse,
    MediaUploadResponse,
)
```

Methods:

- <code title="get /media/{media_name}">client.media.<a href="./src/telnyx/resources/media.py">retrieve</a>(media_name) -> <a href="./src/telnyx/types/media_retrieve_response.py">MediaRetrieveResponse</a></code>
- <code title="put /media/{media_name}">client.media.<a href="./src/telnyx/resources/media.py">update</a>(media_name, \*\*<a href="src/telnyx/types/media_update_params.py">params</a>) -> <a href="./src/telnyx/types/media_update_response.py">MediaUpdateResponse</a></code>
- <code title="get /media">client.media.<a href="./src/telnyx/resources/media.py">list</a>(\*\*<a href="src/telnyx/types/media_list_params.py">params</a>) -> <a href="./src/telnyx/types/media_list_response.py">MediaListResponse</a></code>
- <code title="delete /media/{media_name}">client.media.<a href="./src/telnyx/resources/media.py">delete</a>(media_name) -> None</code>
- <code title="get /media/{media_name}/download">client.media.<a href="./src/telnyx/resources/media.py">download</a>(media_name) -> BinaryAPIResponse</code>
- <code title="post /media">client.media.<a href="./src/telnyx/resources/media.py">upload</a>(\*\*<a href="src/telnyx/types/media_upload_params.py">params</a>) -> <a href="./src/telnyx/types/media_upload_response.py">MediaUploadResponse</a></code>

# Messages

Types:

```python
from telnyx.types import (
    Error,
    MessagingError,
    OutboundMessagePayload,
    MessageRetrieveResponse,
    MessageCancelScheduledResponse,
    MessageScheduleResponse,
    MessageSendResponse,
    MessageSendGroupMmsResponse,
    MessageSendLongCodeResponse,
    MessageSendNumberPoolResponse,
    MessageSendShortCodeResponse,
)
```

Methods:

- <code title="get /messages/{id}">client.messages.<a href="./src/telnyx/resources/messages/messages.py">retrieve</a>(id) -> <a href="./src/telnyx/types/message_retrieve_response.py">MessageRetrieveResponse</a></code>
- <code title="delete /messages/{id}">client.messages.<a href="./src/telnyx/resources/messages/messages.py">cancel_scheduled</a>(id) -> <a href="./src/telnyx/types/message_cancel_scheduled_response.py">MessageCancelScheduledResponse</a></code>
- <code title="post /messages/schedule">client.messages.<a href="./src/telnyx/resources/messages/messages.py">schedule</a>(\*\*<a href="src/telnyx/types/message_schedule_params.py">params</a>) -> <a href="./src/telnyx/types/message_schedule_response.py">MessageScheduleResponse</a></code>
- <code title="post /messages">client.messages.<a href="./src/telnyx/resources/messages/messages.py">send</a>(\*\*<a href="src/telnyx/types/message_send_params.py">params</a>) -> <a href="./src/telnyx/types/message_send_response.py">MessageSendResponse</a></code>
- <code title="post /messages/group_mms">client.messages.<a href="./src/telnyx/resources/messages/messages.py">send_group_mms</a>(\*\*<a href="src/telnyx/types/message_send_group_mms_params.py">params</a>) -> <a href="./src/telnyx/types/message_send_group_mms_response.py">MessageSendGroupMmsResponse</a></code>
- <code title="post /messages/long_code">client.messages.<a href="./src/telnyx/resources/messages/messages.py">send_long_code</a>(\*\*<a href="src/telnyx/types/message_send_long_code_params.py">params</a>) -> <a href="./src/telnyx/types/message_send_long_code_response.py">MessageSendLongCodeResponse</a></code>
- <code title="post /messages/number_pool">client.messages.<a href="./src/telnyx/resources/messages/messages.py">send_number_pool</a>(\*\*<a href="src/telnyx/types/message_send_number_pool_params.py">params</a>) -> <a href="./src/telnyx/types/message_send_number_pool_response.py">MessageSendNumberPoolResponse</a></code>
- <code title="post /messages/short_code">client.messages.<a href="./src/telnyx/resources/messages/messages.py">send_short_code</a>(\*\*<a href="src/telnyx/types/message_send_short_code_params.py">params</a>) -> <a href="./src/telnyx/types/message_send_short_code_response.py">MessageSendShortCodeResponse</a></code>

## Rcs

Types:

```python
from telnyx.types.messages import RcGenerateDeeplinkResponse
```

Methods:

- <code title="get /messages/rcs/deeplinks/{agent_id}">client.messages.rcs.<a href="./src/telnyx/resources/messages/rcs.py">generate_deeplink</a>(agent_id, \*\*<a href="src/telnyx/types/messages/rc_generate_deeplink_params.py">params</a>) -> <a href="./src/telnyx/types/messages/rc_generate_deeplink_response.py">RcGenerateDeeplinkResponse</a></code>

# Messaging

## Rcs

Types:

```python
from telnyx.types.messaging import (
    RcsCapabilities,
    RcInviteTestNumberResponse,
    RcListBulkCapabilitiesResponse,
    RcRetrieveCapabilitiesResponse,
)
```

Methods:

- <code title="put /messaging/rcs/test_number_invite/{id}/{phone_number}">client.messaging.rcs.<a href="./src/telnyx/resources/messaging/rcs.py">invite_test_number</a>(phone_number, \*, id) -> <a href="./src/telnyx/types/messaging/rc_invite_test_number_response.py">RcInviteTestNumberResponse</a></code>
- <code title="post /messaging/rcs/bulk_capabilities">client.messaging.rcs.<a href="./src/telnyx/resources/messaging/rcs.py">list_bulk_capabilities</a>(\*\*<a href="src/telnyx/types/messaging/rc_list_bulk_capabilities_params.py">params</a>) -> <a href="./src/telnyx/types/messaging/rc_list_bulk_capabilities_response.py">RcListBulkCapabilitiesResponse</a></code>
- <code title="get /messaging/rcs/capabilities/{agent_id}/{phone_number}">client.messaging.rcs.<a href="./src/telnyx/resources/messaging/rcs.py">retrieve_capabilities</a>(phone_number, \*, agent_id) -> <a href="./src/telnyx/types/messaging/rc_retrieve_capabilities_response.py">RcRetrieveCapabilitiesResponse</a></code>

# MessagingHostedNumberOrders

Types:

```python
from telnyx.types import (
    MessagingHostedNumberOrderCreateResponse,
    MessagingHostedNumberOrderRetrieveResponse,
    MessagingHostedNumberOrderListResponse,
    MessagingHostedNumberOrderDeleteResponse,
    MessagingHostedNumberOrderCheckEligibilityResponse,
    MessagingHostedNumberOrderCreateVerificationCodesResponse,
    MessagingHostedNumberOrderValidateCodesResponse,
)
```

Methods:

- <code title="post /messaging_hosted_number_orders">client.messaging_hosted_number_orders.<a href="./src/telnyx/resources/messaging_hosted_number_orders/messaging_hosted_number_orders.py">create</a>(\*\*<a href="src/telnyx/types/messaging_hosted_number_order_create_params.py">params</a>) -> <a href="./src/telnyx/types/messaging_hosted_number_order_create_response.py">MessagingHostedNumberOrderCreateResponse</a></code>
- <code title="get /messaging_hosted_number_orders/{id}">client.messaging_hosted_number_orders.<a href="./src/telnyx/resources/messaging_hosted_number_orders/messaging_hosted_number_orders.py">retrieve</a>(id) -> <a href="./src/telnyx/types/messaging_hosted_number_order_retrieve_response.py">MessagingHostedNumberOrderRetrieveResponse</a></code>
- <code title="get /messaging_hosted_number_orders">client.messaging_hosted_number_orders.<a href="./src/telnyx/resources/messaging_hosted_number_orders/messaging_hosted_number_orders.py">list</a>(\*\*<a href="src/telnyx/types/messaging_hosted_number_order_list_params.py">params</a>) -> <a href="./src/telnyx/types/messaging_hosted_number_order_list_response.py">MessagingHostedNumberOrderListResponse</a></code>
- <code title="delete /messaging_hosted_number_orders/{id}">client.messaging_hosted_number_orders.<a href="./src/telnyx/resources/messaging_hosted_number_orders/messaging_hosted_number_orders.py">delete</a>(id) -> <a href="./src/telnyx/types/messaging_hosted_number_order_delete_response.py">MessagingHostedNumberOrderDeleteResponse</a></code>
- <code title="post /messaging_hosted_number_orders/eligibility_numbers_check">client.messaging_hosted_number_orders.<a href="./src/telnyx/resources/messaging_hosted_number_orders/messaging_hosted_number_orders.py">check_eligibility</a>(\*\*<a href="src/telnyx/types/messaging_hosted_number_order_check_eligibility_params.py">params</a>) -> <a href="./src/telnyx/types/messaging_hosted_number_order_check_eligibility_response.py">MessagingHostedNumberOrderCheckEligibilityResponse</a></code>
- <code title="post /messaging_hosted_number_orders/{id}/verification_codes">client.messaging_hosted_number_orders.<a href="./src/telnyx/resources/messaging_hosted_number_orders/messaging_hosted_number_orders.py">create_verification_codes</a>(id, \*\*<a href="src/telnyx/types/messaging_hosted_number_order_create_verification_codes_params.py">params</a>) -> <a href="./src/telnyx/types/messaging_hosted_number_order_create_verification_codes_response.py">MessagingHostedNumberOrderCreateVerificationCodesResponse</a></code>
- <code title="post /messaging_hosted_number_orders/{id}/validation_codes">client.messaging_hosted_number_orders.<a href="./src/telnyx/resources/messaging_hosted_number_orders/messaging_hosted_number_orders.py">validate_codes</a>(id, \*\*<a href="src/telnyx/types/messaging_hosted_number_order_validate_codes_params.py">params</a>) -> <a href="./src/telnyx/types/messaging_hosted_number_order_validate_codes_response.py">MessagingHostedNumberOrderValidateCodesResponse</a></code>

## Actions

Types:

```python
from telnyx.types.messaging_hosted_number_orders import ActionUploadFileResponse
```

Methods:

- <code title="post /messaging_hosted_number_orders/{id}/actions/file_upload">client.messaging_hosted_number_orders.actions.<a href="./src/telnyx/resources/messaging_hosted_number_orders/actions.py">upload_file</a>(id, \*\*<a href="src/telnyx/types/messaging_hosted_number_orders/action_upload_file_params.py">params</a>) -> <a href="./src/telnyx/types/messaging_hosted_number_orders/action_upload_file_response.py">ActionUploadFileResponse</a></code>

# MessagingHostedNumbers

Types:

```python
from telnyx.types import MessagingHostedNumberDeleteResponse
```

Methods:

- <code title="delete /messaging_hosted_numbers/{id}">client.messaging_hosted_numbers.<a href="./src/telnyx/resources/messaging_hosted_numbers.py">delete</a>(id) -> <a href="./src/telnyx/types/messaging_hosted_number_delete_response.py">MessagingHostedNumberDeleteResponse</a></code>

# MessagingNumbersBulkUpdates

Types:

```python
from telnyx.types import (
    MessagingNumbersBulkUpdateCreateResponse,
    MessagingNumbersBulkUpdateRetrieveResponse,
)
```

Methods:

- <code title="post /messaging_numbers_bulk_updates">client.messaging_numbers_bulk_updates.<a href="./src/telnyx/resources/messaging_numbers_bulk_updates.py">create</a>(\*\*<a href="src/telnyx/types/messaging_numbers_bulk_update_create_params.py">params</a>) -> <a href="./src/telnyx/types/messaging_numbers_bulk_update_create_response.py">MessagingNumbersBulkUpdateCreateResponse</a></code>
- <code title="get /messaging_numbers_bulk_updates/{order_id}">client.messaging_numbers_bulk_updates.<a href="./src/telnyx/resources/messaging_numbers_bulk_updates.py">retrieve</a>(order_id) -> <a href="./src/telnyx/types/messaging_numbers_bulk_update_retrieve_response.py">MessagingNumbersBulkUpdateRetrieveResponse</a></code>

# MessagingOptouts

Types:

```python
from telnyx.types import MessagingOptoutListResponse
```

Methods:

- <code title="get /messaging_optouts">client.messaging_optouts.<a href="./src/telnyx/resources/messaging_optouts.py">list</a>(\*\*<a href="src/telnyx/types/messaging_optout_list_params.py">params</a>) -> <a href="./src/telnyx/types/messaging_optout_list_response.py">MessagingOptoutListResponse</a></code>

# MessagingProfiles

Types:

```python
from telnyx.types import (
    MessagingProfile,
    NumberPoolSettings,
    URLShortenerSettings,
    MessagingProfileCreateResponse,
    MessagingProfileRetrieveResponse,
    MessagingProfileUpdateResponse,
    MessagingProfileListResponse,
    MessagingProfileDeleteResponse,
    MessagingProfileListPhoneNumbersResponse,
    MessagingProfileListShortCodesResponse,
)
```

Methods:

- <code title="post /messaging_profiles">client.messaging_profiles.<a href="./src/telnyx/resources/messaging_profiles/messaging_profiles.py">create</a>(\*\*<a href="src/telnyx/types/messaging_profile_create_params.py">params</a>) -> <a href="./src/telnyx/types/messaging_profile_create_response.py">MessagingProfileCreateResponse</a></code>
- <code title="get /messaging_profiles/{id}">client.messaging_profiles.<a href="./src/telnyx/resources/messaging_profiles/messaging_profiles.py">retrieve</a>(id) -> <a href="./src/telnyx/types/messaging_profile_retrieve_response.py">MessagingProfileRetrieveResponse</a></code>
- <code title="patch /messaging_profiles/{id}">client.messaging_profiles.<a href="./src/telnyx/resources/messaging_profiles/messaging_profiles.py">update</a>(id, \*\*<a href="src/telnyx/types/messaging_profile_update_params.py">params</a>) -> <a href="./src/telnyx/types/messaging_profile_update_response.py">MessagingProfileUpdateResponse</a></code>
- <code title="get /messaging_profiles">client.messaging_profiles.<a href="./src/telnyx/resources/messaging_profiles/messaging_profiles.py">list</a>(\*\*<a href="src/telnyx/types/messaging_profile_list_params.py">params</a>) -> <a href="./src/telnyx/types/messaging_profile_list_response.py">MessagingProfileListResponse</a></code>
- <code title="delete /messaging_profiles/{id}">client.messaging_profiles.<a href="./src/telnyx/resources/messaging_profiles/messaging_profiles.py">delete</a>(id) -> <a href="./src/telnyx/types/messaging_profile_delete_response.py">MessagingProfileDeleteResponse</a></code>
- <code title="get /messaging_profiles/{id}/phone_numbers">client.messaging_profiles.<a href="./src/telnyx/resources/messaging_profiles/messaging_profiles.py">list_phone_numbers</a>(id, \*\*<a href="src/telnyx/types/messaging_profile_list_phone_numbers_params.py">params</a>) -> <a href="./src/telnyx/types/messaging_profile_list_phone_numbers_response.py">MessagingProfileListPhoneNumbersResponse</a></code>
- <code title="get /messaging_profiles/{id}/short_codes">client.messaging_profiles.<a href="./src/telnyx/resources/messaging_profiles/messaging_profiles.py">list_short_codes</a>(id, \*\*<a href="src/telnyx/types/messaging_profile_list_short_codes_params.py">params</a>) -> <a href="./src/telnyx/types/messaging_profile_list_short_codes_response.py">MessagingProfileListShortCodesResponse</a></code>

## AutorespConfigs

Types:

```python
from telnyx.types.messaging_profiles import (
    AutoRespConfig,
    AutoRespConfigCreate,
    AutoRespConfigResponse,
    AutorespConfigListResponse,
)
```

Methods:

- <code title="post /messaging_profiles/{profile_id}/autoresp_configs">client.messaging_profiles.autoresp_configs.<a href="./src/telnyx/resources/messaging_profiles/autoresp_configs.py">create</a>(profile_id, \*\*<a href="src/telnyx/types/messaging_profiles/autoresp_config_create_params.py">params</a>) -> <a href="./src/telnyx/types/messaging_profiles/auto_resp_config_response.py">AutoRespConfigResponse</a></code>
- <code title="get /messaging_profiles/{profile_id}/autoresp_configs/{autoresp_cfg_id}">client.messaging_profiles.autoresp_configs.<a href="./src/telnyx/resources/messaging_profiles/autoresp_configs.py">retrieve</a>(autoresp_cfg_id, \*, profile_id) -> <a href="./src/telnyx/types/messaging_profiles/auto_resp_config_response.py">AutoRespConfigResponse</a></code>
- <code title="put /messaging_profiles/{profile_id}/autoresp_configs/{autoresp_cfg_id}">client.messaging_profiles.autoresp_configs.<a href="./src/telnyx/resources/messaging_profiles/autoresp_configs.py">update</a>(autoresp_cfg_id, \*, profile_id, \*\*<a href="src/telnyx/types/messaging_profiles/autoresp_config_update_params.py">params</a>) -> <a href="./src/telnyx/types/messaging_profiles/auto_resp_config_response.py">AutoRespConfigResponse</a></code>
- <code title="get /messaging_profiles/{profile_id}/autoresp_configs">client.messaging_profiles.autoresp_configs.<a href="./src/telnyx/resources/messaging_profiles/autoresp_configs.py">list</a>(profile_id, \*\*<a href="src/telnyx/types/messaging_profiles/autoresp_config_list_params.py">params</a>) -> <a href="./src/telnyx/types/messaging_profiles/autoresp_config_list_response.py">AutorespConfigListResponse</a></code>
- <code title="delete /messaging_profiles/{profile_id}/autoresp_configs/{autoresp_cfg_id}">client.messaging_profiles.autoresp_configs.<a href="./src/telnyx/resources/messaging_profiles/autoresp_configs.py">delete</a>(autoresp_cfg_id, \*, profile_id) -> object</code>

# MessagingTollfree

## Verification

### Requests

Types:

```python
from telnyx.types.messaging_tollfree.verification import (
    TfPhoneNumber,
    TfVerificationRequest,
    TfVerificationStatus,
    URL,
    UseCaseCategories,
    VerificationRequestEgress,
    VerificationRequestStatus,
    Volume,
    RequestListResponse,
)
```

Methods:

- <code title="post /messaging_tollfree/verification/requests">client.messaging_tollfree.verification.requests.<a href="./src/telnyx/resources/messaging_tollfree/verification/requests.py">create</a>(\*\*<a href="src/telnyx/types/messaging_tollfree/verification/request_create_params.py">params</a>) -> <a href="./src/telnyx/types/messaging_tollfree/verification/verification_request_egress.py">VerificationRequestEgress</a></code>
- <code title="get /messaging_tollfree/verification/requests/{id}">client.messaging_tollfree.verification.requests.<a href="./src/telnyx/resources/messaging_tollfree/verification/requests.py">retrieve</a>(id) -> <a href="./src/telnyx/types/messaging_tollfree/verification/verification_request_status.py">VerificationRequestStatus</a></code>
- <code title="patch /messaging_tollfree/verification/requests/{id}">client.messaging_tollfree.verification.requests.<a href="./src/telnyx/resources/messaging_tollfree/verification/requests.py">update</a>(id, \*\*<a href="src/telnyx/types/messaging_tollfree/verification/request_update_params.py">params</a>) -> <a href="./src/telnyx/types/messaging_tollfree/verification/verification_request_egress.py">VerificationRequestEgress</a></code>
- <code title="get /messaging_tollfree/verification/requests">client.messaging_tollfree.verification.requests.<a href="./src/telnyx/resources/messaging_tollfree/verification/requests.py">list</a>(\*\*<a href="src/telnyx/types/messaging_tollfree/verification/request_list_params.py">params</a>) -> <a href="./src/telnyx/types/messaging_tollfree/verification/request_list_response.py">RequestListResponse</a></code>
- <code title="delete /messaging_tollfree/verification/requests/{id}">client.messaging_tollfree.verification.requests.<a href="./src/telnyx/resources/messaging_tollfree/verification/requests.py">delete</a>(id) -> object</code>

# MessagingURLDomains

Types:

```python
from telnyx.types import MessagingURLDomainListResponse
```

Methods:

- <code title="get /messaging_url_domains">client.messaging_url_domains.<a href="./src/telnyx/resources/messaging_url_domains.py">list</a>(\*\*<a href="src/telnyx/types/messaging_url_domain_list_params.py">params</a>) -> <a href="./src/telnyx/types/messaging_url_domain_list_response.py">MessagingURLDomainListResponse</a></code>

# Messsages

Types:

```python
from telnyx.types import (
    RcsAgentMessage,
    RcsCardContent,
    RcsContentInfo,
    RcsSuggestion,
    MesssageRcsResponse,
)
```

Methods:

- <code title="post /messsages/rcs">client.messsages.<a href="./src/telnyx/resources/messsages.py">rcs</a>(\*\*<a href="src/telnyx/types/messsage_rcs_params.py">params</a>) -> <a href="./src/telnyx/types/messsage_rcs_response.py">MesssageRcsResponse</a></code>

# MobileNetworkOperators

Types:

```python
from telnyx.types import MobileNetworkOperatorListResponse
```

Methods:

- <code title="get /mobile_network_operators">client.mobile_network_operators.<a href="./src/telnyx/resources/mobile_network_operators.py">list</a>(\*\*<a href="src/telnyx/types/mobile_network_operator_list_params.py">params</a>) -> <a href="./src/telnyx/types/mobile_network_operator_list_response.py">MobileNetworkOperatorListResponse</a></code>

# MobilePushCredentials

Types:

```python
from telnyx.types import PushCredential, PushCredentialResponse, MobilePushCredentialListResponse
```

Methods:

- <code title="post /mobile_push_credentials">client.mobile_push_credentials.<a href="./src/telnyx/resources/mobile_push_credentials.py">create</a>(\*\*<a href="src/telnyx/types/mobile_push_credential_create_params.py">params</a>) -> <a href="./src/telnyx/types/push_credential_response.py">PushCredentialResponse</a></code>
- <code title="get /mobile_push_credentials/{push_credential_id}">client.mobile_push_credentials.<a href="./src/telnyx/resources/mobile_push_credentials.py">retrieve</a>(push_credential_id) -> <a href="./src/telnyx/types/push_credential_response.py">PushCredentialResponse</a></code>
- <code title="get /mobile_push_credentials">client.mobile_push_credentials.<a href="./src/telnyx/resources/mobile_push_credentials.py">list</a>(\*\*<a href="src/telnyx/types/mobile_push_credential_list_params.py">params</a>) -> <a href="./src/telnyx/types/mobile_push_credential_list_response.py">MobilePushCredentialListResponse</a></code>
- <code title="delete /mobile_push_credentials/{push_credential_id}">client.mobile_push_credentials.<a href="./src/telnyx/resources/mobile_push_credentials.py">delete</a>(push_credential_id) -> None</code>

# NetworkCoverage

Types:

```python
from telnyx.types import AvailableService, NetworkCoverageListResponse
```

Methods:

- <code title="get /network_coverage">client.network_coverage.<a href="./src/telnyx/resources/network_coverage.py">list</a>(\*\*<a href="src/telnyx/types/network_coverage_list_params.py">params</a>) -> <a href="./src/telnyx/types/network_coverage_list_response.py">NetworkCoverageListResponse</a></code>

# Networks

Types:

```python
from telnyx.types import (
    InterfaceStatus,
    NetworkCreate,
    NetworkCreateResponse,
    NetworkRetrieveResponse,
    NetworkUpdateResponse,
    NetworkListResponse,
    NetworkDeleteResponse,
    NetworkListInterfacesResponse,
)
```

Methods:

- <code title="post /networks">client.networks.<a href="./src/telnyx/resources/networks/networks.py">create</a>(\*\*<a href="src/telnyx/types/network_create_params.py">params</a>) -> <a href="./src/telnyx/types/network_create_response.py">NetworkCreateResponse</a></code>
- <code title="get /networks/{id}">client.networks.<a href="./src/telnyx/resources/networks/networks.py">retrieve</a>(id) -> <a href="./src/telnyx/types/network_retrieve_response.py">NetworkRetrieveResponse</a></code>
- <code title="patch /networks/{id}">client.networks.<a href="./src/telnyx/resources/networks/networks.py">update</a>(id, \*\*<a href="src/telnyx/types/network_update_params.py">params</a>) -> <a href="./src/telnyx/types/network_update_response.py">NetworkUpdateResponse</a></code>
- <code title="get /networks">client.networks.<a href="./src/telnyx/resources/networks/networks.py">list</a>(\*\*<a href="src/telnyx/types/network_list_params.py">params</a>) -> <a href="./src/telnyx/types/network_list_response.py">NetworkListResponse</a></code>
- <code title="delete /networks/{id}">client.networks.<a href="./src/telnyx/resources/networks/networks.py">delete</a>(id) -> <a href="./src/telnyx/types/network_delete_response.py">NetworkDeleteResponse</a></code>
- <code title="get /networks/{id}/network_interfaces">client.networks.<a href="./src/telnyx/resources/networks/networks.py">list_interfaces</a>(id, \*\*<a href="src/telnyx/types/network_list_interfaces_params.py">params</a>) -> <a href="./src/telnyx/types/network_list_interfaces_response.py">NetworkListInterfacesResponse</a></code>

## DefaultGateway

Types:

```python
from telnyx.types.networks import (
    DefaultGatewayCreateResponse,
    DefaultGatewayRetrieveResponse,
    DefaultGatewayDeleteResponse,
)
```

Methods:

- <code title="post /networks/{id}/default_gateway">client.networks.default_gateway.<a href="./src/telnyx/resources/networks/default_gateway.py">create</a>(id, \*\*<a href="src/telnyx/types/networks/default_gateway_create_params.py">params</a>) -> <a href="./src/telnyx/types/networks/default_gateway_create_response.py">DefaultGatewayCreateResponse</a></code>
- <code title="get /networks/{id}/default_gateway">client.networks.default_gateway.<a href="./src/telnyx/resources/networks/default_gateway.py">retrieve</a>(id) -> <a href="./src/telnyx/types/networks/default_gateway_retrieve_response.py">DefaultGatewayRetrieveResponse</a></code>
- <code title="delete /networks/{id}/default_gateway">client.networks.default_gateway.<a href="./src/telnyx/resources/networks/default_gateway.py">delete</a>(id) -> <a href="./src/telnyx/types/networks/default_gateway_delete_response.py">DefaultGatewayDeleteResponse</a></code>

# NotificationChannels

Types:

```python
from telnyx.types import (
    NotificationChannel,
    NotificationChannelCreateResponse,
    NotificationChannelRetrieveResponse,
    NotificationChannelUpdateResponse,
    NotificationChannelListResponse,
    NotificationChannelDeleteResponse,
)
```

Methods:

- <code title="post /notification_channels">client.notification_channels.<a href="./src/telnyx/resources/notification_channels.py">create</a>(\*\*<a href="src/telnyx/types/notification_channel_create_params.py">params</a>) -> <a href="./src/telnyx/types/notification_channel_create_response.py">NotificationChannelCreateResponse</a></code>
- <code title="get /notification_channels/{id}">client.notification_channels.<a href="./src/telnyx/resources/notification_channels.py">retrieve</a>(id) -> <a href="./src/telnyx/types/notification_channel_retrieve_response.py">NotificationChannelRetrieveResponse</a></code>
- <code title="patch /notification_channels/{id}">client.notification_channels.<a href="./src/telnyx/resources/notification_channels.py">update</a>(id, \*\*<a href="src/telnyx/types/notification_channel_update_params.py">params</a>) -> <a href="./src/telnyx/types/notification_channel_update_response.py">NotificationChannelUpdateResponse</a></code>
- <code title="get /notification_channels">client.notification_channels.<a href="./src/telnyx/resources/notification_channels.py">list</a>(\*\*<a href="src/telnyx/types/notification_channel_list_params.py">params</a>) -> <a href="./src/telnyx/types/notification_channel_list_response.py">NotificationChannelListResponse</a></code>
- <code title="delete /notification_channels/{id}">client.notification_channels.<a href="./src/telnyx/resources/notification_channels.py">delete</a>(id) -> <a href="./src/telnyx/types/notification_channel_delete_response.py">NotificationChannelDeleteResponse</a></code>

# NotificationEventConditions

Types:

```python
from telnyx.types import NotificationEventConditionListResponse
```

Methods:

- <code title="get /notification_event_conditions">client.notification_event_conditions.<a href="./src/telnyx/resources/notification_event_conditions.py">list</a>(\*\*<a href="src/telnyx/types/notification_event_condition_list_params.py">params</a>) -> <a href="./src/telnyx/types/notification_event_condition_list_response.py">NotificationEventConditionListResponse</a></code>

# NotificationEvents

Types:

```python
from telnyx.types import NotificationEventListResponse
```

Methods:

- <code title="get /notification_events">client.notification_events.<a href="./src/telnyx/resources/notification_events.py">list</a>(\*\*<a href="src/telnyx/types/notification_event_list_params.py">params</a>) -> <a href="./src/telnyx/types/notification_event_list_response.py">NotificationEventListResponse</a></code>

# NotificationProfiles

Types:

```python
from telnyx.types import (
    NotificationProfile,
    NotificationProfileCreateResponse,
    NotificationProfileRetrieveResponse,
    NotificationProfileUpdateResponse,
    NotificationProfileListResponse,
    NotificationProfileDeleteResponse,
)
```

Methods:

- <code title="post /notification_profiles">client.notification_profiles.<a href="./src/telnyx/resources/notification_profiles.py">create</a>(\*\*<a href="src/telnyx/types/notification_profile_create_params.py">params</a>) -> <a href="./src/telnyx/types/notification_profile_create_response.py">NotificationProfileCreateResponse</a></code>
- <code title="get /notification_profiles/{id}">client.notification_profiles.<a href="./src/telnyx/resources/notification_profiles.py">retrieve</a>(id) -> <a href="./src/telnyx/types/notification_profile_retrieve_response.py">NotificationProfileRetrieveResponse</a></code>
- <code title="patch /notification_profiles/{id}">client.notification_profiles.<a href="./src/telnyx/resources/notification_profiles.py">update</a>(id, \*\*<a href="src/telnyx/types/notification_profile_update_params.py">params</a>) -> <a href="./src/telnyx/types/notification_profile_update_response.py">NotificationProfileUpdateResponse</a></code>
- <code title="get /notification_profiles">client.notification_profiles.<a href="./src/telnyx/resources/notification_profiles.py">list</a>(\*\*<a href="src/telnyx/types/notification_profile_list_params.py">params</a>) -> <a href="./src/telnyx/types/notification_profile_list_response.py">NotificationProfileListResponse</a></code>
- <code title="delete /notification_profiles/{id}">client.notification_profiles.<a href="./src/telnyx/resources/notification_profiles.py">delete</a>(id) -> <a href="./src/telnyx/types/notification_profile_delete_response.py">NotificationProfileDeleteResponse</a></code>

# NotificationSettings

Types:

```python
from telnyx.types import (
    NotificationSetting,
    NotificationSettingCreateResponse,
    NotificationSettingRetrieveResponse,
    NotificationSettingListResponse,
    NotificationSettingDeleteResponse,
)
```

Methods:

- <code title="post /notification_settings">client.notification_settings.<a href="./src/telnyx/resources/notification_settings.py">create</a>(\*\*<a href="src/telnyx/types/notification_setting_create_params.py">params</a>) -> <a href="./src/telnyx/types/notification_setting_create_response.py">NotificationSettingCreateResponse</a></code>
- <code title="get /notification_settings/{id}">client.notification_settings.<a href="./src/telnyx/resources/notification_settings.py">retrieve</a>(id) -> <a href="./src/telnyx/types/notification_setting_retrieve_response.py">NotificationSettingRetrieveResponse</a></code>
- <code title="get /notification_settings">client.notification_settings.<a href="./src/telnyx/resources/notification_settings.py">list</a>(\*\*<a href="src/telnyx/types/notification_setting_list_params.py">params</a>) -> <a href="./src/telnyx/types/notification_setting_list_response.py">NotificationSettingListResponse</a></code>
- <code title="delete /notification_settings/{id}">client.notification_settings.<a href="./src/telnyx/resources/notification_settings.py">delete</a>(id) -> <a href="./src/telnyx/types/notification_setting_delete_response.py">NotificationSettingDeleteResponse</a></code>

# NumberBlockOrders

Types:

```python
from telnyx.types import (
    NumberBlockOrder,
    NumberBlockOrderCreateResponse,
    NumberBlockOrderRetrieveResponse,
    NumberBlockOrderListResponse,
)
```

Methods:

- <code title="post /number_block_orders">client.number_block_orders.<a href="./src/telnyx/resources/number_block_orders.py">create</a>(\*\*<a href="src/telnyx/types/number_block_order_create_params.py">params</a>) -> <a href="./src/telnyx/types/number_block_order_create_response.py">NumberBlockOrderCreateResponse</a></code>
- <code title="get /number_block_orders/{number_block_order_id}">client.number_block_orders.<a href="./src/telnyx/resources/number_block_orders.py">retrieve</a>(number_block_order_id) -> <a href="./src/telnyx/types/number_block_order_retrieve_response.py">NumberBlockOrderRetrieveResponse</a></code>
- <code title="get /number_block_orders">client.number_block_orders.<a href="./src/telnyx/resources/number_block_orders.py">list</a>(\*\*<a href="src/telnyx/types/number_block_order_list_params.py">params</a>) -> <a href="./src/telnyx/types/number_block_order_list_response.py">NumberBlockOrderListResponse</a></code>

# NumberLookup

Types:

```python
from telnyx.types import NumberLookupRetrieveResponse
```

Methods:

- <code title="get /number_lookup/{phone_number}">client.number_lookup.<a href="./src/telnyx/resources/number_lookup.py">retrieve</a>(phone_number, \*\*<a href="src/telnyx/types/number_lookup_retrieve_params.py">params</a>) -> <a href="./src/telnyx/types/number_lookup_retrieve_response.py">NumberLookupRetrieveResponse</a></code>

# NumberOrderPhoneNumbers

Types:

```python
from telnyx.types import (
    NumberOrderPhoneNumber,
    UpdateRegulatoryRequirement,
    NumberOrderPhoneNumberRetrieveResponse,
    NumberOrderPhoneNumberListResponse,
    NumberOrderPhoneNumberUpdateRequirementGroupResponse,
    NumberOrderPhoneNumberUpdateRequirementsResponse,
)
```

Methods:

- <code title="get /number_order_phone_numbers/{number_order_phone_number_id}">client.number_order_phone_numbers.<a href="./src/telnyx/resources/number_order_phone_numbers.py">retrieve</a>(number_order_phone_number_id) -> <a href="./src/telnyx/types/number_order_phone_number_retrieve_response.py">NumberOrderPhoneNumberRetrieveResponse</a></code>
- <code title="get /number_order_phone_numbers">client.number_order_phone_numbers.<a href="./src/telnyx/resources/number_order_phone_numbers.py">list</a>(\*\*<a href="src/telnyx/types/number_order_phone_number_list_params.py">params</a>) -> <a href="./src/telnyx/types/number_order_phone_number_list_response.py">NumberOrderPhoneNumberListResponse</a></code>
- <code title="post /number_order_phone_numbers/{id}/requirement_group">client.number_order_phone_numbers.<a href="./src/telnyx/resources/number_order_phone_numbers.py">update_requirement_group</a>(id, \*\*<a href="src/telnyx/types/number_order_phone_number_update_requirement_group_params.py">params</a>) -> <a href="./src/telnyx/types/number_order_phone_number_update_requirement_group_response.py">NumberOrderPhoneNumberUpdateRequirementGroupResponse</a></code>
- <code title="patch /number_order_phone_numbers/{number_order_phone_number_id}">client.number_order_phone_numbers.<a href="./src/telnyx/resources/number_order_phone_numbers.py">update_requirements</a>(number_order_phone_number_id, \*\*<a href="src/telnyx/types/number_order_phone_number_update_requirements_params.py">params</a>) -> <a href="./src/telnyx/types/number_order_phone_number_update_requirements_response.py">NumberOrderPhoneNumberUpdateRequirementsResponse</a></code>

# NumberOrders

Types:

```python
from telnyx.types import (
    NumberOrderWithPhoneNumbers,
    PhoneNumber,
    NumberOrderCreateResponse,
    NumberOrderRetrieveResponse,
    NumberOrderUpdateResponse,
    NumberOrderListResponse,
)
```

Methods:

- <code title="post /number_orders">client.number_orders.<a href="./src/telnyx/resources/number_orders.py">create</a>(\*\*<a href="src/telnyx/types/number_order_create_params.py">params</a>) -> <a href="./src/telnyx/types/number_order_create_response.py">NumberOrderCreateResponse</a></code>
- <code title="get /number_orders/{number_order_id}">client.number_orders.<a href="./src/telnyx/resources/number_orders.py">retrieve</a>(number_order_id) -> <a href="./src/telnyx/types/number_order_retrieve_response.py">NumberOrderRetrieveResponse</a></code>
- <code title="patch /number_orders/{number_order_id}">client.number_orders.<a href="./src/telnyx/resources/number_orders.py">update</a>(number_order_id, \*\*<a href="src/telnyx/types/number_order_update_params.py">params</a>) -> <a href="./src/telnyx/types/number_order_update_response.py">NumberOrderUpdateResponse</a></code>
- <code title="get /number_orders">client.number_orders.<a href="./src/telnyx/resources/number_orders.py">list</a>(\*\*<a href="src/telnyx/types/number_order_list_params.py">params</a>) -> <a href="./src/telnyx/types/number_order_list_response.py">NumberOrderListResponse</a></code>

# NumberReservations

Types:

```python
from telnyx.types import (
    NumberReservation,
    ReservedPhoneNumber,
    NumberReservationCreateResponse,
    NumberReservationRetrieveResponse,
    NumberReservationListResponse,
)
```

Methods:

- <code title="post /number_reservations">client.number_reservations.<a href="./src/telnyx/resources/number_reservations/number_reservations.py">create</a>(\*\*<a href="src/telnyx/types/number_reservation_create_params.py">params</a>) -> <a href="./src/telnyx/types/number_reservation_create_response.py">NumberReservationCreateResponse</a></code>
- <code title="get /number_reservations/{number_reservation_id}">client.number_reservations.<a href="./src/telnyx/resources/number_reservations/number_reservations.py">retrieve</a>(number_reservation_id) -> <a href="./src/telnyx/types/number_reservation_retrieve_response.py">NumberReservationRetrieveResponse</a></code>
- <code title="get /number_reservations">client.number_reservations.<a href="./src/telnyx/resources/number_reservations/number_reservations.py">list</a>(\*\*<a href="src/telnyx/types/number_reservation_list_params.py">params</a>) -> <a href="./src/telnyx/types/number_reservation_list_response.py">NumberReservationListResponse</a></code>

## Actions

Types:

```python
from telnyx.types.number_reservations import ActionExtendResponse
```

Methods:

- <code title="post /number_reservations/{number_reservation_id}/actions/extend">client.number_reservations.actions.<a href="./src/telnyx/resources/number_reservations/actions.py">extend</a>(number_reservation_id) -> <a href="./src/telnyx/types/number_reservations/action_extend_response.py">ActionExtendResponse</a></code>

# NumbersFeatures

Types:

```python
from telnyx.types import NumbersFeatureCreateResponse
```

Methods:

- <code title="post /numbers_features">client.numbers_features.<a href="./src/telnyx/resources/numbers_features.py">create</a>(\*\*<a href="src/telnyx/types/numbers_feature_create_params.py">params</a>) -> <a href="./src/telnyx/types/numbers_feature_create_response.py">NumbersFeatureCreateResponse</a></code>

# OperatorConnect

## Actions

Types:

```python
from telnyx.types.operator_connect import ActionRefreshResponse
```

Methods:

- <code title="post /operator_connect/actions/refresh">client.operator_connect.actions.<a href="./src/telnyx/resources/operator_connect/actions.py">refresh</a>() -> <a href="./src/telnyx/types/operator_connect/action_refresh_response.py">ActionRefreshResponse</a></code>

# OtaUpdates

Types:

```python
from telnyx.types import OtaUpdateRetrieveResponse, OtaUpdateListResponse
```

Methods:

- <code title="get /ota_updates/{id}">client.ota_updates.<a href="./src/telnyx/resources/ota_updates.py">retrieve</a>(id) -> <a href="./src/telnyx/types/ota_update_retrieve_response.py">OtaUpdateRetrieveResponse</a></code>
- <code title="get /ota_updates">client.ota_updates.<a href="./src/telnyx/resources/ota_updates.py">list</a>(\*\*<a href="src/telnyx/types/ota_update_list_params.py">params</a>) -> <a href="./src/telnyx/types/ota_update_list_response.py">OtaUpdateListResponse</a></code>

# OutboundVoiceProfiles

Types:

```python
from telnyx.types import (
    OutboundCallRecording,
    OutboundVoiceProfile,
    ServicePlan,
    TrafficType,
    UsagePaymentMethod,
    OutboundVoiceProfileCreateResponse,
    OutboundVoiceProfileRetrieveResponse,
    OutboundVoiceProfileUpdateResponse,
    OutboundVoiceProfileListResponse,
    OutboundVoiceProfileDeleteResponse,
)
```

Methods:

- <code title="post /outbound_voice_profiles">client.outbound_voice_profiles.<a href="./src/telnyx/resources/outbound_voice_profiles.py">create</a>(\*\*<a href="src/telnyx/types/outbound_voice_profile_create_params.py">params</a>) -> <a href="./src/telnyx/types/outbound_voice_profile_create_response.py">OutboundVoiceProfileCreateResponse</a></code>
- <code title="get /outbound_voice_profiles/{id}">client.outbound_voice_profiles.<a href="./src/telnyx/resources/outbound_voice_profiles.py">retrieve</a>(id) -> <a href="./src/telnyx/types/outbound_voice_profile_retrieve_response.py">OutboundVoiceProfileRetrieveResponse</a></code>
- <code title="patch /outbound_voice_profiles/{id}">client.outbound_voice_profiles.<a href="./src/telnyx/resources/outbound_voice_profiles.py">update</a>(id, \*\*<a href="src/telnyx/types/outbound_voice_profile_update_params.py">params</a>) -> <a href="./src/telnyx/types/outbound_voice_profile_update_response.py">OutboundVoiceProfileUpdateResponse</a></code>
- <code title="get /outbound_voice_profiles">client.outbound_voice_profiles.<a href="./src/telnyx/resources/outbound_voice_profiles.py">list</a>(\*\*<a href="src/telnyx/types/outbound_voice_profile_list_params.py">params</a>) -> <a href="./src/telnyx/types/outbound_voice_profile_list_response.py">OutboundVoiceProfileListResponse</a></code>
- <code title="delete /outbound_voice_profiles/{id}">client.outbound_voice_profiles.<a href="./src/telnyx/resources/outbound_voice_profiles.py">delete</a>(id) -> <a href="./src/telnyx/types/outbound_voice_profile_delete_response.py">OutboundVoiceProfileDeleteResponse</a></code>

# Payment

## AutoRechargePrefs

Types:

```python
from telnyx.types.payment import AutoRechargePrefUpdateResponse, AutoRechargePrefListResponse
```

Methods:

- <code title="patch /payment/auto_recharge_prefs">client.payment.auto_recharge_prefs.<a href="./src/telnyx/resources/payment/auto_recharge_prefs.py">update</a>(\*\*<a href="src/telnyx/types/payment/auto_recharge_pref_update_params.py">params</a>) -> <a href="./src/telnyx/types/payment/auto_recharge_pref_update_response.py">AutoRechargePrefUpdateResponse</a></code>
- <code title="get /payment/auto_recharge_prefs">client.payment.auto_recharge_prefs.<a href="./src/telnyx/resources/payment/auto_recharge_prefs.py">list</a>() -> <a href="./src/telnyx/types/payment/auto_recharge_pref_list_response.py">AutoRechargePrefListResponse</a></code>

# PhoneNumberAssignmentByProfile

Types:

```python
from telnyx.types import (
    TaskStatus,
    PhoneNumberAssignmentByProfileAssignResponse,
    PhoneNumberAssignmentByProfileRetrievePhoneNumberStatusResponse,
    PhoneNumberAssignmentByProfileRetrieveStatusResponse,
)
```

Methods:

- <code title="post /phoneNumberAssignmentByProfile">client.phone_number_assignment_by_profile.<a href="./src/telnyx/resources/phone_number_assignment_by_profile.py">assign</a>(\*\*<a href="src/telnyx/types/phone_number_assignment_by_profile_assign_params.py">params</a>) -> <a href="./src/telnyx/types/phone_number_assignment_by_profile_assign_response.py">PhoneNumberAssignmentByProfileAssignResponse</a></code>
- <code title="get /phoneNumberAssignmentByProfile/{taskId}/phoneNumbers">client.phone_number_assignment_by_profile.<a href="./src/telnyx/resources/phone_number_assignment_by_profile.py">retrieve_phone_number_status</a>(task_id, \*\*<a href="src/telnyx/types/phone_number_assignment_by_profile_retrieve_phone_number_status_params.py">params</a>) -> <a href="./src/telnyx/types/phone_number_assignment_by_profile_retrieve_phone_number_status_response.py">PhoneNumberAssignmentByProfileRetrievePhoneNumberStatusResponse</a></code>
- <code title="get /phoneNumberAssignmentByProfile/{taskId}">client.phone_number_assignment_by_profile.<a href="./src/telnyx/resources/phone_number_assignment_by_profile.py">retrieve_status</a>(task_id) -> <a href="./src/telnyx/types/phone_number_assignment_by_profile_retrieve_status_response.py">PhoneNumberAssignmentByProfileRetrieveStatusResponse</a></code>

# PhoneNumberBlocks

## Jobs

Types:

```python
from telnyx.types.phone_number_blocks import (
    Job,
    JobRetrieveResponse,
    JobListResponse,
    JobDeletePhoneNumberBlockResponse,
)
```

Methods:

- <code title="get /phone_number_blocks/jobs/{id}">client.phone_number_blocks.jobs.<a href="./src/telnyx/resources/phone_number_blocks/jobs.py">retrieve</a>(id) -> <a href="./src/telnyx/types/phone_number_blocks/job_retrieve_response.py">JobRetrieveResponse</a></code>
- <code title="get /phone_number_blocks/jobs">client.phone_number_blocks.jobs.<a href="./src/telnyx/resources/phone_number_blocks/jobs.py">list</a>(\*\*<a href="src/telnyx/types/phone_number_blocks/job_list_params.py">params</a>) -> <a href="./src/telnyx/types/phone_number_blocks/job_list_response.py">JobListResponse</a></code>
- <code title="post /phone_number_blocks/jobs/delete_phone_number_block">client.phone_number_blocks.jobs.<a href="./src/telnyx/resources/phone_number_blocks/jobs.py">delete_phone_number_block</a>(\*\*<a href="src/telnyx/types/phone_number_blocks/job_delete_phone_number_block_params.py">params</a>) -> <a href="./src/telnyx/types/phone_number_blocks/job_delete_phone_number_block_response.py">JobDeletePhoneNumberBlockResponse</a></code>

# PhoneNumberCampaigns

Types:

```python
from telnyx.types import (
    PhoneNumberCampaign,
    PhoneNumberCampaignCreate,
    PhoneNumberCampaignListResponse,
)
```

Methods:

- <code title="post /phone_number_campaigns">client.phone_number_campaigns.<a href="./src/telnyx/resources/phone_number_campaigns.py">create</a>(\*\*<a href="src/telnyx/types/phone_number_campaign_create_params.py">params</a>) -> <a href="./src/telnyx/types/phone_number_campaign.py">PhoneNumberCampaign</a></code>
- <code title="get /phone_number_campaigns/{phoneNumber}">client.phone_number_campaigns.<a href="./src/telnyx/resources/phone_number_campaigns.py">retrieve</a>(phone_number) -> <a href="./src/telnyx/types/phone_number_campaign.py">PhoneNumberCampaign</a></code>
- <code title="put /phone_number_campaigns/{phoneNumber}">client.phone_number_campaigns.<a href="./src/telnyx/resources/phone_number_campaigns.py">update</a>(path_phone_number, \*\*<a href="src/telnyx/types/phone_number_campaign_update_params.py">params</a>) -> <a href="./src/telnyx/types/phone_number_campaign.py">PhoneNumberCampaign</a></code>
- <code title="get /phone_number_campaigns">client.phone_number_campaigns.<a href="./src/telnyx/resources/phone_number_campaigns.py">list</a>(\*\*<a href="src/telnyx/types/phone_number_campaign_list_params.py">params</a>) -> <a href="./src/telnyx/types/phone_number_campaign_list_response.py">PhoneNumberCampaignListResponse</a></code>
- <code title="delete /phone_number_campaigns/{phoneNumber}">client.phone_number_campaigns.<a href="./src/telnyx/resources/phone_number_campaigns.py">delete</a>(phone_number) -> <a href="./src/telnyx/types/phone_number_campaign.py">PhoneNumberCampaign</a></code>

# PhoneNumbers

Types:

```python
from telnyx.types import (
    PhoneNumberDetailed,
    PhoneNumberRetrieveResponse,
    PhoneNumberUpdateResponse,
    PhoneNumberListResponse,
    PhoneNumberDeleteResponse,
    PhoneNumberSlimListResponse,
)
```

Methods:

- <code title="get /phone_numbers/{id}">client.phone_numbers.<a href="./src/telnyx/resources/phone_numbers/phone_numbers.py">retrieve</a>(id) -> <a href="./src/telnyx/types/phone_number_retrieve_response.py">PhoneNumberRetrieveResponse</a></code>
- <code title="patch /phone_numbers/{id}">client.phone_numbers.<a href="./src/telnyx/resources/phone_numbers/phone_numbers.py">update</a>(id, \*\*<a href="src/telnyx/types/phone_number_update_params.py">params</a>) -> <a href="./src/telnyx/types/phone_number_update_response.py">PhoneNumberUpdateResponse</a></code>
- <code title="get /phone_numbers">client.phone_numbers.<a href="./src/telnyx/resources/phone_numbers/phone_numbers.py">list</a>(\*\*<a href="src/telnyx/types/phone_number_list_params.py">params</a>) -> <a href="./src/telnyx/types/phone_number_list_response.py">PhoneNumberListResponse</a></code>
- <code title="delete /phone_numbers/{id}">client.phone_numbers.<a href="./src/telnyx/resources/phone_numbers/phone_numbers.py">delete</a>(id) -> <a href="./src/telnyx/types/phone_number_delete_response.py">PhoneNumberDeleteResponse</a></code>
- <code title="get /phone_numbers/slim">client.phone_numbers.<a href="./src/telnyx/resources/phone_numbers/phone_numbers.py">slim_list</a>(\*\*<a href="src/telnyx/types/phone_number_slim_list_params.py">params</a>) -> <a href="./src/telnyx/types/phone_number_slim_list_response.py">PhoneNumberSlimListResponse</a></code>

## Actions

Types:

```python
from telnyx.types.phone_numbers import (
    PhoneNumberWithVoiceSettings,
    ActionChangeBundleStatusResponse,
    ActionEnableEmergencyResponse,
    ActionVerifyOwnershipResponse,
)
```

Methods:

- <code title="patch /phone_numbers/{id}/actions/bundle_status_change">client.phone_numbers.actions.<a href="./src/telnyx/resources/phone_numbers/actions.py">change_bundle_status</a>(id, \*\*<a href="src/telnyx/types/phone_numbers/action_change_bundle_status_params.py">params</a>) -> <a href="./src/telnyx/types/phone_numbers/action_change_bundle_status_response.py">ActionChangeBundleStatusResponse</a></code>
- <code title="post /phone_numbers/{id}/actions/enable_emergency">client.phone_numbers.actions.<a href="./src/telnyx/resources/phone_numbers/actions.py">enable_emergency</a>(id, \*\*<a href="src/telnyx/types/phone_numbers/action_enable_emergency_params.py">params</a>) -> <a href="./src/telnyx/types/phone_numbers/action_enable_emergency_response.py">ActionEnableEmergencyResponse</a></code>
- <code title="post /phone_numbers/actions/verify_ownership">client.phone_numbers.actions.<a href="./src/telnyx/resources/phone_numbers/actions.py">verify_ownership</a>(\*\*<a href="src/telnyx/types/phone_numbers/action_verify_ownership_params.py">params</a>) -> <a href="./src/telnyx/types/phone_numbers/action_verify_ownership_response.py">ActionVerifyOwnershipResponse</a></code>

## CsvDownloads

Types:

```python
from telnyx.types.phone_numbers import (
    CsvDownload,
    CsvDownloadCreateResponse,
    CsvDownloadRetrieveResponse,
    CsvDownloadListResponse,
)
```

Methods:

- <code title="post /phone_numbers/csv_downloads">client.phone_numbers.csv_downloads.<a href="./src/telnyx/resources/phone_numbers/csv_downloads.py">create</a>(\*\*<a href="src/telnyx/types/phone_numbers/csv_download_create_params.py">params</a>) -> <a href="./src/telnyx/types/phone_numbers/csv_download_create_response.py">CsvDownloadCreateResponse</a></code>
- <code title="get /phone_numbers/csv_downloads/{id}">client.phone_numbers.csv_downloads.<a href="./src/telnyx/resources/phone_numbers/csv_downloads.py">retrieve</a>(id) -> <a href="./src/telnyx/types/phone_numbers/csv_download_retrieve_response.py">CsvDownloadRetrieveResponse</a></code>
- <code title="get /phone_numbers/csv_downloads">client.phone_numbers.csv_downloads.<a href="./src/telnyx/resources/phone_numbers/csv_downloads.py">list</a>(\*\*<a href="src/telnyx/types/phone_numbers/csv_download_list_params.py">params</a>) -> <a href="./src/telnyx/types/phone_numbers/csv_download_list_response.py">CsvDownloadListResponse</a></code>

## Jobs

Types:

```python
from telnyx.types.phone_numbers import (
    PhoneNumbersJob,
    JobRetrieveResponse,
    JobListResponse,
    JobDeleteBatchResponse,
    JobUpdateBatchResponse,
    JobUpdateEmergencySettingsBatchResponse,
)
```

Methods:

- <code title="get /phone_numbers/jobs/{id}">client.phone_numbers.jobs.<a href="./src/telnyx/resources/phone_numbers/jobs.py">retrieve</a>(id) -> <a href="./src/telnyx/types/phone_numbers/job_retrieve_response.py">JobRetrieveResponse</a></code>
- <code title="get /phone_numbers/jobs">client.phone_numbers.jobs.<a href="./src/telnyx/resources/phone_numbers/jobs.py">list</a>(\*\*<a href="src/telnyx/types/phone_numbers/job_list_params.py">params</a>) -> <a href="./src/telnyx/types/phone_numbers/job_list_response.py">JobListResponse</a></code>
- <code title="post /phone_numbers/jobs/delete_phone_numbers">client.phone_numbers.jobs.<a href="./src/telnyx/resources/phone_numbers/jobs.py">delete_batch</a>(\*\*<a href="src/telnyx/types/phone_numbers/job_delete_batch_params.py">params</a>) -> <a href="./src/telnyx/types/phone_numbers/job_delete_batch_response.py">JobDeleteBatchResponse</a></code>
- <code title="post /phone_numbers/jobs/update_phone_numbers">client.phone_numbers.jobs.<a href="./src/telnyx/resources/phone_numbers/jobs.py">update_batch</a>(\*\*<a href="src/telnyx/types/phone_numbers/job_update_batch_params.py">params</a>) -> <a href="./src/telnyx/types/phone_numbers/job_update_batch_response.py">JobUpdateBatchResponse</a></code>
- <code title="post /phone_numbers/jobs/update_emergency_settings">client.phone_numbers.jobs.<a href="./src/telnyx/resources/phone_numbers/jobs.py">update_emergency_settings_batch</a>(\*\*<a href="src/telnyx/types/phone_numbers/job_update_emergency_settings_batch_params.py">params</a>) -> <a href="./src/telnyx/types/phone_numbers/job_update_emergency_settings_batch_response.py">JobUpdateEmergencySettingsBatchResponse</a></code>

## Messaging

Types:

```python
from telnyx.types.phone_numbers import (
    MessagingRetrieveResponse,
    MessagingUpdateResponse,
    MessagingListResponse,
)
```

Methods:

- <code title="get /phone_numbers/{id}/messaging">client.phone_numbers.messaging.<a href="./src/telnyx/resources/phone_numbers/messaging.py">retrieve</a>(id) -> <a href="./src/telnyx/types/phone_numbers/messaging_retrieve_response.py">MessagingRetrieveResponse</a></code>
- <code title="patch /phone_numbers/{id}/messaging">client.phone_numbers.messaging.<a href="./src/telnyx/resources/phone_numbers/messaging.py">update</a>(id, \*\*<a href="src/telnyx/types/phone_numbers/messaging_update_params.py">params</a>) -> <a href="./src/telnyx/types/phone_numbers/messaging_update_response.py">MessagingUpdateResponse</a></code>
- <code title="get /phone_numbers/messaging">client.phone_numbers.messaging.<a href="./src/telnyx/resources/phone_numbers/messaging.py">list</a>(\*\*<a href="src/telnyx/types/phone_numbers/messaging_list_params.py">params</a>) -> <a href="./src/telnyx/types/phone_numbers/messaging_list_response.py">MessagingListResponse</a></code>

## Voice

Types:

```python
from telnyx.types.phone_numbers import (
    CallForwarding,
    CallRecording,
    CnamListing,
    MediaFeatures,
    UpdateVoiceSettings,
    VoiceRetrieveResponse,
    VoiceUpdateResponse,
    VoiceListResponse,
)
```

Methods:

- <code title="get /phone_numbers/{id}/voice">client.phone_numbers.voice.<a href="./src/telnyx/resources/phone_numbers/voice.py">retrieve</a>(id) -> <a href="./src/telnyx/types/phone_numbers/voice_retrieve_response.py">VoiceRetrieveResponse</a></code>
- <code title="patch /phone_numbers/{id}/voice">client.phone_numbers.voice.<a href="./src/telnyx/resources/phone_numbers/voice.py">update</a>(id, \*\*<a href="src/telnyx/types/phone_numbers/voice_update_params.py">params</a>) -> <a href="./src/telnyx/types/phone_numbers/voice_update_response.py">VoiceUpdateResponse</a></code>
- <code title="get /phone_numbers/voice">client.phone_numbers.voice.<a href="./src/telnyx/resources/phone_numbers/voice.py">list</a>(\*\*<a href="src/telnyx/types/phone_numbers/voice_list_params.py">params</a>) -> <a href="./src/telnyx/types/phone_numbers/voice_list_response.py">VoiceListResponse</a></code>

## Voicemail

Types:

```python
from telnyx.types.phone_numbers import (
    VoicemailPrefResponse,
    VoicemailRequest,
    VoicemailCreateResponse,
    VoicemailRetrieveResponse,
    VoicemailUpdateResponse,
)
```

Methods:

- <code title="post /phone_numbers/{phone_number_id}/voicemail">client.phone_numbers.voicemail.<a href="./src/telnyx/resources/phone_numbers/voicemail.py">create</a>(phone_number_id, \*\*<a href="src/telnyx/types/phone_numbers/voicemail_create_params.py">params</a>) -> <a href="./src/telnyx/types/phone_numbers/voicemail_create_response.py">VoicemailCreateResponse</a></code>
- <code title="get /phone_numbers/{phone_number_id}/voicemail">client.phone_numbers.voicemail.<a href="./src/telnyx/resources/phone_numbers/voicemail.py">retrieve</a>(phone_number_id) -> <a href="./src/telnyx/types/phone_numbers/voicemail_retrieve_response.py">VoicemailRetrieveResponse</a></code>
- <code title="patch /phone_numbers/{phone_number_id}/voicemail">client.phone_numbers.voicemail.<a href="./src/telnyx/resources/phone_numbers/voicemail.py">update</a>(phone_number_id, \*\*<a href="src/telnyx/types/phone_numbers/voicemail_update_params.py">params</a>) -> <a href="./src/telnyx/types/phone_numbers/voicemail_update_response.py">VoicemailUpdateResponse</a></code>

# PhoneNumbersRegulatoryRequirements

Types:

```python
from telnyx.types import PhoneNumbersRegulatoryRequirementRetrieveResponse
```

Methods:

- <code title="get /phone_numbers_regulatory_requirements">client.phone_numbers_regulatory_requirements.<a href="./src/telnyx/resources/phone_numbers_regulatory_requirements.py">retrieve</a>(\*\*<a href="src/telnyx/types/phone_numbers_regulatory_requirement_retrieve_params.py">params</a>) -> <a href="./src/telnyx/types/phone_numbers_regulatory_requirement_retrieve_response.py">PhoneNumbersRegulatoryRequirementRetrieveResponse</a></code>

# PortabilityChecks

Types:

```python
from telnyx.types import PortabilityCheckRunResponse
```

Methods:

- <code title="post /portability_checks">client.portability_checks.<a href="./src/telnyx/resources/portability_checks.py">run</a>(\*\*<a href="src/telnyx/types/portability_check_run_params.py">params</a>) -> <a href="./src/telnyx/types/portability_check_run_response.py">PortabilityCheckRunResponse</a></code>

# Porting

Types:

```python
from telnyx.types import PortingListUkCarriersResponse
```

Methods:

- <code title="get /porting/uk_carriers">client.porting.<a href="./src/telnyx/resources/porting/porting.py">list_uk_carriers</a>() -> <a href="./src/telnyx/types/porting_list_uk_carriers_response.py">PortingListUkCarriersResponse</a></code>

## Events

Types:

```python
from telnyx.types.porting import EventRetrieveResponse, EventListResponse
```

Methods:

- <code title="get /porting/events/{id}">client.porting.events.<a href="./src/telnyx/resources/porting/events.py">retrieve</a>(id) -> <a href="./src/telnyx/types/porting/event_retrieve_response.py">EventRetrieveResponse</a></code>
- <code title="get /porting/events">client.porting.events.<a href="./src/telnyx/resources/porting/events.py">list</a>(\*\*<a href="src/telnyx/types/porting/event_list_params.py">params</a>) -> <a href="./src/telnyx/types/porting/event_list_response.py">EventListResponse</a></code>
- <code title="post /porting/events/{id}/republish">client.porting.events.<a href="./src/telnyx/resources/porting/events.py">republish</a>(id) -> None</code>

## Reports

Types:

```python
from telnyx.types.porting import (
    ExportPortingOrdersCsvReport,
    PortingReport,
    ReportCreateResponse,
    ReportRetrieveResponse,
    ReportListResponse,
)
```

Methods:

- <code title="post /porting/reports">client.porting.reports.<a href="./src/telnyx/resources/porting/reports.py">create</a>(\*\*<a href="src/telnyx/types/porting/report_create_params.py">params</a>) -> <a href="./src/telnyx/types/porting/report_create_response.py">ReportCreateResponse</a></code>
- <code title="get /porting/reports/{id}">client.porting.reports.<a href="./src/telnyx/resources/porting/reports.py">retrieve</a>(id) -> <a href="./src/telnyx/types/porting/report_retrieve_response.py">ReportRetrieveResponse</a></code>
- <code title="get /porting/reports">client.porting.reports.<a href="./src/telnyx/resources/porting/reports.py">list</a>(\*\*<a href="src/telnyx/types/porting/report_list_params.py">params</a>) -> <a href="./src/telnyx/types/porting/report_list_response.py">ReportListResponse</a></code>

## LoaConfigurations

Types:

```python
from telnyx.types.porting import (
    PortingLoaConfiguration,
    LoaConfigurationCreateResponse,
    LoaConfigurationRetrieveResponse,
    LoaConfigurationUpdateResponse,
    LoaConfigurationListResponse,
)
```

Methods:

- <code title="post /porting/loa_configurations">client.porting.loa_configurations.<a href="./src/telnyx/resources/porting/loa_configurations.py">create</a>(\*\*<a href="src/telnyx/types/porting/loa_configuration_create_params.py">params</a>) -> <a href="./src/telnyx/types/porting/loa_configuration_create_response.py">LoaConfigurationCreateResponse</a></code>
- <code title="get /porting/loa_configurations/{id}">client.porting.loa_configurations.<a href="./src/telnyx/resources/porting/loa_configurations.py">retrieve</a>(id) -> <a href="./src/telnyx/types/porting/loa_configuration_retrieve_response.py">LoaConfigurationRetrieveResponse</a></code>
- <code title="patch /porting/loa_configurations/{id}">client.porting.loa_configurations.<a href="./src/telnyx/resources/porting/loa_configurations.py">update</a>(id, \*\*<a href="src/telnyx/types/porting/loa_configuration_update_params.py">params</a>) -> <a href="./src/telnyx/types/porting/loa_configuration_update_response.py">LoaConfigurationUpdateResponse</a></code>
- <code title="get /porting/loa_configurations">client.porting.loa_configurations.<a href="./src/telnyx/resources/porting/loa_configurations.py">list</a>(\*\*<a href="src/telnyx/types/porting/loa_configuration_list_params.py">params</a>) -> <a href="./src/telnyx/types/porting/loa_configuration_list_response.py">LoaConfigurationListResponse</a></code>
- <code title="delete /porting/loa_configurations/{id}">client.porting.loa_configurations.<a href="./src/telnyx/resources/porting/loa_configurations.py">delete</a>(id) -> None</code>
- <code title="post /porting/loa_configuration/preview">client.porting.loa_configurations.<a href="./src/telnyx/resources/porting/loa_configurations.py">preview_0</a>(\*\*<a href="src/telnyx/types/porting/loa_configuration_preview_0_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /porting/loa_configurations/{id}/preview">client.porting.loa_configurations.<a href="./src/telnyx/resources/porting/loa_configurations.py">preview_1</a>(id) -> BinaryAPIResponse</code>

# PortingOrders

Types:

```python
from telnyx.types import (
    PortingOrder,
    PortingOrderActivationSettings,
    PortingOrderDocuments,
    PortingOrderEndUser,
    PortingOrderEndUserAdmin,
    PortingOrderEndUserLocation,
    PortingOrderMessaging,
    PortingOrderMisc,
    PortingOrderPhoneNumberConfiguration,
    PortingOrderRequirement,
    PortingOrderType,
    PortingOrderUserFeedback,
    PortingOrdersActivationJob,
    PortingOrderCreateResponse,
    PortingOrderRetrieveResponse,
    PortingOrderUpdateResponse,
    PortingOrderListResponse,
    PortingOrderRetrieveAllowedFocWindowsResponse,
    PortingOrderRetrieveExceptionTypesResponse,
    PortingOrderRetrieveRequirementsResponse,
    PortingOrderRetrieveSubRequestResponse,
)
```

Methods:

- <code title="post /porting_orders">client.porting_orders.<a href="./src/telnyx/resources/porting_orders/porting_orders.py">create</a>(\*\*<a href="src/telnyx/types/porting_order_create_params.py">params</a>) -> <a href="./src/telnyx/types/porting_order_create_response.py">PortingOrderCreateResponse</a></code>
- <code title="get /porting_orders/{id}">client.porting_orders.<a href="./src/telnyx/resources/porting_orders/porting_orders.py">retrieve</a>(id, \*\*<a href="src/telnyx/types/porting_order_retrieve_params.py">params</a>) -> <a href="./src/telnyx/types/porting_order_retrieve_response.py">PortingOrderRetrieveResponse</a></code>
- <code title="patch /porting_orders/{id}">client.porting_orders.<a href="./src/telnyx/resources/porting_orders/porting_orders.py">update</a>(id, \*\*<a href="src/telnyx/types/porting_order_update_params.py">params</a>) -> <a href="./src/telnyx/types/porting_order_update_response.py">PortingOrderUpdateResponse</a></code>
- <code title="get /porting_orders">client.porting_orders.<a href="./src/telnyx/resources/porting_orders/porting_orders.py">list</a>(\*\*<a href="src/telnyx/types/porting_order_list_params.py">params</a>) -> <a href="./src/telnyx/types/porting_order_list_response.py">PortingOrderListResponse</a></code>
- <code title="delete /porting_orders/{id}">client.porting_orders.<a href="./src/telnyx/resources/porting_orders/porting_orders.py">delete</a>(id) -> None</code>
- <code title="get /porting_orders/{id}/allowed_foc_windows">client.porting_orders.<a href="./src/telnyx/resources/porting_orders/porting_orders.py">retrieve_allowed_foc_windows</a>(id) -> <a href="./src/telnyx/types/porting_order_retrieve_allowed_foc_windows_response.py">PortingOrderRetrieveAllowedFocWindowsResponse</a></code>
- <code title="get /porting_orders/exception_types">client.porting_orders.<a href="./src/telnyx/resources/porting_orders/porting_orders.py">retrieve_exception_types</a>() -> <a href="./src/telnyx/types/porting_order_retrieve_exception_types_response.py">PortingOrderRetrieveExceptionTypesResponse</a></code>
- <code title="get /porting_orders/{id}/loa_template">client.porting_orders.<a href="./src/telnyx/resources/porting_orders/porting_orders.py">retrieve_loa_template</a>(id, \*\*<a href="src/telnyx/types/porting_order_retrieve_loa_template_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /porting_orders/{id}/requirements">client.porting_orders.<a href="./src/telnyx/resources/porting_orders/porting_orders.py">retrieve_requirements</a>(id, \*\*<a href="src/telnyx/types/porting_order_retrieve_requirements_params.py">params</a>) -> <a href="./src/telnyx/types/porting_order_retrieve_requirements_response.py">PortingOrderRetrieveRequirementsResponse</a></code>
- <code title="get /porting_orders/{id}/sub_request">client.porting_orders.<a href="./src/telnyx/resources/porting_orders/porting_orders.py">retrieve_sub_request</a>(id) -> <a href="./src/telnyx/types/porting_order_retrieve_sub_request_response.py">PortingOrderRetrieveSubRequestResponse</a></code>

## PhoneNumberConfigurations

Types:

```python
from telnyx.types.porting_orders import (
    PhoneNumberConfigurationCreateResponse,
    PhoneNumberConfigurationListResponse,
)
```

Methods:

- <code title="post /porting_orders/phone_number_configurations">client.porting_orders.phone_number_configurations.<a href="./src/telnyx/resources/porting_orders/phone_number_configurations.py">create</a>(\*\*<a href="src/telnyx/types/porting_orders/phone_number_configuration_create_params.py">params</a>) -> <a href="./src/telnyx/types/porting_orders/phone_number_configuration_create_response.py">PhoneNumberConfigurationCreateResponse</a></code>
- <code title="get /porting_orders/phone_number_configurations">client.porting_orders.phone_number_configurations.<a href="./src/telnyx/resources/porting_orders/phone_number_configurations.py">list</a>(\*\*<a href="src/telnyx/types/porting_orders/phone_number_configuration_list_params.py">params</a>) -> <a href="./src/telnyx/types/porting_orders/phone_number_configuration_list_response.py">PhoneNumberConfigurationListResponse</a></code>

## Actions

Types:

```python
from telnyx.types.porting_orders import (
    ActionActivateResponse,
    ActionCancelResponse,
    ActionConfirmResponse,
    ActionShareResponse,
)
```

Methods:

- <code title="post /porting_orders/{id}/actions/activate">client.porting_orders.actions.<a href="./src/telnyx/resources/porting_orders/actions.py">activate</a>(id) -> <a href="./src/telnyx/types/porting_orders/action_activate_response.py">ActionActivateResponse</a></code>
- <code title="post /porting_orders/{id}/actions/cancel">client.porting_orders.actions.<a href="./src/telnyx/resources/porting_orders/actions.py">cancel</a>(id) -> <a href="./src/telnyx/types/porting_orders/action_cancel_response.py">ActionCancelResponse</a></code>
- <code title="post /porting_orders/{id}/actions/confirm">client.porting_orders.actions.<a href="./src/telnyx/resources/porting_orders/actions.py">confirm</a>(id) -> <a href="./src/telnyx/types/porting_orders/action_confirm_response.py">ActionConfirmResponse</a></code>
- <code title="post /porting_orders/{id}/actions/share">client.porting_orders.actions.<a href="./src/telnyx/resources/porting_orders/actions.py">share</a>(id, \*\*<a href="src/telnyx/types/porting_orders/action_share_params.py">params</a>) -> <a href="./src/telnyx/types/porting_orders/action_share_response.py">ActionShareResponse</a></code>

## ActivationJobs

Types:

```python
from telnyx.types.porting_orders import (
    ActivationJobRetrieveResponse,
    ActivationJobUpdateResponse,
    ActivationJobListResponse,
)
```

Methods:

- <code title="get /porting_orders/{id}/activation_jobs/{activationJobId}">client.porting_orders.activation_jobs.<a href="./src/telnyx/resources/porting_orders/activation_jobs.py">retrieve</a>(activation_job_id, \*, id) -> <a href="./src/telnyx/types/porting_orders/activation_job_retrieve_response.py">ActivationJobRetrieveResponse</a></code>
- <code title="patch /porting_orders/{id}/activation_jobs/{activationJobId}">client.porting_orders.activation_jobs.<a href="./src/telnyx/resources/porting_orders/activation_jobs.py">update</a>(activation_job_id, \*, id, \*\*<a href="src/telnyx/types/porting_orders/activation_job_update_params.py">params</a>) -> <a href="./src/telnyx/types/porting_orders/activation_job_update_response.py">ActivationJobUpdateResponse</a></code>
- <code title="get /porting_orders/{id}/activation_jobs">client.porting_orders.activation_jobs.<a href="./src/telnyx/resources/porting_orders/activation_jobs.py">list</a>(id, \*\*<a href="src/telnyx/types/porting_orders/activation_job_list_params.py">params</a>) -> <a href="./src/telnyx/types/porting_orders/activation_job_list_response.py">ActivationJobListResponse</a></code>

## AdditionalDocuments

Types:

```python
from telnyx.types.porting_orders import (
    AdditionalDocumentCreateResponse,
    AdditionalDocumentListResponse,
)
```

Methods:

- <code title="post /porting_orders/{id}/additional_documents">client.porting_orders.additional_documents.<a href="./src/telnyx/resources/porting_orders/additional_documents.py">create</a>(id, \*\*<a href="src/telnyx/types/porting_orders/additional_document_create_params.py">params</a>) -> <a href="./src/telnyx/types/porting_orders/additional_document_create_response.py">AdditionalDocumentCreateResponse</a></code>
- <code title="get /porting_orders/{id}/additional_documents">client.porting_orders.additional_documents.<a href="./src/telnyx/resources/porting_orders/additional_documents.py">list</a>(id, \*\*<a href="src/telnyx/types/porting_orders/additional_document_list_params.py">params</a>) -> <a href="./src/telnyx/types/porting_orders/additional_document_list_response.py">AdditionalDocumentListResponse</a></code>
- <code title="delete /porting_orders/{id}/additional_documents/{additional_document_id}">client.porting_orders.additional_documents.<a href="./src/telnyx/resources/porting_orders/additional_documents.py">delete</a>(additional_document_id, \*, id) -> None</code>

## Comments

Types:

```python
from telnyx.types.porting_orders import CommentCreateResponse, CommentListResponse
```

Methods:

- <code title="post /porting_orders/{id}/comments">client.porting_orders.comments.<a href="./src/telnyx/resources/porting_orders/comments.py">create</a>(id, \*\*<a href="src/telnyx/types/porting_orders/comment_create_params.py">params</a>) -> <a href="./src/telnyx/types/porting_orders/comment_create_response.py">CommentCreateResponse</a></code>
- <code title="get /porting_orders/{id}/comments">client.porting_orders.comments.<a href="./src/telnyx/resources/porting_orders/comments.py">list</a>(id, \*\*<a href="src/telnyx/types/porting_orders/comment_list_params.py">params</a>) -> <a href="./src/telnyx/types/porting_orders/comment_list_response.py">CommentListResponse</a></code>

## VerificationCodes

Types:

```python
from telnyx.types.porting_orders import VerificationCodeListResponse, VerificationCodeVerifyResponse
```

Methods:

- <code title="get /porting_orders/{id}/verification_codes">client.porting_orders.verification_codes.<a href="./src/telnyx/resources/porting_orders/verification_codes.py">list</a>(id, \*\*<a href="src/telnyx/types/porting_orders/verification_code_list_params.py">params</a>) -> <a href="./src/telnyx/types/porting_orders/verification_code_list_response.py">VerificationCodeListResponse</a></code>
- <code title="post /porting_orders/{id}/verification_codes/send">client.porting_orders.verification_codes.<a href="./src/telnyx/resources/porting_orders/verification_codes.py">send</a>(id, \*\*<a href="src/telnyx/types/porting_orders/verification_code_send_params.py">params</a>) -> None</code>
- <code title="post /porting_orders/{id}/verification_codes/verify">client.porting_orders.verification_codes.<a href="./src/telnyx/resources/porting_orders/verification_codes.py">verify</a>(id, \*\*<a href="src/telnyx/types/porting_orders/verification_code_verify_params.py">params</a>) -> <a href="./src/telnyx/types/porting_orders/verification_code_verify_response.py">VerificationCodeVerifyResponse</a></code>

## ActionRequirements

Types:

```python
from telnyx.types.porting_orders import (
    ActionRequirementListResponse,
    ActionRequirementInitiateResponse,
)
```

Methods:

- <code title="get /porting_orders/{porting_order_id}/action_requirements">client.porting_orders.action_requirements.<a href="./src/telnyx/resources/porting_orders/action_requirements.py">list</a>(porting_order_id, \*\*<a href="src/telnyx/types/porting_orders/action_requirement_list_params.py">params</a>) -> <a href="./src/telnyx/types/porting_orders/action_requirement_list_response.py">ActionRequirementListResponse</a></code>
- <code title="post /porting_orders/{porting_order_id}/action_requirements/{id}/initiate">client.porting_orders.action_requirements.<a href="./src/telnyx/resources/porting_orders/action_requirements.py">initiate</a>(id, \*, porting_order_id, \*\*<a href="src/telnyx/types/porting_orders/action_requirement_initiate_params.py">params</a>) -> <a href="./src/telnyx/types/porting_orders/action_requirement_initiate_response.py">ActionRequirementInitiateResponse</a></code>

## AssociatedPhoneNumbers

Types:

```python
from telnyx.types.porting_orders import (
    PortingAssociatedPhoneNumber,
    AssociatedPhoneNumberCreateResponse,
    AssociatedPhoneNumberListResponse,
    AssociatedPhoneNumberDeleteResponse,
)
```

Methods:

- <code title="post /porting_orders/{porting_order_id}/associated_phone_numbers">client.porting_orders.associated_phone_numbers.<a href="./src/telnyx/resources/porting_orders/associated_phone_numbers.py">create</a>(porting_order_id, \*\*<a href="src/telnyx/types/porting_orders/associated_phone_number_create_params.py">params</a>) -> <a href="./src/telnyx/types/porting_orders/associated_phone_number_create_response.py">AssociatedPhoneNumberCreateResponse</a></code>
- <code title="get /porting_orders/{porting_order_id}/associated_phone_numbers">client.porting_orders.associated_phone_numbers.<a href="./src/telnyx/resources/porting_orders/associated_phone_numbers.py">list</a>(porting_order_id, \*\*<a href="src/telnyx/types/porting_orders/associated_phone_number_list_params.py">params</a>) -> <a href="./src/telnyx/types/porting_orders/associated_phone_number_list_response.py">AssociatedPhoneNumberListResponse</a></code>
- <code title="delete /porting_orders/{porting_order_id}/associated_phone_numbers/{id}">client.porting_orders.associated_phone_numbers.<a href="./src/telnyx/resources/porting_orders/associated_phone_numbers.py">delete</a>(id, \*, porting_order_id) -> <a href="./src/telnyx/types/porting_orders/associated_phone_number_delete_response.py">AssociatedPhoneNumberDeleteResponse</a></code>

## PhoneNumberBlocks

Types:

```python
from telnyx.types.porting_orders import (
    PortingPhoneNumberBlock,
    PhoneNumberBlockCreateResponse,
    PhoneNumberBlockListResponse,
    PhoneNumberBlockDeleteResponse,
)
```

Methods:

- <code title="post /porting_orders/{porting_order_id}/phone_number_blocks">client.porting_orders.phone_number_blocks.<a href="./src/telnyx/resources/porting_orders/phone_number_blocks.py">create</a>(porting_order_id, \*\*<a href="src/telnyx/types/porting_orders/phone_number_block_create_params.py">params</a>) -> <a href="./src/telnyx/types/porting_orders/phone_number_block_create_response.py">PhoneNumberBlockCreateResponse</a></code>
- <code title="get /porting_orders/{porting_order_id}/phone_number_blocks">client.porting_orders.phone_number_blocks.<a href="./src/telnyx/resources/porting_orders/phone_number_blocks.py">list</a>(porting_order_id, \*\*<a href="src/telnyx/types/porting_orders/phone_number_block_list_params.py">params</a>) -> <a href="./src/telnyx/types/porting_orders/phone_number_block_list_response.py">PhoneNumberBlockListResponse</a></code>
- <code title="delete /porting_orders/{porting_order_id}/phone_number_blocks/{id}">client.porting_orders.phone_number_blocks.<a href="./src/telnyx/resources/porting_orders/phone_number_blocks.py">delete</a>(id, \*, porting_order_id) -> <a href="./src/telnyx/types/porting_orders/phone_number_block_delete_response.py">PhoneNumberBlockDeleteResponse</a></code>

## PhoneNumberExtensions

Types:

```python
from telnyx.types.porting_orders import (
    PortingPhoneNumberExtension,
    PhoneNumberExtensionCreateResponse,
    PhoneNumberExtensionListResponse,
    PhoneNumberExtensionDeleteResponse,
)
```

Methods:

- <code title="post /porting_orders/{porting_order_id}/phone_number_extensions">client.porting_orders.phone_number_extensions.<a href="./src/telnyx/resources/porting_orders/phone_number_extensions.py">create</a>(porting_order_id, \*\*<a href="src/telnyx/types/porting_orders/phone_number_extension_create_params.py">params</a>) -> <a href="./src/telnyx/types/porting_orders/phone_number_extension_create_response.py">PhoneNumberExtensionCreateResponse</a></code>
- <code title="get /porting_orders/{porting_order_id}/phone_number_extensions">client.porting_orders.phone_number_extensions.<a href="./src/telnyx/resources/porting_orders/phone_number_extensions.py">list</a>(porting_order_id, \*\*<a href="src/telnyx/types/porting_orders/phone_number_extension_list_params.py">params</a>) -> <a href="./src/telnyx/types/porting_orders/phone_number_extension_list_response.py">PhoneNumberExtensionListResponse</a></code>
- <code title="delete /porting_orders/{porting_order_id}/phone_number_extensions/{id}">client.porting_orders.phone_number_extensions.<a href="./src/telnyx/resources/porting_orders/phone_number_extensions.py">delete</a>(id, \*, porting_order_id) -> <a href="./src/telnyx/types/porting_orders/phone_number_extension_delete_response.py">PhoneNumberExtensionDeleteResponse</a></code>

# PortingPhoneNumbers

Types:

```python
from telnyx.types import PortingPhoneNumberListResponse
```

Methods:

- <code title="get /porting_phone_numbers">client.porting_phone_numbers.<a href="./src/telnyx/resources/porting_phone_numbers.py">list</a>(\*\*<a href="src/telnyx/types/porting_phone_number_list_params.py">params</a>) -> <a href="./src/telnyx/types/porting_phone_number_list_response.py">PortingPhoneNumberListResponse</a></code>

# Portouts

Types:

```python
from telnyx.types import (
    PortoutDetails,
    PortoutRetrieveResponse,
    PortoutListResponse,
    PortoutListRejectionCodesResponse,
    PortoutUpdateStatusResponse,
)
```

Methods:

- <code title="get /portouts/{id}">client.portouts.<a href="./src/telnyx/resources/portouts/portouts.py">retrieve</a>(id) -> <a href="./src/telnyx/types/portout_retrieve_response.py">PortoutRetrieveResponse</a></code>
- <code title="get /portouts">client.portouts.<a href="./src/telnyx/resources/portouts/portouts.py">list</a>(\*\*<a href="src/telnyx/types/portout_list_params.py">params</a>) -> <a href="./src/telnyx/types/portout_list_response.py">PortoutListResponse</a></code>
- <code title="get /portouts/rejections/{portout_id}">client.portouts.<a href="./src/telnyx/resources/portouts/portouts.py">list_rejection_codes</a>(portout_id, \*\*<a href="src/telnyx/types/portout_list_rejection_codes_params.py">params</a>) -> <a href="./src/telnyx/types/portout_list_rejection_codes_response.py">PortoutListRejectionCodesResponse</a></code>
- <code title="patch /portouts/{id}/{status}">client.portouts.<a href="./src/telnyx/resources/portouts/portouts.py">update_status</a>(status, \*, id, \*\*<a href="src/telnyx/types/portout_update_status_params.py">params</a>) -> <a href="./src/telnyx/types/portout_update_status_response.py">PortoutUpdateStatusResponse</a></code>

## Events

Types:

```python
from telnyx.types.portouts import EventRetrieveResponse, EventListResponse
```

Methods:

- <code title="get /portouts/events/{id}">client.portouts.events.<a href="./src/telnyx/resources/portouts/events.py">retrieve</a>(id) -> <a href="./src/telnyx/types/portouts/event_retrieve_response.py">EventRetrieveResponse</a></code>
- <code title="get /portouts/events">client.portouts.events.<a href="./src/telnyx/resources/portouts/events.py">list</a>(\*\*<a href="src/telnyx/types/portouts/event_list_params.py">params</a>) -> <a href="./src/telnyx/types/portouts/event_list_response.py">EventListResponse</a></code>
- <code title="post /portouts/events/{id}/republish">client.portouts.events.<a href="./src/telnyx/resources/portouts/events.py">republish</a>(id) -> None</code>

## Reports

Types:

```python
from telnyx.types.portouts import (
    ExportPortoutsCsvReport,
    PortoutReport,
    ReportCreateResponse,
    ReportRetrieveResponse,
    ReportListResponse,
)
```

Methods:

- <code title="post /portouts/reports">client.portouts.reports.<a href="./src/telnyx/resources/portouts/reports.py">create</a>(\*\*<a href="src/telnyx/types/portouts/report_create_params.py">params</a>) -> <a href="./src/telnyx/types/portouts/report_create_response.py">ReportCreateResponse</a></code>
- <code title="get /portouts/reports/{id}">client.portouts.reports.<a href="./src/telnyx/resources/portouts/reports.py">retrieve</a>(id) -> <a href="./src/telnyx/types/portouts/report_retrieve_response.py">ReportRetrieveResponse</a></code>
- <code title="get /portouts/reports">client.portouts.reports.<a href="./src/telnyx/resources/portouts/reports.py">list</a>(\*\*<a href="src/telnyx/types/portouts/report_list_params.py">params</a>) -> <a href="./src/telnyx/types/portouts/report_list_response.py">ReportListResponse</a></code>

## Comments

Types:

```python
from telnyx.types.portouts import CommentCreateResponse, CommentListResponse
```

Methods:

- <code title="post /portouts/{id}/comments">client.portouts.comments.<a href="./src/telnyx/resources/portouts/comments.py">create</a>(id, \*\*<a href="src/telnyx/types/portouts/comment_create_params.py">params</a>) -> <a href="./src/telnyx/types/portouts/comment_create_response.py">CommentCreateResponse</a></code>
- <code title="get /portouts/{id}/comments">client.portouts.comments.<a href="./src/telnyx/resources/portouts/comments.py">list</a>(id) -> <a href="./src/telnyx/types/portouts/comment_list_response.py">CommentListResponse</a></code>

## SupportingDocuments

Types:

```python
from telnyx.types.portouts import SupportingDocumentCreateResponse, SupportingDocumentListResponse
```

Methods:

- <code title="post /portouts/{id}/supporting_documents">client.portouts.supporting_documents.<a href="./src/telnyx/resources/portouts/supporting_documents.py">create</a>(id, \*\*<a href="src/telnyx/types/portouts/supporting_document_create_params.py">params</a>) -> <a href="./src/telnyx/types/portouts/supporting_document_create_response.py">SupportingDocumentCreateResponse</a></code>
- <code title="get /portouts/{id}/supporting_documents">client.portouts.supporting_documents.<a href="./src/telnyx/resources/portouts/supporting_documents.py">list</a>(id) -> <a href="./src/telnyx/types/portouts/supporting_document_list_response.py">SupportingDocumentListResponse</a></code>

# PrivateWirelessGateways

Types:

```python
from telnyx.types import (
    PrivateWirelessGateway,
    PrivateWirelessGatewayStatus,
    PwgAssignedResourcesSummary,
    PrivateWirelessGatewayCreateResponse,
    PrivateWirelessGatewayRetrieveResponse,
    PrivateWirelessGatewayListResponse,
    PrivateWirelessGatewayDeleteResponse,
)
```

Methods:

- <code title="post /private_wireless_gateways">client.private_wireless_gateways.<a href="./src/telnyx/resources/private_wireless_gateways.py">create</a>(\*\*<a href="src/telnyx/types/private_wireless_gateway_create_params.py">params</a>) -> <a href="./src/telnyx/types/private_wireless_gateway_create_response.py">PrivateWirelessGatewayCreateResponse</a></code>
- <code title="get /private_wireless_gateways/{id}">client.private_wireless_gateways.<a href="./src/telnyx/resources/private_wireless_gateways.py">retrieve</a>(id) -> <a href="./src/telnyx/types/private_wireless_gateway_retrieve_response.py">PrivateWirelessGatewayRetrieveResponse</a></code>
- <code title="get /private_wireless_gateways">client.private_wireless_gateways.<a href="./src/telnyx/resources/private_wireless_gateways.py">list</a>(\*\*<a href="src/telnyx/types/private_wireless_gateway_list_params.py">params</a>) -> <a href="./src/telnyx/types/private_wireless_gateway_list_response.py">PrivateWirelessGatewayListResponse</a></code>
- <code title="delete /private_wireless_gateways/{id}">client.private_wireless_gateways.<a href="./src/telnyx/resources/private_wireless_gateways.py">delete</a>(id) -> <a href="./src/telnyx/types/private_wireless_gateway_delete_response.py">PrivateWirelessGatewayDeleteResponse</a></code>

# PublicInternetGateways

Types:

```python
from telnyx.types import (
    Interface,
    RegionIn,
    PublicInternetGatewayCreateResponse,
    PublicInternetGatewayRetrieveResponse,
    PublicInternetGatewayListResponse,
    PublicInternetGatewayDeleteResponse,
)
```

Methods:

- <code title="post /public_internet_gateways">client.public_internet_gateways.<a href="./src/telnyx/resources/public_internet_gateways.py">create</a>(\*\*<a href="src/telnyx/types/public_internet_gateway_create_params.py">params</a>) -> <a href="./src/telnyx/types/public_internet_gateway_create_response.py">PublicInternetGatewayCreateResponse</a></code>
- <code title="get /public_internet_gateways/{id}">client.public_internet_gateways.<a href="./src/telnyx/resources/public_internet_gateways.py">retrieve</a>(id) -> <a href="./src/telnyx/types/public_internet_gateway_retrieve_response.py">PublicInternetGatewayRetrieveResponse</a></code>
- <code title="get /public_internet_gateways">client.public_internet_gateways.<a href="./src/telnyx/resources/public_internet_gateways.py">list</a>(\*\*<a href="src/telnyx/types/public_internet_gateway_list_params.py">params</a>) -> <a href="./src/telnyx/types/public_internet_gateway_list_response.py">PublicInternetGatewayListResponse</a></code>
- <code title="delete /public_internet_gateways/{id}">client.public_internet_gateways.<a href="./src/telnyx/resources/public_internet_gateways.py">delete</a>(id) -> <a href="./src/telnyx/types/public_internet_gateway_delete_response.py">PublicInternetGatewayDeleteResponse</a></code>

# Queues

Types:

```python
from telnyx.types import QueueRetrieveResponse
```

Methods:

- <code title="get /queues/{queue_name}">client.queues.<a href="./src/telnyx/resources/queues/queues.py">retrieve</a>(queue_name) -> <a href="./src/telnyx/types/queue_retrieve_response.py">QueueRetrieveResponse</a></code>

## Calls

Types:

```python
from telnyx.types.queues import CallRetrieveResponse, CallListResponse
```

Methods:

- <code title="get /queues/{queue_name}/calls/{call_control_id}">client.queues.calls.<a href="./src/telnyx/resources/queues/calls.py">retrieve</a>(call_control_id, \*, queue_name) -> <a href="./src/telnyx/types/queues/call_retrieve_response.py">CallRetrieveResponse</a></code>
- <code title="get /queues/{queue_name}/calls">client.queues.calls.<a href="./src/telnyx/resources/queues/calls.py">list</a>(queue_name, \*\*<a href="src/telnyx/types/queues/call_list_params.py">params</a>) -> <a href="./src/telnyx/types/queues/call_list_response.py">CallListResponse</a></code>

# RcsAgents

Types:

```python
from telnyx.types import RcsAgent, RcsAgentResponse, RcsAgentListResponse
```

Methods:

- <code title="get /rcs_agents/{id}">client.rcs_agents.<a href="./src/telnyx/resources/rcs_agents.py">retrieve</a>(id) -> <a href="./src/telnyx/types/rcs_agent_response.py">RcsAgentResponse</a></code>
- <code title="patch /rcs_agents/{id}">client.rcs_agents.<a href="./src/telnyx/resources/rcs_agents.py">update</a>(id, \*\*<a href="src/telnyx/types/rcs_agent_update_params.py">params</a>) -> <a href="./src/telnyx/types/rcs_agent_response.py">RcsAgentResponse</a></code>
- <code title="get /rcs_agents">client.rcs_agents.<a href="./src/telnyx/resources/rcs_agents.py">list</a>(\*\*<a href="src/telnyx/types/rcs_agent_list_params.py">params</a>) -> <a href="./src/telnyx/types/rcs_agent_list_response.py">RcsAgentListResponse</a></code>

# RecordingTranscriptions

Types:

```python
from telnyx.types import (
    RecordingTranscription,
    RecordingTranscriptionRetrieveResponse,
    RecordingTranscriptionListResponse,
    RecordingTranscriptionDeleteResponse,
)
```

Methods:

- <code title="get /recording_transcriptions/{recording_transcription_id}">client.recording_transcriptions.<a href="./src/telnyx/resources/recording_transcriptions.py">retrieve</a>(recording_transcription_id) -> <a href="./src/telnyx/types/recording_transcription_retrieve_response.py">RecordingTranscriptionRetrieveResponse</a></code>
- <code title="get /recording_transcriptions">client.recording_transcriptions.<a href="./src/telnyx/resources/recording_transcriptions.py">list</a>() -> <a href="./src/telnyx/types/recording_transcription_list_response.py">RecordingTranscriptionListResponse</a></code>
- <code title="delete /recording_transcriptions/{recording_transcription_id}">client.recording_transcriptions.<a href="./src/telnyx/resources/recording_transcriptions.py">delete</a>(recording_transcription_id) -> <a href="./src/telnyx/types/recording_transcription_delete_response.py">RecordingTranscriptionDeleteResponse</a></code>

# Recordings

Types:

```python
from telnyx.types import (
    RecordingResponseData,
    RecordingRetrieveResponse,
    RecordingListResponse,
    RecordingDeleteResponse,
)
```

Methods:

- <code title="get /recordings/{recording_id}">client.recordings.<a href="./src/telnyx/resources/recordings.py">retrieve</a>(recording_id) -> <a href="./src/telnyx/types/recording_retrieve_response.py">RecordingRetrieveResponse</a></code>
- <code title="get /recordings">client.recordings.<a href="./src/telnyx/resources/recordings.py">list</a>(\*\*<a href="src/telnyx/types/recording_list_params.py">params</a>) -> <a href="./src/telnyx/types/recording_list_response.py">RecordingListResponse</a></code>
- <code title="delete /recordings/{recording_id}">client.recordings.<a href="./src/telnyx/resources/recordings.py">delete</a>(recording_id) -> <a href="./src/telnyx/types/recording_delete_response.py">RecordingDeleteResponse</a></code>

# Regions

Types:

```python
from telnyx.types import RegionListResponse
```

Methods:

- <code title="get /regions">client.regions.<a href="./src/telnyx/resources/regions.py">list</a>() -> <a href="./src/telnyx/types/region_list_response.py">RegionListResponse</a></code>

# RegulatoryRequirements

Types:

```python
from telnyx.types import RegulatoryRequirementRetrieveResponse
```

Methods:

- <code title="get /regulatory_requirements">client.regulatory_requirements.<a href="./src/telnyx/resources/regulatory_requirements.py">retrieve</a>(\*\*<a href="src/telnyx/types/regulatory_requirement_retrieve_params.py">params</a>) -> <a href="./src/telnyx/types/regulatory_requirement_retrieve_response.py">RegulatoryRequirementRetrieveResponse</a></code>

# Reports

Types:

```python
from telnyx.types import ReportListMdrsResponse, ReportListWdrsResponse
```

Methods:

- <code title="get /reports/mdrs">client.reports.<a href="./src/telnyx/resources/reports/reports.py">list_mdrs</a>(\*\*<a href="src/telnyx/types/report_list_mdrs_params.py">params</a>) -> <a href="./src/telnyx/types/report_list_mdrs_response.py">ReportListMdrsResponse</a></code>
- <code title="get /reports/wdrs">client.reports.<a href="./src/telnyx/resources/reports/reports.py">list_wdrs</a>(\*\*<a href="src/telnyx/types/report_list_wdrs_params.py">params</a>) -> <a href="./src/telnyx/types/report_list_wdrs_response.py">ReportListWdrsResponse</a></code>

## CdrUsageReports

Types:

```python
from telnyx.types.reports import CdrUsageReportFetchSyncResponse
```

Methods:

- <code title="get /reports/cdr_usage_reports/sync">client.reports.cdr_usage_reports.<a href="./src/telnyx/resources/reports/cdr_usage_reports.py">fetch_sync</a>(\*\*<a href="src/telnyx/types/reports/cdr_usage_report_fetch_sync_params.py">params</a>) -> <a href="./src/telnyx/types/reports/cdr_usage_report_fetch_sync_response.py">CdrUsageReportFetchSyncResponse</a></code>

## MdrUsageReports

Types:

```python
from telnyx.types.reports import (
    MdrUsageReport,
    MdrUsageReportCreateResponse,
    MdrUsageReportRetrieveResponse,
    MdrUsageReportListResponse,
    MdrUsageReportDeleteResponse,
    MdrUsageReportFetchSyncResponse,
)
```

Methods:

- <code title="post /reports/mdr_usage_reports">client.reports.mdr_usage_reports.<a href="./src/telnyx/resources/reports/mdr_usage_reports.py">create</a>(\*\*<a href="src/telnyx/types/reports/mdr_usage_report_create_params.py">params</a>) -> <a href="./src/telnyx/types/reports/mdr_usage_report_create_response.py">MdrUsageReportCreateResponse</a></code>
- <code title="get /reports/mdr_usage_reports/{id}">client.reports.mdr_usage_reports.<a href="./src/telnyx/resources/reports/mdr_usage_reports.py">retrieve</a>(id) -> <a href="./src/telnyx/types/reports/mdr_usage_report_retrieve_response.py">MdrUsageReportRetrieveResponse</a></code>
- <code title="get /reports/mdr_usage_reports">client.reports.mdr_usage_reports.<a href="./src/telnyx/resources/reports/mdr_usage_reports.py">list</a>(\*\*<a href="src/telnyx/types/reports/mdr_usage_report_list_params.py">params</a>) -> <a href="./src/telnyx/types/reports/mdr_usage_report_list_response.py">MdrUsageReportListResponse</a></code>
- <code title="delete /reports/mdr_usage_reports/{id}">client.reports.mdr_usage_reports.<a href="./src/telnyx/resources/reports/mdr_usage_reports.py">delete</a>(id) -> <a href="./src/telnyx/types/reports/mdr_usage_report_delete_response.py">MdrUsageReportDeleteResponse</a></code>
- <code title="get /reports/mdr_usage_reports/sync">client.reports.mdr_usage_reports.<a href="./src/telnyx/resources/reports/mdr_usage_reports.py">fetch_sync</a>(\*\*<a href="src/telnyx/types/reports/mdr_usage_report_fetch_sync_params.py">params</a>) -> <a href="./src/telnyx/types/reports/mdr_usage_report_fetch_sync_response.py">MdrUsageReportFetchSyncResponse</a></code>

# RequirementGroups

Types:

```python
from telnyx.types import RequirementGroup, RequirementGroupListResponse
```

Methods:

- <code title="post /requirement_groups">client.requirement_groups.<a href="./src/telnyx/resources/requirement_groups.py">create</a>(\*\*<a href="src/telnyx/types/requirement_group_create_params.py">params</a>) -> <a href="./src/telnyx/types/requirement_group.py">RequirementGroup</a></code>
- <code title="get /requirement_groups/{id}">client.requirement_groups.<a href="./src/telnyx/resources/requirement_groups.py">retrieve</a>(id) -> <a href="./src/telnyx/types/requirement_group.py">RequirementGroup</a></code>
- <code title="patch /requirement_groups/{id}">client.requirement_groups.<a href="./src/telnyx/resources/requirement_groups.py">update</a>(id, \*\*<a href="src/telnyx/types/requirement_group_update_params.py">params</a>) -> <a href="./src/telnyx/types/requirement_group.py">RequirementGroup</a></code>
- <code title="get /requirement_groups">client.requirement_groups.<a href="./src/telnyx/resources/requirement_groups.py">list</a>(\*\*<a href="src/telnyx/types/requirement_group_list_params.py">params</a>) -> <a href="./src/telnyx/types/requirement_group_list_response.py">RequirementGroupListResponse</a></code>
- <code title="delete /requirement_groups/{id}">client.requirement_groups.<a href="./src/telnyx/resources/requirement_groups.py">delete</a>(id) -> <a href="./src/telnyx/types/requirement_group.py">RequirementGroup</a></code>
- <code title="post /requirement_groups/{id}/submit_for_approval">client.requirement_groups.<a href="./src/telnyx/resources/requirement_groups.py">submit_for_approval</a>(id) -> <a href="./src/telnyx/types/requirement_group.py">RequirementGroup</a></code>

# RequirementTypes

Types:

```python
from telnyx.types import RequirementTypeRetrieveResponse, RequirementTypeListResponse
```

Methods:

- <code title="get /requirement_types/{id}">client.requirement_types.<a href="./src/telnyx/resources/requirement_types.py">retrieve</a>(id) -> <a href="./src/telnyx/types/requirement_type_retrieve_response.py">RequirementTypeRetrieveResponse</a></code>
- <code title="get /requirement_types">client.requirement_types.<a href="./src/telnyx/resources/requirement_types.py">list</a>(\*\*<a href="src/telnyx/types/requirement_type_list_params.py">params</a>) -> <a href="./src/telnyx/types/requirement_type_list_response.py">RequirementTypeListResponse</a></code>

# Requirements

Types:

```python
from telnyx.types import RequirementRetrieveResponse, RequirementListResponse
```

Methods:

- <code title="get /requirements/{id}">client.requirements.<a href="./src/telnyx/resources/requirements.py">retrieve</a>(id) -> <a href="./src/telnyx/types/requirement_retrieve_response.py">RequirementRetrieveResponse</a></code>
- <code title="get /requirements">client.requirements.<a href="./src/telnyx/resources/requirements.py">list</a>(\*\*<a href="src/telnyx/types/requirement_list_params.py">params</a>) -> <a href="./src/telnyx/types/requirement_list_response.py">RequirementListResponse</a></code>

# RoomCompositions

Types:

```python
from telnyx.types import (
    RoomComposition,
    VideoRegion,
    RoomCompositionCreateResponse,
    RoomCompositionRetrieveResponse,
    RoomCompositionListResponse,
)
```

Methods:

- <code title="post /room_compositions">client.room_compositions.<a href="./src/telnyx/resources/room_compositions.py">create</a>(\*\*<a href="src/telnyx/types/room_composition_create_params.py">params</a>) -> <a href="./src/telnyx/types/room_composition_create_response.py">RoomCompositionCreateResponse</a></code>
- <code title="get /room_compositions/{room_composition_id}">client.room_compositions.<a href="./src/telnyx/resources/room_compositions.py">retrieve</a>(room_composition_id) -> <a href="./src/telnyx/types/room_composition_retrieve_response.py">RoomCompositionRetrieveResponse</a></code>
- <code title="get /room_compositions">client.room_compositions.<a href="./src/telnyx/resources/room_compositions.py">list</a>(\*\*<a href="src/telnyx/types/room_composition_list_params.py">params</a>) -> <a href="./src/telnyx/types/room_composition_list_response.py">RoomCompositionListResponse</a></code>
- <code title="delete /room_compositions/{room_composition_id}">client.room_compositions.<a href="./src/telnyx/resources/room_compositions.py">delete</a>(room_composition_id) -> None</code>

# RoomParticipants

Types:

```python
from telnyx.types import RoomParticipantRetrieveResponse, RoomParticipantListResponse
```

Methods:

- <code title="get /room_participants/{room_participant_id}">client.room_participants.<a href="./src/telnyx/resources/room_participants.py">retrieve</a>(room_participant_id) -> <a href="./src/telnyx/types/room_participant_retrieve_response.py">RoomParticipantRetrieveResponse</a></code>
- <code title="get /room_participants">client.room_participants.<a href="./src/telnyx/resources/room_participants.py">list</a>(\*\*<a href="src/telnyx/types/room_participant_list_params.py">params</a>) -> <a href="./src/telnyx/types/room_participant_list_response.py">RoomParticipantListResponse</a></code>

# RoomRecordings

Types:

```python
from telnyx.types import (
    RoomRecordingRetrieveResponse,
    RoomRecordingListResponse,
    RoomRecordingDeleteBulkResponse,
)
```

Methods:

- <code title="get /room_recordings/{room_recording_id}">client.room_recordings.<a href="./src/telnyx/resources/room_recordings.py">retrieve</a>(room_recording_id) -> <a href="./src/telnyx/types/room_recording_retrieve_response.py">RoomRecordingRetrieveResponse</a></code>
- <code title="get /room_recordings">client.room_recordings.<a href="./src/telnyx/resources/room_recordings.py">list</a>(\*\*<a href="src/telnyx/types/room_recording_list_params.py">params</a>) -> <a href="./src/telnyx/types/room_recording_list_response.py">RoomRecordingListResponse</a></code>
- <code title="delete /room_recordings/{room_recording_id}">client.room_recordings.<a href="./src/telnyx/resources/room_recordings.py">delete</a>(room_recording_id) -> None</code>
- <code title="delete /room_recordings">client.room_recordings.<a href="./src/telnyx/resources/room_recordings.py">delete_bulk</a>(\*\*<a href="src/telnyx/types/room_recording_delete_bulk_params.py">params</a>) -> <a href="./src/telnyx/types/room_recording_delete_bulk_response.py">RoomRecordingDeleteBulkResponse</a></code>

# Rooms

Types:

```python
from telnyx.types import (
    Room,
    RoomSession,
    RoomCreateResponse,
    RoomRetrieveResponse,
    RoomUpdateResponse,
    RoomListResponse,
)
```

Methods:

- <code title="post /rooms">client.rooms.<a href="./src/telnyx/resources/rooms/rooms.py">create</a>(\*\*<a href="src/telnyx/types/room_create_params.py">params</a>) -> <a href="./src/telnyx/types/room_create_response.py">RoomCreateResponse</a></code>
- <code title="get /rooms/{room_id}">client.rooms.<a href="./src/telnyx/resources/rooms/rooms.py">retrieve</a>(room_id, \*\*<a href="src/telnyx/types/room_retrieve_params.py">params</a>) -> <a href="./src/telnyx/types/room_retrieve_response.py">RoomRetrieveResponse</a></code>
- <code title="patch /rooms/{room_id}">client.rooms.<a href="./src/telnyx/resources/rooms/rooms.py">update</a>(room_id, \*\*<a href="src/telnyx/types/room_update_params.py">params</a>) -> <a href="./src/telnyx/types/room_update_response.py">RoomUpdateResponse</a></code>
- <code title="get /rooms">client.rooms.<a href="./src/telnyx/resources/rooms/rooms.py">list</a>(\*\*<a href="src/telnyx/types/room_list_params.py">params</a>) -> <a href="./src/telnyx/types/room_list_response.py">RoomListResponse</a></code>
- <code title="delete /rooms/{room_id}">client.rooms.<a href="./src/telnyx/resources/rooms/rooms.py">delete</a>(room_id) -> None</code>

## Actions

Types:

```python
from telnyx.types.rooms import (
    ActionGenerateJoinClientTokenResponse,
    ActionRefreshClientTokenResponse,
)
```

Methods:

- <code title="post /rooms/{room_id}/actions/generate_join_client_token">client.rooms.actions.<a href="./src/telnyx/resources/rooms/actions.py">generate_join_client_token</a>(room_id, \*\*<a href="src/telnyx/types/rooms/action_generate_join_client_token_params.py">params</a>) -> <a href="./src/telnyx/types/rooms/action_generate_join_client_token_response.py">ActionGenerateJoinClientTokenResponse</a></code>
- <code title="post /rooms/{room_id}/actions/refresh_client_token">client.rooms.actions.<a href="./src/telnyx/resources/rooms/actions.py">refresh_client_token</a>(room_id, \*\*<a href="src/telnyx/types/rooms/action_refresh_client_token_params.py">params</a>) -> <a href="./src/telnyx/types/rooms/action_refresh_client_token_response.py">ActionRefreshClientTokenResponse</a></code>

## Sessions

Types:

```python
from telnyx.types.rooms import (
    SessionRetrieveResponse,
    SessionList0Response,
    SessionList1Response,
    SessionRetrieveParticipantsResponse,
)
```

Methods:

- <code title="get /room_sessions/{room_session_id}">client.rooms.sessions.<a href="./src/telnyx/resources/rooms/sessions/sessions.py">retrieve</a>(room_session_id, \*\*<a href="src/telnyx/types/rooms/session_retrieve_params.py">params</a>) -> <a href="./src/telnyx/types/rooms/session_retrieve_response.py">SessionRetrieveResponse</a></code>
- <code title="get /room_sessions">client.rooms.sessions.<a href="./src/telnyx/resources/rooms/sessions/sessions.py">list_0</a>(\*\*<a href="src/telnyx/types/rooms/session_list_0_params.py">params</a>) -> <a href="./src/telnyx/types/rooms/session_list_0_response.py">SessionList0Response</a></code>
- <code title="get /rooms/{room_id}/sessions">client.rooms.sessions.<a href="./src/telnyx/resources/rooms/sessions/sessions.py">list_1</a>(room_id, \*\*<a href="src/telnyx/types/rooms/session_list_1_params.py">params</a>) -> <a href="./src/telnyx/types/rooms/session_list_1_response.py">SessionList1Response</a></code>
- <code title="get /room_sessions/{room_session_id}/participants">client.rooms.sessions.<a href="./src/telnyx/resources/rooms/sessions/sessions.py">retrieve_participants</a>(room_session_id, \*\*<a href="src/telnyx/types/rooms/session_retrieve_participants_params.py">params</a>) -> <a href="./src/telnyx/types/rooms/session_retrieve_participants_response.py">SessionRetrieveParticipantsResponse</a></code>

### Actions

Types:

```python
from telnyx.types.rooms.sessions import (
    ActionsParticipantsRequest,
    ActionEndResponse,
    ActionKickResponse,
    ActionMuteResponse,
    ActionUnmuteResponse,
)
```

Methods:

- <code title="post /room_sessions/{room_session_id}/actions/end">client.rooms.sessions.actions.<a href="./src/telnyx/resources/rooms/sessions/actions.py">end</a>(room_session_id) -> <a href="./src/telnyx/types/rooms/sessions/action_end_response.py">ActionEndResponse</a></code>
- <code title="post /room_sessions/{room_session_id}/actions/kick">client.rooms.sessions.actions.<a href="./src/telnyx/resources/rooms/sessions/actions.py">kick</a>(room_session_id, \*\*<a href="src/telnyx/types/rooms/sessions/action_kick_params.py">params</a>) -> <a href="./src/telnyx/types/rooms/sessions/action_kick_response.py">ActionKickResponse</a></code>
- <code title="post /room_sessions/{room_session_id}/actions/mute">client.rooms.sessions.actions.<a href="./src/telnyx/resources/rooms/sessions/actions.py">mute</a>(room_session_id, \*\*<a href="src/telnyx/types/rooms/sessions/action_mute_params.py">params</a>) -> <a href="./src/telnyx/types/rooms/sessions/action_mute_response.py">ActionMuteResponse</a></code>
- <code title="post /room_sessions/{room_session_id}/actions/unmute">client.rooms.sessions.actions.<a href="./src/telnyx/resources/rooms/sessions/actions.py">unmute</a>(room_session_id, \*\*<a href="src/telnyx/types/rooms/sessions/action_unmute_params.py">params</a>) -> <a href="./src/telnyx/types/rooms/sessions/action_unmute_response.py">ActionUnmuteResponse</a></code>

# Seti

Types:

```python
from telnyx.types import SetiRetrieveBlackBoxTestResultsResponse
```

Methods:

- <code title="get /seti/black_box_test_results">client.seti.<a href="./src/telnyx/resources/seti.py">retrieve_black_box_test_results</a>(\*\*<a href="src/telnyx/types/seti_retrieve_black_box_test_results_params.py">params</a>) -> <a href="./src/telnyx/types/seti_retrieve_black_box_test_results_response.py">SetiRetrieveBlackBoxTestResultsResponse</a></code>

# ShortCodes

Types:

```python
from telnyx.types import ShortCodeRetrieveResponse, ShortCodeUpdateResponse, ShortCodeListResponse
```

Methods:

- <code title="get /short_codes/{id}">client.short_codes.<a href="./src/telnyx/resources/short_codes.py">retrieve</a>(id) -> <a href="./src/telnyx/types/short_code_retrieve_response.py">ShortCodeRetrieveResponse</a></code>
- <code title="patch /short_codes/{id}">client.short_codes.<a href="./src/telnyx/resources/short_codes.py">update</a>(id, \*\*<a href="src/telnyx/types/short_code_update_params.py">params</a>) -> <a href="./src/telnyx/types/short_code_update_response.py">ShortCodeUpdateResponse</a></code>
- <code title="get /short_codes">client.short_codes.<a href="./src/telnyx/resources/short_codes.py">list</a>(\*\*<a href="src/telnyx/types/short_code_list_params.py">params</a>) -> <a href="./src/telnyx/types/short_code_list_response.py">ShortCodeListResponse</a></code>

# SimCardDataUsageNotifications

Types:

```python
from telnyx.types import (
    SimCardDataUsageNotification,
    SimCardDataUsageNotificationCreateResponse,
    SimCardDataUsageNotificationRetrieveResponse,
    SimCardDataUsageNotificationUpdateResponse,
    SimCardDataUsageNotificationListResponse,
    SimCardDataUsageNotificationDeleteResponse,
)
```

Methods:

- <code title="post /sim_card_data_usage_notifications">client.sim_card_data_usage_notifications.<a href="./src/telnyx/resources/sim_card_data_usage_notifications.py">create</a>(\*\*<a href="src/telnyx/types/sim_card_data_usage_notification_create_params.py">params</a>) -> <a href="./src/telnyx/types/sim_card_data_usage_notification_create_response.py">SimCardDataUsageNotificationCreateResponse</a></code>
- <code title="get /sim_card_data_usage_notifications/{id}">client.sim_card_data_usage_notifications.<a href="./src/telnyx/resources/sim_card_data_usage_notifications.py">retrieve</a>(id) -> <a href="./src/telnyx/types/sim_card_data_usage_notification_retrieve_response.py">SimCardDataUsageNotificationRetrieveResponse</a></code>
- <code title="patch /sim_card_data_usage_notifications/{id}">client.sim_card_data_usage_notifications.<a href="./src/telnyx/resources/sim_card_data_usage_notifications.py">update</a>(id, \*\*<a href="src/telnyx/types/sim_card_data_usage_notification_update_params.py">params</a>) -> <a href="./src/telnyx/types/sim_card_data_usage_notification_update_response.py">SimCardDataUsageNotificationUpdateResponse</a></code>
- <code title="get /sim_card_data_usage_notifications">client.sim_card_data_usage_notifications.<a href="./src/telnyx/resources/sim_card_data_usage_notifications.py">list</a>(\*\*<a href="src/telnyx/types/sim_card_data_usage_notification_list_params.py">params</a>) -> <a href="./src/telnyx/types/sim_card_data_usage_notification_list_response.py">SimCardDataUsageNotificationListResponse</a></code>
- <code title="delete /sim_card_data_usage_notifications/{id}">client.sim_card_data_usage_notifications.<a href="./src/telnyx/resources/sim_card_data_usage_notifications.py">delete</a>(id) -> <a href="./src/telnyx/types/sim_card_data_usage_notification_delete_response.py">SimCardDataUsageNotificationDeleteResponse</a></code>

# SimCardGroups

Types:

```python
from telnyx.types import (
    ConsumedData,
    SimCardGroup,
    SimCardGroupCreateResponse,
    SimCardGroupRetrieveResponse,
    SimCardGroupUpdateResponse,
    SimCardGroupListResponse,
    SimCardGroupDeleteResponse,
)
```

Methods:

- <code title="post /sim_card_groups">client.sim_card_groups.<a href="./src/telnyx/resources/sim_card_groups/sim_card_groups.py">create</a>(\*\*<a href="src/telnyx/types/sim_card_group_create_params.py">params</a>) -> <a href="./src/telnyx/types/sim_card_group_create_response.py">SimCardGroupCreateResponse</a></code>
- <code title="get /sim_card_groups/{id}">client.sim_card_groups.<a href="./src/telnyx/resources/sim_card_groups/sim_card_groups.py">retrieve</a>(id, \*\*<a href="src/telnyx/types/sim_card_group_retrieve_params.py">params</a>) -> <a href="./src/telnyx/types/sim_card_group_retrieve_response.py">SimCardGroupRetrieveResponse</a></code>
- <code title="patch /sim_card_groups/{id}">client.sim_card_groups.<a href="./src/telnyx/resources/sim_card_groups/sim_card_groups.py">update</a>(id, \*\*<a href="src/telnyx/types/sim_card_group_update_params.py">params</a>) -> <a href="./src/telnyx/types/sim_card_group_update_response.py">SimCardGroupUpdateResponse</a></code>
- <code title="get /sim_card_groups">client.sim_card_groups.<a href="./src/telnyx/resources/sim_card_groups/sim_card_groups.py">list</a>(\*\*<a href="src/telnyx/types/sim_card_group_list_params.py">params</a>) -> <a href="./src/telnyx/types/sim_card_group_list_response.py">SimCardGroupListResponse</a></code>
- <code title="delete /sim_card_groups/{id}">client.sim_card_groups.<a href="./src/telnyx/resources/sim_card_groups/sim_card_groups.py">delete</a>(id) -> <a href="./src/telnyx/types/sim_card_group_delete_response.py">SimCardGroupDeleteResponse</a></code>

## Actions

Types:

```python
from telnyx.types.sim_card_groups import (
    SimCardGroupAction,
    ActionRetrieveResponse,
    ActionListResponse,
    ActionRemovePrivateWirelessGatewayResponse,
    ActionRemoveWirelessBlocklistResponse,
    ActionSetPrivateWirelessGatewayResponse,
    ActionSetWirelessBlocklistResponse,
)
```

Methods:

- <code title="get /sim_card_group_actions/{id}">client.sim_card_groups.actions.<a href="./src/telnyx/resources/sim_card_groups/actions.py">retrieve</a>(id) -> <a href="./src/telnyx/types/sim_card_groups/action_retrieve_response.py">ActionRetrieveResponse</a></code>
- <code title="get /sim_card_group_actions">client.sim_card_groups.actions.<a href="./src/telnyx/resources/sim_card_groups/actions.py">list</a>(\*\*<a href="src/telnyx/types/sim_card_groups/action_list_params.py">params</a>) -> <a href="./src/telnyx/types/sim_card_groups/action_list_response.py">ActionListResponse</a></code>
- <code title="post /sim_card_groups/{id}/actions/remove_private_wireless_gateway">client.sim_card_groups.actions.<a href="./src/telnyx/resources/sim_card_groups/actions.py">remove_private_wireless_gateway</a>(id) -> <a href="./src/telnyx/types/sim_card_groups/action_remove_private_wireless_gateway_response.py">ActionRemovePrivateWirelessGatewayResponse</a></code>
- <code title="post /sim_card_groups/{id}/actions/remove_wireless_blocklist">client.sim_card_groups.actions.<a href="./src/telnyx/resources/sim_card_groups/actions.py">remove_wireless_blocklist</a>(id) -> <a href="./src/telnyx/types/sim_card_groups/action_remove_wireless_blocklist_response.py">ActionRemoveWirelessBlocklistResponse</a></code>
- <code title="post /sim_card_groups/{id}/actions/set_private_wireless_gateway">client.sim_card_groups.actions.<a href="./src/telnyx/resources/sim_card_groups/actions.py">set_private_wireless_gateway</a>(id, \*\*<a href="src/telnyx/types/sim_card_groups/action_set_private_wireless_gateway_params.py">params</a>) -> <a href="./src/telnyx/types/sim_card_groups/action_set_private_wireless_gateway_response.py">ActionSetPrivateWirelessGatewayResponse</a></code>
- <code title="post /sim_card_groups/{id}/actions/set_wireless_blocklist">client.sim_card_groups.actions.<a href="./src/telnyx/resources/sim_card_groups/actions.py">set_wireless_blocklist</a>(id, \*\*<a href="src/telnyx/types/sim_card_groups/action_set_wireless_blocklist_params.py">params</a>) -> <a href="./src/telnyx/types/sim_card_groups/action_set_wireless_blocklist_response.py">ActionSetWirelessBlocklistResponse</a></code>

# SimCardOrderPreview

Types:

```python
from telnyx.types import SimCardOrderPreviewPreviewResponse
```

Methods:

- <code title="post /sim_card_order_preview">client.sim_card_order_preview.<a href="./src/telnyx/resources/sim_card_order_preview.py">preview</a>(\*\*<a href="src/telnyx/types/sim_card_order_preview_preview_params.py">params</a>) -> <a href="./src/telnyx/types/sim_card_order_preview_preview_response.py">SimCardOrderPreviewPreviewResponse</a></code>

# SimCardOrders

Types:

```python
from telnyx.types import (
    SimCardOrder,
    SimCardOrderCreateResponse,
    SimCardOrderRetrieveResponse,
    SimCardOrderListResponse,
)
```

Methods:

- <code title="post /sim_card_orders">client.sim_card_orders.<a href="./src/telnyx/resources/sim_card_orders.py">create</a>(\*\*<a href="src/telnyx/types/sim_card_order_create_params.py">params</a>) -> <a href="./src/telnyx/types/sim_card_order_create_response.py">SimCardOrderCreateResponse</a></code>
- <code title="get /sim_card_orders/{id}">client.sim_card_orders.<a href="./src/telnyx/resources/sim_card_orders.py">retrieve</a>(id) -> <a href="./src/telnyx/types/sim_card_order_retrieve_response.py">SimCardOrderRetrieveResponse</a></code>
- <code title="get /sim_card_orders">client.sim_card_orders.<a href="./src/telnyx/resources/sim_card_orders.py">list</a>(\*\*<a href="src/telnyx/types/sim_card_order_list_params.py">params</a>) -> <a href="./src/telnyx/types/sim_card_order_list_response.py">SimCardOrderListResponse</a></code>

# SimCards

Types:

```python
from telnyx.types import (
    SimCard,
    SimCardRetrieveResponse,
    SimCardUpdateResponse,
    SimCardListResponse,
    SimCardDeleteResponse,
    SimCardGetActivationCodeResponse,
    SimCardGetDeviceDetailsResponse,
    SimCardGetPublicIPResponse,
    SimCardListWirelessConnectivityLogsResponse,
)
```

Methods:

- <code title="get /sim_cards/{id}">client.sim_cards.<a href="./src/telnyx/resources/sim_cards/sim_cards.py">retrieve</a>(id, \*\*<a href="src/telnyx/types/sim_card_retrieve_params.py">params</a>) -> <a href="./src/telnyx/types/sim_card_retrieve_response.py">SimCardRetrieveResponse</a></code>
- <code title="patch /sim_cards/{id}">client.sim_cards.<a href="./src/telnyx/resources/sim_cards/sim_cards.py">update</a>(id, \*\*<a href="src/telnyx/types/sim_card_update_params.py">params</a>) -> <a href="./src/telnyx/types/sim_card_update_response.py">SimCardUpdateResponse</a></code>
- <code title="get /sim_cards">client.sim_cards.<a href="./src/telnyx/resources/sim_cards/sim_cards.py">list</a>(\*\*<a href="src/telnyx/types/sim_card_list_params.py">params</a>) -> <a href="./src/telnyx/types/sim_card_list_response.py">SimCardListResponse</a></code>
- <code title="delete /sim_cards/{id}">client.sim_cards.<a href="./src/telnyx/resources/sim_cards/sim_cards.py">delete</a>(id, \*\*<a href="src/telnyx/types/sim_card_delete_params.py">params</a>) -> <a href="./src/telnyx/types/sim_card_delete_response.py">SimCardDeleteResponse</a></code>
- <code title="get /sim_cards/{id}/activation_code">client.sim_cards.<a href="./src/telnyx/resources/sim_cards/sim_cards.py">get_activation_code</a>(id) -> <a href="./src/telnyx/types/sim_card_get_activation_code_response.py">SimCardGetActivationCodeResponse</a></code>
- <code title="get /sim_cards/{id}/device_details">client.sim_cards.<a href="./src/telnyx/resources/sim_cards/sim_cards.py">get_device_details</a>(id) -> <a href="./src/telnyx/types/sim_card_get_device_details_response.py">SimCardGetDeviceDetailsResponse</a></code>
- <code title="get /sim_cards/{id}/public_ip">client.sim_cards.<a href="./src/telnyx/resources/sim_cards/sim_cards.py">get_public_ip</a>(id) -> <a href="./src/telnyx/types/sim_card_get_public_ip_response.py">SimCardGetPublicIPResponse</a></code>
- <code title="get /sim_cards/{id}/wireless_connectivity_logs">client.sim_cards.<a href="./src/telnyx/resources/sim_cards/sim_cards.py">list_wireless_connectivity_logs</a>(id, \*\*<a href="src/telnyx/types/sim_card_list_wireless_connectivity_logs_params.py">params</a>) -> <a href="./src/telnyx/types/sim_card_list_wireless_connectivity_logs_response.py">SimCardListWirelessConnectivityLogsResponse</a></code>

## Actions

Types:

```python
from telnyx.types.sim_cards import (
    SimCardAction,
    ActionRetrieveResponse,
    ActionListResponse,
    ActionBulkSetPublicIPsResponse,
    ActionDisableResponse,
    ActionEnableResponse,
    ActionRemovePublicIPResponse,
    ActionSetPublicIPResponse,
    ActionSetStandbyResponse,
    ActionValidateRegistrationCodesResponse,
)
```

Methods:

- <code title="get /sim_card_actions/{id}">client.sim_cards.actions.<a href="./src/telnyx/resources/sim_cards/actions.py">retrieve</a>(id) -> <a href="./src/telnyx/types/sim_cards/action_retrieve_response.py">ActionRetrieveResponse</a></code>
- <code title="get /sim_card_actions">client.sim_cards.actions.<a href="./src/telnyx/resources/sim_cards/actions.py">list</a>(\*\*<a href="src/telnyx/types/sim_cards/action_list_params.py">params</a>) -> <a href="./src/telnyx/types/sim_cards/action_list_response.py">ActionListResponse</a></code>
- <code title="post /sim_cards/actions/bulk_set_public_ips">client.sim_cards.actions.<a href="./src/telnyx/resources/sim_cards/actions.py">bulk_set_public_ips</a>(\*\*<a href="src/telnyx/types/sim_cards/action_bulk_set_public_ips_params.py">params</a>) -> <a href="./src/telnyx/types/sim_cards/action_bulk_set_public_ips_response.py">ActionBulkSetPublicIPsResponse</a></code>
- <code title="post /sim_cards/{id}/actions/disable">client.sim_cards.actions.<a href="./src/telnyx/resources/sim_cards/actions.py">disable</a>(id) -> <a href="./src/telnyx/types/sim_cards/action_disable_response.py">ActionDisableResponse</a></code>
- <code title="post /sim_cards/{id}/actions/enable">client.sim_cards.actions.<a href="./src/telnyx/resources/sim_cards/actions.py">enable</a>(id) -> <a href="./src/telnyx/types/sim_cards/action_enable_response.py">ActionEnableResponse</a></code>
- <code title="post /sim_cards/{id}/actions/remove_public_ip">client.sim_cards.actions.<a href="./src/telnyx/resources/sim_cards/actions.py">remove_public_ip</a>(id) -> <a href="./src/telnyx/types/sim_cards/action_remove_public_ip_response.py">ActionRemovePublicIPResponse</a></code>
- <code title="post /sim_cards/{id}/actions/set_public_ip">client.sim_cards.actions.<a href="./src/telnyx/resources/sim_cards/actions.py">set_public_ip</a>(id, \*\*<a href="src/telnyx/types/sim_cards/action_set_public_ip_params.py">params</a>) -> <a href="./src/telnyx/types/sim_cards/action_set_public_ip_response.py">ActionSetPublicIPResponse</a></code>
- <code title="post /sim_cards/{id}/actions/set_standby">client.sim_cards.actions.<a href="./src/telnyx/resources/sim_cards/actions.py">set_standby</a>(id) -> <a href="./src/telnyx/types/sim_cards/action_set_standby_response.py">ActionSetStandbyResponse</a></code>
- <code title="post /sim_cards/actions/validate_registration_codes">client.sim_cards.actions.<a href="./src/telnyx/resources/sim_cards/actions.py">validate_registration_codes</a>(\*\*<a href="src/telnyx/types/sim_cards/action_validate_registration_codes_params.py">params</a>) -> <a href="./src/telnyx/types/sim_cards/action_validate_registration_codes_response.py">ActionValidateRegistrationCodesResponse</a></code>

# SiprecConnectors

Types:

```python
from telnyx.types import (
    SiprecConnectorCreateResponse,
    SiprecConnectorRetrieveResponse,
    SiprecConnectorUpdateResponse,
)
```

Methods:

- <code title="post /siprec_connectors">client.siprec_connectors.<a href="./src/telnyx/resources/siprec_connectors.py">create</a>(\*\*<a href="src/telnyx/types/siprec_connector_create_params.py">params</a>) -> <a href="./src/telnyx/types/siprec_connector_create_response.py">SiprecConnectorCreateResponse</a></code>
- <code title="get /siprec_connectors/{connector_name}">client.siprec_connectors.<a href="./src/telnyx/resources/siprec_connectors.py">retrieve</a>(connector_name) -> <a href="./src/telnyx/types/siprec_connector_retrieve_response.py">SiprecConnectorRetrieveResponse</a></code>
- <code title="put /siprec_connectors/{connector_name}">client.siprec_connectors.<a href="./src/telnyx/resources/siprec_connectors.py">update</a>(connector_name, \*\*<a href="src/telnyx/types/siprec_connector_update_params.py">params</a>) -> <a href="./src/telnyx/types/siprec_connector_update_response.py">SiprecConnectorUpdateResponse</a></code>
- <code title="delete /siprec_connectors/{connector_name}">client.siprec_connectors.<a href="./src/telnyx/resources/siprec_connectors.py">delete</a>(connector_name) -> None</code>

# Storage

Types:

```python
from telnyx.types import StorageListMigrationSourceCoverageResponse
```

Methods:

- <code title="get /storage/migration_source_coverage">client.storage.<a href="./src/telnyx/resources/storage/storage.py">list_migration_source_coverage</a>() -> <a href="./src/telnyx/types/storage_list_migration_source_coverage_response.py">StorageListMigrationSourceCoverageResponse</a></code>

## Buckets

Types:

```python
from telnyx.types.storage import BucketCreatePresignedURLResponse
```

Methods:

- <code title="post /storage/buckets/{bucketName}/{objectName}/presigned_url">client.storage.buckets.<a href="./src/telnyx/resources/storage/buckets/buckets.py">create_presigned_url</a>(object_name, \*, bucket_name, \*\*<a href="src/telnyx/types/storage/bucket_create_presigned_url_params.py">params</a>) -> <a href="./src/telnyx/types/storage/bucket_create_presigned_url_response.py">BucketCreatePresignedURLResponse</a></code>

### SslCertificate

Types:

```python
from telnyx.types.storage.buckets import (
    SslCertificate,
    SslCertificateCreateResponse,
    SslCertificateRetrieveResponse,
    SslCertificateDeleteResponse,
)
```

Methods:

- <code title="put /storage/buckets/{bucketName}/ssl_certificate">client.storage.buckets.ssl_certificate.<a href="./src/telnyx/resources/storage/buckets/ssl_certificate.py">create</a>(bucket_name, \*\*<a href="src/telnyx/types/storage/buckets/ssl_certificate_create_params.py">params</a>) -> <a href="./src/telnyx/types/storage/buckets/ssl_certificate_create_response.py">SslCertificateCreateResponse</a></code>
- <code title="get /storage/buckets/{bucketName}/ssl_certificate">client.storage.buckets.ssl_certificate.<a href="./src/telnyx/resources/storage/buckets/ssl_certificate.py">retrieve</a>(bucket_name) -> <a href="./src/telnyx/types/storage/buckets/ssl_certificate_retrieve_response.py">SslCertificateRetrieveResponse</a></code>
- <code title="delete /storage/buckets/{bucketName}/ssl_certificate">client.storage.buckets.ssl_certificate.<a href="./src/telnyx/resources/storage/buckets/ssl_certificate.py">delete</a>(bucket_name) -> <a href="./src/telnyx/types/storage/buckets/ssl_certificate_delete_response.py">SslCertificateDeleteResponse</a></code>

### Usage

Types:

```python
from telnyx.types.storage.buckets import (
    PaginationMetaSimple,
    UsageGetAPIUsageResponse,
    UsageGetBucketUsageResponse,
)
```

Methods:

- <code title="get /storage/buckets/{bucketName}/usage/api">client.storage.buckets.usage.<a href="./src/telnyx/resources/storage/buckets/usage.py">get_api_usage</a>(bucket_name, \*\*<a href="src/telnyx/types/storage/buckets/usage_get_api_usage_params.py">params</a>) -> <a href="./src/telnyx/types/storage/buckets/usage_get_api_usage_response.py">UsageGetAPIUsageResponse</a></code>
- <code title="get /storage/buckets/{bucketName}/usage/storage">client.storage.buckets.usage.<a href="./src/telnyx/resources/storage/buckets/usage.py">get_bucket_usage</a>(bucket_name) -> <a href="./src/telnyx/types/storage/buckets/usage_get_bucket_usage_response.py">UsageGetBucketUsageResponse</a></code>

## MigrationSources

Types:

```python
from telnyx.types.storage import (
    MigrationSourceParams,
    MigrationSourceCreateResponse,
    MigrationSourceRetrieveResponse,
    MigrationSourceListResponse,
    MigrationSourceDeleteResponse,
)
```

Methods:

- <code title="post /storage/migration_sources">client.storage.migration_sources.<a href="./src/telnyx/resources/storage/migration_sources.py">create</a>(\*\*<a href="src/telnyx/types/storage/migration_source_create_params.py">params</a>) -> <a href="./src/telnyx/types/storage/migration_source_create_response.py">MigrationSourceCreateResponse</a></code>
- <code title="get /storage/migration_sources/{id}">client.storage.migration_sources.<a href="./src/telnyx/resources/storage/migration_sources.py">retrieve</a>(id) -> <a href="./src/telnyx/types/storage/migration_source_retrieve_response.py">MigrationSourceRetrieveResponse</a></code>
- <code title="get /storage/migration_sources">client.storage.migration_sources.<a href="./src/telnyx/resources/storage/migration_sources.py">list</a>() -> <a href="./src/telnyx/types/storage/migration_source_list_response.py">MigrationSourceListResponse</a></code>
- <code title="delete /storage/migration_sources/{id}">client.storage.migration_sources.<a href="./src/telnyx/resources/storage/migration_sources.py">delete</a>(id) -> <a href="./src/telnyx/types/storage/migration_source_delete_response.py">MigrationSourceDeleteResponse</a></code>

## Migrations

Types:

```python
from telnyx.types.storage import (
    MigrationParams,
    MigrationCreateResponse,
    MigrationRetrieveResponse,
    MigrationListResponse,
)
```

Methods:

- <code title="post /storage/migrations">client.storage.migrations.<a href="./src/telnyx/resources/storage/migrations/migrations.py">create</a>(\*\*<a href="src/telnyx/types/storage/migration_create_params.py">params</a>) -> <a href="./src/telnyx/types/storage/migration_create_response.py">MigrationCreateResponse</a></code>
- <code title="get /storage/migrations/{id}">client.storage.migrations.<a href="./src/telnyx/resources/storage/migrations/migrations.py">retrieve</a>(id) -> <a href="./src/telnyx/types/storage/migration_retrieve_response.py">MigrationRetrieveResponse</a></code>
- <code title="get /storage/migrations">client.storage.migrations.<a href="./src/telnyx/resources/storage/migrations/migrations.py">list</a>() -> <a href="./src/telnyx/types/storage/migration_list_response.py">MigrationListResponse</a></code>

### Actions

Types:

```python
from telnyx.types.storage.migrations import ActionStopResponse
```

Methods:

- <code title="post /storage/migrations/{id}/actions/stop">client.storage.migrations.actions.<a href="./src/telnyx/resources/storage/migrations/actions.py">stop</a>(id) -> <a href="./src/telnyx/types/storage/migrations/action_stop_response.py">ActionStopResponse</a></code>

# SubNumberOrders

Types:

```python
from telnyx.types import (
    SubNumberOrder,
    SubNumberOrderRegulatoryRequirement,
    SubNumberOrderRetrieveResponse,
    SubNumberOrderUpdateResponse,
    SubNumberOrderListResponse,
    SubNumberOrderCancelResponse,
    SubNumberOrderUpdateRequirementGroupResponse,
)
```

Methods:

- <code title="get /sub_number_orders/{sub_number_order_id}">client.sub_number_orders.<a href="./src/telnyx/resources/sub_number_orders.py">retrieve</a>(sub_number_order_id, \*\*<a href="src/telnyx/types/sub_number_order_retrieve_params.py">params</a>) -> <a href="./src/telnyx/types/sub_number_order_retrieve_response.py">SubNumberOrderRetrieveResponse</a></code>
- <code title="patch /sub_number_orders/{sub_number_order_id}">client.sub_number_orders.<a href="./src/telnyx/resources/sub_number_orders.py">update</a>(sub_number_order_id, \*\*<a href="src/telnyx/types/sub_number_order_update_params.py">params</a>) -> <a href="./src/telnyx/types/sub_number_order_update_response.py">SubNumberOrderUpdateResponse</a></code>
- <code title="get /sub_number_orders">client.sub_number_orders.<a href="./src/telnyx/resources/sub_number_orders.py">list</a>(\*\*<a href="src/telnyx/types/sub_number_order_list_params.py">params</a>) -> <a href="./src/telnyx/types/sub_number_order_list_response.py">SubNumberOrderListResponse</a></code>
- <code title="patch /sub_number_orders/{sub_number_order_id}/cancel">client.sub_number_orders.<a href="./src/telnyx/resources/sub_number_orders.py">cancel</a>(sub_number_order_id) -> <a href="./src/telnyx/types/sub_number_order_cancel_response.py">SubNumberOrderCancelResponse</a></code>
- <code title="post /sub_number_orders/{id}/requirement_group">client.sub_number_orders.<a href="./src/telnyx/resources/sub_number_orders.py">update_requirement_group</a>(id, \*\*<a href="src/telnyx/types/sub_number_order_update_requirement_group_params.py">params</a>) -> <a href="./src/telnyx/types/sub_number_order_update_requirement_group_response.py">SubNumberOrderUpdateRequirementGroupResponse</a></code>

# SubNumberOrdersReport

Types:

```python
from telnyx.types import (
    SubNumberOrdersReportCreateResponse,
    SubNumberOrdersReportRetrieveResponse,
    SubNumberOrdersReportDownloadResponse,
)
```

Methods:

- <code title="post /sub_number_orders_report">client.sub_number_orders_report.<a href="./src/telnyx/resources/sub_number_orders_report.py">create</a>(\*\*<a href="src/telnyx/types/sub_number_orders_report_create_params.py">params</a>) -> <a href="./src/telnyx/types/sub_number_orders_report_create_response.py">SubNumberOrdersReportCreateResponse</a></code>
- <code title="get /sub_number_orders_report/{report_id}">client.sub_number_orders_report.<a href="./src/telnyx/resources/sub_number_orders_report.py">retrieve</a>(report_id) -> <a href="./src/telnyx/types/sub_number_orders_report_retrieve_response.py">SubNumberOrdersReportRetrieveResponse</a></code>
- <code title="get /sub_number_orders_report/{report_id}/download">client.sub_number_orders_report.<a href="./src/telnyx/resources/sub_number_orders_report.py">download</a>(report_id) -> str</code>

# TelephonyCredentials

Types:

```python
from telnyx.types import (
    TelephonyCredential,
    TelephonyCredentialCreateResponse,
    TelephonyCredentialRetrieveResponse,
    TelephonyCredentialUpdateResponse,
    TelephonyCredentialListResponse,
    TelephonyCredentialDeleteResponse,
    TelephonyCredentialCreateTokenResponse,
)
```

Methods:

- <code title="post /telephony_credentials">client.telephony_credentials.<a href="./src/telnyx/resources/telephony_credentials.py">create</a>(\*\*<a href="src/telnyx/types/telephony_credential_create_params.py">params</a>) -> <a href="./src/telnyx/types/telephony_credential_create_response.py">TelephonyCredentialCreateResponse</a></code>
- <code title="get /telephony_credentials/{id}">client.telephony_credentials.<a href="./src/telnyx/resources/telephony_credentials.py">retrieve</a>(id) -> <a href="./src/telnyx/types/telephony_credential_retrieve_response.py">TelephonyCredentialRetrieveResponse</a></code>
- <code title="patch /telephony_credentials/{id}">client.telephony_credentials.<a href="./src/telnyx/resources/telephony_credentials.py">update</a>(id, \*\*<a href="src/telnyx/types/telephony_credential_update_params.py">params</a>) -> <a href="./src/telnyx/types/telephony_credential_update_response.py">TelephonyCredentialUpdateResponse</a></code>
- <code title="get /telephony_credentials">client.telephony_credentials.<a href="./src/telnyx/resources/telephony_credentials.py">list</a>(\*\*<a href="src/telnyx/types/telephony_credential_list_params.py">params</a>) -> <a href="./src/telnyx/types/telephony_credential_list_response.py">TelephonyCredentialListResponse</a></code>
- <code title="delete /telephony_credentials/{id}">client.telephony_credentials.<a href="./src/telnyx/resources/telephony_credentials.py">delete</a>(id) -> <a href="./src/telnyx/types/telephony_credential_delete_response.py">TelephonyCredentialDeleteResponse</a></code>
- <code title="post /telephony_credentials/{id}/token">client.telephony_credentials.<a href="./src/telnyx/resources/telephony_credentials.py">create_token</a>(id) -> str</code>

# Texml

Types:

```python
from telnyx.types import TexmlSecretsResponse
```

Methods:

- <code title="post /texml/secrets">client.texml.<a href="./src/telnyx/resources/texml/texml.py">secrets</a>(\*\*<a href="src/telnyx/types/texml_secrets_params.py">params</a>) -> <a href="./src/telnyx/types/texml_secrets_response.py">TexmlSecretsResponse</a></code>

## Accounts

Types:

```python
from telnyx.types.texml import (
    TexmlGetCallRecordingResponseBody,
    TexmlRecordingSubresourcesUris,
    AccountRetrieveRecordingsJsonResponse,
    AccountRetrieveTranscriptionsJsonResponse,
)
```

Methods:

- <code title="get /texml/Accounts/{account_sid}/Recordings.json">client.texml.accounts.<a href="./src/telnyx/resources/texml/accounts/accounts.py">retrieve_recordings_json</a>(account_sid, \*\*<a href="src/telnyx/types/texml/account_retrieve_recordings_json_params.py">params</a>) -> <a href="./src/telnyx/types/texml/account_retrieve_recordings_json_response.py">AccountRetrieveRecordingsJsonResponse</a></code>
- <code title="get /texml/Accounts/{account_sid}/Transcriptions.json">client.texml.accounts.<a href="./src/telnyx/resources/texml/accounts/accounts.py">retrieve_transcriptions_json</a>(account_sid, \*\*<a href="src/telnyx/types/texml/account_retrieve_transcriptions_json_params.py">params</a>) -> <a href="./src/telnyx/types/texml/account_retrieve_transcriptions_json_response.py">AccountRetrieveTranscriptionsJsonResponse</a></code>

### Calls

Types:

```python
from telnyx.types.texml.accounts import (
    UpdateCall,
    CallRetrieveResponse,
    CallUpdateResponse,
    CallCallsResponse,
    CallRetrieveCallsResponse,
    CallSiprecJsonResponse,
    CallStreamsJsonResponse,
)
```

Methods:

- <code title="get /texml/Accounts/{account_sid}/Calls/{call_sid}">client.texml.accounts.calls.<a href="./src/telnyx/resources/texml/accounts/calls/calls.py">retrieve</a>(call_sid, \*, account_sid) -> <a href="./src/telnyx/types/texml/accounts/call_retrieve_response.py">CallRetrieveResponse</a></code>
- <code title="post /texml/Accounts/{account_sid}/Calls/{call_sid}">client.texml.accounts.calls.<a href="./src/telnyx/resources/texml/accounts/calls/calls.py">update</a>(call_sid, \*, account_sid, \*\*<a href="src/telnyx/types/texml/accounts/call_update_params.py">params</a>) -> <a href="./src/telnyx/types/texml/accounts/call_update_response.py">CallUpdateResponse</a></code>
- <code title="post /texml/Accounts/{account_sid}/Calls">client.texml.accounts.calls.<a href="./src/telnyx/resources/texml/accounts/calls/calls.py">calls</a>(account_sid, \*\*<a href="src/telnyx/types/texml/accounts/call_calls_params.py">params</a>) -> <a href="./src/telnyx/types/texml/accounts/call_calls_response.py">CallCallsResponse</a></code>
- <code title="get /texml/Accounts/{account_sid}/Calls">client.texml.accounts.calls.<a href="./src/telnyx/resources/texml/accounts/calls/calls.py">retrieve_calls</a>(account_sid, \*\*<a href="src/telnyx/types/texml/accounts/call_retrieve_calls_params.py">params</a>) -> <a href="./src/telnyx/types/texml/accounts/call_retrieve_calls_response.py">CallRetrieveCallsResponse</a></code>
- <code title="post /texml/Accounts/{account_sid}/Calls/{call_sid}/Siprec.json">client.texml.accounts.calls.<a href="./src/telnyx/resources/texml/accounts/calls/calls.py">siprec_json</a>(call_sid, \*, account_sid, \*\*<a href="src/telnyx/types/texml/accounts/call_siprec_json_params.py">params</a>) -> <a href="./src/telnyx/types/texml/accounts/call_siprec_json_response.py">CallSiprecJsonResponse</a></code>
- <code title="post /texml/Accounts/{account_sid}/Calls/{call_sid}/Streams.json">client.texml.accounts.calls.<a href="./src/telnyx/resources/texml/accounts/calls/calls.py">streams_json</a>(call_sid, \*, account_sid, \*\*<a href="src/telnyx/types/texml/accounts/call_streams_json_params.py">params</a>) -> <a href="./src/telnyx/types/texml/accounts/call_streams_json_response.py">CallStreamsJsonResponse</a></code>

#### RecordingsJson

Types:

```python
from telnyx.types.texml.accounts.calls import (
    RecordingsJsonRecordingsJsonResponse,
    RecordingsJsonRetrieveRecordingsJsonResponse,
)
```

Methods:

- <code title="post /texml/Accounts/{account_sid}/Calls/{call_sid}/Recordings.json">client.texml.accounts.calls.recordings_json.<a href="./src/telnyx/resources/texml/accounts/calls/recordings_json.py">recordings_json</a>(call_sid, \*, account_sid, \*\*<a href="src/telnyx/types/texml/accounts/calls/recordings_json_recordings_json_params.py">params</a>) -> <a href="./src/telnyx/types/texml/accounts/calls/recordings_json_recordings_json_response.py">RecordingsJsonRecordingsJsonResponse</a></code>
- <code title="get /texml/Accounts/{account_sid}/Calls/{call_sid}/Recordings.json">client.texml.accounts.calls.recordings_json.<a href="./src/telnyx/resources/texml/accounts/calls/recordings_json.py">retrieve_recordings_json</a>(call_sid, \*, account_sid) -> <a href="./src/telnyx/types/texml/accounts/calls/recordings_json_retrieve_recordings_json_response.py">RecordingsJsonRetrieveRecordingsJsonResponse</a></code>

#### Recordings

Types:

```python
from telnyx.types.texml.accounts.calls import RecordingRecordingSidJsonResponse
```

Methods:

- <code title="post /texml/Accounts/{account_sid}/Calls/{call_sid}/Recordings/{recording_sid}.json">client.texml.accounts.calls.recordings.<a href="./src/telnyx/resources/texml/accounts/calls/recordings.py">recording_sid_json</a>(recording_sid, \*, account_sid, call_sid, \*\*<a href="src/telnyx/types/texml/accounts/calls/recording_recording_sid_json_params.py">params</a>) -> <a href="./src/telnyx/types/texml/accounts/calls/recording_recording_sid_json_response.py">RecordingRecordingSidJsonResponse</a></code>

#### Siprec

Types:

```python
from telnyx.types.texml.accounts.calls import SiprecSiprecSidJsonResponse
```

Methods:

- <code title="post /texml/Accounts/{account_sid}/Calls/{call_sid}/Siprec/{siprec_sid}.json">client.texml.accounts.calls.siprec.<a href="./src/telnyx/resources/texml/accounts/calls/siprec.py">siprec_sid_json</a>(siprec_sid, \*, account_sid, call_sid, \*\*<a href="src/telnyx/types/texml/accounts/calls/siprec_siprec_sid_json_params.py">params</a>) -> <a href="./src/telnyx/types/texml/accounts/calls/siprec_siprec_sid_json_response.py">SiprecSiprecSidJsonResponse</a></code>

#### Streams

Types:

```python
from telnyx.types.texml.accounts.calls import StreamStreamingSidJsonResponse
```

Methods:

- <code title="post /texml/Accounts/{account_sid}/Calls/{call_sid}/Streams/{streaming_sid}.json">client.texml.accounts.calls.streams.<a href="./src/telnyx/resources/texml/accounts/calls/streams.py">streaming_sid_json</a>(streaming_sid, \*, account_sid, call_sid, \*\*<a href="src/telnyx/types/texml/accounts/calls/stream_streaming_sid_json_params.py">params</a>) -> <a href="./src/telnyx/types/texml/accounts/calls/stream_streaming_sid_json_response.py">StreamStreamingSidJsonResponse</a></code>

### Conferences

Types:

```python
from telnyx.types.texml.accounts import (
    ConferenceRetrieveResponse,
    ConferenceUpdateResponse,
    ConferenceRetrieveConferencesResponse,
    ConferenceRetrieveRecordingsResponse,
    ConferenceRetrieveRecordingsJsonResponse,
)
```

Methods:

- <code title="get /texml/Accounts/{account_sid}/Conferences/{conference_sid}">client.texml.accounts.conferences.<a href="./src/telnyx/resources/texml/accounts/conferences/conferences.py">retrieve</a>(conference_sid, \*, account_sid) -> <a href="./src/telnyx/types/texml/accounts/conference_retrieve_response.py">ConferenceRetrieveResponse</a></code>
- <code title="post /texml/Accounts/{account_sid}/Conferences/{conference_sid}">client.texml.accounts.conferences.<a href="./src/telnyx/resources/texml/accounts/conferences/conferences.py">update</a>(conference_sid, \*, account_sid, \*\*<a href="src/telnyx/types/texml/accounts/conference_update_params.py">params</a>) -> <a href="./src/telnyx/types/texml/accounts/conference_update_response.py">ConferenceUpdateResponse</a></code>
- <code title="get /texml/Accounts/{account_sid}/Conferences">client.texml.accounts.conferences.<a href="./src/telnyx/resources/texml/accounts/conferences/conferences.py">retrieve_conferences</a>(account_sid, \*\*<a href="src/telnyx/types/texml/accounts/conference_retrieve_conferences_params.py">params</a>) -> <a href="./src/telnyx/types/texml/accounts/conference_retrieve_conferences_response.py">ConferenceRetrieveConferencesResponse</a></code>
- <code title="get /texml/Accounts/{account_sid}/Conferences/{conference_sid}/Recordings">client.texml.accounts.conferences.<a href="./src/telnyx/resources/texml/accounts/conferences/conferences.py">retrieve_recordings</a>(conference_sid, \*, account_sid) -> <a href="./src/telnyx/types/texml/accounts/conference_retrieve_recordings_response.py">ConferenceRetrieveRecordingsResponse</a></code>
- <code title="get /texml/Accounts/{account_sid}/Conferences/{conference_sid}/Recordings.json">client.texml.accounts.conferences.<a href="./src/telnyx/resources/texml/accounts/conferences/conferences.py">retrieve_recordings_json</a>(conference_sid, \*, account_sid) -> <a href="./src/telnyx/types/texml/accounts/conference_retrieve_recordings_json_response.py">ConferenceRetrieveRecordingsJsonResponse</a></code>

#### Participants

Types:

```python
from telnyx.types.texml.accounts.conferences import (
    ParticipantRetrieveResponse,
    ParticipantUpdateResponse,
    ParticipantParticipantsResponse,
    ParticipantRetrieveParticipantsResponse,
)
```

Methods:

- <code title="get /texml/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid_or_participant_label}">client.texml.accounts.conferences.participants.<a href="./src/telnyx/resources/texml/accounts/conferences/participants.py">retrieve</a>(call_sid_or_participant_label, \*, account_sid, conference_sid) -> <a href="./src/telnyx/types/texml/accounts/conferences/participant_retrieve_response.py">ParticipantRetrieveResponse</a></code>
- <code title="post /texml/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid_or_participant_label}">client.texml.accounts.conferences.participants.<a href="./src/telnyx/resources/texml/accounts/conferences/participants.py">update</a>(call_sid_or_participant_label, \*, account_sid, conference_sid, \*\*<a href="src/telnyx/types/texml/accounts/conferences/participant_update_params.py">params</a>) -> <a href="./src/telnyx/types/texml/accounts/conferences/participant_update_response.py">ParticipantUpdateResponse</a></code>
- <code title="delete /texml/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid_or_participant_label}">client.texml.accounts.conferences.participants.<a href="./src/telnyx/resources/texml/accounts/conferences/participants.py">delete</a>(call_sid_or_participant_label, \*, account_sid, conference_sid) -> None</code>
- <code title="post /texml/Accounts/{account_sid}/Conferences/{conference_sid}/Participants">client.texml.accounts.conferences.participants.<a href="./src/telnyx/resources/texml/accounts/conferences/participants.py">participants</a>(conference_sid, \*, account_sid, \*\*<a href="src/telnyx/types/texml/accounts/conferences/participant_participants_params.py">params</a>) -> <a href="./src/telnyx/types/texml/accounts/conferences/participant_participants_response.py">ParticipantParticipantsResponse</a></code>
- <code title="get /texml/Accounts/{account_sid}/Conferences/{conference_sid}/Participants">client.texml.accounts.conferences.participants.<a href="./src/telnyx/resources/texml/accounts/conferences/participants.py">retrieve_participants</a>(conference_sid, \*, account_sid) -> <a href="./src/telnyx/types/texml/accounts/conferences/participant_retrieve_participants_response.py">ParticipantRetrieveParticipantsResponse</a></code>

### Recordings

#### Json

Methods:

- <code title="delete /texml/Accounts/{account_sid}/Recordings/{recording_sid}.json">client.texml.accounts.recordings.json.<a href="./src/telnyx/resources/texml/accounts/recordings/json.py">delete_recording_sid_json</a>(recording_sid, \*, account_sid) -> None</code>
- <code title="get /texml/Accounts/{account_sid}/Recordings/{recording_sid}.json">client.texml.accounts.recordings.json.<a href="./src/telnyx/resources/texml/accounts/recordings/json.py">retrieve_recording_sid_json</a>(recording_sid, \*, account_sid) -> <a href="./src/telnyx/types/texml/texml_get_call_recording_response_body.py">TexmlGetCallRecordingResponseBody</a></code>

### Transcriptions

#### Json

Types:

```python
from telnyx.types.texml.accounts.transcriptions import (
    JsonRetrieveRecordingTranscriptionSidJsonResponse,
)
```

Methods:

- <code title="delete /texml/Accounts/{account_sid}/Transcriptions/{recording_transcription_sid}.json">client.texml.accounts.transcriptions.json.<a href="./src/telnyx/resources/texml/accounts/transcriptions/json.py">delete_recording_transcription_sid_json</a>(recording_transcription_sid, \*, account_sid) -> None</code>
- <code title="get /texml/Accounts/{account_sid}/Transcriptions/{recording_transcription_sid}.json">client.texml.accounts.transcriptions.json.<a href="./src/telnyx/resources/texml/accounts/transcriptions/json.py">retrieve_recording_transcription_sid_json</a>(recording_transcription_sid, \*, account_sid) -> <a href="./src/telnyx/types/texml/accounts/transcriptions/json_retrieve_recording_transcription_sid_json_response.py">JsonRetrieveRecordingTranscriptionSidJsonResponse</a></code>

## Calls

Types:

```python
from telnyx.types.texml import CallUpdateResponse
```

Methods:

- <code title="post /texml/calls/{call_sid}/update">client.texml.calls.<a href="./src/telnyx/resources/texml/calls.py">update</a>(call_sid, \*\*<a href="src/telnyx/types/texml/call_update_params.py">params</a>) -> <a href="./src/telnyx/types/texml/call_update_response.py">CallUpdateResponse</a></code>

# TexmlApplications

Types:

```python
from telnyx.types import (
    TexmlApplication,
    TexmlApplicationCreateResponse,
    TexmlApplicationRetrieveResponse,
    TexmlApplicationUpdateResponse,
    TexmlApplicationListResponse,
    TexmlApplicationDeleteResponse,
)
```

Methods:

- <code title="post /texml_applications">client.texml_applications.<a href="./src/telnyx/resources/texml_applications.py">create</a>(\*\*<a href="src/telnyx/types/texml_application_create_params.py">params</a>) -> <a href="./src/telnyx/types/texml_application_create_response.py">TexmlApplicationCreateResponse</a></code>
- <code title="get /texml_applications/{id}">client.texml_applications.<a href="./src/telnyx/resources/texml_applications.py">retrieve</a>(id) -> <a href="./src/telnyx/types/texml_application_retrieve_response.py">TexmlApplicationRetrieveResponse</a></code>
- <code title="patch /texml_applications/{id}">client.texml_applications.<a href="./src/telnyx/resources/texml_applications.py">update</a>(id, \*\*<a href="src/telnyx/types/texml_application_update_params.py">params</a>) -> <a href="./src/telnyx/types/texml_application_update_response.py">TexmlApplicationUpdateResponse</a></code>
- <code title="get /texml_applications">client.texml_applications.<a href="./src/telnyx/resources/texml_applications.py">list</a>(\*\*<a href="src/telnyx/types/texml_application_list_params.py">params</a>) -> <a href="./src/telnyx/types/texml_application_list_response.py">TexmlApplicationListResponse</a></code>
- <code title="delete /texml_applications/{id}">client.texml_applications.<a href="./src/telnyx/resources/texml_applications.py">delete</a>(id) -> <a href="./src/telnyx/types/texml_application_delete_response.py">TexmlApplicationDeleteResponse</a></code>

# TextToSpeech

Types:

```python
from telnyx.types import TextToSpeechListVoicesResponse
```

Methods:

- <code title="post /text-to-speech/speech">client.text_to_speech.<a href="./src/telnyx/resources/text_to_speech.py">generate_speech</a>(\*\*<a href="src/telnyx/types/text_to_speech_generate_speech_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="get /text-to-speech/voices">client.text_to_speech.<a href="./src/telnyx/resources/text_to_speech.py">list_voices</a>(\*\*<a href="src/telnyx/types/text_to_speech_list_voices_params.py">params</a>) -> <a href="./src/telnyx/types/text_to_speech_list_voices_response.py">TextToSpeechListVoicesResponse</a></code>

# UsageReports

Types:

```python
from telnyx.types import UsageReportListResponse, UsageReportGetOptionsResponse
```

Methods:

- <code title="get /usage_reports">client.usage_reports.<a href="./src/telnyx/resources/usage_reports.py">list</a>(\*\*<a href="src/telnyx/types/usage_report_list_params.py">params</a>) -> <a href="./src/telnyx/types/usage_report_list_response.py">UsageReportListResponse</a></code>
- <code title="get /usage_reports/options">client.usage_reports.<a href="./src/telnyx/resources/usage_reports.py">get_options</a>(\*\*<a href="src/telnyx/types/usage_report_get_options_params.py">params</a>) -> <a href="./src/telnyx/types/usage_report_get_options_response.py">UsageReportGetOptionsResponse</a></code>

# UserAddresses

Types:

```python
from telnyx.types import (
    UserAddress,
    UserAddressCreateResponse,
    UserAddressRetrieveResponse,
    UserAddressListResponse,
)
```

Methods:

- <code title="post /user_addresses">client.user_addresses.<a href="./src/telnyx/resources/user_addresses.py">create</a>(\*\*<a href="src/telnyx/types/user_address_create_params.py">params</a>) -> <a href="./src/telnyx/types/user_address_create_response.py">UserAddressCreateResponse</a></code>
- <code title="get /user_addresses/{id}">client.user_addresses.<a href="./src/telnyx/resources/user_addresses.py">retrieve</a>(id) -> <a href="./src/telnyx/types/user_address_retrieve_response.py">UserAddressRetrieveResponse</a></code>
- <code title="get /user_addresses">client.user_addresses.<a href="./src/telnyx/resources/user_addresses.py">list</a>(\*\*<a href="src/telnyx/types/user_address_list_params.py">params</a>) -> <a href="./src/telnyx/types/user_address_list_response.py">UserAddressListResponse</a></code>

# UserTags

Types:

```python
from telnyx.types import UserTagListResponse
```

Methods:

- <code title="get /user_tags">client.user_tags.<a href="./src/telnyx/resources/user_tags.py">list</a>(\*\*<a href="src/telnyx/types/user_tag_list_params.py">params</a>) -> <a href="./src/telnyx/types/user_tag_list_response.py">UserTagListResponse</a></code>

# Verifications

Types:

```python
from telnyx.types import CreateVerificationResponse, Verification, VerificationRetrieveResponse
```

Methods:

- <code title="get /verifications/{verification_id}">client.verifications.<a href="./src/telnyx/resources/verifications/verifications.py">retrieve</a>(verification_id) -> <a href="./src/telnyx/types/verification_retrieve_response.py">VerificationRetrieveResponse</a></code>
- <code title="post /verifications/call">client.verifications.<a href="./src/telnyx/resources/verifications/verifications.py">trigger_call</a>(\*\*<a href="src/telnyx/types/verification_trigger_call_params.py">params</a>) -> <a href="./src/telnyx/types/create_verification_response.py">CreateVerificationResponse</a></code>
- <code title="post /verifications/flashcall">client.verifications.<a href="./src/telnyx/resources/verifications/verifications.py">trigger_flashcall</a>(\*\*<a href="src/telnyx/types/verification_trigger_flashcall_params.py">params</a>) -> <a href="./src/telnyx/types/create_verification_response.py">CreateVerificationResponse</a></code>
- <code title="post /verifications/sms">client.verifications.<a href="./src/telnyx/resources/verifications/verifications.py">trigger_sms</a>(\*\*<a href="src/telnyx/types/verification_trigger_sms_params.py">params</a>) -> <a href="./src/telnyx/types/create_verification_response.py">CreateVerificationResponse</a></code>

## ByPhoneNumber

Types:

```python
from telnyx.types.verifications import ByPhoneNumberListResponse
```

Methods:

- <code title="get /verifications/by_phone_number/{phone_number}">client.verifications.by_phone_number.<a href="./src/telnyx/resources/verifications/by_phone_number/by_phone_number.py">list</a>(phone_number) -> <a href="./src/telnyx/types/verifications/by_phone_number_list_response.py">ByPhoneNumberListResponse</a></code>

### Actions

Types:

```python
from telnyx.types.verifications.by_phone_number import VerifyVerificationCodeResponse
```

Methods:

- <code title="post /verifications/by_phone_number/{phone_number}/actions/verify">client.verifications.by_phone_number.actions.<a href="./src/telnyx/resources/verifications/by_phone_number/actions.py">verify</a>(phone_number, \*\*<a href="src/telnyx/types/verifications/by_phone_number/action_verify_params.py">params</a>) -> <a href="./src/telnyx/types/verifications/by_phone_number/verify_verification_code_response.py">VerifyVerificationCodeResponse</a></code>

## Actions

Methods:

- <code title="post /verifications/{verification_id}/actions/verify">client.verifications.actions.<a href="./src/telnyx/resources/verifications/actions.py">verify</a>(verification_id, \*\*<a href="src/telnyx/types/verifications/action_verify_params.py">params</a>) -> <a href="./src/telnyx/types/verifications/by_phone_number/verify_verification_code_response.py">VerifyVerificationCodeResponse</a></code>

# VerifiedNumbers

Types:

```python
from telnyx.types import (
    VerifiedNumber,
    VerifiedNumberDataWrapper,
    VerifiedNumberCreateResponse,
    VerifiedNumberListResponse,
)
```

Methods:

- <code title="post /verified_numbers">client.verified_numbers.<a href="./src/telnyx/resources/verified_numbers/verified_numbers.py">create</a>(\*\*<a href="src/telnyx/types/verified_number_create_params.py">params</a>) -> <a href="./src/telnyx/types/verified_number_create_response.py">VerifiedNumberCreateResponse</a></code>
- <code title="get /verified_numbers/{phone_number}">client.verified_numbers.<a href="./src/telnyx/resources/verified_numbers/verified_numbers.py">retrieve</a>(phone_number) -> <a href="./src/telnyx/types/verified_number_data_wrapper.py">VerifiedNumberDataWrapper</a></code>
- <code title="get /verified_numbers">client.verified_numbers.<a href="./src/telnyx/resources/verified_numbers/verified_numbers.py">list</a>(\*\*<a href="src/telnyx/types/verified_number_list_params.py">params</a>) -> <a href="./src/telnyx/types/verified_number_list_response.py">VerifiedNumberListResponse</a></code>
- <code title="delete /verified_numbers/{phone_number}">client.verified_numbers.<a href="./src/telnyx/resources/verified_numbers/verified_numbers.py">delete</a>(phone_number) -> <a href="./src/telnyx/types/verified_number_data_wrapper.py">VerifiedNumberDataWrapper</a></code>

## Actions

Methods:

- <code title="post /verified_numbers/{phone_number}/actions/verify">client.verified_numbers.actions.<a href="./src/telnyx/resources/verified_numbers/actions.py">submit_verification_code</a>(phone_number, \*\*<a href="src/telnyx/types/verified_numbers/action_submit_verification_code_params.py">params</a>) -> <a href="./src/telnyx/types/verified_number_data_wrapper.py">VerifiedNumberDataWrapper</a></code>

# VerifyProfiles

Types:

```python
from telnyx.types import (
    VerifyProfile,
    VerifyProfileData,
    VerifyProfileListResponse,
    VerifyProfileRetrieveTemplatesResponse,
)
```

Methods:

- <code title="post /verify_profiles">client.verify_profiles.<a href="./src/telnyx/resources/verify_profiles.py">create</a>(\*\*<a href="src/telnyx/types/verify_profile_create_params.py">params</a>) -> <a href="./src/telnyx/types/verify_profile_data.py">VerifyProfileData</a></code>
- <code title="get /verify_profiles/{verify_profile_id}">client.verify_profiles.<a href="./src/telnyx/resources/verify_profiles.py">retrieve</a>(verify_profile_id) -> <a href="./src/telnyx/types/verify_profile_data.py">VerifyProfileData</a></code>
- <code title="patch /verify_profiles/{verify_profile_id}">client.verify_profiles.<a href="./src/telnyx/resources/verify_profiles.py">update</a>(verify_profile_id, \*\*<a href="src/telnyx/types/verify_profile_update_params.py">params</a>) -> <a href="./src/telnyx/types/verify_profile_data.py">VerifyProfileData</a></code>
- <code title="get /verify_profiles">client.verify_profiles.<a href="./src/telnyx/resources/verify_profiles.py">list</a>(\*\*<a href="src/telnyx/types/verify_profile_list_params.py">params</a>) -> <a href="./src/telnyx/types/verify_profile_list_response.py">VerifyProfileListResponse</a></code>
- <code title="delete /verify_profiles/{verify_profile_id}">client.verify_profiles.<a href="./src/telnyx/resources/verify_profiles.py">delete</a>(verify_profile_id) -> <a href="./src/telnyx/types/verify_profile_data.py">VerifyProfileData</a></code>
- <code title="get /verify_profiles/templates">client.verify_profiles.<a href="./src/telnyx/resources/verify_profiles.py">retrieve_templates</a>() -> <a href="./src/telnyx/types/verify_profile_retrieve_templates_response.py">VerifyProfileRetrieveTemplatesResponse</a></code>

# VirtualCrossConnects

Types:

```python
from telnyx.types import (
    VirtualCrossConnectCreateResponse,
    VirtualCrossConnectRetrieveResponse,
    VirtualCrossConnectUpdateResponse,
    VirtualCrossConnectListResponse,
    VirtualCrossConnectDeleteResponse,
)
```

Methods:

- <code title="post /virtual_cross_connects">client.virtual_cross_connects.<a href="./src/telnyx/resources/virtual_cross_connects.py">create</a>(\*\*<a href="src/telnyx/types/virtual_cross_connect_create_params.py">params</a>) -> <a href="./src/telnyx/types/virtual_cross_connect_create_response.py">VirtualCrossConnectCreateResponse</a></code>
- <code title="get /virtual_cross_connects/{id}">client.virtual_cross_connects.<a href="./src/telnyx/resources/virtual_cross_connects.py">retrieve</a>(id) -> <a href="./src/telnyx/types/virtual_cross_connect_retrieve_response.py">VirtualCrossConnectRetrieveResponse</a></code>
- <code title="patch /virtual_cross_connects/{id}">client.virtual_cross_connects.<a href="./src/telnyx/resources/virtual_cross_connects.py">update</a>(id, \*\*<a href="src/telnyx/types/virtual_cross_connect_update_params.py">params</a>) -> <a href="./src/telnyx/types/virtual_cross_connect_update_response.py">VirtualCrossConnectUpdateResponse</a></code>
- <code title="get /virtual_cross_connects">client.virtual_cross_connects.<a href="./src/telnyx/resources/virtual_cross_connects.py">list</a>(\*\*<a href="src/telnyx/types/virtual_cross_connect_list_params.py">params</a>) -> <a href="./src/telnyx/types/virtual_cross_connect_list_response.py">VirtualCrossConnectListResponse</a></code>
- <code title="delete /virtual_cross_connects/{id}">client.virtual_cross_connects.<a href="./src/telnyx/resources/virtual_cross_connects.py">delete</a>(id) -> <a href="./src/telnyx/types/virtual_cross_connect_delete_response.py">VirtualCrossConnectDeleteResponse</a></code>

# VirtualCrossConnectsCoverage

Types:

```python
from telnyx.types import VirtualCrossConnectsCoverageListResponse
```

Methods:

- <code title="get /virtual_cross_connects_coverage">client.virtual_cross_connects_coverage.<a href="./src/telnyx/resources/virtual_cross_connects_coverage.py">list</a>(\*\*<a href="src/telnyx/types/virtual_cross_connects_coverage_list_params.py">params</a>) -> <a href="./src/telnyx/types/virtual_cross_connects_coverage_list_response.py">VirtualCrossConnectsCoverageListResponse</a></code>

# WebhookDeliveries

Types:

```python
from telnyx.types import WebhookDeliveryRetrieveResponse, WebhookDeliveryListResponse
```

Methods:

- <code title="get /webhook_deliveries/{id}">client.webhook_deliveries.<a href="./src/telnyx/resources/webhook_deliveries.py">retrieve</a>(id) -> <a href="./src/telnyx/types/webhook_delivery_retrieve_response.py">WebhookDeliveryRetrieveResponse</a></code>
- <code title="get /webhook_deliveries">client.webhook_deliveries.<a href="./src/telnyx/resources/webhook_deliveries.py">list</a>(\*\*<a href="src/telnyx/types/webhook_delivery_list_params.py">params</a>) -> <a href="./src/telnyx/types/webhook_delivery_list_response.py">WebhookDeliveryListResponse</a></code>

# WireguardInterfaces

Types:

```python
from telnyx.types import (
    WireguardInterfaceCreateResponse,
    WireguardInterfaceRetrieveResponse,
    WireguardInterfaceListResponse,
    WireguardInterfaceDeleteResponse,
)
```

Methods:

- <code title="post /wireguard_interfaces">client.wireguard_interfaces.<a href="./src/telnyx/resources/wireguard_interfaces.py">create</a>(\*\*<a href="src/telnyx/types/wireguard_interface_create_params.py">params</a>) -> <a href="./src/telnyx/types/wireguard_interface_create_response.py">WireguardInterfaceCreateResponse</a></code>
- <code title="get /wireguard_interfaces/{id}">client.wireguard_interfaces.<a href="./src/telnyx/resources/wireguard_interfaces.py">retrieve</a>(id) -> <a href="./src/telnyx/types/wireguard_interface_retrieve_response.py">WireguardInterfaceRetrieveResponse</a></code>
- <code title="get /wireguard_interfaces">client.wireguard_interfaces.<a href="./src/telnyx/resources/wireguard_interfaces.py">list</a>(\*\*<a href="src/telnyx/types/wireguard_interface_list_params.py">params</a>) -> <a href="./src/telnyx/types/wireguard_interface_list_response.py">WireguardInterfaceListResponse</a></code>
- <code title="delete /wireguard_interfaces/{id}">client.wireguard_interfaces.<a href="./src/telnyx/resources/wireguard_interfaces.py">delete</a>(id) -> <a href="./src/telnyx/types/wireguard_interface_delete_response.py">WireguardInterfaceDeleteResponse</a></code>

# WireguardPeers

Types:

```python
from telnyx.types import (
    WireguardPeerPatch,
    WireguardPeerCreateResponse,
    WireguardPeerRetrieveResponse,
    WireguardPeerUpdateResponse,
    WireguardPeerListResponse,
    WireguardPeerDeleteResponse,
    WireguardPeerRetrieveConfigResponse,
)
```

Methods:

- <code title="post /wireguard_peers">client.wireguard_peers.<a href="./src/telnyx/resources/wireguard_peers.py">create</a>(\*\*<a href="src/telnyx/types/wireguard_peer_create_params.py">params</a>) -> <a href="./src/telnyx/types/wireguard_peer_create_response.py">WireguardPeerCreateResponse</a></code>
- <code title="get /wireguard_peers/{id}">client.wireguard_peers.<a href="./src/telnyx/resources/wireguard_peers.py">retrieve</a>(id) -> <a href="./src/telnyx/types/wireguard_peer_retrieve_response.py">WireguardPeerRetrieveResponse</a></code>
- <code title="patch /wireguard_peers/{id}">client.wireguard_peers.<a href="./src/telnyx/resources/wireguard_peers.py">update</a>(id, \*\*<a href="src/telnyx/types/wireguard_peer_update_params.py">params</a>) -> <a href="./src/telnyx/types/wireguard_peer_update_response.py">WireguardPeerUpdateResponse</a></code>
- <code title="get /wireguard_peers">client.wireguard_peers.<a href="./src/telnyx/resources/wireguard_peers.py">list</a>(\*\*<a href="src/telnyx/types/wireguard_peer_list_params.py">params</a>) -> <a href="./src/telnyx/types/wireguard_peer_list_response.py">WireguardPeerListResponse</a></code>
- <code title="delete /wireguard_peers/{id}">client.wireguard_peers.<a href="./src/telnyx/resources/wireguard_peers.py">delete</a>(id) -> <a href="./src/telnyx/types/wireguard_peer_delete_response.py">WireguardPeerDeleteResponse</a></code>
- <code title="get /wireguard_peers/{id}/config">client.wireguard_peers.<a href="./src/telnyx/resources/wireguard_peers.py">retrieve_config</a>(id) -> str</code>

# Wireless

Types:

```python
from telnyx.types import WirelessRetrieveRegionsResponse
```

Methods:

- <code title="get /wireless/regions">client.wireless.<a href="./src/telnyx/resources/wireless/wireless.py">retrieve_regions</a>(\*\*<a href="src/telnyx/types/wireless_retrieve_regions_params.py">params</a>) -> <a href="./src/telnyx/types/wireless_retrieve_regions_response.py">WirelessRetrieveRegionsResponse</a></code>

## DetailRecordsReports

Types:

```python
from telnyx.types.wireless import (
    WdrReport,
    DetailRecordsReportCreateResponse,
    DetailRecordsReportRetrieveResponse,
    DetailRecordsReportListResponse,
    DetailRecordsReportDeleteResponse,
)
```

Methods:

- <code title="post /wireless/detail_records_reports">client.wireless.detail_records_reports.<a href="./src/telnyx/resources/wireless/detail_records_reports.py">create</a>(\*\*<a href="src/telnyx/types/wireless/detail_records_report_create_params.py">params</a>) -> <a href="./src/telnyx/types/wireless/detail_records_report_create_response.py">DetailRecordsReportCreateResponse</a></code>
- <code title="get /wireless/detail_records_reports/{id}">client.wireless.detail_records_reports.<a href="./src/telnyx/resources/wireless/detail_records_reports.py">retrieve</a>(id) -> <a href="./src/telnyx/types/wireless/detail_records_report_retrieve_response.py">DetailRecordsReportRetrieveResponse</a></code>
- <code title="get /wireless/detail_records_reports">client.wireless.detail_records_reports.<a href="./src/telnyx/resources/wireless/detail_records_reports.py">list</a>(\*\*<a href="src/telnyx/types/wireless/detail_records_report_list_params.py">params</a>) -> <a href="./src/telnyx/types/wireless/detail_records_report_list_response.py">DetailRecordsReportListResponse</a></code>
- <code title="delete /wireless/detail_records_reports/{id}">client.wireless.detail_records_reports.<a href="./src/telnyx/resources/wireless/detail_records_reports.py">delete</a>(id) -> <a href="./src/telnyx/types/wireless/detail_records_report_delete_response.py">DetailRecordsReportDeleteResponse</a></code>

# WirelessBlocklistValues

Types:

```python
from telnyx.types import WirelessBlocklistValueListResponse
```

Methods:

- <code title="get /wireless_blocklist_values">client.wireless_blocklist_values.<a href="./src/telnyx/resources/wireless_blocklist_values.py">list</a>(\*\*<a href="src/telnyx/types/wireless_blocklist_value_list_params.py">params</a>) -> <a href="./src/telnyx/types/wireless_blocklist_value_list_response.py">WirelessBlocklistValueListResponse</a></code>

# WirelessBlocklists

Types:

```python
from telnyx.types import (
    WirelessBlocklist,
    WirelessBlocklistCreateResponse,
    WirelessBlocklistRetrieveResponse,
    WirelessBlocklistUpdateResponse,
    WirelessBlocklistListResponse,
    WirelessBlocklistDeleteResponse,
)
```

Methods:

- <code title="post /wireless_blocklists">client.wireless_blocklists.<a href="./src/telnyx/resources/wireless_blocklists.py">create</a>(\*\*<a href="src/telnyx/types/wireless_blocklist_create_params.py">params</a>) -> <a href="./src/telnyx/types/wireless_blocklist_create_response.py">WirelessBlocklistCreateResponse</a></code>
- <code title="get /wireless_blocklists/{id}">client.wireless_blocklists.<a href="./src/telnyx/resources/wireless_blocklists.py">retrieve</a>(id) -> <a href="./src/telnyx/types/wireless_blocklist_retrieve_response.py">WirelessBlocklistRetrieveResponse</a></code>
- <code title="patch /wireless_blocklists">client.wireless_blocklists.<a href="./src/telnyx/resources/wireless_blocklists.py">update</a>(\*\*<a href="src/telnyx/types/wireless_blocklist_update_params.py">params</a>) -> <a href="./src/telnyx/types/wireless_blocklist_update_response.py">WirelessBlocklistUpdateResponse</a></code>
- <code title="get /wireless_blocklists">client.wireless_blocklists.<a href="./src/telnyx/resources/wireless_blocklists.py">list</a>(\*\*<a href="src/telnyx/types/wireless_blocklist_list_params.py">params</a>) -> <a href="./src/telnyx/types/wireless_blocklist_list_response.py">WirelessBlocklistListResponse</a></code>
- <code title="delete /wireless_blocklists/{id}">client.wireless_blocklists.<a href="./src/telnyx/resources/wireless_blocklists.py">delete</a>(id) -> <a href="./src/telnyx/types/wireless_blocklist_delete_response.py">WirelessBlocklistDeleteResponse</a></code>

# PartnerCampaigns

Types:

```python
from telnyx.types import (
    TelnyxDownstreamCampaign,
    PartnerCampaignListResponse,
    PartnerCampaignListSharedByMeResponse,
    PartnerCampaignRetrieveSharingStatusResponse,
)
```

Methods:

- <code title="get /partner_campaigns/{campaignId}">client.partner_campaigns.<a href="./src/telnyx/resources/partner_campaigns.py">retrieve</a>(campaign_id) -> <a href="./src/telnyx/types/telnyx_downstream_campaign.py">TelnyxDownstreamCampaign</a></code>
- <code title="patch /partner_campaigns/{campaignId}">client.partner_campaigns.<a href="./src/telnyx/resources/partner_campaigns.py">update</a>(campaign_id, \*\*<a href="src/telnyx/types/partner_campaign_update_params.py">params</a>) -> <a href="./src/telnyx/types/telnyx_downstream_campaign.py">TelnyxDownstreamCampaign</a></code>
- <code title="get /partner_campaigns">client.partner_campaigns.<a href="./src/telnyx/resources/partner_campaigns.py">list</a>(\*\*<a href="src/telnyx/types/partner_campaign_list_params.py">params</a>) -> <a href="./src/telnyx/types/partner_campaign_list_response.py">PartnerCampaignListResponse</a></code>
- <code title="get /partnerCampaign/sharedByMe">client.partner_campaigns.<a href="./src/telnyx/resources/partner_campaigns.py">list_shared_by_me</a>(\*\*<a href="src/telnyx/types/partner_campaign_list_shared_by_me_params.py">params</a>) -> <a href="./src/telnyx/types/partner_campaign_list_shared_by_me_response.py">PartnerCampaignListSharedByMeResponse</a></code>
- <code title="get /partnerCampaign/{campaignId}/sharing">client.partner_campaigns.<a href="./src/telnyx/resources/partner_campaigns.py">retrieve_sharing_status</a>(campaign_id) -> <a href="./src/telnyx/types/partner_campaign_retrieve_sharing_status_response.py">PartnerCampaignRetrieveSharingStatusResponse</a></code>
