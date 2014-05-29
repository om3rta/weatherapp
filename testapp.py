import pycurl
import cStringIO
import json


import pycurl
import cStringIO
 
buf = cStringIO.StringIO()
 
c = pycurl.Curl()
c.setopt(c.URL, "http://api.wunderground.com/api/3ff15933e8683503/conditions/q/48198.json")
c.setopt(c.WRITEFUNCTION, buf.write)
c.perform()
 
print buf.getvalue()
buf.close()