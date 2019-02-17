import requests
r = requests.post('https://hacknyu2019.us-east.mybluemix.net/site', data = {'uri':'grantsteinfeld.com'})

print r.text