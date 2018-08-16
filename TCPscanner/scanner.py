#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import optparse
parser = optparse.OptionParser('usage %prog –H <target host> -p <target port>')
parser.add_option('-H', dest='targetHost', type='string', help='specify target host')
parser.add_option('-p', dest='targetPort', type='int', help='specify target port')
(option, args) = parser.parse_args()
if (options.targetHost == None) | (options.targetPort == None):
	print parser.usage
	exit(0)
else:
	tgtHost = options.targetHost
	tgtPort = options.targetPort