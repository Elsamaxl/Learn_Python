#Filename:backup_ver1.py

import os
import time

#1.The files and directories to be backed up are specified in a list
source=[r'D:\test',r'D:\test1']

#2.The backup must be stored in a main backup directory
target_dir="D:\\"

#3.The files are backed up into a zip file.
#4.The name of the zip file is the current date and time.
target=target_dir+time.strftime('%Y%m%d%H%M%S')+'.zip'

#5.We use the zip command to put the files in a zip file.
zip_command=r'7z a %s %s' %(target,' '.join(source))

print target
print zip_command

#Run the backup
if os.system(zip_command)==0:
	print 'Successful backup to ',target
else :
	print 'Backup FAILED'
	