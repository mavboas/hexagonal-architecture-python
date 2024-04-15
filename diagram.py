from diagrams import Diagram
from diagrams.onprem.security import Vault
from diagrams.onprem.client import Client
from diagrams.onprem.compute import Server


with Diagram("authentication_app", show=False):
    Client("Client") >> Server("Application") >> Vault("HashiCorpVault")
