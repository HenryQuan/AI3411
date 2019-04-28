#!/bin/bash
./servt -p $2 & sleep 0.1
# fight again yourself and get stronger
./agent -p $2 & sleep 0.1
./$1 -p $2
