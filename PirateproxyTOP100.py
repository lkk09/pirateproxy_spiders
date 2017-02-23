#!#!/usr/bin/python

import requests,time,xlwt
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

            workbook = xlwt.Workbook()
            sheet = workbook.add_sheet("TOP 100")

            sheet.write(0, 0, 'title')
            sheet.write(0, 1, 'url')

            for i in range(len(title)):
                sheet.write(i+1, 0,title[i].text)
                sheet.write(i+1, 1, href[i]["href"])

            workbook.save(time.strftime("%Y-%m-%d", time.localtime())+"_Pirateproxy_TOP100.xls")


if __name__ == "__main__":
    main()