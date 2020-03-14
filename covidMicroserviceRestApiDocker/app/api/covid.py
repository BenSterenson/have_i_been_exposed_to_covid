import base64
import logging
import datetime
from requests import codes

logger = logging.getLogger('cves_micro_service')


def post_greeting(name):
    return 'Hello {name}'.format(name=name)
