#!/bin/bash
./servt -p $2 & sleep 0.1
# fight again yourself and get stronger
./$1 -p $2 & sleep 0.1
./lookt -p $2 -d 3
