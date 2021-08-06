def _all_():
    import os
    import time
    import sys
    from colorama import Fore
    from baner import baner

    os.system("clear")
    baner()
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t     ["  + Fore.GREEN + "1" + Fore.YELLOW + "]" + Fore.BLACK + "  ~ "+Fore.CYAN + "Brout Fource Panel Admin WordPress")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t     ["  + Fore.GREEN + "2" + Fore.YELLOW + "]" + Fore.BLACK + "  ~ "+Fore.CYAN + "Bug /wp-json/v2/users/")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t     ["  + Fore.GREEN + "3" + Fore.YELLOW + "]" + Fore.BLACK + "  ~ "+Fore.CYAN + "Bug XMLRPC")
    time.sleep(0.3)
 
    ####################   GET NUMBER   ####################
    try:
        number = int(input(Fore.LIGHTWHITE_EX + "\n[!] ~ Enter Your Number" + Fore.RED + " >>>" + Fore.GREEN + " "))
    except:
        time.sleep(1)
        print(Fore.RED + "[-] Your Input Is Not Number !!!")
        sys.exit()
    if number == 1:
        import brout_force_wp
        brout_force_wp._all_()
        # _Test_Fore_Back_The_Meno

    if number == 2:
        import wp_json
        wp_json._all_()
        # _Test_Fore_Back_The_Meno

    if number == 3:
        import xmlrpc
        xmlrpc._all_()
        # _Test_Fore_Back_The_Meno

    else:
        time.sleep(1)
        print(Fore.RED + "[-] Your Number Is Not Found !!!")
        sys.exit()
_all_()
