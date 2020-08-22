import os


def get_root_path() -> str:
    return "/".join(os.path.dirname(__file__).split("/")[:-1])


def get_version_config_url() -> str:
    return "/".join([get_root_path(), "config", "touch.version"])


def get_touch_config_url() -> str:
    return "/".join([get_root_path(), "config", "touch.ini"])
