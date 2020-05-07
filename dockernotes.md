
OFFICIAL LOCUST IMAGE
https://hub.docker.com/r/locustio/locust

# I NEED TO OPEN THE FIREWALL FOR THE PORTS

<!-- grubys image -->
sudo docker pull grubykarol/locust

<!-- undedited from dockerhub -->
docker run --rm --name standalone --hostname standalone -e ATTACKED_HOST=http://example.com -e "LOCUST_OPTS=--no-web" -d -v $MY_SCRIPTS:/locust grubykarol/locust

<!-- WORKING, DO NOT TOUCH -->
sudo docker run --name standalone --hostname standalone \
-e ATTACKED_HOST=https://demoblaze.com \
-e "LOCUST_OPTS=--no-web" \
-v /home/mavric/stresstestingstore:/locust \
grubykarol/locust   



<!-- ISSUES TO ADDRESS:
0.) PROCESS RAN ENDLESSLY BECAUSE I RAN IT ATTACHED INSTEAD OF DETACHED 
1.) I HAD TO DELETE DOCKERFILE
2.) I HAD TO RENAME justbrowsingswarm.py to locustfile.py
3.) I HAD TO RENAME StressTestingStore to stresstestingstore
-->

sudo docker run --name standalone --hostname standalone \
-e ATTACKED_HOST=https://demoblaze.com \
-e "LOCUST_OPTS=--no-web" \
-v /home/mavric/stresstestingstore:/locust \
grubykarol/locust   

<!-- not working -->
<!-- sudo docker run --name swarmcontainer --hostname swarmcontainer \
-e ATTACKED_HOST=https://demoblaze.com \
-e LOCUST_OPTS="--no-web" \
-e LOCUST_FILE= /StressTestingStore/justbrowsingswarm.py \
-v /home/mavric/stresstestingstore: /stresstestingstore
-p 8089:8089 -->

<!-- Volumes allow you to share files with the host and the container -->

<!--  -->
<!--  -->
### WORKFLOW
TODO- I still need to get my locustfile logic into the image.
People are suggested using volumes. I think volumes are only used for real time updating
I can also just run commands from within the docker image themselves(so git clone would work)

sudo docker pull locustio/locust:latest
<!-- Pull retrieves the image from the dockerhub  -->

sudo docker images
<!-- Prints a list of all images on this system -->

sudo docker build -t mylocustimage /locationtodockerfile/
<!-- builds an image with name mylocustimage where dockefile is located at /location... -->

<!-- Example run -->
sudo docker run -p 8080:8080 mylocustimage

sudo docker run --volume $PWD/dir/of/locustfile:/mnt/locust -e LOCUSTFILE_PATH=/mnt/locust/locustfile.py -e TARGET_URL=https://abc.com -e LOCUST_OPTS="--clients=10 --no-web --run-time=600" locustio/locust



sudo docker container ls
<!-- this will show us our running containers, ls -a for all -->

sudo docker container stop (((imagename?)))
<!-- stop a docker container without removing it -->

sudo docker container rm ((((container_id[0:5])))) -f 
<!-- kill a docker container AND REMOVE IT BY FORCE-->


sudo docker container exec -it (((imagename))) bash
<!-- enters into a container -->
docker attach







https://docs.docker.com/get-started/



# install instructions
# https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository
######################################### DOKER SETUP START
#################### SEE https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo apt-key fingerprint 0EBFCD88 

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

##################################### DOKER SETUP END
#################### (verify docker is working by: sudo docker hello-world

