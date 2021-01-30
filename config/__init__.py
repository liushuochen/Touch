from util.url import get_touch_config_url
from configparser import ConfigParser


def get_service_info():
    conf = ConfigParser()
    conf.read(get_touch_config_url())
    host = conf.get("service", "host")
    port = conf.get("service", "port")
    return host, port


def get_pool_info():
    conf = ConfigParser()
    conf.read(get_touch_config_url())
    size = conf.getint("pool", "size")
    return size
