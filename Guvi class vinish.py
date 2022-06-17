'''
#assignment1(register and login)


with open('trial.txt', 'r') as f:
    content = f.read()

a = int(input("To login press 0 \nTo Register press 1 \n"))

if a == 0:
    name2 = input("enter the name: ")
    if name2 in content:
        password2 = input("Enter the password: ")
        if password2 in content:
            print("You are loggedin")
        else:
            print("wrong password")
    else:
        print("not registered. Go for registration")

if a == 1:
    name = input("Enter the name: ")
    list = ["yahoo.com", "gmail.com"]
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    if name[0] in alpha:
        if '@' in name:
            a = name.find("@")
            #print(a)
            if name[a + 1:] in list:
                print("user id valid")
                if name in content:
                    print("username exists. Choose a unique one.")
                else:
                    password = input("Enter the password: ")
                    import re

                    pattern = "^.*(?=.{5,16})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@?#$%^&+=]).*$"
                    password = input("Enter Password:")
                    result = re.findall(pattern, password)
                    if (result):
                        print("Password is valid")
                    else:
                        print("Password is not valid")
                    with open('trial.txt', 'a') as g:
                        g.write("\n")
                        g.write("username: ")
                        g.write(name)
                        g.write("\n")
                        g.write("password: ")
                        g.write(password)
                        print("you are registered")
            else:
                print("user id not valid")
        else:
            print("user id not valid")
    else:
        print("user id not valid")
'''





























