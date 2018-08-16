#!/usr/bin/env python
# -*- coding=utf-8 -*-
import zipfile
import os
import optparse
from threading import Thread
def extractFile(zipFile, password):
    try :
        zipFile.extractall(pwd=password)
        print '[+] Found password ' + password + '\n'
    except Exception, e:
        pass

def main():
    # zFile = zipfile.ZipFile("evil.zip")
    # passFile = open('dictionary.txt')
    print 'zipCrack'
    parser = optparse.OptionParser("usage %prog " +"-f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string', help= 'name of the zip file' )
    parser.add_option('-d', dest='dname', type='string', help= 'name of the dict file' )
    (options, args) = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        print parser.usage
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)    
    for line in passFile.readlines():
        password = line.strip('\n')
        # guess = extractFile(zFile, password)
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()
        # if guess:
        #     print '[+] Password = ' + password + '\n'
        #     exit(0)
    # print 'password not found'
    # os.rmdir('evil')

if __name__ == '__main__':
    main()