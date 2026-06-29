#!/usr/bin/python3


attempt = 0

print("you have three attempts for this code")


while attempt < 3:
 
    attempt += 1

    secret_code = (input("enter the secret_code:"))

    if secret_code == "`42`":

        print("unlocked")

        break   

    else:
        print("wrong code. abeg repeat:")
else:
    print("you have exceeded the number of attempts")
