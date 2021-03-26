import os
import time

'''
This scrpits autometically detacts file type in download folder and move it into appropriate folder. This runs i
in background and checks the download folder every thirty miniutes.

'''

photos = ['.png', '.jpg', '.jpeg', '.svg']
pdf = ['.pdf', 'docs']
archieve = ['.tar', '.xz','.deb']

path = '/home/shyam/Downloads'

os.chdir(path)


while True:
    items = items = os.listdir()
    for item in items:
        f_name , f_ext = os.path.splitext(item)
        if f_ext in photos:
            os.renames(item, 'Phtotos/'+item)
        elif f_ext in pdf:
            os.renames(item, 'Documents/'+item)
    
    time.sleep(1800)