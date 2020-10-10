# How to run

Prerequisites: Having docker on linux/Mac Machine

1. Go to urls_django/
2. run: docker build -t django-docker .
3. run: docker run -dit -p 8000:8000 django-docker:latest
4. After the container has been created do docker ps and see the
   id (CONTAINER_ID) of the just created container
5. Copy this id. Below it will be mentioned as CONTAINER_ID
6. run: docker exec -it CONTAINER_ID sh
(With the previous command you will log in in the new container)
7. Now in the newly created container:
   run: pytest $TEST_PATH/test*


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

# Next steps

1. Use Dockercompose to create 2 containers. One with the django image and one with the database
   and make changes to django configuration so it works correctly.
2. Write more documentation.