#!/bin/bash
## enable it without sudo
sudo groupadd docker
sudo gpasswd -a $USER docker
newgrp dockerTest
docker run hello-world
