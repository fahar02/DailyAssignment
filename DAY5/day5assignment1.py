'''
Question-8:
Given a URL, download that and parse 
and download all links inside that page 
    Use ThreadPoolExecutor or ProcessPoolExecutor 
    BeautifulSoup for parsing html, requests for downloading
    '''
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import os
def download_links(link,path):
    try:
        response=requests.get(link)
        if response.ok:
            soup=BeautifulSoup(response.text,'html.parser')
            createfile=link.replace('https://',"").replace("/","_")[:50]+".html"
            filepath=os.path.join(path,createfile)
            with open(filepath,'w',encoding='utf-8') as f:
                f.write(soup.prettify())
                print(f"download {link} and {path}")
        else:
            print("download fail")
    except Exception as e:
        print(f" Error downloading {link}: {e}")    

def parse_html(link,path,worker):
    try:
        print("parsing link")
        response=requests.get(link,timeout=10)
        if response.ok:
            soup=BeautifulSoup(response.text,'html.parser')
            links=list({a.attrs['href'] for a in soup.select('a') if a.attrs['href'].startswith('https')})
            print('link dowwloading')
            result=[]
            for i in links:
                result.append(worker.submit(download_links,i,path))
        
            for j in result:
                j.result()
        else:
            print(f"parse fail {link}")
    except Exception as e:
        print(f" Error parsing {link}: {e}") 
        
        

if __name__=='__main__':
    #the html file link to download the all links inside it 
    link=r"https://docs.python.org/3/index.html"
    #path to store the links inside the page
    path=r'C:\Users\Fahar Jamadar\handson\thread\downloads'
    with ThreadPoolExecutor(max_workers=8) as worker:
        file=worker.submit(parse_html,link,path,worker)
        file.result()