from pydantic import BaseSettings


class AuthSettings(BaseSettings):
    """Casdoor settings."""
    AUTH_ENDPOINT: str
    AUTH_CLIENT_ID: str
    AUTH_CLIENT_SECRET: str
    AUTH_CERT: str
    AUTH_ORG_NAME: str
    AUTH_APP_NAME: str
    # AUTH_FORCE_USER_ACTIVATED = False


class AuthSettingFromEnvFile(AuthSettings):
    class Config:
        env_file = '.env'

