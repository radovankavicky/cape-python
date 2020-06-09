from cape.utils import base64

SECRET_BYTES = 16
VERSION = b"\x01"


class APIToken:
    token_id: str
    version: bytes
    secret: bytes
    raw: str

    def __init__(self, token: str):
        self.raw = token
        splits = token.split(",")
        self.token_id = splits[0]

        token_bytes = bytes(base64.from_string(splits[1]))
        self.version = token_bytes[0]
        self.secret = token_bytes[1:]


def create_api_token(token_id, secret) -> APIToken:
    token_bytes = bytes(VERSION) + bytes(secret, "utf-8")
    b64 = base64.Base64(token_bytes)

    token = f"{token_id},{b64}"

    return APIToken(token)