#!/usr/bin/env python3
'''this module works only on the current working directory'''
import os
from datetime import datetime, timedelta
import shutil

print(f'current working directory :- {os.getcwd()}')

def files_in_cwd(cwd):
    '''gets the files in the current working directory'''
    files = [file for file in os.listdir() if os.path.isfile(file) and file != 'file_handling.py']
    return files

def identification(files):
    '''identifies the files that are created in 24 hrs time'''
    list_of_files = []
    for file in files:
        created = datetime.fromtimestamp(os.stat(file).st_ctime)
        modified = datetime.fromtimestamp(os.stat(file).st_mtime)
        current_date = datetime.now()

        created_duration = current_date - created
        modified_duration = current_date - modified

        if created_duration.days < 1 and modified_duration.days < 1:
            update_files(file)
            list_of_files.append(file)
    
    return list_of_files


def update_files(file):
    '''appends timestamps to a file'''
    current_date = datetime.timestamp(datetime.now())

    with open(file, '+a') as f:
        f.write('\n' + str(current_date) + '\n')

def move_files(list_of_files):
    '''moves list of files to a folder called last_24hours'''
    des_path = "last_24hours"

    if not os.path.exists(des_path):
        os.mkdir(des_path)
    
    for file in list_of_files:
        shutil.move(file, des_path)

def main():
    '''where the excution begins'''
    files = files_in_cwd(os.getcwd())
    identified_files = []

    if files != []:
        identified_files = identification(files)
    
    if identified_files != []:
        move_files(identified_files)
    else:
        print('There is no files created and modified in 24 hours')


if __name__ == '__main__':
    main()
