import pytest
import requests
import json

from app_urls.tests import constants
from app_urls.models import URLS
from app_urls.utils.datetimeUtils import militaryTimeNow, compareMilitaryTime

def test_stats_notFoundShortcode():

    # Check if in the database we already have the specific shortcode and delete it.
    item = URLS.objects.filter(shortcode=constants.testValueShortcode)
    if len(item)==1:
        item.delete()

    # Check the stats for a non existing shortcode
    request = requests.get(url=constants.urlShortcodeStats,verify=False)

    # Assert that the status_code is 404 and the error message is the correct one
    status_code=request.status_code
    assert status_code==404

    # Assert that the message returned is the correct one
    jsonResponse = request.json()
    assert(jsonResponse["ERROR"]=="Shortcode not found")


def test_stats_smoke():

    # Check if in the database we already have the specific url and delete it.
    item = URLS.objects.filter(url=constants.testValueUrl)
    if len(item)==1:
        item.delete()

    # Check if in the database we already have the specific shortcode and delete it.
    item = URLS.objects.filter(shortcode=constants.testValueShortcode)
    if len(item)==1:
        item.delete()


    # Create a new item with url https://www.google.pl and shortcode 999999
    item = URLS(url=constants.testValueUrl,shortcode=constants.testValueShortcode,created=militaryTimeNow(),\
                            lastRedirect="",redirectCount=0)
    item.save()

    # request the GET /shortcode API with shortcode that does not exist in the database
    # This request is used in order one redirection to happen
    requestRedirect = requests.get(url=constants.urlGetShortcode,verify=False)

    # Check the stats for an existing shortcode
    request = requests.get(url=constants.urlShortcodeStats,verify=False)


    # Assert that the status_code is 404 and the error message is the correct one
    status_code=request.status_code
    assert status_code==200

    # Assert that count has been increased by 1
    jsonResponse = request.json()
    assert jsonResponse["redirectCount"]==1

    #!TODO: The two checks below must become more precise
    # assert last redirect is less than 5 seconds now
    assert(compareMilitaryTime(militaryTimeNow(),jsonResponse["lastRedirect"]).seconds<=5)

    # assert time created is less than 5 seconds now
    assert(compareMilitaryTime(militaryTimeNow(),jsonResponse["created"]).seconds<=5)

