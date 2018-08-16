#!/usr/bin/env python
# -*- coding: utf-8 -*-
#crack the /etc/shadow file
import crypt
def testPass(cryptPass,salt):
    fo = open('dictionary.txt','r')
    for word in fo.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word,salt)
        if (cryptWord == cryptPass):
            print "[+] Found Password: "+word+"\n"
            return
    print "[-] Password Not Found.\n"
    return
def main():
    passFile = open('passwords.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            if "$" in line:
                salt = '$'+line.split('$')[1].strip(' ')+'$'+line.split('$')[2].strip(' ')
                print "[∗] Cracking Password For: "+user
                testPass(cryptPass,salt)
if __name__ == "__main__":
    main()