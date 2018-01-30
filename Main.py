__author__ = "Andre Barbe"
__project__ = "Python for GTAP"
__created__ = "2018-1-25"
__altered__ = "2018-1-30"

# Define Control Variables
# these variables control the options for the files below
gtapversion = "GTAPv7"
solution_method = "default_j"
variables_to_export = [
    "qxw\n",
    "qmw\n",
    "qo\n",
    "pb\n",
    "vgdp\n",
    "ev"  # This variable only has one matrix and so can sometime cause problems
]
simulation_list=["-10x10"]

# Import Methods
import os
import subprocess

from Cleanup import Cleanup
from CopyInputFiles import CopyInputFiles
from CreateCMF import CreateCMF
from CreateSTI import CreateSTI
from CreateMAP import CreateMAP
from CreateOutput import CreateOutput

# Setup Files
Cleanup().create()
CopyInputFiles(gtapversion).create()

os.chdir("Work_Files")
CreateSTI(gtapversion, simulation_list).create()
for simulation in simulation_list:
    #Create files
    CreateCMF(gtapversion, simulation, solution_method).create()
    CreateMAP(gtapversion, variables_to_export).create()

    # Run Simulations
    # Change working directory to Work_Files so all output (and logs) will go there when model.exe or sltoht is called
    subprocess.call("{0} -cmf {0}{1}.cmf".format(gtapversion,simulation)) # run model.exe
    subprocess.call("sltoht -sti {0}{1}.sti".format(gtapversion,simulation))  # run sltoht

    # Export Results
    # change working directory one level up. This is necessary to access both the output and work files directory for
    # copying
    os.chdir("..")
    # Put results in output directory
    CreateOutput(["{0}{1}.csv".format(gtapversion,simulation)]).create()