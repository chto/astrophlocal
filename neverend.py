import sys
import os
from datetime import datetime,timedelta
while(True):
    if datetime.now().strftime("%H:%M:%S")=="22:10:00":
        try:
            os.system("sh bash.sh")
        except:
            print(datetime.now(), "not working")
    if datetime.now().strftime("%H:%M:%S")=="4:00:00":
        try:
            os.system("sh bash.sh")
        except:
            print(datetime.now(), "not working")
