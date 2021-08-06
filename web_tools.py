def _all_():
    import os
    import time
    import sys
    from colorama import Fore
    from baner import baner

    os.system("clear")
    baner()
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t ["  + Fore.GREEN + "1" + Fore.YELLOW + "]" + Fore.BLACK + "  ~ "+Fore.CYAN + "Obtain Target Programming Plugins And Information")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t ["  + Fore.GREEN + "2" + Fore.YELLOW + "]" + Fore.BLACK + "  ~ "+Fore.CYAN + "Obtain Sites On The Server")
    time.sleep(0.5)


    ####################   GET NUMBER   ####################
    try:
        number = int(input(Fore.LIGHTWHITE_EX + "\n[!] ~ Enter Your Number" + Fore.RED + " >>>" + Fore.GREEN + " "))
    except:
        time.sleep(1)
        print(Fore.RED + "[-] Your Input Is Not Number !!!")
        sys.exit()
    if number == 1:
        import builtwith
        builtwith._all_()
        # _Test_Fore_Back_The_Meno

    if number == 2:
        import site_on_server
        site_on_server._all_()
        # _Test_Fore_Back_The_Meno
    
    else:
        time.sleep(1)
        print(Fore.RED + "[-] Your Number Is Not Found !!!")
        sys.exit()
_all_()
