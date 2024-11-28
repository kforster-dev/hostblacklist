# Blacklist Utilities Module
import os, re

Dir = os.getenv('windir') + '\\System32\\drivers\\etc\\hosts'

def checkExists(DomainString):
    # Look for String in Hosts File
    HostsLines = open(Dir).readlines()
    for i in HostsLines:
        if DomainString in i:
            return True
    return False

def checkIP(IPString):
    return bool(re.search("[0-9].[0-9].[0-9].[0-9]", IPString))

def modifyHost(DomainString, newIP):
    HostsFile = open(Dir, mode="r")
    NewCopy = open("tempfile.txt", "a+")
    #Create edited file without the removed domain.
    for i in HostsFile.readlines():
        if DomainString in i:
            #Determine if we are deleting or modifying the line.
            if newIP == False:
                print("Removing... ",i)
            elif checkIP(newIP) == True: #add a check for formatting.
                newLine = newIP + " " + DomainString
                print("Modifying... ", i, " into... ", newLine)
                NewCopy.write(newLine+'\n')
            else:
                # Cancel the function and clean up.
                print("Invalid Input. Try Again.")
                HostsFile.close()
                NewCopy.close()
                os.system('del tempfile.txt')
                return
        else:
            NewCopy.write(i)
    HostsFile.close()
    NewCopy.close()
    #Overwrite Hosts file with adjusted version.
    CopyTxt = open('tempfile.txt', 'r').read()
    HostsFile = open(Dir, mode="w")
    HostsFile.write(CopyTxt)
    HostsFile.close()
    os.system('del tempfile.txt')

def blacklist(DomainString, newIP):
    HostsFile = open(Dir,mode='a+')
    Addition = "\n"+ newIP +" " + DomainString
    HostsFile.write(Addition)
    HostsFile.close()