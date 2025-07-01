"""
Main interface for lambda service.

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_lambda import (
        Client,
        FunctionActiveV2Waiter,
        FunctionActiveWaiter,
        FunctionExistsWaiter,
        FunctionUpdatedV2Waiter,
        FunctionUpdatedWaiter,
        LambdaClient,
        ListAliasesPaginator,
        ListCodeSigningConfigsPaginator,
        ListEventSourceMappingsPaginator,
        ListFunctionEventInvokeConfigsPaginator,
        ListFunctionUrlConfigsPaginator,
        ListFunctionsByCodeSigningConfigPaginator,
        ListFunctionsPaginator,
        ListLayerVersionsPaginator,
        ListLayersPaginator,
        ListProvisionedConcurrencyConfigsPaginator,
        ListVersionsByFunctionPaginator,
        PublishedVersionActiveWaiter,
    )

    session = Session()
    client: LambdaClient = session.client("lambda")

    function_active_waiter: FunctionActiveWaiter = client.get_waiter("function_active")
    function_active_v2_waiter: FunctionActiveV2Waiter = client.get_waiter("function_active_v2")
    function_exists_waiter: FunctionExistsWaiter = client.get_waiter("function_exists")
    function_updated_waiter: FunctionUpdatedWaiter = client.get_waiter("function_updated")
    function_updated_v2_waiter: FunctionUpdatedV2Waiter = client.get_waiter("function_updated_v2")
    published_version_active_waiter: PublishedVersionActiveWaiter = client.get_waiter("published_version_active")

    list_aliases_paginator: ListAliasesPaginator = client.get_paginator("list_aliases")
    list_code_signing_configs_paginator: ListCodeSigningConfigsPaginator = client.get_paginator("list_code_signing_configs")
    list_event_source_mappings_paginator: ListEventSourceMappingsPaginator = client.get_paginator("list_event_source_mappings")
    list_function_event_invoke_configs_paginator: ListFunctionEventInvokeConfigsPaginator = client.get_paginator("list_function_event_invoke_configs")
    list_function_url_configs_paginator: ListFunctionUrlConfigsPaginator = client.get_paginator("list_function_url_configs")
    list_functions_paginator: ListFunctionsPaginator = client.get_paginator("list_functions")
    list_functions_by_code_signing_config_paginator: ListFunctionsByCodeSigningConfigPaginator = client.get_paginator("list_functions_by_code_signing_config")
    list_layer_versions_paginator: ListLayerVersionsPaginator = client.get_paginator("list_layer_versions")
    list_layers_paginator: ListLayersPaginator = client.get_paginator("list_layers")
    list_provisioned_concurrency_configs_paginator: ListProvisionedConcurrencyConfigsPaginator = client.get_paginator("list_provisioned_concurrency_configs")
    list_versions_by_function_paginator: ListVersionsByFunctionPaginator = client.get_paginator("list_versions_by_function")
    ```
"""

from .client import LambdaClient
from .paginator import (
    ListAliasesPaginator,
    ListCodeSigningConfigsPaginator,
    ListEventSourceMappingsPaginator,
    ListFunctionEventInvokeConfigsPaginator,
    ListFunctionsByCodeSigningConfigPaginator,
    ListFunctionsPaginator,
    ListFunctionUrlConfigsPaginator,
    ListLayersPaginator,
    ListLayerVersionsPaginator,
    ListProvisionedConcurrencyConfigsPaginator,
    ListVersionsByFunctionPaginator,
)
from .waiter import (
    FunctionActiveV2Waiter,
    FunctionActiveWaiter,
    FunctionExistsWaiter,
    FunctionUpdatedV2Waiter,
    FunctionUpdatedWaiter,
    PublishedVersionActiveWaiter,
)

Client = LambdaClient


__all__ = (
    "Client",
    "FunctionActiveV2Waiter",
    "FunctionActiveWaiter",
    "FunctionExistsWaiter",
    "FunctionUpdatedV2Waiter",
    "FunctionUpdatedWaiter",
    "LambdaClient",
    "ListAliasesPaginator",
    "ListCodeSigningConfigsPaginator",
    "ListEventSourceMappingsPaginator",
    "ListFunctionEventInvokeConfigsPaginator",
    "ListFunctionUrlConfigsPaginator",
    "ListFunctionsByCodeSigningConfigPaginator",
    "ListFunctionsPaginator",
    "ListLayerVersionsPaginator",
    "ListLayersPaginator",
    "ListProvisionedConcurrencyConfigsPaginator",
    "ListVersionsByFunctionPaginator",
    "PublishedVersionActiveWaiter",
)
