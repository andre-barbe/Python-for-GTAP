__author__ = "Andre Barbe"
__project__ = "Python for GTAP"
__created__ = "2018-1-25"
__altered__ = "2018-1-29"

import shutil


class CopyInputFiles(object):
    """Copies files from the input files directory to the work files directory"""

    # __slots__ = []

    def create(self) -> None:
        #Define lists of files to copy.
        list_gtap_gemsim = [
            "gtapv7.tab",
            "gtapv7.gss",
            "gtapv7.gst",
            "gtapv7.min",
            "gtapv7.axs",
            "gtapv7.axt",
            "gtapv7.exe",
            # "gtap.cmf",
            "GTAPv7-10x10.cmf"
        ]

        list_shocks_gemsim = [
            "Shocks-10x10.har"
            # "shocks.tab",
            # "shocks.gss",
            # "shocks.gst",
            # "shocks.min",
            # "shocks.cmf"
        ]

        list_gtap_data = [
            "basedata-10x10.har",
            #"basedata.har",
            #"baserate.har",
            #"baseview.har",
            "sets-10x10.har",
            #"sets.har",
            "default-10x10.prm",
            #"default.prm"
        ]

        list_shocks_data = [

        ]

        list_of_files_to_copy = list_gtap_gemsim\
                                + list_gtap_data\
                                + list_shocks_gemsim\
                                + list_shocks_data

        for file_name in list_of_files_to_copy:
            # copy files with file_name from Input_Files to Work_Files
            shutil.copy('Input_Files\\GTAP2\\{0}'.format(file_name), 'Work_Files\\{0}'.format(file_name))
