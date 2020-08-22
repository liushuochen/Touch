from util.url import get_version_config_url


def get_version() -> str:
    with open(get_version_config_url(), "r") as file:
        version = file.read().strip()
    return version
