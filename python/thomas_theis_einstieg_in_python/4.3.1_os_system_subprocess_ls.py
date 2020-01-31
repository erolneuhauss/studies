#!/usr/bin/python
import os

#ls = os.popen('ls').readlines()

#print ls

#print len(ls)

#for zeile in ls:
#    print zeile

import subprocess

ls = subprocess.call(['ls', '-hlt'], shell=True)
