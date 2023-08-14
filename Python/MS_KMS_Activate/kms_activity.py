import os
import platform
import requests
import json
import time

# Use online or offline,
# Online requires web to provide JSON
networkStatus = "offline"

Keys = {}
Commands = {}
KeyFlag = None

class CommandType:
    windows = "Windows"
    office = "Office x86"
    officex64 = "Office x86_64"


def config():
    if networkStatus == "online":
        global KEY_URL, COMMAND_URL, HEADERS
        KEY_URL = "your key json url"
        COMMAND_URL = "your command json url"
        HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"}
        GetKey()
        GetCommand()
    else:
        global KMS_SERVER
        KMS_SERVER = ""
        ReadFile()

def ReadFile():
    global Keys, Commands
    with open("./key.json", "r", encoding="utf-8") as f:
        Keys = json.load(f)
    with open("./command.json", "r", encoding="utf-8") as f:
        Commands = json.load(f)

def GetKey():
    global Keys
    # get web json for link
    response = requests.get(KEY_URL, headers=HEADERS)
    # get json file content
    response_json = json.loads(response.text)
    Keys = response_json

def WindowsKeyShow():
    global KeyFlag
    print("System Versions")
    if (Keys == ""):
        print("Not Found key")
    else:
        select = Keys
        while (KeyFlag == None):    # Loop
            select = PrintDict(select)
        print(f"Your Select Key: {select}")

def GetCommand():
    global Commands
    # get web json for link
    response = requests.get(COMMAND_URL, headers=HEADERS)
    # get json file content
    response_json = json.loads(response.text)
    Commands = response_json

def PrintDict(dict):
    global KeyFlag
    current = 1
    printList = []
    for i in dict:
        print(f"{current}. {i}")
        printList.append(i)
        current += 1
    number = int(input('Enter Number: ')) - 1       # Receive User Input Number
    selectData = dict[printList[number]]
    if (type(selectData) == str):
        KeyFlag = selectData
    return selectData      # Return User Select Params

def CheckKey():
    print("Check Keys(Yes/No): ")
    check = input()
    if check.lower == "yes" or check.lower == "y":
        ExecuteCommand(CommandType.windows)
    else:
        Menu()

def ExecuteCommand(type: CommandType):
    for i in Commands[type]:
        command = i
        if networkStatus != "online":
            if "{KMS IP}" in command:
                command = command.replace("{KMS IP}", KMS_SERVER)
        if "{KEYS}" in command:
            command = command.replace("{KEYS}", KeyFlag)
        print(command)
        executeResult = os.popen(command)
        print(executeResult)
        time.sleep(1)
        
def Menu():
    os.system("cls")
    print("       _____          __  .__  ".center(80))   
    print("  /  _  \   _____/  |_|__|__  __ ____  ".center(80))   
    print(" /  /_\  \_/ ___\   __\  \  \/ // __ \ ".center(80))   
    print("/    |    \  \___|  | |  |\   /\  ___/ ".center(80))   
    print("\____|__  /\___  >__| |__| \_/  \___  >".center(80))   
    print("        \/     \/                   \/ ".center(80))            
    print("version: 2023.08".rjust(80))
    status = "online" if "online" in networkStatus else "offline"
    print(f"Script Status: {status}".rjust(80))
    print("-"*84)    
    print("|","Machine Info".center(80),"|")
    print("|",f"Version: {platform.version()}".ljust(80),"|")
    print("|",f"Architecture: {platform.architecture()}".ljust(80),"|")
    print("|",f"Machine: {platform.machine()}".ljust(80),"|")
    print("|",f"Processor: {platform.processor()}".ljust(80),"|")
    print("|",f"Node: {platform.node()}".ljust(80),"|")
    print("|",f"Platform: {platform.platform()}".ljust(80),"|")
    print("|",f"System: {platform.system()}".ljust(80),"|")
    print("|",f"Release: {platform.release()}".ljust(80),"|")
    print("-"*84)
    print("Menu".center(50))
    print("1. Active Windows".ljust(50))
    print("2. Active Office x86".ljust(50))
    print("3. Active Office x64".ljust(50))
    number = int(input("Enter Number: "))
    if number == 1:
        os.system("cls")
        WindowsKeyShow()
    elif number == 2:
        print("Not Supported Yet")
    elif number == 3:
        print("Not Supported Yet")
    else:
        print("Invalid Number")

def main():
    config()
    Menu()
    

if __name__ == "__main__":
    main()


