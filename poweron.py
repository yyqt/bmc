import urllib2
from config import *

#start bmc
url = 'http://172.18.26.83/chassis.html?PwrCtrl=PowerUp&Button1=Apply'
username = 'admin'
password = 'admin'
p = urllib2.HTTPPasswordMgrWithDefaultRealm()

p.add_password(None, url, username, password)

handler = urllib2.HTTPDigestAuthHandler(p)
opener = urllib2.build_opener(handler)
urllib2.install_opener(opener)

page = urllib2.urlopen(url).read()
