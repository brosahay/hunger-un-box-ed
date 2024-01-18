from datetime import date
from src.interfaces.Interfaces import RequestInterface, ResponseInterface


class User(RequestInterface, ResponseInterface):
    # REQUEST
    username: str
    password: str
    grant_type: str
    client_id: str
    client_secret: str
    company_id: int
    # RESPONSE
    access_token: str
    expires_in: date
    token_type: str
    scope: str
    refresh_token: str

    def serialize(self) -> dict | None:
        return super().serialize()

    def deserialize(self, json_str: str) -> object:
        return super().deserialize(json_str)
