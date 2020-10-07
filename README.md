# urls_django
get/post API django

#
export DJANGO_SETTINGS_MODULE=project_urls.settings

# How to run
Having docker installed:
docker build -t django-docker .
docker run -dit -p 8000:8000 django-docker:latest

192.168.99.100