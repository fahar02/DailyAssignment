'''
Question-4:
Recursively go below a dir and based on filter, dump those files in to  single file 
(work with only text file)
'''
#importing modulus to perform operation on dir and files
import glob
import os

#(outer)function defination to call Recursively to get iterate through the dir
def read_append_opeartion(read_path,append_path):
    #(inner/nested)function to check the files path
    def files(path):
        file=glob.glob(os.path.join(path,"*"))
        for f in file:
            if os.path.isfile(f):
                #condition to check if the current file is .txt
                if f.endswith('.txt'):
                    #opening the file to read the data and if it contain the specail character ignore them
                    with open(f,'r',encoding="utf-8", errors="ignore") as r:
                        content=r.read()
                        #opening the file to append the data into that file open after other
                        with open(append_path,'a',encoding="utf-8", errors="ignore") as w:
                            w.write(content+'\n')
                            print(f"Appended content from {f} to new.txt")
            elif os.path.isdir(f):
                files(f)
    return files(read_path)

if __name__ == '__main__':
    #path of the file which is present in my machine
    #from which the .txt file is to de read
    read_path = r"C:\Users\Fahar Jamadar\handson"
    
    #path of the file which is present in my machine
    #to which the read data is to be append
    append_path=r"C:\Users\Fahar Jamadar\assignment\DAY2\new.txt"
    
    read_append_opeartion(read_path,append_path)