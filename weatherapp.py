#Starting app
import pycurl
import cStringIO
 
buf = cStringIO.StringIO()
 
c = pycurl.Curl()
c.setopt(c.URL, 'http://api.wunderground.com/api/3ff15933e8683503/conditions/q/CA/San_Francisco.json')
c.setopt(c.WRITEFUNCTION, buf.write)
c.perform()
 
weather_info = buf.getvalue()
buf.close()

print weather_info["response"]