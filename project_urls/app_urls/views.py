from django.shortcuts import render
from django.http import HttpResponse


# Create your views here  
def shortenView(request):
    return HttpResponse("<h1>Shorten View</h1>")
    
def shortcodeView(request,shortcode):
    return HttpResponse("<h1>Shortcode View {}</h1>".format(shortcode))
    
    
def shortcodeStatsView(request,shortcode):
    return HttpResponse("<h1>ShortcodeStats View {}</h1>".format(shortcode))
