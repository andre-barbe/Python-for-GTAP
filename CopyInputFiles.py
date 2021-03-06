__author__ = "Andre Barbe"
__project__ = "Python for GTAP"
__created__ = "2018-1-25"
__altered__ = "2018-1-30"

import shutil


class CopyInputFiles(object):
    """Copies files from the input files directory to the work files directory"""

    __slots__ = ["gtapversion"]

    def __init__(self, gtapversion: str) -> None:
        self.gtapversion = gtapversion

    def create(self) -> None:
        # Define lists of files to copy.
        if self.gtapversion == "GTAPv7":
            list_gtap_gemsim = [
                "gtapv7.tab",
                "gtapv7.axs",
                "gtapv7.axt",
                "gtapv7.exe"
                #"GTAPv7-10x10.cmf"
            ]
            list_shocks_gemsim = [
                "Shocks.har"
            ]
            list_gtap_data = [
                "basedata.har",
                "sets.har",
                "default.prm",
            ]
            list_shocks_data = [
            ]

        if self.gtapversion == "GTAP":
            list_gtap_gemsim = [
                "gtap.tab",
                "gtap.gss",
                "gtap.gst",
                "gtap.min",
                # "gtap.cmf",
            ]
            list_shocks_gemsim = [
                "shocks.tab",
                "shocks.gss",
                "shocks.gst",
                "shocks.min",
                "shocks.cmf"
            ]
            list_gtap_data = [
                "basedata.har",
                "baserate.har",
                "baseview.har",
                "sets.har",
                "default.prm"
            ]
            list_shocks_data = [
            ]

        list_of_files_to_copy = list_gtap_gemsim \
                                + list_gtap_data \
                                + list_shocks_gemsim \
                                + list_shocks_data

        for file_name in list_of_files_to_copy:
            # copy files with file_name from Input_Files to Work_Files
            shutil.copy('Input_Files\\{1}\\{0}'.format(file_name,self.gtapversion), 'Work_Files\\{0}'.format(file_name))
