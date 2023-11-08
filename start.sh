#/bin/bash
source /app/MYWEB_U/bin/activate


if [ $1 == "get" ]
then 
URL=$(curl http://127.0.0.1:4040/api/tunnels -s |python -m json.tool | grep "public_url" | awk -F '"' '{print $4}')
echo $URL
curl "https://api.telegram.org/bot$(cat /app/TELEGRAM_BOT/bot_api)/sendMessage?chat_id=$(cat /app/TELEGRAM_BOT/chat_id)&text=$URL"
elif [ $1 == "start" ]
then
nc -z 192.168.1.6 8000
if [ $? -eq 0 ]
then
 echo "site up already"
exit
else
	nohup python /app/EGIN/manage.py runserver 0.0.0.0:8000 &
	nohup /usr/local/bin/ngrok http 8000 &
	curl http://127.0.0.1:4040/api/tunnels
fi
elif [ $1 == "stop" ]
then
pkill -f /app/EGIN/manage.py
pkill -f /usr/local/bin/ngrok
fi
