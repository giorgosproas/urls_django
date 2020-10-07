import django
django.setup()

ip="192.168.99.100"
ip="localhost"

urlShorten = "http://{}:8000/shorten".format(ip)
url = "http://{}:8000/ewx123/stats".format(ip)