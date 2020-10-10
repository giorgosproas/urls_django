# urls_django
get/post API django

#
export DJANGO_SETTINGS_MODULE=project_urls.settings

# How to run
Having docker installed:
Go inside folder /projects_urls
docker build -t django-docker .
docker run -dit -p 8000:8000 django-docker:latest

Do docker ps and see the id of the just created container
Copy this id. Below it will be mentioned as ID_OF_THE_CONTAINER
Then execute:
   docker exec -it ID_OF_THE_CONTAINER sh

With the previous command you will log in in the new container
execute:
   export DJANGO_SETTINGS_MODULE=project_urls.settings
   cd /code/app_urls/tests
   pytest test*
192.168.99.100



# ASSUMPTIONS/ Other Details
1. When someone requests GET /<shortcode> we have to select check how this will be
   handled by the backend. I could create a view which checks if the value
   <shortcode> is valid or not and return the message respectively. However,
   I decided to check directly in the urls session. So if the <shortcode> is
   not valid no view is called and 404 Page not found error is returned.

2. We have to handle the POST /shorten API when in the request body the url already
   exists in the database. Our main purpose is to count how many times we redirected
   someone to a specific URL. Making the URL not unique would mess the system and 
   would not fullfill our real application target

3. We could test the django app by using its own testing way but i prefered to use pytest for
   that because it is more generic. The code might seem a little bit repetitive but i tried 
   to cover the cases by deleting or adding a new row in the database as needed. Also because
   of time limitations i didnt add fixtures (and thats the main reason the code seems repetitive)
   In case more time is available the pytests have to fixed and fixtures have to be used instead.
