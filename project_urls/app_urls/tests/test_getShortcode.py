import pytest
import requests
import json

from app_urls.tests import constants
from app_urls.models import URLS


def test_getShortcode_smoke():

    # Check if in the database we already have the specific url and delete it.
    item = URLS.objects.filter(url=constants.testValueUrl)
    if len(item)==1:
        item.delete()

    # Check if in the database we already have the specific shortcode and delete it.
    item = URLS.objects.filter(shortcode=constants.testValueShortcode)
    if len(item)==1:
        item.delete()


    # Add new item in database to check request it.
    body = {"url":constants.testValueUrl,"shortcode":constants.testValueShortcode}
    request = requests.post(url=constants.urlShorten,data=json.dumps(body),verify=False)

    # request the GET /shortcode API with the newly added item
    request = requests.get(url=constants.urlGetShortcode,verify=False,allow_redirects=False)
    status_code=request.status_code
    
    # Assert that the status code is 302 and the error message is the correct one
    assert status_code==302

    # Assert that the header location is the URL of the specified shortcode.
    assert(request.headers['Location']==URLS.objects.filter(shortcode=constants.testValueShortcode)[0].url)

    # Delete the item that has just been added
    item = URLS.objects.filter(url=constants.testValueUrl)
    if len(item)==1:
        item.delete()



def test_getShortcode_shortcodeNotFound():

    # Check if in the database we already have the specific url and delete it.
    item = URLS.objects.filter(url=constants.testValueUrl)
    if len(item)==1:
        item.delete()

    # Check if in the database we already have the specific shortcode and delete it.
    item = URLS.objects.filter(shortcode=constants.testValueShortcode)
    if len(item)==1:
        item.delete()

    # request the GET /shortcode API with shortcode that does not exist in the database
    request = requests.get(url=constants.urlGetShortcode,verify=False,allow_redirects=False)
    status_code=request.status_code
    
    # Assert that the status code is 404 and the error message is the correct one
    assert status_code==404

    # Assert that the message returned is the correct one
    jsonResponse = request.json()
    assert(jsonResponse["ERROR"]=="Shortcode not found")


    # Delete the item that has just been added
    item = URLS.objects.filter(url=constants.testValueUrl)
    if len(item)==1:
        item.delete()