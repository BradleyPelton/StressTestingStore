
OFFICIAL LOCUST IMAGE
https://hub.docker.com/r/locustio/locust




### WORKFLOW

sudo docker pull locustio/locust:latest
<!-- Pull retrieves the image from the dockerhub  -->

sudo docker images
<!-- Prints a list of all images on this system -->

sudo docker run ()()()()










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

