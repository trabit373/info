def baner():
  import os
  import time
  import sys
  from colorama import Fore
  text = (Fore.LIGHTBLACK_EX +  """
  ██╗  ██╗                ███╗   ██╗██╗    ██╗██╗    ██╗██████╗
  ██║  ██║                ████╗  ██║██║    ██║██║    ██║██╔══██╗
  ███████║                ██╔██╗ ██║██║ █╗ ██║██║ █╗ ██║██████╔╝
  ██╔══██║                ██║╚██╗██║██║███╗██║██║███╗██║██╔══██╗
  ██║  ██║    ███████╗    ██║ ╚████║╚███╔███╔╝╚███╔███╔╝██████╔╝
  ╚═╝  ╚═╝    ╚══════╝    ╚═╝  ╚═══╝ ╚══╝╚══╝  ╚══╝╚══╝ ╚═════╝

  ═════════════════════════════════════════════════════════════
  **                    Name : ?                             **
  **                    Family : ?                           **
  **                    Muzic : A M R O F - C O L            **
  **                    Live : M U Z I C                     **
  ═════════════════════════════════════════════════════════════
  """)



  os.system("clear")
  count = 0
  while True:
    try:
      text_me = text[int(count)]
      sys.stdout.write(f"{str(text_me)}"),sys.stdout.flush()
      count += 1
      time.sleep(0.003)
    except:
      print("")
      break
