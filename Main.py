__author__ = "Andre Barbe"
__project__ = "Python for GTAP"
__created__ = "2018-1-25"
__altered__ = "2018-1-25"

# Define Control Variables
# these variables control the options for the files below
gtapversion = "v7"
solution_method = "default_j"
variables_to_export = [
    "qxw\n",
    "qmw\n",
    "qo\n",
    "pb\n",
    "vgdp\n",
    "ev"  # This variable only has one matrix and so can sometime cause problems
]

# Import Methods
import os
import subprocess

from Cleanup import Cleanup
from CopyInputFiles import CopyInputFiles
from CreateCMF import CreateCMF
from CreateSTI import CreateSTI
from CreateMAP import CreateMAP

# Setup Files
Cleanup().create()
CopyInputFiles(gtapversion).create()
CreateCMF("gtapv7", solution_method).create()
os.chdir("Work_Files")
CreateSTI("GTAPv7", ["-10x10"]).create()
CreateMAP("GTAPv7", variables_to_export).create()

# Run Simulations
# Change working directory to Work_Files so all output (and logs) will go there when gemsim or sltoht is called
subprocess.call("GTAPv7 -cmf GTAPv7-10x10.cmf")
subprocess.call("sltoht -sti GTAPv7-10x10.sti")  # run sltoht
# change working directory one level up. This is necessary to access both the output and work files directory for
# copying
os.chdir("..")
# Put results in output directory

# Export Results
