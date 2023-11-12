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

# Create your views here.

from django.http import HttpResponse

def index(request):
    playlist = request.GET.get('play')
    context = {'playlist': playlist}
    return render(request, 'index.html',context)


def play_list1(request):
#    directorys = directory.objects.all()
#def my_api_view(request):
    request_host = request.META.get('HTTP_HOST')
    # Use the request_host variable as needed

    # Return a JSON response
    response_data = [{ 'name': 'Muruga - 0',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Aadhaaram Enrum Neethane.mp3'
  },
{ 'name': 'Muruga - 49',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Neela Mayil Meethu.mp3'
  },
{ 'name': 'Muruga - 50',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Neeye En Vazhvukku.mp3'
  }]
#    return JsonResponse(response_data)
    response_data3 = {'data': response_data}
    return JsonResponse(response_data3)
def play_list2(request):
    request_host = request.META.get('HTTP_HOST')
    playlist = request.GET.get('play')
    directory="/Music"
    mp3_files=[]
    song_name=[]
    song_artist=[]
    song_image=[]
    song_path=[]
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and filename.endswith(".mp3"):
            tag=TinyTag.get('/Music/'+filename)
            tmptl = format(tag.title)
            song_name.append(tmptl + playlist) 
            song_artist.append(tag.artist)
            song_image.append(request.scheme + '://' + request_host +'/static/music/image/music_icon.png')
            song_path.append(request.scheme + '://' + request_host +'/static/music/Music_S/'+filename)
    keys = [ 'name', 'artist', 'image', 'path' ]
    items = [dict(zip(keys, [n, a, i, p]))for n, a, i, p in zip (song_name,song_artist,song_image,song_path)]
    d = {'data':items}
    return JsonResponse(d)
    #    directory_path = '/Music'
#    request_host = request.META.get('HTTP_HOST')
#    directory_set = os.listdir(directory_path)
#    directory_list = list(directory_set)
#    directory_list_with_extension = [file.replace(' ', '%20')for file in directory_list]
#    response = {'directories': directory_list_with_extension}
#    json_response = json.dumps(response)
#return json_response(d)

# Specify the path of the directory you want to list

# Specify the extension you want to add (e.g., '.txt', '.csv')
# Get the directory list with the extension and replaced spaces

# Create a dictionary to hold the response

# Convert the dictionary to JSON

# Print the JSON response
def play_list3(request):
    url = "https://raw.githubusercontent.com/kannarajesh/EGIN_MUSIC/main/MUSIC/travel.linklist"
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
#    for obj in json_objects:
#    response_data.append(json.dumps(obj, indent=2))
    #response_data.append({"data": json_objects})  # Append the entire list as a JSON object
    response_data = {"data": json_objects} 
    return JsonResponse(response_data, json_dumps_params={'indent': 2}, safe=False)
#    response_data4 = {'data': response_data}
#    return JsonResponse(response_data4)
###################################
def play_list(request):
    request_host = request.META.get('HTTP_HOST')
    playlist = request.GET.get('play')
    if playlist == "GYM":
        print("INside GYM playlist")
        return play_list2(request)
    elif playlist == "travel":
        return play_list3(request)
    else: 
        return play_list1(request)

