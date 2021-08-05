def _all_():
    try:
        import os
        import time
        import sys
        import subprocess
        from baner import baner
        try:
            from colorama import Fore
        except:
            time.sleep(1)
            print("[-] Pleass Install The Librery --> colorama")
            sys.exit()
        try:
            import re
        except:
            time.sleep(1)
            print("[-] Pleass Install The Librery --> re")
            sys.exit()
        try:
            import netifaces
        except:
            time.sleep(1)
            print("[-] Pleass Install The Librery --> netifaces")
            sys.exit()
        import platform
        name_system = platform.system()
        if name_system == "Linux":
            pass
        else:
            time.sleep(1)
            print(Fore.RED + "[-] Your OS System Not The Linux !!!")
            sys.exit()

        check_mac1 = subprocess.getoutput("ifconfig")
        my_mac1 = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w:" , check_mac1)
        baner()
        time.sleep(0.3)
        text = Fore.LIGHTWHITE_EX + "  [!] " +  Fore.CYAN + "Enter Your New MAC Address !\n"
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
        new_mac =  input(Fore.RED+"  ┌─["+Fore.GREEN+"H_NWWB"+Fore.BLUE+"~"+Fore.WHITE+"@Information-Data-For-IP"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"MAC-Changer"+Fore.RED+"""]
      └──╼ """+Fore.WHITE+"卐 ")
        
        if new_mac == "" or None :
            time.sleep(1)
            print(Fore.RED + "[-] Your Input Is Not Found !!!")
            sys.exit()
        else:
            count = 0
            for i in new_mac:
                if i == ":":
                    count += 1
                else:
                    pass
            if count == 5:
                pass
            else:
                time.sleep(1)
                print(Fore.RED + "[-] Yout Nwe Mac Is Not Found !!!")
                sys.exit()

                
        time.sleep(0.3)
        text = Fore.LIGHTWHITE_EX + "  [!] " +  Fore.CYAN + "Enter Your Name Network !\n"
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
        name_network =  input(Fore.RED+"  ┌─["+Fore.GREEN+"H_NWWB"+Fore.BLUE+"~"+Fore.WHITE+"@Information-Data-For-IP"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"MAC-Changer"+Fore.RED+"""]
      └──╼ """+Fore.WHITE+"卐 ")
                
                
        if name_network == "" or None:
            time.sleep(1)
            print(Fore.RED + "[-] Your Input Is Not Found !!!")
            sys.exit()
        else:
            all_name_network = netifaces.interfaces()
            if name_network not in all_name_network:
                time.sleep(1)
                print(Fore.RED + "[-] Your Name Network Is Not Found !!!")
                sys.exit()
            else:
                pass
        #_________________________________________________
        """
        تا اینجای کار ما تایید کردیم که  مک آدرس جدید و اسم شبکه درست است ,الان باید با دستورات سیستمی بیاایم و کار را شروع کنیم
        """
        #_________________________________________________
        subprocess.run(["sudo" , "ifconfig" , name_network , "down"] , shell=True)
        try:
            subprocess.run(["sudo" , "ifconfig" , name_network , "hw" , "ether" , new_mac])
        except:
            subprocess.run(["sudo" , "ifconfig" , name_network , "hw" , "ether" , new_mac])
        subprocess.run(["sudo" , "ifconfig" , name_network , "up"] , shell=True)

        check_mac2 = subprocess.getoutput("ifconfig")
        my_mac2 = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w:" , check_mac1)
        if my_mac1 == my_mac2:
            time.sleep(1)
            print(Fore.RED + "[-] The Your MAC Address Did Not Change")
            sys.exit()
        else:
            time.sleep(1)
            print(Fore.GREEN + "The Your MAC Address Is  Changing")
            sys.exit()
    except KeyboardInterrupt:
        time.sleep(1)
        print(Fore.YELLOW + "\n\n[!] Ok Good Lunch :)))")
        sys.exit()
