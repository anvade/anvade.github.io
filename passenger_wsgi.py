import os
import sys

INTERP = os.path.expanduser("/var/www/u2341884/data/mySite/bin/python")

if sys.executable != INTERP:
   os.execl(INTERP, INTERP, *sys.argv)
   
sys.path.append(os.getcwd())

from app import application