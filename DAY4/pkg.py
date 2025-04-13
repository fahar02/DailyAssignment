'''
from pkg.poly import Poly 
a = Poly(1,2,3)  #an, ...., a0 
b = Poly(1,0,1,1,2,3)
c = a+b 
print(c) #Poly ( 1,0,1, 2,4,6)
'''
import os.path
import glob
import sys
import time
from datetime import datetime, date
class Poly:
    def __init__(self,*ls):
        self.l=list(ls)
        
    def __str__(self):
        return str(self.l)
        
    def __add__(self,temp):
        max_len=max(len(self.l),len(temp.l))
        self.l=self.l[::-1]+[0]*(max_len-len(self.l))
        temp.l=temp.l[::-1]+[0]*(max_len-len(temp.l))
        result=[]
        for i in range(len(self.l)):
            result.append(self.l[i]+temp.l[i])
            demo=result[::-1]
        return demo 
        
class File:
    def __init__(self,path):
        self.path=path
     
    def getMaxSizeFile(self,count):
        def getFile(path,result={}):
            files=glob.glob(os.path.join(path,'*'))
            for f in files:
                if os.path.isfile(f):
                    result[f] = os.path.getsize(f)
                elif os.path.isdir(f):
                    getFile(f,result)
            return result
        allfiles=getFile(self.path)
        result = sorted(allfiles, key=lambda k: allfiles[k],reverse=True)
        #return max length file name and check if path is empty return ''
        return result[:count:] if result else '' 
        
    def getLatestFiles(self,filterdate):
        def getFile(path,latest_date={}):
            files=glob.glob(os.path.join(path,'*'))
            for f in files:
                if os.path.isfile(f):
                    file_created_time=os.path.getctime(f)
                    file_create_date=datetime.fromtimestamp(file_created_time).date()
                    if file_create_date>=filterdate:
                        latest_date[f]=file_create_date
                elif os.path.isdir(f):
                    getFile(f,latest_date)
            return latest_date
        latest_date=getFile(self.path)
        result = sorted(latest_date.items(), key=lambda k: k[1],reverse=True)
        return result if result else ''
        
        