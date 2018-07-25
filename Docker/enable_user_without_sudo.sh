#!/bin/bash
## enable it without sudo
sudo groupadd docker
sudo gpasswd -a $USER docker
newgrp docker
docker run hello-world