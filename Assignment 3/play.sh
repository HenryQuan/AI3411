#!/bin/bash
./servt -p $2 & sleep 0.1
# fight again yourself and get stronger
./lookt -p $2 -d 5 & sleep 0.1
./$1 -p $2
