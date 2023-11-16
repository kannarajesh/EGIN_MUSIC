import requests
import json
import html_to_json
import sys

##RUN AS python insert_songs.py "https://www.friendstamilmp3.in/songs2/Kuthu Songs/Super Kuthu Songs/" travel.linklist
##IT will update the file travel.linklist

URL=sys.argv[1]
file=sys.argv[2]
url=URL.replace(" ","%20")
print (url)
#url="https://www.friendstamilmp3.in/songs2/Kuthu%20Songs/Super%20Kuthu%20Songs/"
XMLO=requests.get(url)
output_json = html_to_json.convert(XMLO.text)
i=len(output_json["html"][0]['body'][0]['table'][0]['tr'])
i=i-2
data=[]
file = open(file, 'a')
for x in range(3, i):
    MP3url=url+output_json["html"][0]['body'][0]['table'][0]['tr'][x]['td'][1]['a'][0]['_attributes']['href']
    file.write(MP3url+"\n")
file.close()
print (MP3url)
