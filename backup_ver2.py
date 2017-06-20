#Filename:backup_ver2.py

import os
import time

#1.The files and directories to be backed up are specified in a list
source=[r'D:\MJL\Python\backup_test\test',r'D:\MJL\Python\backup_test\test1']

#2.The backup must be stored in a main backup directory
target_dir='D:\\MJL\\Python\\backup_test\\'

#3.The files are backed up into a zip file.
#4.The name of the zip file is the current date and time.
today=target_dir+time.strftime('%Y%m%d')

#The current time is the name of the zip archive
now=time.strftime('%H%M%S')

if not os.path.exists(today):
	os.mkdir(today)
	print 'Successful created directory',today

#The name of the zip file
target=today+os.sep+now+'.zip'

#5.We use the zip command to put the files in a zip archive
zip_command='7z a %s %s' %(target,' '.join(source))

print target
print zip_command
print today

if os.system(zip_command)==0:
	print 'Successful backup to',target
else :
	print 'Backuo FAILED'