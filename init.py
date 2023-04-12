from casdoor import AsyncCasdoorSDK

from .settings import AuthSettings, AuthSettingFromEnvFile


casdoor: AsyncCasdoorSDK = None
auth_settings: AuthSettings = None


def init_casdoor(settings: AuthSettings = None):
    if not settings:
        settings = AuthSettingFromEnvFile()

    global auth_settings
    auth_settings = settings

    global casdoor
    casdoor = AsyncCasdoorSDK(
        auth_settings.AUTH_ENDPOINT,
        auth_settings.AUTH_CLIENT_ID,
        auth_settings.AUTH_CLIENT_SECRET,
        auth_settings.AUTH_CERT,
        auth_settings.AUTH_ORG_NAME,
        auth_settings.AUTH_APP_NAME,
    )


def get_caseoor() -> AsyncCasdoorSDK:
    return casdoor


def get_auth_settings() -> AuthSettings:
    return auth_settings
