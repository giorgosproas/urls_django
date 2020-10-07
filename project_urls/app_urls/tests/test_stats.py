import pytest
import requests

from app_urls.tests import constants

def test_stats_random():

    request = requests.get(constants.url)
    status_code=request.status_code
    assert status_code==200