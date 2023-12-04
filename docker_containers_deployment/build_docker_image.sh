#!/bin/sh

# Variables for setup.
ImageName="stud_app_image"
ContainerName="stud_app_container"
MySQLUser="defaultUser"
MySQLPassword="defaultPWD"


while [ "$#" -gt 0 ];
do
    case $1 in
		-h | --help) echo "Run build_docker_image.sh -imn 'your image name' -cn 'your container name' -msu 'your mysql user' -msp 'your mysql password'. \
								Or --image_name , --container_name, --mysql_user, --mysql_password. "; exit;;
		-imn | --image_name) ImageName="$2"; shift;;
		-cn | --container_name) ContainerName="$2"; shift;;
		-msu | --mysql_user) MySQLUser="$2"; shift;;
		-msp | --mysql_password) MySQLPassword="$2"; shift;;
        *) echo "Wrong parameters. Enter -h or --help for help."; exit ;;
    esac
    shift
done

echo "user name: " $MySQLUser
echo "user pass: " $MySQLPassword
echo "user image_name: " $ImageName
echo "user container_name: " $ContainerName

docker build . -t $ImageName \
							--build-arg MySQLUser=$MySQLUser \
							--build-arg MySQLPassword=$MySQLPassword #\
							#-q

docker ps -as

docker run -it --name $ContainerName $ImageName #bash

#ls / -l
#bash /test_docker.sh
#bash /students_accommodation/orchestration/setupDB.sh

#docker container exec -it $ContainerName bash

#docker container restart $ContainerName
