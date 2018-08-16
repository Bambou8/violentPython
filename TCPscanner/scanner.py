#!/usr/bin/env python
# -*- coding=utf-8 -*-
import optparse
from socket import *

parser = optparse.OptionParser('usage %prog –H <target host> -p <target port>')
parser.add_option('-H', dest='targetHost', type='string', help='specify target host')
parser.add_option('-p', dest='targetPort', type='int', help='specify target port')
(options, args) = parser.parse_args()

if (options.targetHost == None) | (options.targetPort == None):
	print parser.usage
	exit(0)
else:
	tgtHost = options.targetHost
	tgtPort = options.targetPort


def connScan(tgtHost, tgtPort):
	print tgtHost+':'+tgtPort+'\n'
	try:
		connSock = socket(AF_INET, SOCK_STREAM)
		connSock.connect((tgtHost, tgtPort))
		print '[+]%d/tcp open'% tgtPort
		connSock.close()
	except Exception as e:
		print '[-]%d/tcp closed'% tgtPort

def portScan(tgtHost, tgtPorts):
	print '<>portScan'
	try:
		tgtIP = gethostbyname(tgtHost)
		print "[+]host resolved"
	except:
		print "[-] Cannot resolve '%s': Unknown host"%tgtHost
		return
	try:
		tgtName = gethostbyaddr(tgtIP)
		print '\n[+] Scan Results for: ' + tgtName[0]
	except:
		print '\n[+] Scan Results for: ' + tgtIP
		setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		print 'Scanning port ' + tgtPort
		connScan(tgtHost, int(tgtPort))
			