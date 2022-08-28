"""
Akant's Password Generator
"""
import string
import time
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    allchar = []  # all the characters in it for generating a password
    allchar.extend(list(s1))
    allchar.extend(list(s2))
    allchar.extend(list(s3))
    allchar.extend(list(s4))
    bold = '\033[1m'  # for printing bold fonts
    while True:
        print("\t<Password Generator>")
        pass_len = int(input("Enter length for password : "))
        if pass_len >= 8:
            random.shuffle(allchar)
            password = "".join(allchar[0:pass_len])
            print("WAIT MACHINE IS GENERATING...")
            time.sleep(5)
            print("YOUR PASSWORD IS : ", bold, password)
        else:
            print("\tLength !< 8")
        x = input("TRY Again Press Y\t").lower()
        if x != "y":
            print("Program Exited")
            break
