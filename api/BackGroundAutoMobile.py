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
from automobilewebscrapper.models import Marque, VoitureNeuf, VendeurPro, VoitureOccasion, Concessionnaires

print("Hello !!")
# This part for declaration variable
tagsMarqueVoituresNeuf = []
tagAltNewCar = []
tagSrcNewCar = []
tagsVoiNeufLink=[]

#Variable for get information of new cars
tagsVoiNeufModelSpan=[]
tagsVoiNeufModelH2=[]
tagsVoiNeufModelImg = []
tagsVoiNeufModelPrice = []
tagsVoiNeufModelSpanFinalList = []
tagsVoiNeufModelH2FinalList = []

#Variables for the occasion cars
linkPages = []
linkPageWithoutFooter = []
allYearOfCarOcc = []
allRoadOfCarOcc = []
allEnergiesOfCarOcc = []
allVitesssOfCarOcc = []
nameCarOcc = []
localiteCarOcc = []
descrCarOcc = []
priceCarOcc = []
imgCarOcc = []

nameMarque = []
nameMarqueFinal = []
imgCarOccFinal = []
descrCarOccFinal = []

#Variables for Vendor pro
nameVendeurList = []
imagesVendeurList = []
addressVendeurList = []
phoneVendeurList = []
faxVendeurList = []
addressVendeurListNew = []
phoneVendeurListNew = []
faxVendeurListNew = []

# Store the given url in an attribute named URL
URL = "https://www.automobile.tn/fr"
#[:21] it mean give me from 0 position to 21 position
WebSite = URL[:25]
# To make a request to a web page with specific URl  
result = requests.get(URL)

#Parse the result using the HTML mode
doc = BeautifulSoup(result.text, "html.parser")

#To automate the work we will look for all the links to find the links to access the computers and the phones 
#We use the find_all to get a list of links and next we will make some filters to get the correct informations
#We notice in the inspection mode(On browser) what we are looking for have a common class dropdown-item
#So we will search in all the file with filtering by class
tags = doc.find_all('a',{"class":"dropdown-item"})


#The result of find_all given us all the tags of <a>.....</a>
#So for takes only the content of those tags we make this scripts
#1. Loop on the tags (The tags in the list)
for tag in tags:
    #2. We append only the content of those tags on a new list named tagsMarqueVoituresNeuf and etc...
    if(tag['href'] in "/fr/neuf"):
        tagsMarqueVoituresNeuf.append(tag['href'])

URLFORVoiNeuf = WebSite + tagsMarqueVoituresNeuf[0]
# To make a request to a web page for get all the new cars
resultVoiNeuf = requests.get(URLFORVoiNeuf)

#Parse the result using the HTML mode
docVoiNeuf = BeautifulSoup(resultVoiNeuf.text, "html.parser")

#To automate the work we will look for all the links to find the links to access the computers and the phones 
#We use the find_all to get a list of links and next we will make some filters to get the correct informations
#We notice in the inspection mode(On browser) what we are looking for have a common class dropdown-item
#So we will search in all the file with filtering by class
tagsVoiNeuf= docVoiNeuf.find_all('img',alt=True)

#The result of find_all given us all the tags of <img>.....</img>
#So for takes only the content of those tags we make this scripts
#1. Loop on the tags (The tags in the list)
for tag in tagsVoiNeuf:
    #2. We append only the content of those tags on a new list named tagAltNewCar and etc...
    tagAltNewCar.append(tag['alt'])
    tagSrcNewCar.append(tag['src'])

#If we have some empty element with this instruction you will get an list without any element
tagAltNewCar = list(filter((None), tagAltNewCar))
# print(tagAltNewCar)

tagSrcNewCar = list(filter((None), tagSrcNewCar))
#There is in the list first and the element an URL not have any meaning so we deleted
tagSrcNewCar = tagSrcNewCar[1:len(tagSrcNewCar)-1]
# print(tagSrcNewCar)

#Function to convert an image from url web site to an image base64 after that we will stock it in the database
def get_as_base64(url):
    return base64.b64encode(requests.get(url).content)

'''This par for a new cars'''
# To access on each marque automatically we do this instructions
# We find in the inspection part that each last year URL(https://www.automobile.tn/fr/neuf) concatenate with model of cars
# But in our list we have this model with espace so we replace the space between all the string with dash
# Next we just concatenate the URL + / + model name and we get it
for i in range(len(tagAltNewCar)):
    tagsVoiNeufLink.append(URLFORVoiNeuf + "/" +tagAltNewCar[i].replace(' ','-'))

