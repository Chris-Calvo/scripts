#!/usr/bin/python3
import os

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
        else:
            return False

# Option 1 - Create a link
def c_link():
    fname = input("Enter FILENAME: ")
    found = find(fname, "/home")
    print("Creating link...")

    if (found != False):
        os.symlink(found, "/home")
    else:
        print("ERROR: FILE COULD NOT BE FOUND")

# Option 2 - Remove a link
def del_link():
    name = input("Enter NAME of shortcut")
    print("Removing link...")
    if (os.path.exists):
        os.unlink("/home" + name)
    else:
        print("INVAID SHORTCUT NAME")

# Option 3 - List all links
def sum_link():
    os.system("cd /home")
    os.system("find . -maxdepth 1 -type l -ls")

# Starting menu
def printStart():
	print(
	"##################################################################\n\n"
	+"                     Select an option\n\n"
	+"##################################################################\n\n"
	+"               1: Create a Symbolic Link\n"
	+"               2: Remove a Symbolic Link\n"
	+"               3: List Existing Symbolic Links\n"
	+"               Q or q to QUIT\n"
	)

# Reset output
def reset():
	input("Press any key to continue...")
	os.system("clear")
	printStart()

def main():
    printStart()
    while(True):
        val = input(">> ")
        if(val == "1"):
            c_link()
            reset()
        elif(val == "2"):
            del_link()
            reset()
        elif(val == "3"):
            sum_link()
            reset()
        elif(val == "q" or val == "Q"):
            print("Exiting program...")
            break
        else:
            print("\033[31;1mINVALID COMMAND\033[37;0m")
        printStart()

print(find("1_ping_test.py", "C:\CSEC"))
