from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view

from app_urls.utils.response import errorResponse, successfulResponse
from app_urls.utils.regexUtils import isValidShortcode
from app_urls.utils.shortcodeGenerator import get_shortcode
from app_urls.utils.datetimeUtils import militaryTimeNow

from app_urls.models import URLS

import json

# Create your views here
@api_view(['POST'])
@csrf_exempt 
def shortenView(request):
    jsonResponse = json.loads(request.body.decode('utf8'))

    # First check if url exists in the request body
    # If url exists in request body then read the value of the url
    # If the value of url already exists in database return error code 409
    # If the value of url doesnt already exist in database then continue with reading shortcode
    # If url does not exist in the request body return error code 400.
    try:
        url=jsonResponse["url"]
        if URLS.objects.filter(url=url).exists():
                return errorResponse("409","URL already in use")
    except:
        return errorResponse("400",'Url not present')

    # Check if the shortcode exists in request body. If True then do all actions mentioned below.
    # If not then create a new random shortcode and loop until this random shortcode is not in the database
    # When the new shortcode is not in the database create a new item with this shortcode.
    try:
        shortcode=jsonResponse["shortcode"]
        # Check is shortcode is valid or not. If shortcode is not valid return error code 412
        # If shortcode is valid then check if shortcode is already in the database or not.
        # If the valid shortcode is already in the database then return an error code and if 
        # the shortcode is not in the database then create a new item in the database and return
        # successfull code.
        if isValidShortcode(shortcode):
            if URLS.objects.filter(shortcode=shortcode).exists():
                return errorResponse("409","Shortcode already in use")
            else:
                item = URLS(url=url,shortcode=shortcode,created=militaryTimeNow(),\
                            lastRedirect="",redirectCount=0)
                item.save()
                return successfulResponse("201",{"shortcode":shortcode}) 
        else:
            return errorResponse("412",'The provided shortcode is invalid')      
    except:
        while True:
            shortcode = get_shortcode(6)
            if not URLS.objects.filter(shortcode=shortcode).exists():
                item = URLS(url=url,shortcode=shortcode,created=militaryTimeNow(),\
                            lastRedirect="",redirectCount=0)
                item.save()
                break
        return successfulResponse("201",{"shortcode":shortcode})

@api_view(['GET'])
@csrf_exempt     
def shortcodeView(request,shortcode):
    if URLS.objects.filter(shortcode=shortcode).exists():
        #TODO
        pass
    else:
        return errorResponse("404","Shortcode not found")

    
@api_view(['GET'])
@csrf_exempt     
def shortcodeStatsView(request,shortcode):
    if URLS.objects.filter(shortcode=shortcode).exists():
        obj=URLS.objects.filter(shortcode=shortcode)[0]
        return successfulResponse("200",{"created":obj.created,\
                                         "lastRedirect":obj.lastRedirect,\
                                         "redirectCount":obj.redirectCount})
    else:
        return errorResponse("404","Shortcode not found")
