docker build -t django-docker .
containerID=$(docker run -dit -p 8000:8000 django-docker:latest)
function path_remove {
  # Delete path by parts so we can never accidentally remove sub paths
  PATH=${PATH//":$1:"/":"} # delete any instances in the middle
  PATH=${PATH/#"$1:"/} # delete any instance at the beginning
  PATH=${PATH/%":$1"/} # delete any instance in the at the end
}

TEST_PATH=/code/app_urls/tests
winpty docker exec -it $containerID pytest $(path_remove $TEST_PATH/test*) --html=report.html
docker cp $containerID:code/report.html .
docker stop $containerID


