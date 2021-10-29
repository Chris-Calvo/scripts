import csv
import os

filename = "C:/Users/Chris/Downloads/linux_users.csv"

def create_username(aList):
    if (len(aList) < 2):
        print("INVALID RECORD")
    else:
        tokens = list(aList[2])
        username = tokens[0].lower() + aList[1].lower()
        return username

with open(filename) as f_handle:
    csv_reader = csv.reader(f_handle)
    next(csv_reader)
    userList = []
    groupList = []
    recordCopy = []
    rep = 0
    tick = True

    for record in csv_reader:
        if (record[7] == ""):
            record.remove(record[7])

        for data in record:
            if (data == ""):
                print("ERROR: MISSING INFORMATION. USER ID: " + record[0] + " HAS NOT BEEN ADDED")
                tick = False
        
        if ((record[6] not in groupList) and (tick == True)):
            groupList.append(record[6])

        if (tick == True):
            username = create_username(record)
            if (username in userList):
                username += str(rep)
                rep += 1
            userList.append(username)
            recordCopy.append(record)

        else:
            tick = True
    
    for group in groupList:
        # os.system("groupadd " + group)
        print("GROUP: " + group + " HAS SUCCESSFULLY BEEN CREATED")
    
    i = 0
    for record in recordCopy:
        if (record[5] == "ceo"):
            # os.system("adduser " + username + ' "' + record[1] + " " + record[2] + '" ' + "-G " + record[6] +
            # " -d /home/" + record[5] + " -s /bin/csh -u " + record[0] + " -p password -c OFFICE:" + record[3] + 
            # "| PHONE: " + record[4])
            print("adduser " + userList[i] + ' "' + record[2] + " " + record[1] + '" ' + "-G " + record[6] +
            " -d /home/" + record[5] + " -s /bin/csh -u " + record[0] + " -p password -c OFFICE: " + record[3] + 
            " | PHONE: " + record[4])
            print("passwrd -expire " + userList[i])
        else:
            print("adduser " + userList[i] + ' "' + record[2] + " " + record[1] + '" ' + "-G " + record[6] +
            " -d /home/" + record[5] + " -s /bin/ -u " + record[0] + " -p password -c OFFICE: " + record[3] + 
            " | PHONE: " + record[4])
            print("passwrd -expire " + userList[i])
        i += 1
        print("USER: " + record[0] + " HAS SUCCESSFULLY BEEN ADDED")

        
            

        