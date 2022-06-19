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
urlPages = ["https://afariat.com/emploi-affaires-et-services"]
nameEmploi = []
imageEmploi = []
priceEmploi = []
dateEmploi = []
annoceEmploi = []
villeEmploi = []
#Function to convert an image from url web site to an image base64 after that we will stock it in the database
def get_as_base64(url):
    return base64.b64encode(requests.get(url).content)

def getNumberOfPage(url):
    # To make a request to a web page with specific URl  
    result = requests.get(url)

    #Parse the result using the HTML mode
    doc = BeautifulSoup(result.text, "html.parser")

    tags = doc.find_all('ul',{"class":"pagination"})
    
    for tNP in tags:
        for tNPTags in tNP.find_all('a'):
            # print(tNPTags['href'])
            tagNumberPagination.append(tNPTags['href'][29:])
    
    for urlP in range(2, int(tagNumberPagination[-1])+1):
        urlPages.append("https://afariat.com/emploi-affaires-et-services/"+str(urlP))

    return urlPages

resultFunction1 = getNumberOfPage("https://afariat.com/emploi-affaires-et-services")

# print(resultFunction1)
def getInformationFromWebSite():
    # resF1 = resultFunction1[0]
    for resF1 in resultFunction1:
        # To make a request to a web page with specific URl  
        result = requests.get(resF1)

        #Parse the result using the HTML mode
        doc = BeautifulSoup(result.text, "html.parser")

        tags = doc.find_all('div',{"class":"hidden-lg hidden-md"})
                    
        for tag in tags:
            for tInFW in tag.find_all('div',{"class":"col-xs-5 col-sm-4 padding-lr5 center-block"}):
                for image in tInFW.find_all('img',{"class":"img-responsive"}):
                    if ("data:image/" in image['src']):
                        print("Don't do anything")
                        imageEmploi.append(image['src'])
                    else:
                        print("It works")
                        # imageEmploi.append(get_as_base64(image['src']))  
                        imageEmploi.append(image['src']) 

            for tInFW in tag.find_all('div',{"class":"col-xs-7 col-sm-8 padding0"}):
                for tNI in tInFW.find_all('a',{"class":"link"}):
                    for name in tNI.find_all('strong',{"class":''}):
                        nameEmploi.append(name.text)

                for tNI in tInFW.find_all('span',{"class":"col-xs-4 padding-lr0"}):
                    for priceInformation in tNI.find_all('strong',{"class","price pull-right"}):
                        for price in priceInformation.find_all('span'):
                            priceEmploi.append(price.text)

                for tNI in tInFW.find_all('div',{"class":"col-xs-12 grayColor padding0"}):
                    for dateInformation in tNI.find_all('small',{"class","col-xs-12"}):
                        dateEmploi.append(dateInformation.text)

                for tNI in tInFW.find_all('div',{"class":"col-xs-12 padding0"}):
                    for placeInformation in tNI.find_all('span',{"class","col-xs-12"}):
                        for place in placeInformation.find_all('a',{"class","grayColor link"}):
                            if("/annonces-" in place['href']):
                                annoceEmploi.append(place['href'][10:])
                            if("/ville/" in place['href']):
                                villeEmploi.append(place['href'][7:])

getInformationFromWebSite()

print(len(nameEmploi))
print(len(imageEmploi))
print(len(priceEmploi))
print(len(dateEmploi))
print(len(annoceEmploi))
print(len(villeEmploi))
