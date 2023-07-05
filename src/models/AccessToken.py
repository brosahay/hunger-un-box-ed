import src.interfaces.Interfaces as Interfaces


class AccessTokenResponse(Interfaces.ResponseInterface):
    access_token: str
    expires_in: int
    token_type: str
    scope: str
    refresh_token: str


class AccessTokenRequest(Interfaces.RequestInterface):
    username: str
    password: str
    grant_type: str
    client_id: str
    client_secret: str
    company_id: int
