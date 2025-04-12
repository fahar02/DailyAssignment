'''
Question-3:
Given a directory, find out the file Name 
having max size recursively
'''
#importing modulus to perform operation on dir and files
import glob 
import os.path 
import sys
#Given a directory path, find out the file Name having max size recursively 
def max_len(path):
    # nested function contain path of dir and default dictionry
    def get_files(path, ed={}):
        files = glob.glob(os.path.join(path, "*"))
        for f in files:
            if os.path.isfile(f):
                ed[f] = os.path.getsize(f)
            elif os.path.isdir(f):
                get_files(f, ed)
        return ed     
    allfiles = get_files(path)
    #sorting to get the max file size
    std = sorted(allfiles, key=lambda k: allfiles[k])
    #return max length file name and check if path is empty return ''
    return std[-1] if std else ''
    
if __name__ == '__main__':
    #path of the file which is present in my machine
    path = r"C:\Users\Fahar Jamadar\assignment\DAY2"
    print(max_len(path))
    
#output:C:\Users\Fahar Jamadar\assignment\DAY2\new.txt