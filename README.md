# urls_django
get/post API django

#
export DJANGO_SETTINGS_MODULE=project_urls.settings

# How to run
Having docker installed:
docker build -t django-docker .
docker run -dit -p 8000:8000 django-docker:latest

192.168.99.100



# ASSUMPTIONS
1. When someone requests GET /<shortcode> we have to select check how this will be
   handled by the backend. I could create a view which checks if the value
   <shortcode> is valid or not and return the message respectively. However,
   I decided to check directly in the urls session. So if the <shortcode> is
   not valid no view is called and 404 Page not found error is returned.

2. We have to handle the POST /shorten API when in the request body the url already
   exists in the database. Our main purpose is to count how many times we redirected
   someone to a specific URL. Making the URL not unique would mess the system and 
   would not fullfill our real application target

3. 
