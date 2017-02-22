#!#!/usr/bin/python

import requests,time
from bs4 import BeautifulSoup



def main():
    try:
        response=requests.get("https://pirateproxy.vip/top/all",timeout=6)
    except requests.exceptions.ReadTimeout as e:
        print("请重试或使用VPN网络.",e)
    except Exception as e:
        print("网络故障:",e)
    else:
        if response.status_code==200:
            soup=BeautifulSoup(response.text,"lxml")

            title=soup.find_all("div",{"class":"detName"})

            href=soup.find_all("a",{"title":"Download this torrent using magnet"})

            with open(time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())+".txt","w") as f:
                for i in range(100):
                    f.write(title[i].text)
                    f.write("\t")
                    f.write(href[i]["href"])
                    f.write("\n")



main()