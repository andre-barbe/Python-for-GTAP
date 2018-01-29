__author__ = "Andre Barbe"
__project__ = "Python for GTAP"
__created__ = "2018-1-25"
__altered__ = "2018-1-25"

# Import Methods
from Cleanup import Cleanup
from CopyInputFiles import CopyInputFiles

# Setup Files
Cleanup().create()
CopyInputFiles().create()

# Run Simulations

# Export Results
