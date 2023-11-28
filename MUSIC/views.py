from django.shortcuts import render
from django.http import JsonResponse
import os
import json
import hashlib
import urllib.parse
import requests
import json
from tinytag import TinyTag
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.http import HttpResponse


@login_required(login_url='login')
def index(request):
    playlist = request.GET.get('play')
    context = {'playlist': playlist}
    return render(request, 'index.html',context)

def play_list_n(request,playlist):
    url = "https://raw.githubusercontent.com/kannarajesh/EGIN_MUSIC/main/MUSIC/"+playlist+".linklist"
    print ("url that will be played",url)
    request_host = request.META.get('HTTP_HOST')
    response = requests.get(url)
    data = response.text
    lines = data.split('\n')  # Split the text into lines
    json_objects = []
    response_data = []
    for line in lines:
        # Ignore empty lines
        if line.strip():
            # Create a dictionary from the line and append it to the list
            try:
                url_parts = line.strip().split("/")
                last_part = url_parts[-1].replace(".mp3", "").replace("%20", " ") 
                last_part_1 = url_parts[-2].replace("%20", " ") 
                last_part_without_extension = last_part.split(".", 1)[0] if "." in last_part else last_part
                json_object = {"url": line.strip()}
                json_object = {"name": last_part, "artist": last_part_1 ,"image": "http" + "://" + request_host +"/static/music/Music_S/egin.jpg","path": line.strip()}
                json_objects.append(json_object)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON from line: {line}\nError: {e}")
    response_data = {"data": json_objects} 
    return JsonResponse(response_data, json_dumps_params={'indent': 2}, safe=False)

def play_list(request):
    request_host = request.META.get('HTTP_HOST')
    playlist = request.GET.get('play')
    return play_list_n(request,playlist)
