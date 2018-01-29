! closure for ALTERTAX simulation
Exogenous ! Part of closure for altertax runs
          pop
          psaveslack pfactwld
          profitslack incomeslack endwslack
!          cgdslack 
          tradslack
          ams atm atf ats atd
          aosec aoreg avasec avareg
          aintsec aintreg aintall
          afcom afsec afreg afecom afesec afereg
          aoall afall afeall
          au dppriv dpgov dpsave
          to tinc 
          tp tm tms tx txs
          qe
          qesf
!    del_tbalr exogenous for all regions except one,
!    and SAVESLACK exogenous for that one region (which can be any one).

del_tbal(XREG)
cgdslack(REG1);
Rest endogenous;
