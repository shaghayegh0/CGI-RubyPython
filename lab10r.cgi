#!/usr/bin/ruby -wT
print "Content-type: text/html\n\n"




require 'cgi'
# Create a cgi object, with HTML 5 generation methods.
cgi = CGI.new("html5")


city = cgi['city'].capitalize()
province = cgi['pro'].capitalize()
country = cgi['country'].capitalize()
url = cgi['url']




puts "<div style='
        font-size : xx-large;
        top : 0;
        color: brown;
        background-color: blanchedalmond;
        text-align: center; '>" + city + "<br />" + province + "<br />" + country + "</div>"


puts "<br /><img src =  #{url} style='background-repeat: no-repeat;
background-position: center;
background-size: cover;
width: 100%;'>"