import sys
import os
from datetime import datetime,timedelta
while(True):
    if (datetime.now().strftime("%H:%M:%S")=="22:10:00") or (datetime.now().strftime("%H:%M:%S")=="04:00:00") or (datetime.now().strftime("%H:%M:%S")=="11:55:00"):
        try:
            os.system("sh bash.sh")
        except:
            print(datetime.now(), "not working")
