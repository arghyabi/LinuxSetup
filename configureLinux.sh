#!/bin/bash

chmod +x update
sudo cp update /usr/bin

update

sudo apt-get install python-is-python3 -y

python updateBashrc.py

source .~/.bashrc

cd ../ && rm -rf LinuxSetup
