__author__ = "Andre Barbe"
__project__ = "Python for GTAP"
__created__ = "2018-1-25"
__altered__ = "2018-1-25"

import shutil


class CopyInputFiles(object):
    """Copies files from the input files directory to the work files directory"""

    # __slots__ = []

    def create(self) -> None:
        #Define lists of files to copy.
        list_gtap_gemsim = [
            "gtap.tab",
            "gtap.gss",
            "gtap.gst",
            "gtap.min"
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
            "co2.har",
            "default.prm"
        ]

        list_shocks_data = [
            ""
        ]

        list_of_files_to_copy = list_gtap_gemsim + list_gtap_data + list_shocks_gemsim + list_shocks_data

        for file_name in list_of_files_to_copy:
            # copy files with file_name from Input_Files to Work_Files
            shutil.copy('Input_Files\\{0}'.format(file_name), 'Work_Files\\{0}'.format(file_name))
