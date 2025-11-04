import os
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
# Replace <storage-account-name> with your actual storage account name
account_url = "https://timeman.blob.core.windows.net"
credential = DefaultAzureCredential()
# Create the BlobServiceClient object
blob_service_client = BlobServiceClient(account_url, credential=credential)

def upload_blob_file(blob_service_client, container_name):
    container_client = blob_service_client.get_container_client(container=container_name)
    
    with open(file=os.path.join('C:/Users/IliaZubov/Documents/Skillio/week 3/src/data/', 'something.txt'), mode="rb") as data:
        blob_client = container_client.upload_blob(name="report-blob.txt", data=data, overwrite=True)
        
#upload_blob_file(blob_service_client, "report-container")

container_name = "report-container"

blob_name = "report-blob.txt"

download_path = "C:/Users/IliaZubov/Downloads/report-blob.txt"

# Initialize client
blob_service_client = BlobServiceClient(account_url, credential=credential)
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

# Download blob
with open(download_path, "wb") as file:
    file.write(blob_client.download_blob().readall())