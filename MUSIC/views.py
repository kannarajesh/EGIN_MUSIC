from django.shortcuts import render
from django.http import JsonResponse
import os
import json
import hashlib
import urllib.parse
import os
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
{ 'name': 'Muruga - 1',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Aadhaaram Neeye.mp3'
  },
{ 'name': 'Muruga - 2',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Aadhaaram Nin Sirippatharam.mp3'
  },
{ 'name': 'Muruga - 3',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Aadheenampaal Kodukka.mp3'
  },
{ 'name': 'Muruga - 4',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Aadu Mayile.mp3'
  },
{ 'name': 'Muruga - 5',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Aaru Padai Veedugalil.mp3'
  },
{ 'name': 'Muruga - 6',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Aarumugamana Porul.mp3'
  },
{ 'name': 'Muruga - 7',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Aarumugane Asai Manasukkul.mp3'
  },
{ 'name': 'Muruga - 8',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Aarupadai Veedu Konda.mp3'
  },
{ 'name': 'Muruga - 9',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Aaruthal Arulvai.mp3'
  },
{ 'name': 'Muruga - 10',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Aaruvayal Kaadu Angamellam Thanga Nagai.mp3'
  },
{ 'name': 'Muruga - 11',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Aayiram Paatezhuthi.mp3'
  },
{ 'name': 'Muruga - 12',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Aiyappa Saranam Saranam.mp3'
  },
{ 'name': 'Muruga - 13',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Ariyathu Ketkum.mp3'
  },
{ 'name': 'Muruga - 14',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Arogara Enru Solli.mp3'
  },
{ 'name': 'Muruga - 15',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/En Appane Ennai Aiyane.mp3'
  },
{ 'name': 'Muruga - 16',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Engellam Theduvatho.mp3'
  },
{ 'name': 'Muruga - 17',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Engum Thirinthu Varum.mp3'
  },
{ 'name': 'Muruga - 18',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Gnamum Kalviyum.mp3'
  },
{ 'name': 'Muruga - 19',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Ka Ka Kandhane Varuga.mp3'
  },
{ 'name': 'Muruga - 20',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Kaalai Ilam Kathiril.mp3'
  },
{ 'name': 'Muruga - 21',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Kaalamenum Thottathile.mp3'
  },
{ 'name': 'Muruga - 22',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Kadalil Alai Thulla.mp3'
  },
{ 'name': 'Muruga - 23',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Kandha Sasti Kavasam.mp3'
  },
{ 'name': 'Muruga - 24',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Kandhan Kaaladiyai.mp3'
  },
{ 'name': 'Muruga - 25',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Kandhan Thiruneeraninthal.mp3'
  },
{ 'name': 'Muruga - 26',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Kandhanum Varuvan.mp3'
  },
{ 'name': 'Muruga - 27',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Kandhar Sasti Kavasam.mp3'
  },
{ 'name': 'Muruga - 28',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Kandu Konden.mp3'
  },
{ 'name': 'Muruga - 29',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Kanni Thamilukku.mp3'
  },
{ 'name': 'Muruga - 30',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Karpanai Enralum Karsilai.mp3'
  },
{ 'name': 'Muruga - 31',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Kolamayil Thiru Vadivam.mp3'
  },
{ 'name': 'Muruga - 32',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Konjum Kili Kuruvi.mp3'
  },
{ 'name': 'Muruga - 33',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Koodave Iruppan Kumaran.mp3'
  },
{ 'name': 'Muruga - 34',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Koopitta Kuralukku.mp3'
  },
{ 'name': 'Muruga - 35',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Kundrathile Kumaranukku.mp3'
  },
{ 'name': 'Muruga - 36',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Kundru Valar Kandhan.mp3'
  },
{ 'name': 'Muruga - 37',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Kurinjiyile Poo Malarnthu.mp3'
  },
{ 'name': 'Muruga - 38',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Maalai Vanna Maalai.mp3'
  },
{ 'name': 'Muruga - 39',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Manimudi Oraaru.mp3'
  },
{ 'name': 'Muruga - 40',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Mannukkum Vinnukkum.mp3'
  },
{ 'name': 'Muruga - 41',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Margali Sendru Thai Madham.mp3'
  },
{ 'name': 'Muruga - 42',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Muruga Muruga.mp3'
  },
{ 'name': 'Muruga - 43',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Muruga Nee Varavendum.mp3'
  },
{ 'name': 'Muruga - 44',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Muruga Un Kunam.mp3'
  },
{ 'name': 'Muruga - 45',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/MuruganaiKoopittu.mp3'
  },
{ 'name': 'Muruga - 46',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Muththana Muthukumara.mp3'
  },
{ 'name': 'Muruga - 47',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Nee Allaal Theivam.mp3'
  },
{ 'name': 'Muruga - 48',
    'artist': 'GOD',
    'image': 'http' + '://' + request_host +'/static/music/Music_S/egin.jpg',
    'path': 'http://www.friendstamilmp3.in/songs2/Devotional Collections/Hindu Collections/Murugan Songs 1/Nee Oru Thaai Aanal.mp3'
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

def play_list(request):
    request_host = request.META.get('HTTP_HOST')
    playlist = request.GET.get('play')
    if playlist == "GYM":
        print("INside GYM playlist")
        return play_list2(request)
    else:
        return play_list1(request)
