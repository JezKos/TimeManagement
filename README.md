# TimeManagement

## Creating the database and tables



## Creating virtual environment

`python3 -m venv venv`

Installing packages and creating requirements file.

pip freeze > requirements.txt


## Creating VM and managing access/identity

- Followed the steps of the rosehosting tutorial to setup ubuntu22.04 on the VM.
- Virtual environment from the requirements.txt


Storage account -> Shared access signature, add VM IP to allowed IP-addresses
- Identity: managed-identity on
- Access control: Add role storage account contributor
- Need permissions from account manager



## Postman + Flask on VM (postVM)

- Add port (5000) in Azure to the allowed ports:
`az vm open-port --resource-group $RESOURCE_GROUP --name $VM2_NAME --port 5000 --priority 1001`
- app.run(host='0.0.0.0') # show the app endpoints to external
- keep the app Running on the VM

## reportvm

- SQL query + save report
- SDK to send the report to blob storage

## ssh key

We generated ssh-keys for connecting our github repo with our VM. 

`ssh-keygen  -t ed25519 -C "email"`

Added the public and private keys to our VM and the public key as deploy key to the github repo. 

Troubleshooting: ssh connection not working, not permissions to pull.
- `eval $(ssh-agent -s)`
- `ssh-add ~/.ssh/id_rsa`

## Azure key vault

Adding keys in Azure to the group.
- Add permissions to the key vault to the VMs