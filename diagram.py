from diagrams import Diagram
from diagrams.aws.compute import Fargate
from diagrams.onprem.security import Vault
from diagrams.onprem.client import Client
from diagrams.aws.network import NLB
from diagrams.aws.network import APIGateway


with Diagram("authentication_app", show=False):
    Client("Client") >> APIGateway("gtw") >> NLB("NLB") >>Fargate("AuthenticationApp") >> Vault("HashiCorpVault")



