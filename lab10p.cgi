#!/usr/bin/python
print "Content-type:text/html\n\n"

import os,cgi




form = cgi.FieldStorage()
city = form.getvalue('city').upper()
pro = form.getvalue('pro').upper()
country = form.getvalue('country').upper()
url = form.getvalue('url')



print "<div style='font-size : xx-large;top : 0;color: white;background-color: green;text-align: center; '>" + city + "<br />" + pro + "<br />" + country + "</div>"


print "<br /><img src = '%s'" % str(url) +  "style='background-repeat: no-repeat;background-position: center;background-size: cover;width: 80%;border: 10px solid purple;'>" 