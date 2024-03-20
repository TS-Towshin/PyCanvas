import datetime
import os

def isPath(file_path):
    dirs = os.listdir()
    for dir in dirs:
        if dir == file_path:
            return True
    return False

def fileName(file_path, file_type) -> str:
    if not isPath(file_path):
        os.mkdir(file_path)
    
    file_name = str(datetime.datetime.now())
    file_name = file_name.replace(' ', '-')
    file_name = file_name.replace(':', '')
    file_name = file_name.replace('.', '')
    file_name = f"{file_path}\\{file_name}.{file_type}"

    return file_name
