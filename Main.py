__author__ = "Andre Barbe"
__project__ = "Python for GTAP"
__created__ = "2018-1-25"
__altered__ = "2018-1-25"

# Import Methods
import os
import subprocess

from Cleanup import Cleanup
from CopyInputFiles import CopyInputFiles
from CreateCMF import CreateCMF


# Setup Files
Cleanup().create()
CopyInputFiles().create()
CreateCMF("gtapv7", "default_j").create()

# Run Simulations
# Change working directory to Work_Files so all output (and logs) will go there when gemsim or sltoht is called
os.chdir("Work_Files")
#subprocess.call("gemsim -cmf GTAPv7-10x10.cmf")
subprocess.call("GTAPv7 -cmf GTAPv7-10x10.cmf")


# Export Results
