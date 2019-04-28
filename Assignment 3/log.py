#!/usr/bin/python3

'''
A simple wrapper around play.sh to prevent connection issue (log version)
'''

import random
import os

# get a random port
port = random.randint(1000, 60000)
os.system('./play.sh agent.py {} > out.log'.format(port))