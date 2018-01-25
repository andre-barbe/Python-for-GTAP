__author__ = "Andre Barbe"
__project__ = "Python for GTAP"
__created__ = "2018-1-25"
__altered__ = "2018-1-25"

import os, shutil


class Cleanup(object):
    """Cleanup for next run by deleting files from work directory"""

    # __slots__ = []

    def create(self) -> None:

        folder = 'Work_Files'
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)
