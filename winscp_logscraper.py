import sys
import csv
import string
from datetime import date
from time import strptime
import datetime
import re
import argparse


dateuploaded=""
logfilename=""
extension=""
parser=argparse.ArgumentParser(description="winscp_logscraper gets a list of transmitted files of an extension by date")
parser.add_argument('-d',action="store",dest="dateuploaded")
parser.add_argument('-f',action="store",dest="logfilename")
parser.add_argument('-e',action="store",dest="extension")
results=parser.parse_args()

dateuploaded=results.dateuploaded
logfilename=results.logfilename
extension=results.extension

files=set()

rr=csv.reader(open(logfilename,'rb'),delimiter=' ',quotechar='\'')

for r in rr:
	if r[1]==dateuploaded:
		for a in r:
			if extension in a:
				a=a.replace("c:\\xifin_patientscan_docs\\",'')
				a=a.replace("c:\\xifin_patient_reports\\",'')
				a=a.replace('"','')
				files.add(a)

for f in files:
	print f