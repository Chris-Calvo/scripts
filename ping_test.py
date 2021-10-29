#!/usr/bin/python3
# Script01 - 9.20.21
# Christopher Calvani

import os, socket, struct, subprocess

os.system("clear")
global tick

# Prints starting menu
def printStart():
	print(
	"##################################################################\n\n"
	+"                     Select an option\n\n"
	+"##################################################################\n\n"
	+"               1: Test for connectivity to gateway\n"
	+"               2: Test for remote connectivity\n"
	+"               3: Test for DNS resolution\n"
	+"               4: Display Gateway IP Address\n"
	)

# Used to retrieve DG from /proc/net/route
def getGateway():
	with open("/proc/net/route") as fh:
		for line in fh:
			fields = line.strip().split()
			#If fields[1] != DG or RTF_GATEWAY, skip
			if fields[1] != "00000000" or not int(fields[3], 16) & 2:
				continue
			return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))
# Option 1 - ping DG
def testGateway():
	hostname = getGateway()
	response = subprocess.run(["ping", "-c", "1", hostname])
	os.system("clear")
	if subprocess.check_output(["ping", "-c", "1", "192.168.1.254"]):
		return("Option 1 - The test was \033[32;1m SUCCESSFUL \033[37;0m")
	else:
		return("The test has \033[31;1m FAILED \033[37;0m")

# Option 2 - ping RIT (remote)
def testRemote():
	hostname = "129.21.3.17"
	response = os.system("ping -c 1 " + hostname)
	os.system("clear")
	if response == 0:
		return("Option 2 - The test was \033[32;1m SUCCESSFUL \033[37;0m")
	else:
		return("The test has \033[31;1m FAILED \033[37;0m")

# Option 3 - resolve DNS
def testDNS():
	os.system("clear")
	try:	
		#This returns an IP, or exception is caught
		addr = socket.gethostbyname("www.google.com")
		os.system("clear")
		return("Option 3 - The test was \033[32;1m SUCCESSFUL \033[37;0m : DNS resolved to " + addr)
	except socket.error:
		return("The test has \033[31;1m FAILED \033[37;0m")

# Option 4 - display GW
def displayAddr():
	os.system("clear")
	print("Option 4 - The default gateway of this machine is: \033[36;1m" + getGateway() + "\033[37;0m")	

# Reset output
def reset():
	input("Press any key to continue...")
	os.system("clear")
	printStart()

# Starting main
printStart()
val = ""
run = True

# Checks for user input and runs correct test based on input 
while(val != "q" or val != "Q"):
	val = input(">>")
	if(val == "1"):
		print(testGateway())
		reset()
	elif(val == "2"):
		print(testRemote())
		reset()
	elif(val == "3"):
		print(testDNS())
		reset()
	elif(val == "4"):
		displayAddr()
		reset()
	elif(val == "q" or val == "Q"):
		print("Exiting program...")
		break
	else:
		print("\033[31;1mINVALID COMMAND\033[37;0m")