# print(tagsVoiNeufLink)
####################### Get Information From the new cars #######################
####################### Marque Part #######################
#This function to get all the information from each marque is existing from the website
def getInformationForVoiNeuf(URLWebSite):
    resultVoiNeufModel = requests.get(URLWebSite)

    #Parse the result using the HTML mode
    docVoiNeufModel1 = BeautifulSoup(resultVoiNeufModel.text, "html.parser")

    tagsVoiNeufModel = docVoiNeufModel1.find_all('div',{"class":"versions-item"})

    for tVM in tagsVoiNeufModel:
        for span in tVM.find_all('span',{"class":"tag stock-limite"}):
            tagsVoiNeufModelSpan.append(span.find_all(text=True))
        
        for h2 in tVM.find_all('h2'):
            tagsVoiNeufModelH2.append(h2.find_all(text=True))

        for img in tVM.find_all('img', {"class":"img-fluid"}):
            tagsVoiNeufModelImg.append(img['src'])

        for spanPrix in tVM.find_all('div',{"class":"price"}):
            for spanPrixDetal in spanPrix.find_all('span'):
                if(spanPrixDetal.find_all(text=True)[0] !="DT"):
                    tagsVoiNeufModelPrice.append(spanPrixDetal.find_all(text=True)[0])

print('Hello2')

####################### Get Information From concessionaires #######################
####################### Concessionaires Part #######################

resultConcessionaires = requests.get(URLFORVoiNeuf+"/concessionnaires")

#Parse the result using the HTML mode
docConcessionaires = BeautifulSoup(resultConcessionaires.text, "html.parser")

tagsConcessionaires = docConcessionaires.find_all('div',{"class":"infos-wrapper"})

tagsConcessionairesH2 = []
tagsConcessionairesH2List = []
tagsConcessionairesBTel = []

for tC in tagsConcessionaires:
    for tCh2 in tC.find_all('h2',{"style":"font-weight: bold; font-size: 15px;"}):
        tagsConcessionairesH2.append(tCh2.find_all(text=True))

    
    for tCb2 in tC.find_all("b", text="Tél. : "):
        tagsConcessionairesBTel.append(tCb2.next_sibling.strip())

print('Hello3')

for tag in tags:
    if("recherche" in tag['href']):
        URLVoiOccRech = URL + tag['href'][3:]
# print(URLVoiOccRech)


resultConAncVoit = requests.get(URLVoiOccRech)

#Parse the result using the HTML mode
docConAncVoit = BeautifulSoup(resultConAncVoit.text, "html.parser")

tagsConAncVoit = docConAncVoit.find_all('a')

nameAllConAncVoit = []
linkAllConAncVoit = []
for tCAV in tagsConAncVoit:
    # print(tCAV['href'])
    if("/fr/occasion?" in tCAV['href']):
        nameAllConAncVoit.append(tCAV['href'][25:].replace('-',' '))
        linkAllConAncVoit.append(URL + tCAV['href'][3:])


def getAllPagesOfCarsOcc(linkPagesFinal):
    #You will define en function right here for the if statement and else to
    linkPagesFinal = list(set(linkPages))

    return (linkPagesFinal)

def getInformationFromCArsOcc(linkPagesFinal):

    for lPF in linkPagesFinal:
        resultVoiOccModel = requests.get(lPF)

        #Parse the result using the HTML mode
        docVoiOccModel1 = BeautifulSoup(resultVoiOccModel.text, "html.parser")


        for liYear in docVoiOccModel1.find_all('li',{"class":"year"}):
            for spanYear in liYear.find_all('span',{"class":"value"}):
                if("https://" not in spanYear.find_all(text=True)[0]):
                    allYearOfCarOcc.append(spanYear.find_all(text=True)[0])

        for liRoad in docVoiOccModel1.find_all('li',{"class":"road"}):
            for spanRoad in liRoad.find_all('span',{"class":"value"}):
                if("https://" not in spanRoad.find_all(text=True)[0]):
                    allRoadOfCarOcc.append(spanRoad.find_all(text=True)[0])
        
        for liEnergy in docVoiOccModel1.find_all('li',{"class":"fuel"}):
            for spanEnergy in liEnergy.find_all('span',{"class":"value"}):
                if("https://" not in spanEnergy.find_all(text=True)[0]):
                    allEnergiesOfCarOcc.append(spanEnergy.find_all(text=True)[0])

        for liVitesse in docVoiOccModel1.find_all('li',{"class":"boite"}):
            for spanVitesse in liVitesse.find_all('span',{"class":"value"}):
                if("https://" not in spanVitesse.find_all(text=True)[0]):
                    allVitesssOfCarOcc.append(spanVitesse.find_all(text=True)[0])

        for liMap in docVoiOccModel1.find_all('li',{"class":"map"}):
            for spanMap in liMap.find_all('span',{"class":"value"}):
                if("https://" not in spanMap.find_all(text=True)[0]):
                    localiteCarOcc.append(spanMap.find_all(text=True)[0])

        for divNameCar in docVoiOccModel1.find_all('div',{"class":"thumb-caption"}):
            for h2NameCar in divNameCar.find_all('h2'):
                for spanNameCar in h2NameCar.find_all('span'):
                    nameCarOcc.append(spanNameCar.find_all(text=True)[0])

        for adescCarOcc in docVoiOccModel1.find_all('a',{"class":"details-container"}):
            for pdescCarOcc in adescCarOcc.find_all('p'):
                descrCarOcc.append(pdescCarOcc.find_all(text=True)[0].replace('\n                ',''))

        for divCarPrice in docVoiOccModel1.find_all('div',{"class":"price"}):
            if(divCarPrice.find_all(text=True)[0] !="\n"):
                priceCarOcc.append(divCarPrice.find_all(text=True)[0].replace('\n                    ',''))

        for imgOfCarOcc in docVoiOccModel1.find_all('div',{"class":"details-wrapper"}):
            for images in imgOfCarOcc.find_all('img'):
                imgCarOcc.append(images['src'])


    for nCO in nameCarOcc:
        nameMarque.append(nCO.split(" ",1)[0])

