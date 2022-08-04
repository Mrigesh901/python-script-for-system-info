import os
import platform

print(" Welcome To Menu Script Program ")

print()
print('Press 1: Home directory')
print('Press 2: OS name & version')
print('Press 3: Current working directory')
print('Press 4: Number of users logged In')
print('Press 5: Hard disk information')
print('Press 6: CPU information')
print('Press 7: Memory information')
print('Press 8: Exit From Menu')
print()

while True:
    print("Enter Your Choice : ", end='')
    p = input()

    if int(p) == 1:
        a = os.path.expanduser("~")
        print(a)
    elif int(p) == 2:
        print(platform.platform())
    elif int(p) == 3:
        print(os.getcwd())
    elif int(p) == 4:
        os.system("whoami")
    elif int(p) == 5:
        os.system("wmic diskdrive get model, serialNumber, size, mediaType")
    elif int(p) == 6:
        os.system("wmic cpu")
    elif int(p) == 7:
        os.system("wmic memorychip")
    elif int(p) == 8:
        os.system("exit()")
        break
    else:
        print("invalid option")
