
from .serializers import SearchMedInfoSerializer
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
#return json response
from django.http import JsonResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer




# Create your views here.

# set csrf token to false
@api_view(('POST','GET'))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))

def SearchMedInfo(request):
    if request.method == "POST":
        print("request",request.POST.get("search"))
        serializer = SearchMedInfoSerializer(data="sample")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        serializer = SearchMedInfoSerializer()
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    






