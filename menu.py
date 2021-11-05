"""
Main menu driver for Python Tools

To run either run from either:
- A Python shell like IDLE
- The command line: python menu.py
- The batch file: menu.bat
"""
import sys
import argparse
import random
import urllib.request as req

def fetch_url(url, fname):
    fin = req.urlopen(url)
    data = fin.read()
    fout = open(fname, mode='wb')
    fout.write(data)
    fout.close()

def from_file(fname, size):
    fin = open(fname, encoding='utf8')
    txt = fin.read()
    return Markov(txt, size)

def opt_url_to_file():
    url = input('URL: ')
    file = input('File: ')
    fetch_url(url, file)

def menu():

    options = {
        '1': 'Fetch URL to File',
        '99': 'Exit'
    }
    
    print("Welcome to Menu!")
    print("Hit ctl-c to exit")
    while True:
        for opt in sorted(options) :
            print(f'{opt}) {options[opt]}')

        try:
            selection=input('> ')
        except KeyboardInterrupt:
            print('Goodbye!')
            break
        
        if selection == '1':
            opt_url_to_file()
        elif selection == '99':
            break
        else:
            print('Unknown option selected!')

def main(opts):
    # python my.py -f pp.txt -s 4
    ap = argparse.ArgumentParser()
    #ap.add_argument('-f', '--file', help='file to load')
    #ap.add_argument('-s', '--size', help='Markov size (default 1)', default=1, type=int)
    args = ap.parse_args(opts)
    menu()
        
if __name__ == '__main__':
    main(sys.argv[1:])
else:
    print('loading as library')
    
