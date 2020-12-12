import os 
import nmap 
import pyfiglet

blok1 = pyfiglet.figlet_format("Hellu")
print(blok1)

target = input("target: ")
os.system("nmap -sV -Pn " + target)

blok2 = pyfiglet.figlet_format("BY")
print(blok2)

exit = input("exit:")