import relay
import time
from config import *

#power off relay
s=relay.createSocket()
try:
    if relay.ison(relaych,s):
        #time.sleep(5)
        relay.poweroff(relaych,s)
        print('power off relay')
except Exception as ex:
    print(ex)
finally:
    s.close()
