# EasybillPythonClient

An Eaybill API Client generator for Python.

To update the client, pull this repository and run the following command:

```bash
make
```

Afterwards push the changes to the repository.
Create a new tag on the remote repository.
Name it according to the API version so that it stays uniform.

## Installation

The client can be installed via pip:

```bash
pip install "git+https://hendrik-pfaffendorf-navcomm:<token>@github.com/hendrik-pfaffendorf-navcomm/EasybillPythonClient.git@main#egg=easybill_client&subdirectory=easybill_client_package"
```

The token is saved in 1Password under the name `EasybillPythonClient Pip Token`
