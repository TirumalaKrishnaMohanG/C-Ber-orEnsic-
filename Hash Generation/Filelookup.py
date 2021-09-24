#!/usr/bin/env python

# Headers 
import os
import sys
import glob
import os.path
import hashlib
import pandas as pd

#from os import *
from tabulate import tabulate
from datetime import datetime
from datetime import timezone
from datetime import timedelta

# Current Time
curr_DT = datetime.now().strftime("%Y-%m-%d %H:%M")

# Lists
filelist,fetchfiles,listhash = [],[],[]

# Function to fetch info
def getFile():
	print("Results".center(os.get_terminal_size().columns))
	print("-------".center(os.get_terminal_size().columns))
	# Getting OS Details
	get_OSDET = os.uname()
	Sysname = "sysname : "+(get_OSDET[0])
	OS = "os : "+(get_OSDET[1])
	Release = "release : "+(get_OSDET[2])
	Version = "version : "+(get_OSDET[3])
	Machine = "machine : "+(get_OSDET[4])
	# Fetching Current Path
	get_CWD = os.getcwd()
	print('System Details'.center(os.get_terminal_size().columns))
	print('--------------'.center(os.get_terminal_size().columns))
	print(Sysname.center(os.get_terminal_size().columns))
	print(OS.center(os.get_terminal_size().columns))
	print(Release.center(os.get_terminal_size().columns))
	print(Version.center(os.get_terminal_size().columns))
	print(Machine.center(os.get_terminal_size().columns))

	print('Current Path'.center(os.get_terminal_size().columns))
	print('------------'.center(os.get_terminal_size().columns))
	print(get_CWD.center(os.get_terminal_size().columns))
	print('  '.center(os.get_terminal_size().columns))
	return get_CWD

# Function to List files
def getDIR():
	get_LT = getFile()
	for root, dirs, files in os.walk(get_LT):
		for file in files:
			filelist.append(os.path.join(root,file))

	return filelist

# Generate a file based hash
def getHASH():
	print('\n')
	get_HASH_LT = getDIR()
	for rFile in get_HASH_LT:
		hash_MD5 = (hashlib.md5(open(rFile,'rb').read()).hexdigest())
		hash_SHA1 = (hashlib.sha1(open(rFile,'rb').read()).hexdigest())
		hash_SHA224 = (hashlib.sha224(open(rFile,'rb').read()).hexdigest())
		hash_SHA256 = (hashlib.sha256(open(rFile,'rb').read()).hexdigest())
		hash_SHA384 = (hashlib.sha384(open(rFile,'rb').read()).hexdigest())
		hash_SHA512 = (hashlib.sha512(open(rFile,'rb').read()).hexdigest())
		listhash.append({'file':rFile,'md5':hash_MD5,'sha1':hash_SHA1,'sha224':hash_SHA224,'sha256':hash_SHA256,'sha384':hash_SHA384,'sha512':hash_SHA512})

	finRes_HASH = pd.DataFrame(listhash,columns=['file','md5','sha1','sha224','sha256','sha384','sha512'])
	finRes_HASH.to_csv('output.csv')
	return finRes_HASH[['file','md5','sha1']]

if __name__ == "__main__":
	print(tabulate(getHASH(),headers='keys',tablefmt='psql'))
	print("Ouput is generated in the following path:",os.getcwd()+"/output.csv")