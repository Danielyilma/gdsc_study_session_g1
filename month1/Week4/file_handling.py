import os
from datetime import datetime

def listing_file():
    print(os.listdir())


def file_identification():
    recent_modify = []
    for file in os.listdir():
        if os.path.isfile(file):
            date = os.stat(file).st_ctime
            print(datetime.fromtimestamp(date))

file_identification()