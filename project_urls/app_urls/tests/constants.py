import django
django.setup()

ip="192.168.99.100"
ip="localhost"

testValueShortcode="999999"
testValueUrl="http://www.google.pl"

urlShorten = "http://{}:8000/shorten".format(ip)
urlGetShortcode = "http://{}:8000/{}".format(ip,testValueShortcode)
urlShortcodeStats = "http://{}:8000/{}/stats".format(ip,testValueShortcode)