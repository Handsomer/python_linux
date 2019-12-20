import sys
from os.path import abspath, join, dirname
import pdb

#print sys.path
print abspath(dirname(__file__))
print join(abspath(dirname(__file__)),'src')
print sys.path
