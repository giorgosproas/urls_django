import pytest
import requests

ip="192.168.99.100"
url = "http://{}:8000/ewx123/stats".format(ip)

def test_stats_random():

    request = requests.get(url)
    status_code=request.status_code
    assert status_code==200