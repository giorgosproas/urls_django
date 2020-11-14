from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


class JsonResponses(Response):

    def __init__(self,status,jsonReponse):
        self.media_and_content_type="application/json"         
        self.content_type=self.media_and_content_type
        self.accepted_media_type =self.media_and_content_type
        self.accepted_renderer=JSONRenderer()
        self.renderer_context = {}
        super().__init__(status=status,data=jsonReponse)
        

class RedirectionResponses(Response):

    def __init__(self,status,url):
        self.status=status
        super().__init__(status=self.status,headers={"Location":url})
