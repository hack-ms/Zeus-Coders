# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import wget
from pathlib import Path
import os
import sys
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

def GetAllFilesOnWebsite(myPath):
    try:
        # Create target Directory
        os.mkdir(myPath)
        print("Directory " , myPath ,  " Created ") 
    except FileExistsError:
        print("Directory " , myPath ,  " already exists")

    session = requests.Session()

    retries = Retry(connect=3, backoff_factor=0.5)
    session.mount('http://', HTTPAdapter(max_retries=retries))

    url = "http://www.dados.ms.gov.br/dataset?groups=educacao"
    r  =  session.get(url=url)
    data = r.text
    soupPrincipal = BeautifulSoup(data, 'html.parser')

    sys.stdout.write("\nURL principal: " + url)
    sys.stdout.write("\n-----Começando download dos arquivo------")
    sys.stdout.write("\nTotal de links: " + str(len(soupPrincipal.find_all("a", attrs={"data-format" : "txt"}))))
    sys.stdout.flush()

    for crawler in soupPrincipal.find_all("a", attrs={"data-format" : "txt"}):
        if crawler.get("data-format").find("txt") != -1:
            url = "http://www.dados.ms.gov.br" + crawler.get("href")
            r  = session.get(url=url)
            data = r.text
            soupDownload = BeautifulSoup(data, 'html.parser')

            for link in soupDownload.find_all("a"):
                if link.get("href") != None:
                    if link.get("href").find("txt") != -1:
                        download = link.get("href").replace("./", "")
                        splitString = download.split('/')
                        aux = splitString[-1]
                        existFile = myPath + aux
                        importedFile = myPath + "IMPORTADO - " + aux
                        hasFile = os.path.isfile(existFile)
                        hasImported = os.path.isfile(importedFile)
                        if hasFile == False and hasImported == False:
                            wget.download(link.get("href").replace("./", ""), myPath)
    
    session.close()
