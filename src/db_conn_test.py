from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Replace with your Key Vault URL
key_vault_url = "https://group3keys.vault.azure.net/"

# Authenticate and connect to Key Vault
credential = DefaultAzureCredential()
client = SecretClient(vault_url=key_vault_url, credential=credential)

# Retrieve the secret
secret_name = "db-connection-string"
retrieved_secret = client.get_secret(secret_name)
print(f"Database Connection String: {retrieved_secret.value}")
