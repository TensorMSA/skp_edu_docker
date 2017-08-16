import tensorflow as tf
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from .tf_service_logic import TfExamBackendService as tebs

import sys
sys.path.insert(0, '/jupyter/chap06_image/')
import restTest

class TfImageService(APIView):

    def post(self, request):
        print("post")
        return_data = {"status":"200","result":"put"}
        return Response(json.dumps(return_data))


    def get(self, request):
        print("get")
        return_data = {"status":"200","result":"put"}
        return Response(json.dumps(return_data))


    def put(self, request):
        print("put")
        return_data = {"status":"200","result":"put"}
        return Response(json.dumps(return_data))


    def delete(self, request):
        print("delete")
        return_data = {"status":"200","result":"delete"}
        return Response(json.dumps(return_data))

