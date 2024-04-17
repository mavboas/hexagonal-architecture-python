import pytest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from src.app.main import app
from src.test.mock.mock_vault import return_vault_response
import json
from src.app.utils.dict_to_object import DictToObject

client = TestClient(app)


class TestTokenController:

    @patch('src.app.adapters.port_out.vault.vault.Vault')
    @patch('src.app.applications.use_cases.token.DTO.vault_dto.VaultDTO')
    def test_token_generate(self, mock_vault, mock_vault_dto):
        mock_vault.return_value.return_secret.return_value = return_vault_response()
        mock_vault_dto.private_key.return_value = MagicMock()
        response = client.post("/token", json={"grant_type": "client_credentials",
                                               "client_id": "99dc1d2b-fe01-4364-b565-072ca90c87ab",
                                               "client_secret": "ed95ac5d-001b-4406-ae84-597344337b87"})
        response_object = DictToObject(json.loads(response.text))
        assert response.status_code == 201
        assert response_object.token_type == "Bearer"
        assert response_object.expires_in == 300
    # @patch('src.app.applications.token_generate_service.TokenGenerateUseCase')
    # def test_token_generate(self, mock_token_generate_use_case):
    #     mock_token_generate_use_case.return_value.execute.return_value = Token(
    #         access_token='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI5OWRjMWQyYi1mZTAxLTQzNjQtYjU2NS0wNzJjYTkwYzg3YWIiLCJjbGllbnRfaWQiOiI5OWRjMWQyYi1mZTAxLTQzNjQtYjU2NS0wNzJjYTkwYzg3YWIiLCJpYXQiOjE3MTMzMDMzOTAsImV4cCI6MTcxMzMwMzY5MH0.XZh_bieL3wH7MSE49_XFCrcaLizVGqppT9N88HZO6xZ_wB5dAkiQlWSyjMTbb4uj5kOFb9glrfV30xw15WM8Q4zM67d_eeMp2Db1TGNvAIV65UzRcg3ezJuone5ZPUYVrZQv8x5rRyDDIdqkd9ecO5oqad0oxnhsgo5rbEYeuu7ENz2Rm_fYrqCC4ZGdh54gi6270nwjcHhRvUYWwGlhDFzn0SPUmqkFh9aLPiOaQJeUJCNswDJhnebzQNg-RoseTckRrCMxRlHIycIMB3f6R3oZGVD9ync0bUL0baE9oZQJbrH4-6nEncGNafGgnUleMmgfaGqUhATTnojYN-X_SA',
    #         token_type='Bearer',
    #         expires_in=300,
    #         refresh_token='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI5OWRjMWQyYi1mZTAxLTQzNjQtYjU2NS0wNzJjYTkwYzg3YWIiLCJjbGllbnRfaWQiOiI5OWRjMWQyYi1mZTAxLTQzNjQtYjU2NS0wNzJjYTkwYzg3YWIiLCJpYXQiOjE3MTMzMDMzOTAsImV4cCI6MTcxMzMwMzY5MH0.XZh_bieL3wH7MSE49_XFCrcaLizVGqppT9N88HZO6xZ_wB5dAkiQlWSyjMTbb4uj5kOFb9glrfV30xw15WM8Q4zM67d_eeMp2Db1TGNvAIV65UzRcg3ezJuone5ZPUYVrZQv8x5rRyDDIdqkd9ecO5oqad0oxnhsgo5rbEYeuu7ENz2Rm_fYrqCC4ZGdh54gi6270nwjcHhRvUYWwGlhDFzn0SPUmqkFh9aLPiOaQJeUJCNswDJhnebzQNg-RoseTckRrCMxRlHIycIMB3f6R3oZGVD9ync0bUL0baE9oZQJbrH4-6nEncGNafGgnUleMmgfaGqUhATTnojYN-X_SA'
    #     )
    #     token_generate_service = TokenGenerateService('client_credentials', '99dc1d2b-fe01-4364-b565-072ca90c87ab',
    #                                                   '99dc1d2b-fe01-4364-b565-072ca90c87ab')
    #     assert token_generate_service.token_generate() == Token(
    #         access_token='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI5OWRjMWQyYi1mZTAxLTQzNjQtYjU2NS0wNzJjYTkwYzg3YWIiLCJjbGllbnRfaWQiOiI5OWRjMWQyYi1mZTAxLTQzNjQtYjU2NS0wNzJjYTkwYzg3YWIiLCJpYXQiOjE3MTMzMDMzOTAsImV4cCI6MTcxMzMwMzY5MH0.XZh_bieL3wH7MSE49_XFCrcaLizVGqppT9N88HZO6xZ_wB5dAkiQlWSyjMTbb4uj5kOFb9glrfV30xw15WM8Q4zM67d_eeMp2Db1TGNvAIV65UzRcg3ezJuone5ZPUYVrZQv8x5rRyDDIdqkd9ecO5oqad0oxnhsgo5rbEYeuu7ENz2Rm_fYrqCC4ZGdh54gi6270nwjcHhRvUYWwGlhDFzn0SPUmqkFh9aLPiOaQJeUJCNswDJhnebzQNg-RoseTckRrCMxRlHIycIMB3f6R3oZGVD9ync0bUL0baE9oZQJbrH4-6nEncGNafGgnUleMmgfaGqUhATTnojYN-X_SA',
    #         token_type='Bearer',
    #         expires_in=300,
    #         refresh_token='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI5OWRjMWQyYi1mZTAxLTQzNjQtYjU2NS0wNzJjYTkwYzg3YWIiLCJjbGllbnRfaWQiOiI5OWRjMWQyYi1mZTAxLTQzNjQtYjU2NS0wNzJjYTkwYzg3YWIiLCJpYXQiOjE3MTMzMDMzOTAsImV4cCI6MTcxMzMwMzY5MH0.XZh_bieL3wH7MSE49_XFCrcaLizVGqppT9N88HZO6xZ_wB5dAkiQlWSyjMTbb4uj5kOFb9glrfV30xw15WM8Q4zM67d_eeMp2Db1TGNvAIV65UzRcg3ezJuone5ZPUYVrZQv8x5rRyDDIdqkd9ecO5oqad0oxnhsgo5rbEYeuu7ENz2Rm_fYrqCC4ZGdh54gi6270nwjcHhRvUYWwGlhDFzn0SPUmqkFh9aLPiOaQJeUJCNswDJhnebzQNg-RoseTckRrCMxRlHIycIMB3f6R3oZGVD9ync0bUL0baE9oZQJbrH4-6nEncGNafGgnUleMmgfaGqUhATTnojYN-X_SA'
    #     )
    #
    # def test_token_generate_error_grant_type(self):
    #     token_generate_service = TokenGenerateService('resource_onwer', '99dc1d2b-fe01-4364-b565-072ca90c87ab',
    #                                                   '99dc1d2b-fe01-4364-b565-072ca90c87ab')
    #     with pytest.raises(HTTPException) as excinfo:
    #         token_generate_service.token_generate()
    #     assert excinfo.value.status_code == 401
    #     assert excinfo.value.detail == {'code': 101, 'message': 'Invalid authentication method'}
