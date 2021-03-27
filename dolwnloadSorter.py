import os
import time

'''
This scrpits autometically detacts file type in download folder and move it into appropriate folder. This runs i
in background and checks the download folder every thirty miniutes.

'''



class sorter:

    def __init__(self, path):

        photos = ['.png', '.jpg', '.jpeg', '.svg']
        pdf = ['.pdf', 'docs']
        archieve = ['.tar', '.xz','.deb']

        self.path = path
        os.chdir(path)

        items = os.listdir()
        print(items)
        for item in items:
            f_name , f_ext = os.path.splitext(item)
            if f_ext in photos:
                os.renames(item, 'Sort_Photos/'+item)
            elif f_ext in pdf:
                os.renames(item, 'Sort_Docs/'+item)

if __name__ == '__main__':
    sorter('/run/user/1000/gvfs/google-drive:host=gmail.com,user=shyam10kwd')
