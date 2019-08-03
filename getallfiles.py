# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import wget
from pathlib import Path
import os
import sys

def GetAll(myPath):
    try:
        # Create target Directory
        os.mkdir(myPath)
        print("Directory " , myPath ,  " Created ") 
    except FileExistsError:
        print("Directory " , myPath ,  " already exists")

    url = "http://www.dados.ms.gov.br/dataset"
    r  = requests.get(url)
    data = r.text
    soupPrincipal = BeautifulSoup(data, 'html.parser')

    sys.stdout.write("\nURL principal: " + url)
    sys.stdout.write("\n-----Começando download dos arquivo------")
    sys.stdout.write("\nTotal de links: " + str(len(soupPrincipal.find_all("a", attrs={"data-format" : "txt"}))))
    sys.stdout.flush()

    for crawler in soupPrincipal.find_all("a", attrs={"data-format" : "txt"}):
        if crawler.get("data-format").find("txt") != -1:
            url = "http://www.dados.ms.gov.br" + crawler.get("href")
            r  = requests.get(url)
            data = r.text
            soupDownload = BeautifulSoup(data, 'html.parser')

            for link in soupDownload.find_all("a"):
                if link.get("href") != None:
                    if link.get("href").find("txt") != -1:
                        wget.download(link.get("href").replace("./", ""), myPath)
