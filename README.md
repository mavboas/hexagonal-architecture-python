# Hexagonal architecture with python and fastapi

This project was created in order to exemplify some concepts about fast api and hexagonal architecture.

## Application

The principal object of this application is to provide two method to simulate a STS application.

## Endpoints:

| Method       | description                                                                        | 
|--------------|------------------------------------------------------------------------------------|
| POST: /token | Method responsible to generate a token based in client credentials passed via body | 
| GET: /token  | Method responsible to validate de token passed by query parameters                 |

```
POST: /token 
Request: 
    curl -X 'POST' \
      'http://127.0.0.1:8000/token' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "grant_type": "string",
      "client_secret": "string",
      "client_id": "string"
    }'
Response:
{
	"access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI5OWRjMWQyYi1mZTAxLTQzNjQtYjU2NS0wNzJjYTkwYzg3YWIiLCJjbGllbnRfaWQiOiI5OWRjMWQyYi1mZTAxLTQzNjQtYjU2NS0wNzJjYTkwYzg3YWIiLCJpYXQiOjE3MTMwNTg1NDcsImV4cCI6MTcxMzA1ODg0N30.l7CQmvGASRLg5JdND1ev-sEcPi7PF-vv3sGEp_oOXuZBPVTw4HaIOGHZwvL9yt0D_QRRrGeaBAjBhQhIGUSsekr-0vg6BzQoM4xdWxOUCfFGiemqJNr4myYJaJ10-G52RkFIbvpfsIIr4-RNcIVUCCAa28LA-jR4Akw1irOxq1JUCGpuRsyvyaiXe5r3gOXqy8l6WKeyAPrxX18f022t2WdeQLiRwwO8p942IqVj5ffbHApjqb3yzLorrk3U3LUsE8nR87k8e8prrxls_XYnQTWart0FeV4CYs25_M4lEltnnaN61hG1CLPiULgu8KjR7BJZs6Ujj4GztwjU2gkAlg",
	"token_type": "Bearer",
	"expires_in": 300,
	"refresh_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI5OWRjMWQyYi1mZTAxLTQzNjQtYjU2NS0wNzJjYTkwYzg3YWIiLCJjbGllbnRfaWQiOiI5OWRjMWQyYi1mZTAxLTQzNjQtYjU2NS0wNzJjYTkwYzg3YWIiLCJpYXQiOjE3MTMwNTg1NDcsImV4cCI6MTcxMzA1ODg0N30.l7CQmvGASRLg5JdND1ev-sEcPi7PF-vv3sGEp_oOXuZBPVTw4HaIOGHZwvL9yt0D_QRRrGeaBAjBhQhIGUSsekr-0vg6BzQoM4xdWxOUCfFGiemqJNr4myYJaJ10-G52RkFIbvpfsIIr4-RNcIVUCCAa28LA-jR4Akw1irOxq1JUCGpuRsyvyaiXe5r3gOXqy8l6WKeyAPrxX18f022t2WdeQLiRwwO8p942IqVj5ffbHApjqb3yzLorrk3U3LUsE8nR87k8e8prrxls_XYnQTWart0FeV4CYs25_M4lEltnnaN61hG1CLPiULgu8KjR7BJZs6Ujj4GztwjU2gkAlg"
}
```

```
GET: /token 
Request: 
curl --request GET \
  --url 'http://127.0.0.1:8000/token?token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI5OWRjMWQyYi1mZTAxLTQzNjQtYjU2NS0wNzJjYTkwYzg3YWIiLCJjbGllbnRfaWQiOiI5OWRjMWQyYi1mZTAxLTQzNjQtYjU2NS0wNzJjYTkwYzg3YWIiLCJpYXQiOjE3MTMwNTg1NDcsImV4cCI6MTcxMzA1ODg0N30.l7CQmvGASRLg5JdND1ev-sEcPi7PF-vv3sGEp_oOXuZBPVTw4HaIOGHZwvL9yt0D_QRRrGeaBAjBhQhIGUSsekr-0vg6BzQoM4xdWxOUCfFGiemqJNr4myYJaJ10-G52RkFIbvpfsIIr4-RNcIVUCCAa28LA-jR4Akw1irOxq1JUCGpuRsyvyaiXe5r3gOXqy8l6WKeyAPrxX18f022t2WdeQLiRwwO8p942IqVj5ffbHApjqb3yzLorrk3U3LUsE8nR87k8e8prrxls_XYnQTWart0FeV4CYs25_M4lEltnnaN61hG1CLPiULgu8KjR7BJZs6Ujj4GztwjU2gkAlg' \
  --header 'accept: application/json'
Response:
{
	"client_id": "99dc1d2b-fe01-4364-b565-072ca90c87ab",
	"iat": 1713058547,
	"exp": 1713058847,
	"validate": true,
	"time_to_expire": "0:03:57.927275"
}
```

## How set the application

1. You will need set the environment variable bellow:

```
ENV=dev
```

2. You all will need set a hashicorp vault, in order to fulfil this requirement, you can use this documentation:
   https://hub.docker.com/r/hashicorp/vault

3. After the start of vault application that was necessary set the access token and config.yaml file:

```
  vault_token: "s.VrKSUVKmrtZGMdV6MiFLVW7Z"
```

4. To finish, you will need set your credentials in vault in the path /credentials informing the client_id,
   client_secret, grant_type, public_key e private_key.
```
  {
    "grant_type": "client_credentials",
    "client_id": "99dc1d2b-fe01-4364-b565-072ca90c87ab",
    "client_secret": "ed95ac5d-001b-4406-ae84-597344337b87",
    "public_key": "base64 your public_key.pem",
    "private_key": "base64 your private_key.pem"
}
```

