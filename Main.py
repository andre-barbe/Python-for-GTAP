__author__ = "Andre Barbe"
__project__ = "Python for GTAP"
__created__ = "2018-1-25"
__altered__ = "2018-1-25"


#Define Control Variables
#these variables control the options for the files below
gtapversion="v7"
solution_method="default_j"

# Import Methods
import os
import subprocess

from Cleanup import Cleanup
from CopyInputFiles import CopyInputFiles
from CreateCMF import CreateCMF
from CreateSTI import CreateSTI

# Setup Files
Cleanup().create()
CopyInputFiles(gtapversion).create()
CreateCMF("gtapv7", solution_method).create()

# Run Simulations
# Change working directory to Work_Files so all output (and logs) will go there when gemsim or sltoht is called
os.chdir("Work_Files")
subprocess.call("GTAPv7 -cmf GTAPv7-10x10.cmf")
CreateSTI("GTAPv7", ["-10x10"]).create()
subprocess.call("sltoht -sti GTAPv7-10x10.sti")  # run sltoht
# change working directory one level up. This is necessary to access both the output and work files directory for
# copying
os.chdir("..")
# Put results in output directory

# Export Results
