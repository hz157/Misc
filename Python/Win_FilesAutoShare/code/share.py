### Windows_Smb_Share（batch）
### manual：https://blog.csdn.net/m0_50238829/article/details/108136451

import os
import sys
import xlrd

# Read user Table
def read_xlsx(path):
    data = xlrd.open_workbook(path)
    table = data.sheet_by_index(0)
    hang = int(table.nrows)
    lie = int(table.ncols)
    list_ls = [] 
    for i in range(hang):
        dic = {"name":"null","password":"null","group":"null"}
        dic["name"] = str(table.cell_value(i,0))
        dic["password"] = str(table.cell_value(i,1))
        dic["group"] = str(table.cell_value(i,2))
        list_ls.append(dic)
    return list_ls


# Create User
def creat(user, password):
    # net user username password /add
    # cmd add user command
    command = "net user %s %s /add" %(user, password)
    os.system(command)

# Set UserGroup
def set_group(user, group):
    # net localgroup groupname username /add
    # cmd add user group command
    command1 = "net localgroup %s %s /add" %(group, user)
    os.system(command1)
    # net localgroup groupname username /del
    # cmd delete the user from the group command
    command2 = "net localgroup Users %s /del" %(user)
    os.system(command2)

# Create user folder and set permissions
def creat_file(file_dict):
    for i in file_dict:
        name = i["name"]
        # md d:\share\student1
        # cmd create folder command
        command1 = "md d:\share\%s" %(name)
        os.system(command1)
        # user permissions
        command2 = "Cacls d:\share\%s /t /e /c /g %s:F" %(name, name)
        os.system(command2)

# Set up home folder sharing
def share_file():
    print("Please enter a share name", end=' ')
    file_name = input()
    command = "net share %s=d:\share" %(file_name)
    os.system(command)


# 主函数
def main(file_path):
    user_dict = read_xlsx(file_path) # user list
    for i in user_dict:
        username = i["name"]
        password = i["password"]
        groupname = i["group"]
        # create user
        creat(username, password)
        # 设置用户隶属组
        set_group(username,groupname)
    # create user folder
    command = "md d:\share"
    os.system(command)
    tip(user_dict)    
    share_file()

# Manual operation prompt
def tip(user_dict):
    print("Please set the file permissions manually, and continue operation after setting!!（Y/N）：", end=' ')
    check_flag = input()
    if check_flag == "y" or check_flag == "Y":
        creat_file(user_dict)



print("\t Automatically create user scripts (SMB version)")
print("Tips: Please check whether the anti-virus software is turned off before use. (Y/N) :",end=' ')
flag = input()
if flag == "Y" or flag == "y" :
    print("Do I need to create a new user group? (Y/N) :",end=' ')
    flag1 = input()
    if flag1 == "Y" or flag1 =="y":
        print("Please enter the user group name that you want to create (the same user group name in excel file) :",end=' ')
        flag2 = input()
        command = "net localgroup %s /add" %(flag2)
        os.system(command)
    print("Please enter the user table path：")
    path = input()
    main(path)
else:
    print("Please close the antivirus software and open the script again")
    print("End of the script")
    sys.exit(0)





    
