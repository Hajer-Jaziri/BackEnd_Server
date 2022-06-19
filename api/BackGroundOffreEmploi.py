# This part for library
from bs4 import BeautifulSoup
import requests
import re
import csv
from itertools import zip_longest
from selenium import webdriver
import urllib.request
import base64
import itertools 

# from DBConnection import *

tagNumberPagination = []
urlPages = ["https://www.offre-emploi.tn/"]
jobTitleList = []
locationList = []
previewList = []
dateEmploi = []
previewListNew = []
previewListNew2 = []
dateEmploiNew= []
locationListNew = []
job = []
local = []

#Function to convert an image from url web site to an image base64 after that we will stock it in the database
def get_as_base64(url):
    return base64.b64encode(requests.get(url).content)

def getNumberOfPage(url):
    maxInt = []
    # To make a request to a web page with specific URl  
    result = requests.get(url)

    #Parse the result using the HTML mode
    doc = BeautifulSoup(result.text, "html.parser")

    tags = doc.find_all('div',{"class":"paging light-theme simple-pagination"})
    
    for tNP in tags:
        for tNPTags in tNP.find_all('a'):
            maxInt.append(int(tNPTags['href'][33:len(tNPTags['href'])-1]))
            # tagNumberPagination.append(tNPTags['href'][29:])
    
    max_number = max(maxInt)
    
    for urlP in range(2, max_number+1):
        urlPages.append("https://www.offre-emploi.tn/page/"+str(urlP))

    return urlPages

resultFunction1 = getNumberOfPage("https://www.offre-emploi.tn")

def getInformationFromWebSite():
    # resF1 = resultFunction1[0]
    for resF1 in resultFunction1:
        # To make a request to a web page with specific URl  
        result = requests.get(resF1)

        #Parse the result using the HTML mode
        doc = BeautifulSoup(result.text, "html.parser")

        tags = doc.find_all('article',{"class":"js_result_row"})
                        
        for tag in tags:
            for tInFW in tag.find_all('div',{"class":"jobTitle"}):
                for jobTitle in tInFW.find_all('a'):
                    jobTitleList.append(jobTitle.text)

            for tInFW in tag.find_all('div',{"class":"location"}):
                for tNI in tInFW.find_all('a'):
                    locationList.append(tNI.text)

            for tNPr in tag.find_all('div',{"class":"preview"}):
                previewList.append(tNPr.text)

            for tNDate in tag.find_all('div',{"class":"extras"}):
                for dateInformation in tNDate.find_all('div',{"class":"postedDate"}):
                    for timeInformation in dateInformation.find_all('time'):
                        dateEmploi.append(timeInformation.text)

    for x0 in dateEmploi:
        dateEmploiNew.append(x0.replace("            ",""))

    for x1 in previewList:
        previewListNew.append(x1.replace("\n        ",""))
    for x2 in previewListNew:
        previewListNew2.append(x2.replace("    ",""))
    
    for x in locationList:
        locationListNew.append(x.replace("\n",""))


    for y1 in range(0,len(locationListNew),2):
        job.append(locationListNew[y1])

    for y2 in range(1, len(locationListNew),2):
        local.append(locationListNew[y2])
getInformationFromWebSite()


print(len(jobTitleList))
print(len(job))
print(len(local))
print(len(previewListNew2))
print(len(dateEmploiNew))