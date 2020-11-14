from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


class JsonResponses(Response):

    def __init__(self,status,jsonReponse):
        self.status=status
        self.data=jsonReponse
        self.media_and_content_type="application/json"         
        self.content_type=self.media_and_content_type
        self.accepted_media_type =self.media_and_content_type
        self.accepted_renderer=JSONRenderer()
        self.renderer_context = {}
        super().__init__(status=self.status,data=self.data)
        

#Response
def errorResponse(statusCode,errorMessage):

    errorCodeMapping={"400":status.HTTP_400_BAD_REQUEST,\
                      "412":status.HTTP_412_PRECONDITION_FAILED,\
                      "409":status.HTTP_409_CONFLICT,\
                      "404":status.HTTP_404_NOT_FOUND}

    response = Response(
        {"ERROR": errorMessage},
        content_type="application/json",
        status=errorCodeMapping[statusCode],
    )
    response.accepted_renderer = JSONRenderer()
    response.accepted_media_type = "application/json"
    response.renderer_context = {}
    return response


def successfulResponse(statusCode,context):

    successfulCodeMapping={"201":status.HTTP_201_CREATED,\
                           "200":status.HTTP_200_OK}

    response = Response(
        context,
        content_type="application/json",
        status=successfulCodeMapping[statusCode],
    )
    response.accepted_renderer = JSONRenderer()
    response.accepted_media_type = "application/json"
    response.renderer_context = {}
    return response

def redirectResponse(statusCode,url):
    successfulRedirectMapping={"302":status.HTTP_302_FOUND}

    response = Response(status=successfulRedirectMapping[statusCode])
    response["Location"]=url
    print(url)
    return response