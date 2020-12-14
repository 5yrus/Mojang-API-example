import requests, os, time


def main():
    os.system('cls')
    print(f"            Boogetware Minecraft              ")
    print(f"                                              ")
    print(f"            [1] Username to UUID              ")
    print(f"            [2] UUID to username              ")
    print(f"              [3] Name history                ")
    print(f"                                              ")
    option = int(input("Please select a choice: "))
    
    if option == 1:
        usernameToUUID()
    elif option == 2:
        UUIDToUsername()
    elif option == 3:
        nameHist()
    else:
        print("Invalid option! Going back in 3 seconds.")
        time.sleep(3)
        main()
         
def usernameToUUID():
    os.system('cls')
    # How to get a users UUID from there Minecraft username
    username = input("Enter the users username: ")
    r = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{username}')
    d = r.json()
    print("Username:", d["name"])
    print("UUID:", d["id"])
    # End of example (Everything else is just extra)
    print("")
    os.system('pause')
    main()
    
def UUIDToUsername():
    os.system('cls')
    # How to get a users username from there Minecraft UUID
    uuid = input("Enter the users UUID: ")
    r = requests.get(f'https://sessionserver.mojang.com/session/minecraft/profile/{uuid}')
    d = r.json()
    print("UUID:", d["id"])
    print("Username:", d["name"])
    # End of example (Everything else is just extra)
    print("")
    os.system('pause')
    main()
    
def nameHist():
    os.system('cls')
    # How to get a users mame history from there Minecraft UUID
    uuid = input("Enter the users UUID: ")
    r = requests.get(f'https://api.mojang.com/user/profiles/{uuid}/names')
    d = r.json()
    print("Usernames:")
    for item in d:
        print(item["name"])
    # End of example (Everything else is just extra)
    os.system('pause')
    main()
    
    
    
if __name__ == "__main__":
    main()