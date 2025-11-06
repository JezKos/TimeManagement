import os
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from datetime import datetime

account_url = "https://timeman.blob.core.windows.net"
credential = DefaultAzureCredential()
# Create the BlobServiceClient object
blob_service_client = BlobServiceClient(account_url, credential=credential)
#blob_service_client = BlobServiceClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=timeman;AccountKey=174prRRvf77WFNCWTCSezs0cJzoqTPIYXms3DTwjwNbgiEFOBj1B/x2lECVtGMFWMFddM8iq3wk0+AStm+tVDQ==;EndpointSuffix=core.windows.net")
today_stamp = datetime.today()
def upload_blob_file(blob_service_client, container_name):
    container_client = blob_service_client.get_container_client(container=container_name)
    
    with open(file=os.path.join('/home/azureuser/TimeManagement/src', 'dailyreport.csv'), mode="rb") as data:
        blob_client = container_client.upload_blob(name=f"dailyreport {today_stamp}.csv", data=data, overwrite=True)
    
    with open(file=os.path.join('/home/azureuser/TimeManagement/src', 'customer_dailyreport.csv'), mode="rb") as data:
        container_client.upload_blob(name=f"customer_dailyreport {today_stamp}.csv", data=data, overwrite=True)
        
upload_blob_file(blob_service_client, "report-container")

#container_name = "report-container"

#blob_name = "report-blob.txt"

# download_path = "C:/Users/IliaZubov/Downloads/report-blob.txt"

# Initialize client
#blob_service_client = BlobServiceClient(account_url, credential=credential)
#blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

# Download blob
#with open(download_path, "wb") as file:
   # file.write(blob_client.download_blob().readall())
