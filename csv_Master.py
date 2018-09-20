#!/usr/bin/python
#Env Setup
#csv_Master by ninex
#
#Using pandas, takes some csv files and parses only the columns you want and puts those in a new file.
#Then takes those new files and merges them on the col# you specifyself.
#Replace "Col#s" with the value of the Column Names in your .csv that you want to see.

import pandas as pd

firstFilefields = ['Col1', 'Col2', 'Col3', 'Col4', 'Col5']

firstFile = pd.read_csv('firstFileName.csv', usecols=firstFilefields)
#Remove the #comment on next line to: See the keys
#print firstFile.keys()
#Remove the #comment on next line to: See content in 'firstFile'
#print firstFile

firstFile.to_csv('firstFileName_Parsed.csv')

# Read Next File
secondFilefields = ['Col1', 'Col2', 'Col3', 'Col4', 'Col5']

secondFile = pd.read_csv('secondFileName.csv', usecols=secondFilefields)
#Remove the #comment on next line to: See the keys
#print secondFile.keys()
#Remove the #comment on next line to: See content in 'secondFile'
#print secondFile

secondFile.to_csv('secondFileName_Parsed.csv')

#Merge two previously parsed files using a specific Col# (Column Name) as key.

a = pd.read_csv("firstFileName_Parsed.csv")

b = pd.read_csv("aw_profilesCheckParsed.csv")

merge = a.merge(b, how='left', on='Col#')

merge.to_csv("finalFileName.csv", index = False)
