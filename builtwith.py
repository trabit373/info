def _all_():
    import os
    import time
    import sys
    try:
      import builtwith
    except:
      print("[-] Pleass Install The Librery --> builtwith")
    from baner import baner
    from colorama import Fore

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
    target =  input(Fore.RED+"  ┌─["+Fore.GREEN+"H_NWWB"+Fore.BLUE+"~"+Fore.WHITE+"@WEB-Tools"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"builtwith"+Fore.RED+"""]
  └──╼ """+Fore.WHITE+"卐 ")
    if target == "" or None:
        time.sleep(1)
        print(Fore.YELLOW + "["+ Fore.RED + "!" + Fore.YELLOW + "]"+ Fore.RED + " Error" + Fore.YELLOW + " >>> " + Fore.RED + "Your Target Ip None !!!")
        time.sleep(0.4)
        sys.exit()
    if "http://" or "https://" not in target:
      target = "https://" + target
    target_new = str(target)
    info = builtwith.parse(target_new)
    for keys,values in info.items():
      print(Fore.GREEN + " [+] " + Fore.YELLOW + keys + "   :   " +Fore.CYAN + str(values))
