import hashlib
import os
import sys

RED='\033[91m'
BLUE='\33[94m'
END='\033[0m'

if len(sys.argv) < 2:
	os.system('cls||clear')
	sys.stdout.write(RED+"""\t\t\t
███╗   ███╗██████╗ ███████╗     ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
████╗ ████║██╔══██╗██╔════╝    ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██╔████╔██║██║  ██║███████╗    ██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██║╚██╔╝██║██║  ██║╚════██║    ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██████╔╝███████║    ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝     ╚═╝╚═════╝ ╚══════╝     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                       



	\n"""+END)
else:
	sys.exit("Usage : python3 nmapscript.py ")
	os.system("cls||clear")

count=0

myhash =input("enter md5 hash : ")
wordlist= input("enter your file name : ")
try:
	 pass_file=open(wordlist,"r")
except:
	print("no file found")
	quit()
	
for word in pass_file:
	encwr=word.encode('utf-8')
	digest=hashlib.md5(encwr.strip()).hexdigest()
	print(myhash +":"+ word)
	
	if digest ==myhash:
		print(RED+"[+]PASSWORD FOUND[+]")
		print(RED+"[+]Password is :"+word)
		count==1
		break
		
if count ==0:
	print ("[+]Password not found[+]")
