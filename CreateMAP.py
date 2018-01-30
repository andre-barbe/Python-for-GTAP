__author__ = "Andre Barbe"
__project__ = "Python for GTAP"
__created__ = "2018-1-30"
__altered__ = "2018-1-30"


class CreateMAP(object):
    """Creates the MAP File for use in SLTOTH
    Map gives the list of variables to be exported from the sl4 to the csv results file"""

    __slots__ = ["file","linelist"]

    def __init__(self, file: str, linelist: list) -> None:
        self.file = file
        self.linelist=linelist

    def create(self) -> None:
        # Create the contents to be written to the file


        # Create final file
        with open("{0}.map".format(self.file), "w+") as writer:  # Create the empty file
            writer.writelines(self.linelist)  # write the line list to the file
