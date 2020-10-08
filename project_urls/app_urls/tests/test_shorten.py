import pytest
import requests
import json


from app_urls.tests import constants
from app_urls.utils.regexUtils import isValidShortcode
from app_urls.utils.shortcodeGenerator import get_shortcode
from app_urls.utils.datetimeUtils import militaryTimeNow
from app_urls.models import URLS

def test_shorten_smoke():

    # Check if in the database we already have the specific url and delete it.
    item = URLS.objects.filter(url=constants.testValueUrl)
    if len(item)==1:
        item.delete()

    # Check if in the database we already have the specific shortcode and delete it.
    item = URLS.objects.filter(shortcode=constants.testValueShortcode)
    if len(item)==1:
        item.delete()


    # Request shorten link with both url and shortcode that dont already exist.
    body = {"url":constants.testValueUrl,"shortcode":constants.testValueShortcode}
    request = requests.post(url=constants.urlShorten,data=json.dumps(body),verify=False)
    status_code=request.status_code
    
    # Assert that the status code is 201 and the error message is the correct one
    assert status_code==201

    jsonResponse = request.json()
    assert(jsonResponse["shortcode"]==constants.testValueShortcode)

    # Delete the item that has just been added
    item = URLS.objects.filter(url=constants.testValueUrl)
    if len(item)==1:
        item.delete()

def test_shorten_shortCodeAlreadyInUse():

    # Check if in the database we already have item with the specific url and delete it.
    item = URLS.objects.filter(url=constants.testValueUrl)
    if len(item)==1:
        item.delete()

    # Check if in the database we already have item the specific shortcode and delete it.
    item = URLS.objects.filter(shortcode=constants.testValueShortcode)
    if len(item)==1:
        item.delete()

    # Create a new item with url https://www.google.pl and shortcode 999999
    item = URLS(url=constants.testValueUrl,shortcode=constants.testValueShortcode,created=militaryTimeNow(),\
                            lastRedirect="",redirectCount=0)
    item.save()


    # Request shorten link with url not existing and shortcode already existing.
    body = {"url":"http://www.hello_world.com","shortcode":constants.testValueShortcode}
    request = requests.post(url=constants.urlShorten,data=json.dumps(body),verify=False)
    status_code=request.status_code
    
    # Assert that the status code is 409 and the error message is the correct one
    assert status_code==409

    jsonResponse = request.json()
    assert(jsonResponse["ERROR"]=="Shortcode already in use")

    # Delete the item that has just been added
    item = URLS.objects.filter(url=constants.testValueUrl)
    if len(item)==1:
        item.delete()

def test_shorten_existingUrlLink():

    #Check if there is any item with shortcode 999999 in the database and if yes delete it.
    item = URLS.objects.filter(shortcode=constants.testValueShortcode)
    if len(item)==1:
        item.delete()

    # Create a new item with url https://www.google.pl and shortcode 999999
    item = URLS(url=constants.testValueUrl,shortcode=constants.testValueShortcode,created=militaryTimeNow(),\
                            lastRedirect="",redirectCount=0)
    item.save()

    # Request shorten link with an already existing url (which has just been added to the database)
    body = {"url":constants.testValueUrl}
    request = requests.post(url=constants.urlShorten,data=json.dumps(body),verify=False)
    status_code=request.status_code
    
    # Assert that the status code is 409 and the error message is the correct on
    assert status_code==409

    jsonResponse = request.json()
    assert(jsonResponse["ERROR"]=="URL already in use")

    # Delete the item that has been added to the database
    item = URLS.objects.filter(shortcode=constants.testValueShortcode)[0]
    item.delete()


def test_shorten_urlNotPresent():
    # Request shorten link with no url.
    body = {"shortcode":constants.testValueShortcode}
    request = requests.post(url=constants.urlShorten,data=json.dumps(body),verify=False)
    status_code=request.status_code
    
    # Assert that the status code is 400 and the error message is the correct on
    assert status_code==400

    jsonResponse = request.json()
    assert(jsonResponse["ERROR"]=="Url not present")
    
    
def test_shorten_longShortcode():

    # Check if in the database we already have the specific url and delete it.
    item = URLS.objects.filter(url=constants.testValueUrl)
    if len(item)==1:
        item.delete()

    # Request shorten link with long shortcode.
    body = {"url":constants.testValueUrl,"shortcode":"1234567"}
    request = requests.post(url=constants.urlShorten,data=json.dumps(body),verify=False)
    status_code=request.status_code
    
    # Assert that the status code is 412 and the error message is the correct one
    assert status_code==412

    jsonResponse = request.json()
    assert(jsonResponse["ERROR"]=="The provided shortcode is invalid")

def test_shorten_shortShortcode():

    # Check if in the database we already have the specific url and delete it.
    item = URLS.objects.filter(url=constants.testValueUrl)
    if len(item)==1:
        item.delete()

    # Request shorten link with short shortcode.
    body = {"url":constants.testValueUrl,"shortcode":"12345"}
    request = requests.post(url=constants.urlShorten,data=json.dumps(body),verify=False)
    status_code=request.status_code
    
    # Assert that the status code is 412 and the error message is the correct one
    assert status_code==412

    jsonResponse = request.json()
    assert(jsonResponse["ERROR"]=="The provided shortcode is invalid")

def test_shorten_extraCharacterInShortcode():

    # Check if in the database we already have the specific url and delete it.
    item = URLS.objects.filter(url=constants.testValueUrl)
    if len(item)==1:
        item.delete()

    # Request shorten link with no url.
    body = {"url":constants.testValueUrl,"shortcode":"12345+"}
    request = requests.post(url=constants.urlShorten,data=json.dumps(body),verify=False)
    status_code=request.status_code
    
    # Assert that the status code is 412 and the error message is the correct one
    assert status_code==412

    jsonResponse = request.json()
    assert(jsonResponse["ERROR"]=="The provided shortcode is invalid")

def test_shorten_noShortcode():

    # Check if in the database we already have the specific url and delete it.
    item = URLS.objects.filter(url=constants.testValueUrl)
    if len(item)==1:
        item.delete()


    # Request shorten link with no shortcode.
    body = {"url":constants.testValueUrl}
    request = requests.post(url=constants.urlShorten,data=json.dumps(body),verify=False)
    status_code=request.status_code
    
    # Assert that the status code is 201 and the error message is the correct one
    assert status_code==201

    jsonResponse = request.json()
    assert(isValidShortcode(jsonResponse["shortcode"]))

    # Delete the Url thas has just been added
    item = URLS.objects.filter(url=constants.testValueUrl)
    if len(item)==1:
        item.delete()



