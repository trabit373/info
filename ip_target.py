def _all_():
    import os
    import sys
    import socket
    import time
    from colorama import Fore
    from baner import baner

    os.system("clear")
    baner()
    time.sleep(1)
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
    target =  input(Fore.RED+"  ┌─["+Fore.GREEN+"H_NWWB"+Fore.BLUE+"~"+Fore.WHITE+"@Information-Data-For-IP"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"ip-target"+Fore.RED+"""]
  └──╼ """+Fore.WHITE+"卐 ")
    if target == "" or None:
        time.sleep(1)
        print(Fore.YELLOW + "["+ Fore.RED + "!" + Fore.YELLOW + "]"+ Fore.RED + " Error" + Fore.YELLOW + " >>> " + Fore.RED + "Your Target Ip None !!!")
        time.sleep(0.4)
        sys.exit()
    else:
        try:
            ip_target = socket.gethostname(target)
        except:
            time.sleep(1)
            print(Fore.RED + "[-] The Required IP Was Not Found")
            time.sleep(0.3)
            sys.exit()
        print(Fore.GREEN + f"[+] Your Target Is : {target}  ,  IP Target Is {ip_target}")
        time.sleep(1)
        print("")
        input(Fore.CYAN + "\n[!] Press Enter For Go The Meno ... ")
        # code  go to the meno
