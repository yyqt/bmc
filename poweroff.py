import urllib2
from config import *
#off bmc

p = urllib2.HTTPPasswordMgrWithDefaultRealm()

p.add_password(None, url, username, password)

handler = urllib2.HTTPDigestAuthHandler(p)
opener = urllib2.build_opener(handler)
urllib2.install_opener(opener)

page = urllib2.urlopen(url).read()
#time.sleep(1)
#page = urllib2.urlopen(url).read()

