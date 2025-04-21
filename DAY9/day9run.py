import os
import requests
if __name__=="__main__":
    #get all data from database url
    """
    url="http://127.0.0.1:8000/helloj/all"
    resp=requests.get(url)
    print(resp.json())
    """
    #insert data in database url
    """
    url="http://127.0.0.1:8000/helloj/create"
    obj=dict(name='sam',age=30)
    resp=requests.post(url,json=obj)
    print(resp.json())
    """
    #update url
    """
    url="http://127.0.0.1:8000/helloj/update"
    obj=dict(name='sam',age=1000)
    resp=requests.put(url,json=obj)
    print(resp.json())
    """
    #delete data from url
    
    url="http://127.0.0.1:8000/helloj/delete/sam"
    resp=requests.delete(url)
    print(resp.json())
    
    