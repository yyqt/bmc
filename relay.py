import socket
import time
from config import *

def tcmd(cmd,s):
    rt=''
    try:
        s.send(cmd.encode())
        time.sleep(0.5)
        reply =s.recv(96)
        replytext=reply.decode()
        rt= replytext
    except Exception as ex:
        print(ex)
        rt=''
        pass
    return rt

def createSocket():
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(15)
    try:
        s.connect(addr)
    except:
        s.close()
    return s

def isoff(ch,s):
    cmd='read'+str(ch)
    rt=tcmd(cmd,s)
    if rt.endswith(('off' + str(ch))):
        return True
    return False

def ison(ch,s):
    cmd='read'+str(ch)
    rt=tcmd(cmd,s)
    if rt.endswith(('on'+str(ch))):
        return True
    return False

def poweron(ch,s):
    cmd='on'+str(ch)
    rt=tcmd(cmd,s)
    if rt.endswith(('on'+str(ch))):
        return True
    return False

def poweroff(ch,s):
    cmd='off'+str(ch)
    rt=tcmd(cmd,s)
    if rt.endswith(('off'+str(ch))):
        return True
    return False
