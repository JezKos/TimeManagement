import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient

#print(os.environ.get("AZURE_SUBSCRIPTION_ID"))

credential = DefaultAzureCredential()

subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

resourse_client = ResourceManagementClient(credential, subscription_id)

RESOURCE_GROUP_NAME = "IlElSaJes-rg"

LOCATION = "swedencentral"

STORAGE_ACCOUNT_NAME = "timeman"

CONTAINER_NAME = "report-container"

storage_client = StorageManagementClient(credential, subscription_id)
"""poller = storage_client.storage_accounts.begin_create(
RESOURCE_GROUP_NAME,
STORAGE_ACCOUNT_NAME,
{
"location": LOCATION,
"kind": "StorageV2",
"sku": {"name": "Standard_LRS"},
},
)
account_result = poller.result()
print(f"Storage account '{STORAGE_ACCOUNT_NAME}' created.")"""

container = storage_client.blob_containers.create(
RESOURCE_GROUP_NAME, STORAGE_ACCOUNT_NAME, CONTAINER_NAME, {}
)
print(f"Blob container '{CONTAINER_NAME}' created.")