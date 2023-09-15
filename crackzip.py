import os
import platform
import time
from sys import argv
from tqdm import tqdm
import zipfile


def bruteforce(path_zip,path_wordlist):
    # Given a wordlist tries to extract a zip archive with password wordlist key
    with open(path_wordlist, "rb") as fh:
        passwords = fh.readlines()
        zip_file = zipfile.ZipFile(path_zip)
        for password in tqdm(passwords):
            try:
                zip_file.extractall(path=".", pwd=password.strip())
                print("\n{***********************SUCCESS***********************}")
                print(f"[ ✔ ] ZIP FILE Password Found: {password.decode().strip()}")
                break
            except:
                continue

if __name__ == "__main__":
    # Check if paths were inputted by the user otherwise quit
    try:
        path_zip = argv[1]
        path_wordlist = argv[2]
    except:
        print("python3 zcrack.py [path_to_zip] [path_to_wordlist]")
        exit()
    bruteforce(path_zip,path_wordlist)
