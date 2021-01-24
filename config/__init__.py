from util.url import get_touch_config_url
from configparser import ConfigParser


def get_start_info() -> tuple:
    conf = ConfigParser()
    conf.read(get_touch_config_url())
    host = conf.get("touch", "host")
    port = conf.get("touch", "port")
    return host, port
