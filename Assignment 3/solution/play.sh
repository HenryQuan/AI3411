#!/bin/sh
# run this game easily with this script

# feel free to change this port
port=12345
../servt -p $port & sleep 0.1
../agent -p $port & sleep 0.1
../lookt -p $port

