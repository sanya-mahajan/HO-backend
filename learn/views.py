

from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .scrapeMedInfo import get_med_info
from django.http import JsonResponse
import json
from django.http import JsonResponse, HttpResponse



# Create your views here.

@csrf_exempt
def SearchMedInfo(request):
    if request.method == "POST":
        # get the search term
        print(request)
        searchTerm = request.POST.get("search")
        print(searchTerm)
        # get the search results
       
            
        # return the search results as a json response
        searchTerm="mental health "
        if searchTerm:
            searchResults = get_med_info(searchTerm)
            return JsonResponse(searchResults, safe=False)

        else:
            return JsonResponse("No results found", safe=False)
    
    

    






