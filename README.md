# TimeManagement

## Creating the database and tables


## Creating virtual environment

`python3 -m venv venv`



## Creating VM and managing access/identity

- Followed the steps to setup ubuntu22.04 on the VM.
- Virtual environment from the requirements.txt

Storage account -> Shared access signature

## ssh key

We generated ssh-keys for connecting our github repo with our VM. 

`ssh-keygen  -t ed25519 -C "email"`

Added the public and private keys to our VM and the public key as deploy key to the github repo. 

Troubleshooting: ssh connection not working, not permissions to pull.
- `eval $(ssh-agent -s)`
- `ssh-add ~/.ssh/id_rsa`

## 