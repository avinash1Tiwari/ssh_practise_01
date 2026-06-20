from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


class UserView(APIView):

    def get(self,request):
        return Response({
            "message" : "Everything is running",
            "status" : True
        },status=200)