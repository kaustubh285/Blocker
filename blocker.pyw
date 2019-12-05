import time
from datetime import datetime as dt

temp_host="hosts"
host_path=r"hosts"
redirect="127.0.0.1"

websites=['facebook.com','www.facebook.com','www.amazon.in','amazon.in']

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,19):
        print("Work hours")
        with open(host_path,"r+") as file:
            content = file.read()
            for items in websites:
                if items in content:
                    pass
                else:
                    file.write(redirect+" "+items+"\n")
        time.sleep(5)
    else:
        print("Enjoy")
        with open(host_path,"r+") as file:
            content = file.readlines()
            file.seek(0)
            for lines in content:
                if not any(website in lines for website in websites):
                    file.write("")
            file.truncate()
        time.sleep(5)
