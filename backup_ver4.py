#Filename:backup_ver4.py

import os
import time

#1.The files and directories to be backed up are specified in a list.
source=[r'D:\MJL\Python\backup_test\test',r'D:\MJL\Python\backup_test\test1']

#2.The back must be stored in a main backup directory.
target_dir='D:\\MJL\\Python\\backup_test\\'

#3.The files are backed into a zip file.
#4.The current day is the name of the subdirectory in the main dircetory.
today=target_dir+time.strftime('%Y%m%d')

#The current time is the name of the zip archive.
now=time.strftime('%H%M%S')

#Take a comment from the user to create the name of the zip archive.
comment=raw_input('Enter a comment-->')
if len(comment)==0:
	target=today+os.sep+now+'.zip'
else :
	target=today+os.sep+now+'_'+\
	comment.replace(' ','_')+'.zip'

#Create the subdirectory if it isn't already there
if not os.path.exists(today):
	os.mkdir(today)
	print 'Successful create the subdirectory',today

#5.We use the zip command to put the files in a zip archive.
zip_command='7z a %s %s' %(target,' '.join(source))

print target
print now
print zip_command

#Run the backup.
if os.system(zip_command)==0:
	print 'Successful backup to',target
else :
	print 'Backup FAILED'

