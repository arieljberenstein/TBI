#!/bin/bash
#sudo apt-get upgrade
sudo apt-get update

#Install packages to allow apt to use a repository over HTTPS:
sudo apt-get install -f \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common

#Add Docker’s official GPG key:
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88


# Use the following command to set up the stable repository. 
#You always need the stable repository, even if you want to install builds from the edge or test repositories as well. 
#To add the edge or test repository, add the word edge or test (or both) after the word stable in the commands below

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"


#Update the apt package index
sudo apt-get update

#Install the latest version of Docker CE, or go to the next step to install a specific version:
sudo apt-get install -f docker-ce

# test and enable it at boot
sudo docker run hello-world
sudo systemctl enable docker

