import relay
import time
from config import *

#power on  relay
s=relay.createSocket()
try:
    if relay.isoff(relaych,s):
        relay.poweron(relaych,s)
        print('poweron relay')
        #time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    s.close()