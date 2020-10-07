import pytest
import requests
import json


from app_urls.tests import constants

from app_urls.utils.regexUtils import isValidShortcode
from app_urls.utils.shortcodeGenerator import get_shortcode
from app_urls.utils.datetimeUtils import militaryTimeNow
from app_urls.models import URLS

def test_shorten_existingUrlLink():

    #Check if there is any item with shortcode 999999 in the database and if yes delete it.
    item = URLS.objects.filter(shortcode="999999")
    if len(item)==1:
        item.delete()

    # Create a new item with url https://www.google.pl and shortcode 999999
    item = URLS(url="https://www.google.pl",shortcode="999999",created=militaryTimeNow(),\
                            lastRedirect="",redirectCount=0)
    item.save()

    # Request shorten link with an already existing url (which has just been added to the database)
    body = {"url":"https://www.google.pl/"}
    request = requests.post(url=constants.urlShorten,data=json.dumps(body),verify=False)
    status_code=request.status_code
    
    # Assert that the status code is 409 and the error message is the correct on
    assert status_code==409

    jsonResponse = request.json()
    assert(jsonResponse["ERROR"]=="URL already in use")

    # Delete the item that has been added to the database
    item = URLS.objects.filter(shortcode="999999")[0]
    item.delete()
    
    

