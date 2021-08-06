def _all_():
    import os
    import time
    import sys
    import requests
    from colorama import Fore
    from baner import baner

    os.system("clear")
    baner()
    time.sleep(0.3)
    text = Fore.LIGHTWHITE_EX + "  [!] " +  Fore.CYAN + "Enter Your Domain Target !\n"
    count = 0
    while True:
        try:
            text_me = text[int(count)]
            sys.stdout.write(f"{str(text_me)}"),sys.stdout.flush()
            count += 1
            time.sleep(0.08)
        except:
            print("")
            break
    target =  input(Fore.RED+"  ┌─["+Fore.GREEN+"H_NWWB"+Fore.BLUE+"~"+Fore.WHITE+"@WP-Hacking"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"xmlrpc"+Fore.RED+"""]
  └──╼ """+Fore.WHITE+"卐 ")
    if target == "" or None:
        time.sleep(1)
        print(Fore.YELLOW + "["+ Fore.RED + "!" + Fore.YELLOW + "]"+ Fore.RED + " Error" + Fore.YELLOW + " >>> " + Fore.RED + "Your Target Ip None !!!")
        time.sleep(0.4)
        sys.exit()
    else:
        my_list = """
        xmlrpc.php
        xmlrpc
        xmrlpc 
        xmrlpc.php
        """.split()
        for i in my_list:
            new_target = target + "/" + i
            R = requests.get(new_target).status_code
            if R == 200 or 400:
                print(Fore.YELLOW + : "[" + Fore.GREEN + "+" + Fore.YELLOW + "]" + Fore.BLUE + " ~ " + Fore.GREEN + "This Is Found " + Fore.YELLOW + ": " + Fore.GREEN + new_target)
            else:
                print(Fore.YELLOW + : "[" + Fore.RED + "+" + Fore.YELLOW + "]" + Fore.CAYN + " ~ " + Fore.RED + "This Is Not Found " + Fore.YELLOW + ": " + Fore.RED + new_target)
    time.sleep(1)
    print("")
    input(Fore.CYAN + "\n[!] Press Enter For Go The Meno ... ")
