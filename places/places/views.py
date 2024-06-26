from .models import Place
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
import json



def PlaceList(request):
    queryset = Place.objects.all()
    context = list(queryset.values('id', 'name'))
    return JsonResponse(context, safe=False)

def PlaceCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        place = Place()
        place.name = data_json['name']
        place.save()
            
        return HttpResponse("successfully created place")
    

def PlacesCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        place_list = [] 
        for place in data_json:
            db_place = Place()
            db_place.name = place['name']
            place_list.append(db_place)
                    
                    
        
        Place.objects.bulk_create(place_list)
        return HttpResponse("successfully created places")