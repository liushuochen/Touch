from util.url import get_touch_config_url
from configparser import ConfigParser


def get_start_info() -> tuple:
    config = ConfigParser()
    config.read(get_touch_config_url())
    host = config.get("touch", "host")
    port = config.get("touch", "port")
    return host, port
