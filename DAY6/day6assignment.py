'''
   Question-9:
Given a URL, download that and parse 
and download all links inside that page 
    in asyncio 
    BeautifulSoup for parsing html, requests for downloading 

'''
import asyncio
import aiohttp
import time
from bs4 import BeautifulSoup
import os
import re

path=r"C:\Users\Fahar Jamadar\handson\thread\downloads"


async def download(session,url):
    try:
        async with session.get(url) as response:
            if response.status==200:
                print(response.status)
                text=await response.text()
                soup=BeautifulSoup(text,"html.parser")
                createfile=url.replace('https://',"").replace('/','_')[:50]+'.html'
                createfile=re.sub(r'[<>:"/\\|?*]','_',createfile)
                filepath=os.path.join(path,createfile)
                with open(filepath,'w',encoding='utf-8') as f:
                    f.write(soup.prettify())
                    print(f"download {link} and {path}")
            else:
                print(f"failed to download") 
    except Exception as e:
        print(f"error {e} {url}")
   
    
async def main(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                html=await response.text()
                soup=BeautifulSoup(html,'html.parser')
                l=list({a.attrs['href'] for a in soup.select('a') if a.attrs['href'].startswith('https')})
                await asyncio.gather(*(download(session,i) for i in l))
        except Exception as e:
            print(f"fail {e}")
    
    
if __name__=="__main__":
    url=r"https://docs.python.org/3/index.html"
    asyncio.run(main(url))
    
    