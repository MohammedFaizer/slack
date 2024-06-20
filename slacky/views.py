from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST'])
def hello_world(request):
    print(request.data)
    return Response({"message": "Hello, world!"})
