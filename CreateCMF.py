__author__ = "Andre Barbe"
__project__ = "Python for GTAP"
__created__ = "2018-1-29"
__altered__ = "2018-1-29"


class CreateCMF(object):
    """Creates an CMF file for controlling gemsim when it runs the policy simulation (as opposed to the shock
    calculation)"""

    __slots__ = ["project", "simulation", "solution_method"]

    def __init__(self, project: str, simulation: str, solution_method: str) -> None:
        self.project = project
        self.solution_method = solution_method
        self.simulation = simulation

    def create(self) -> None:

        # Create final file
        with open("{0}{1}.cmf".format(self.project, self.simulation), "w+") as writer:  # Create the empty file
            writer.writelines(CreateCMF(self.project, self.simulation,
                                        self.solution_method).createlinelists())  # write the line list to the file

    def createlinelists(self):
        # Create list of lines to be added to CMF file

        # Create lines for solution method
        if self.solution_method == "default_j":
            line_list_method = [
                "Method = Johansen;\n",
                "Steps = 1;\n",
                "automatic accuracy = no;\n",
                "subintervals = 1;\n",
                "\n"]
        elif self.solution_method == "default_g":
            line_list_method = [
                "!Method = johansen;\n",
                "Method = Gragg;\n",
                "Steps = 3 5 7;\n",
                "automatic accuracy = yes;\n",
                "subintervals = 5;\n",
                "accuracy figures = 5;\n",
                "accuracy percent = 90;\n",
                "Equations file = gtapv7;\n",
                ""]
        else:
            raise ValueError('Unknown solution method in CMF')

        # Create lines for header that gives file locations
        line_list_header = [
            "! This CMF file is used for running the GTAP model outside of RunGTAP !\n",
            "auxiliary files = gtapv7;           \n",
            "check-on-read elements = warn; \n",
            "cpu=yes ; \n",
            "log file = yes;  \n",
            "start with MMNZ = 200000000;\n",
            "!Equations file = gtapv7-eqns;\n",
            "\n"
        ]
        if self.project == "GTAPv7":
            line_input_output_files = [
                "! Input files: \n",
                "File GTAPSETS = SETS.har; \n",
                "File GTAPDATA = BASEDATA.har;\n",
                "File GTAPPARM = Default.prm;\n",
                "\n",
                "! Updated files:\n",
                "Updated File GTAPDATA = <CMF>.UPD;\n",
                "! Output files:\n",
                "File GTAPVOL = GTAPVOL-<CMF>.har; ! HAR file of volume changes\n",
                "File WELVIEW = WELVIEW-<CMF>.har; ! HAR file of volume changes\n",
                "File GTAPSUM = SUMMARY-<CMF>.har; ! Summary/Diagnostics file\n",
                ""]


        line_list_exogendo = [
            "Exogenous\n",
            "          pop\n",
            "          psaveslack pfactwld\n",
            "          profitslack incomeslack endwslack\n",
            "          cgdslack \n",
            "          tradslack\n",
            "          ams atm atf ats atd\n",
            "          aosec aoreg avasec avareg\n",
            "          aintsec aintreg aintall\n",
            "          afcom afsec afreg afecom afesec afereg\n",
            "          aoall afall afeall\n",
            "          au dppriv dpgov dpsave\n",
            "          to tinc \n",
            "          tp tm tms tx txs\n",
            "          qe\n",
            "          qesf\n",
            ";\n",
            "Rest endogenous;"]

        line_list_shocks = [
            "Verbal Description = Test shocks;\n",
            "\n",
            "!====================\n",
            "!       Shocks      \n",
            "!====================\n",
            " \n",
            "!------------------------\n",
            "! (A) Nominal homogeneity\n",
            "!------------------------\n",
            "!Shock pfactwld = 0;\n",
            "!Shock pfactwld = 5;\n",
            "\n",
            "!--------------\n",
            "! (B) Endowment\n",
            "!--------------\n",
            "!Shock qe = uniform 5;\n",
            "!Shock qesf = uniform 1;\n",
            "\n",
            "!----------------\n",
            "! (C) Tech change  \n",
            "!----------------\n",
            "! Note: ao shocks in GTAPv7 is equivalent to   \n",
            "!           aoall(PROD_COMM,REG) \n",
            "!           aosec(PROD_COMM) \n",
            "!       in GTAPv6.2 since ACTS excludes \"cgds\" in GTAPv7  \n",
            "\n",
            "!   --------------\n",
            "!   (c1) ao shocks  \n",
            "!   --------------\n",
            "\n",
            "!   -----------\n",
            "!   (c11) aoreg  \n",
            "!   -----------\n",
            "!Shock aoreg = uniform 5;    !Output augmenting tech change \n",
            "\n",
            "!   -----------\n",
            "!   (c12) aosec \n",
            "!   -----------\n",
            "!Shock aosec= uniform 5;     !Output augmenting tech change\n",
            "\n",
            "!   -----------\n",
            "!   (c13) aoall \n",
            "!   -----------\n",
            "!Shock aoall = uniform 5;    !Output augmenting tech change\n",
            "\n",
            "!   --------\n",
            "!   (c2) ava \n",
            "!   --------\n",
            "!Shock avasec= uniform -5;\n",
            "\n",
            "!   --------------\n",
            "!   (c3) af shocks\n",
            "!   --------------\n",
            "!   -----------\n",
            "!   (c31) afall\n",
            "!   -----------\n",
            "!Shock afall = uniform 5;\n",
            "\n",
            "!   -----------\n",
            "!   (c32) afcom\n",
            "!   -----------\n",
            "!Shock afcom = uniform -10;\n",
            "\n",
            "!   --------------\n",
            "!   (c33) afreg\n",
            "!   --------------\n",
            "!Shock afreg = uniform -5;\n",
            "\n",
            "!   --------------\n",
            "!   (c4) aint shocks\n",
            "!   --------------\n",
            "!Shock aintall = uniform 5;\n",
            "\n",
            "!-----------------------------------------------\n",
            "! (D) Eliminate Output and endowment tax/subsidy \n",
            "!-----------------------------------------------\n",
            "!Shock to   = file SHOCKS.har header \"CTON\";\n",
            "!Shock tinc = file SHOCKS.har header \"CTEN\";\n",
            "\n",
            "!-------------------------\n",
            "! (E) Eliminate Export tax \n",
            "!-------------------------\n",
            "!Shock txs = file SHOCKS.har header \"CTXN\";\n",
            "\n",
            "!---------------------\n",
            "! (F) Eliminate Tariff  \n",
            "!---------------------\n"
        ]
        if self.project == "GTAPv7":
            #line_list_shocks.append("Shock tms = file SHOCKS-10x10.har header \"CTMS\";\n")
        #if self.project == "GTAP":
            line_list_shocks.append("Shock pfactwld = uniform 10;\n")

        line_list_sets = []

        # Combine line lists
        line_list_total = line_list_header \
                          + line_input_output_files \
                          + line_list_method \
                          + line_list_exogendo \
                          + line_list_shocks \
                          + line_list_sets

        return line_list_total
