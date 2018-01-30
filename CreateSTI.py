__author__ = "Andre Barbe"
__project__ = "Python for GTAP"
__created__ = "2018-1-30"
__altered__ = "2018-1-30"


class CreateSTI(object):
    """Creates an STI File for controlling SLTOHT
    SLTOHT exports variables from the .sl4 file to a .csv file
    The STI file tells SLTOHT where its input and output files are"""

    __slots__ = ["project", "simulation_list"]

    def __init__(self, project: str, simulation_list: list) -> None:
        self.project = project
        self.simulation_list = simulation_list

    def create(self) -> None:
        for simulation in self.simulation_list:
            file_name = self.project + simulation

            # Create list of lines to write to STI file
            line_list = [
                # First, select general options
                "bat         		! Run in batch. \n",
                "log		        ! Start a log file \n",
                "b		        	! Output to both terminal and log file \n",
                "{0}_sltoth_sti.log	    	! Name of log file\n".format(file_name),
                "ses                ! Output to spreadsheet with element labels \n",
                ",                  ! Character to use for data separation \n",
                "shl                ! Show level results, if available \n",
                "                   ! Done selecting general options \n",
                "{0}.sl4            ! Location of sl4 file to convert to csv \n".format(file_name),
                "c                  ! Want both levels and cumulative from solution file \n",
                "y                  ! Use file to choose which variables and components to ouptut \n",
                "{0}.map            ! Name of file to use choosing which variables and components to output \n".format(
                    self.project),
                "{0}.csv            ! Name of file to output to".format(file_name)
            ]

            # Create final file
            with open("{0}.sti".format(file_name), "w+") as writer:  # Create the empty file
                writer.writelines(line_list)  # write the line list to the file
