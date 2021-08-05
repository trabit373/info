def _all_():
    import os
    import sys
    import time
    from baner import baner
    try:
        from colorama import Fore
    except:
        time.sleep(1)
        print("[-] Pleass Install The Librery --> colorama")
        sys.exit()
    os.system("clear")
    baner()
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t     ["  + Fore.GREEN + "1" + Fore.YELLOW + "]" + Fore.BLACK + "  ~ "+ Fore.CYAN + "Online Traceroute Using MTR")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t     ["  + Fore.GREEN + "2" + Fore.YELLOW + "]" +  Fore.BLACK + "  ~ "+Fore.CYAN + "Test Ping")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t     ["  + Fore.GREEN + "3" + Fore.YELLOW + "]" + Fore.BLACK + "  ~ "+Fore.CYAN + "DNS Lookup")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t     ["  + Fore.GREEN + "4" + Fore.YELLOW + "]" + Fore.BLACK + "  ~ "+Fore.CYAN + "Reverse DNS Lookup")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t     ["  + Fore.GREEN + "5" + Fore.YELLOW + "]" + Fore.BLACK + "  ~ "+Fore.CYAN + "Find DNS Host Records (Subdomains)")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t     ["  + Fore.GREEN + "6" + Fore.YELLOW + "]" + Fore.BLACK + "  ~ "+Fore.CYAN + "Find Shared DNS Servers")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t     ["  + Fore.GREEN + "7" + Fore.YELLOW + "]" + Fore.BLACK + "  ~ "+Fore.CYAN + "Zone Transfer Online Test")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t     ["  + Fore.GREEN + "8" + Fore.YELLOW + "]" + Fore.BLACK + "  ~ "+Fore.CYAN + "Whois Lookup")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t     ["  + Fore.GREEN + "9" + Fore.YELLOW + "]" + Fore.BLACK + "  ~ "+Fore.CYAN + "GeoIP – IP Location Lookup")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t     ["  + Fore.GREEN + "10" + Fore.YELLOW + "]" + Fore.BLACK + " ~ "+Fore.CYAN + "Reverse IP Lookup")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t     ["  + Fore.GREEN + "11" + Fore.YELLOW + "]" + Fore.BLACK + " ~ "+Fore.CYAN + "TCP Port Scan (Nmap)")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t     ["  + Fore.GREEN + "12" + Fore.YELLOW + "]" + Fore.BLACK + " ~ "+Fore.CYAN + "Subnet Lookup Online")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t     ["  + Fore.GREEN + "13" + Fore.YELLOW + "]" + Fore.BLACK + " ~ "+Fore.CYAN + "Autonomous System Lookup (AS / ASN / IP)")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t     ["  + Fore.GREEN + "14" + Fore.YELLOW + "]" + Fore.BLACK + " ~ "+Fore.CYAN + "Banner Grabbing (Search)")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t     ["  + Fore.GREEN + "15" + Fore.YELLOW + "]" + Fore.BLACK + " ~ "+Fore.CYAN + "HTTP Header Check")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t     ["  + Fore.GREEN + "16" + Fore.YELLOW + "]" + Fore.BLACK + " ~ "+Fore.CYAN + "Extract Links From Page")
    time.sleep(0.3)
    print(Fore.YELLOW + "\t\t\t     ["  + Fore.GREEN + "17" + Fore.YELLOW + "]" + Fore.BLACK + " ~ "+Fore.CYAN + "Reverse Analytics Search")
    time.sleep(0.3)
    ####################   GET NUMBER   ####################
    try:
    number = int(input(Fore.LIGHTWHITE_EX + "\n[!] ~ Enter Your Number" + Fore.RED + " >>>" + Fore.GREEN + " "))
    except:
    time.sleep(1)
    print(Fore.RED + "[-] Your Input Is Not Number !!!")
    sys.exit()
    if number == 1:
        import mtr
        mtr._all_()
        # _Test_Fore_Back_The_Meno

    if number == 2:
        import nping
        nping._all_()
        # _Test_Fore_Back_The_Meno

    if number == 3:
        import dns_lookup
        dns_lookup._all_()
        # _Test_Fore_Back_The_Meno

    if number == 4:
        import reversedns
        reversedns._all_()
        # _Test_Fore_Back_The_Meno

    if number == 5:
        import hostsearch
        hostsearch._all_()
        # _Test_Fore_Back_The_Meno

    if number == 6:
        import findshareddns
        findshareddns._all_()
        # _Test_Fore_Back_The_Meno

    if number == 7:
        import zonetransfer
        zonetransfer._all_()
        # _Test_Fore_Back_The_Meno

    if number == 8:
        import whois
        whois._all_()
        # _Test_Fore_Back_The_Meno

    if number == 9:
        import geoip
        geoip._all_()
        # _Test_Fore_Back_The_Meno

    if number == 10:
        import reverseiplookup
        reverseiplookup._all_()
        # _Test_Fore_Back_The_Meno

    if number == 11:
        import nmap
        nmap._all_()
        # _Test_Fore_Back_The_Meno

    if number == 12:
        import subnetcalc
        subnetcalc._all_()
        # _Test_Fore_Back_The_Meno

    if number == 13:
        import aslookup
        aslookup._all_()
        # _Test_Fore_Back_The_Meno

    if number == 14:
        import bannerlookup
        bannerlookup._all_()
        # _Test_Fore_Back_The_Meno

    if number == 15:
        import httpheaders
        httpheaders._all_()
        # _Test_Fore_Back_The_Meno

    if number == 16:
        import pagelinks
        pagelinks._all_()
        # _Test_Fore_Back_The_Meno


    if number == 17:
        import analyticslookup
        analyticslookup._all_()
        # _Test_Fore_Back_The_Meno
_all_()
