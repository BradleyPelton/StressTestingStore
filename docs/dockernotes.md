
OFFICIAL LOCUST IMAGE
https://hub.docker.com/r/locustio/locust

UNOFFICIAL LINKS
https://gist.github.com/bradtraversy/89fad226dc058a41b596d586022a9bd3
<!-- THE ONE BELOW IS THE BEST LINK -->
https://hub.docker.com/r/grubykarol/locust


<!-- grubys image -->
sudo docker pull grubykarol/locust

<!-- WORKING, DO NOT TOUCH -->
<!-- justbrowsingswarm -->
sudo docker run --name justbrowsingswarm --hostname justbrowsingswarm \
-e ATTACKED_HOST=https://demoblaze.com \
-e "LOCUST_OPTS=--no-web -c 100 -r 10 --run-time 20s" \
-e "LOCUST_FILE= /locust/justbrowsingswarm.py" \
-v /home/mavric/StressTestingStore:/locust \
grubykarol/locust

<!-- coreswarm -->
sudo docker run --name coreswarm --hostname coreswarm \
-e ATTACKED_HOST=https://api.demoblaze.com \
-e "LOCUST_OPTS=--no-web -c 5 -r 1 --run-time 10s" \
-e "LOCUST_FILE= /locust/coreswarm.py" \
-v /home/mavric/StressTestingStore:/locust \
grubykarol/locust

<!-- mycontiner EXPIREMENTATION -->
sudo docker run --name jbscont --hostname jbscont \
-e PYTHONUNBUFFERED=0 \
-e ATTACKED_HOST=https://api.demoblaze.com \
-e "LOCUST_OPTS=--no-web -c 5 -r 1 --run-time 10s" \
-e "LOCUST_FILE=/locust/justbrowsingswarm.py" \
-v /home/mavric/StressTestingStore:/locust \
tbs5

<!-- does a space after equals sign matter????/ -->

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

