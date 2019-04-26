#!/usr/bin/python3

import random
import os

# get a random port
port = random.randint(1000, 60000)
os.system('./play.sh agent.py {}'.format(port))
