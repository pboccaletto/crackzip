# CrackZip 🔐

CrackZip is a simple python script that will bruteforce a password protected zip archive 🗜️ using a dictionary attack. 
The user will provide as input the zip file and the wordlist he wishes to use. 

This project was originally cloned from "git clone https://github.com/machine1337/zipcrack.git". 
Despite that this is not a fork, I've over simplified the code to be run directly from command line.
I ended up rewriting it by removing colors, decorations and interactive user input. Added a progressbar with tqdm.

# Installation:
    1. git clone https://github.com/pboccaletto/crackzip
    2. cd crackzip
    3. python3 -m pip install -r requirements.txt
    
# Requirements:
    1. tqdm
    
# Usage:
    python3 crackzip.py [path_to_zip] [path_to_wordlist]

# Features:
     1) Dictionary Attack