############ Function for all linkAllConAncVoit
tCAVFPFinale = []
for lACAV in linkAllConAncVoit:
    resultConAncVoitFooterPage = requests.get(lACAV)

    #Parse the result using the HTML mode
    docConAncVoitFooterPage = BeautifulSoup(resultConAncVoitFooterPage.text, "html.parser")

    tagsConAncVoitFooterPage = docConAncVoitFooterPage.find_all('a',{"class": "page-link"})
    
    if(tagsConAncVoitFooterPage):
        for tCAVFP in tagsConAncVoitFooterPage:
            tCAVFPFinale.append(URL + tCAVFP['href'][3:])
        tCAVFPFinale2 = list(set(tCAVFPFinale))

    else:
        linkPageWithoutFooter.append(lACAV)

getInformationFromCArsOcc(tCAVFPFinale2)
getInformationFromCArsOcc(linkPageWithoutFooter)

imgCarOccFinal = list(set(imgCarOcc))
nameMarqueFinal = list(set(nameMarque))

for dCO in descrCarOcc:
    enoced = dCO.encode("UTF-8")
    decoded = enoced.decode("UTF-8")
    descrCarOccFinal.append(decoded.replace('\n',' '))

nameMarqueInList = []
marques2 = Marque.objects.values('nomMarque')
print(marques2)
for mq2 in marques2:
    print(mq2['nomMarque'])
    nameMarqueInList.append(mq2['nomMarque'])
print(nameMarqueInList)

nameCarOccAndMarqueCar = []
for i1 in nameCarOcc:
    for j1 in nameMarqueInList:
        if(j1 in i1):
            nameCarOccAndMarqueCar.append(j1)

print(nameCarOccAndMarqueCar)
print(len(nameCarOccAndMarqueCar))
print(len(nameCarOcc))

priceCarOcc2 =[]
for pco in priceCarOcc:
    priceCarOcc2.append(pco.replace(' ',''))

allRoadOfCarOcc2 =[]
for pco2 in allRoadOfCarOcc:
    allRoadOfCarOcc2.append(pco2.replace(' ',''))


nameMarqueInListDB = []
nameCarInListDB = []
resultDB = []

marques3 = Marque.objects.values('nomMarque')
print(marques3)
for mq3 in marques3:
    print(mq3['nomMarque'])
    nameMarqueInListDB.append(mq3['nomMarque'])
print(nameMarqueInListDB)

for i in nameCarOcc:
    for j in nameMarqueInListDB:
        if(j in i):
            resultDB.append(j)
            break

print('Hello4')


for tag in tags:
    if("vendeurs-pro" in tag['href']):
        URLVoiOccVendPro = URL + tag['href'][3:]
print(URLVoiOccVendPro)


resultConAncVoitVendPro = requests.get(URLVoiOccVendPro)

#Parse the result using the HTML mode
docConAncVoitVendPro = BeautifulSoup(resultConAncVoitVendPro.text, "html.parser")

tagsConAncVoitVendPro = docConAncVoitVendPro.find_all('div',{"class":"infos-wrapper"})

for tCAVVP in tagsConAncVoitVendPro:
    for tCAVVPI in tCAVVP.find_all('img'):
        nameVendeurList.append(tCAVVPI['alt'])
        imagesVendeurList.append(URL[:len(URL)-2] + tCAVVPI['src'])

    for tCAVVPA in tCAVVP.find_all('div', {"class":"address"}):
        addressVendeurList.append(tCAVVPA.find_all(text=True))

    for tCAVVPP in tCAVVP.find_all('div', {"class":"phone"}):
        phoneVendeurList.append(tCAVVPP.find_all(text=True))

    for tCAVVPF in tCAVVP.find_all('div', {"class":"fax"}):
        for tCAVVPFB in tCAVVPF.find_all('b',text='Fax. : '):
            faxVendeurList.append(tCAVVPFB.next_sibling)


for aVL in addressVendeurList:
    addressVendeurListNew.append(aVL[0].replace('\n                                                    ',''))

for pVL in phoneVendeurList:
    phoneVendeurListNew.append(pVL[2].replace('                                            ',''))

for fVL in faxVendeurList:
    faxVendeurListNew.append(fVL.replace('                                            ',''))

print('Hello5')