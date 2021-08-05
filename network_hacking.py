def _all_():
    import os
    import time
    import sys
    from colorama import Fore
    from baner import baner

    os.system("clear")
    baner()
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t     ["  + Fore.GREEN + "1" + Fore.YELLOW + "]" + Fore.BLACK + "  ~ "+Fore.CYAN + "MAC Changer")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t     ["  + Fore.GREEN + "2" + Fore.YELLOW + "]" + Fore.BLACK + "  ~ "+Fore.CYAN + "Network Scanner")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t     ["  + Fore.GREEN + "3" + Fore.YELLOW + "]" + Fore.BLACK + "  ~ "+Fore.CYAN + "ARP Spoofer")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t     ["  + Fore.GREEN + "4" + Fore.YELLOW + "]" + Fore.BLACK + "  ~ "+Fore.CYAN + "Disconnect Internet Access")
 
    ####################   GET NUMBER   ####################
    try:
        number = int(input(Fore.LIGHTWHITE_EX + "\n[!] ~ Enter Your Number" + Fore.RED + " >>>" + Fore.GREEN + " "))
    except:
        time.sleep(1)
        print(Fore.RED + "[-] Your Input Is Not Number !!!")
        sys.exit()
    if number == 1:
        import mac_changer
        mac_changer._all_()
        # _Test_Fore_Back_The_Meno

    if number == 2:
        import network_scanner
        network_scanner._all_()
        # _Test_Fore_Back_The_Meno

    if number == 3:
        import arp_spoofer
        arp_spoofer._all_()
        # _Test_Fore_Back_The_Meno

    if number == 4:
        import dis_internet
        dis_internet._all_()
        # _Test_Fore_Back_The_Meno

    else:
        time.sleep(1)
        print(Fore.RED + "[-] Your Number Is Not Found !!!")
        sys.exit()
_all_()
