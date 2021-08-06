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
    target =  input(Fore.RED+"  ┌─["+Fore.GREEN+"H_NWWB"+Fore.BLUE+"~"+Fore.WHITE+"@WP-Hacking"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"wp-json"+Fore.RED+"""]
  └──╼ """+Fore.WHITE+"卐 ")
    if target == "" or None:
        time.sleep(1)
        print(Fore.YELLOW + "["+ Fore.RED + "!" + Fore.YELLOW + "]"+ Fore.RED + " Error" + Fore.YELLOW + " >>> " + Fore.RED + "Your Target Ip None !!!")
        time.sleep(0.4)
        sys.exit()
    else:
        for i in range(1):
          if "http://" or "https://" not in target:
              target = "https://" + target
          new_target = target + "/" + "wp-json/v2/users/"
          try:
            R = requests.get(new_target).text
          except:
              time.sleep(1)
              print(Fore.RED + "[-] Error " + Fore.YELLOW + ">>> " + Fore.RED + "This page Tools Have The Problem !")
              break
          print(Fore.GREEN + f"\n{R}")
    time.sleep(1)
    print("")
    input(Fore.CYAN + "\n[!] Press Enter For Go The Meno ... ")
