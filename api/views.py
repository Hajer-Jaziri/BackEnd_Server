import genericpath
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import generics
from django.contrib.auth.models import User

from .serializers import AnnonceVoitureSerializer, MarqueSerializer, VoitureNeufSerializer, VoitureOccasionSerializer, ImmobilierSerializer, EmploiSerializer, MaterielleInformatiqueSerializer, NotificationSerializer, CategorieSerializer
from Notification.models import Notification
from automobilewebscrapper.models import AnnonceVoiture, Marque, VoitureNeuf, VoitureOccasion, AnnonceVoiture
from CategorieAnnonce.models import Categorie
from afariat.models import Immobilier, Emploi, MaterielleInformatique
from datetime import datetime

from rest_framework.pagination import PageNumberPagination

# Si vous pouvez de lancer le web-scrapping il faut de suprimer tous les commentaires
# Remarque très importante lorsque vous lancer le programme ce bloc va travailler une seul fois 
# Wait until you see this message Starting development server at http://127.0.0.1:8000/
# Quit the server with CTRL-BREAK.

# from .BackGroundAutoMobile import *
# from .BackGroundAfariatImmobilier import *
# from .BackGroundAfariatEmploi import *
# from .BackGroundOffreEmploi import *
# from .BackGroundAfariatMaterielleInformatique import *

'''Cette fonction sera lancée si vous pouvez de faire le web-scrapping'''
# @api_view(['POST'])
# def addMarque(request):
#     for tAltNC, tSNC in zip(tagAltNewCar, tagSrcNewCar):
#         mq = Marque(nomMarque=tAltNC,imageMarque=get_as_base64(tSNC))
#         mq.save()
#     return Response("Add Marque sucess")

'''Cette fonction sera lancée si vous pouvez de faire le web-scrapping'''
# @api_view(['POST'])
# def addVoitureNeuf(request):
    # for tVNL in tagsVoiNeufLink:
    #     getInformationForVoiNeuf(tVNL)
    
    # for tVMS in tagsVoiNeufModelSpan:
    #     tagsVoiNeufModelSpanFinalList.append(tVMS[0])

    # for tVNMH2 in tagsVoiNeufModelH2:
    #     tagsVoiNeufModelH2FinalList.append(tVNMH2[0])

    # marqueAndNameCar =[]
    # for i in tagsVoiNeufModelH2FinalList:
    #     for j in tagAltNewCar:
    #         if(j in i):
    #             marqueAndNameCar.append(j)
    
    # for tVNMH2, tVNMS, tVNMP, tVNMI, tANC in itertools.zip_longest(tagsVoiNeufModelH2FinalList, tagsVoiNeufModelSpanFinalList, tagsVoiNeufModelPrice, tagsVoiNeufModelImg, marqueAndNameCar):
    #     # return Response(tVNMH2)
    #     print(tVNMH2)
    #     mq = Marque.objects.get(nomMarque=tANC)
    #     adminMail = Utilisateur.objects.get(emailUser="hajer-hajer@gmail.com")
    #     categ = Categorie.objects.get(nomCategorie="Voiture")

    #     vn = AnnonceVoiture(idVoiture=categ,nomMarque=mq,nomVoiture=tVNMH2,prix=int(tVNMP.replace(' ','')),
    #     image=get_as_base64(tVNMI),activationAnnonce=1,annoceWNScrappOfAdmin=0,emailUser=adminMail,typeCar="New_Car")
    #     vn.save()
    # annonceVoi = AnnonceVoiture.objects.all()
    # for aV,tVNMS in itertools.zip_longest(annonceVoi,tagsVoiNeufModelSpanFinalList):
    #     vn = VoitureNeuf(annonceVoiture=aV,disponible=tVNMS)
    #     vn.save()

    # return Response("Add new cars sucess")

'''Cette fonction sera lancée si vous pouvez de faire le web-scrapping'''
# @api_view(['POST'])
# def addConcessionnaires(request):
#     for tCNH2 in tagsConcessionairesH2:
#         tagsConcessionairesH2List.append(tCNH2[0])

#     for tCH2L, tCBT in zip(tagsConcessionairesH2List, tagsConcessionairesBTel):
#         c =Concessionnaires(nomConcessionnaires=tCH2L, Tel= tCBT)
#         c.save()
#     return Response("Add new Concessionnaires sucess")

'''Cette fonction sera lancée si vous pouvez de faire le web-scrapping'''
# @api_view(['POST'])
# def addVoitureOccasion(request):
    # for mq2,nCO, pCO, iCO, dCOF, aYOfO, aROCO, llCO, aEOCO, aVOCO in itertools.zip_longest(resultDB, nameCarOcc, 
    # priceCarOcc2, imgCarOccFinal, descrCarOccFinal, allYearOfCarOcc, allRoadOfCarOcc2, localiteCarOcc, 
    # allEnergiesOfCarOcc, allVitesssOfCarOcc):
    #     mq = Marque.objects.get(nomMarque=mq2)

    #     adminMail = Utilisateur.objects.get(emailUser="hajer-hajer@gmail.com")
    #     categ = Categorie.objects.get(nomCategorie="Voiture")

    #     vn = AnnonceVoiture(idVoiture=categ,nomMarque=mq,nomVoiture=str(nCO),prix=int(pCO),
    #     image=get_as_base64(iCO),activationAnnonce=1,annoceWNScrappOfAdmin=0,emailUser=adminMail,typeCar="Occasion_Car")
    #     vn.save()

#     annonceVoi = AnnonceVoiture.objects.filter(typeCar="Occasion_Car")
#     for aV,dCOF,aYOfO,aROCO,llCO,aEOCO,aVOCO in itertools.zip_longest(annonceVoi,descrCarOccFinal,allYearOfCarOcc,allRoadOfCarOcc2,localiteCarOcc
#     ,allEnergiesOfCarOcc,allVitesssOfCarOcc):
    
#         vo = VoitureOccasion(annonceVoiture=aV,description=str(dCOF),annee =str(aYOfO),KMS=int(aROCO),localite=
#         str(llCO),energie=str(aEOCO),boiteVitesse=str(aVOCO))
#         vo.save()

#     return Response("Add new Voiture Occasion sucess")

'''Cette fonction sera lancée si vous pouvez de faire le web-scrapping'''
# @api_view(['POST'])
# def addVendeurPro(request):
#     for iVL2,aVLN,pVLN,fVLN,nVL in itertools.zip_longest(imagesVendeurList,addressVendeurListNew,phoneVendeurListNew,faxVendeurListNew,nameVendeurList):
#         vp = VendeurPro(address=aVLN,Tel=pVLN,Fax=fVLN,image=get_as_base64(iVL2),nomVendeur=nVL)
#         vp.save()
#     return Response("Add a new Vendeur Pro")

'''Cette fonction sera lancée si vous pouvez de faire le web-scrapping'''
# @api_view(['POST'])
# def addImmobilier(request):
#     for nI, iI, pI, dI,aI, vI in itertools.zip_longest(nameImmobilier,imageImmobilier,priceImmobilier,dateImmobilier,annoceImmobilier,villeImmobilier):
#         im = Immobilier(nameImmobilier=nI, imageImmobilier=iI,priceImmobilier=pI,dateImmobilier=dI,annoceImmobilier=aI,villeImmobilier=vI,activationAnnonce=1,idImmobilier="Immobilier",emailUser="hajer-hajer@gmail.com")
#         im.save()
#     return Response("Add Immobilier")

'''Cette fonction sera lancée si vous pouvez de faire le web-scrapping'''
# @api_view(['POST'])
# def addEmploi(request):
#     for nE, iE, pE, dE,aE, vE in itertools.zip_longest(nameEmploi,imageEmploi,priceEmploi,dateEmploi,annoceEmploi,villeEmploi):
#         em = Emploi(nameEmploi=nE, imageEmploi=iE,priceEmploi=pE,dateEmploi=dE,annoceEmploi=aE,villeEmploi=vE,activationAnnonce=1,idEmploi="Emploi",emailUser="hajer-hajer@gmail.com")
#         em.save()
#     return Response("Add Emploi")

'''Cette fonction sera lancée si vous pouvez de faire le web-scrapping'''
# @api_view(['POST'])
# def addEmploiFromOffreEmploi(request):
#     for jtL, j, l, pLN2,DEN in itertools.zip_longest(jobTitleList,job,local,previewListNew2,dateEmploiNew):
#         em = Emploi(nameEmploi=jtL,dateEmploi=DEN,annoceEmploi=pLN2,villeEmploi=l)
#         em.save()
#     return Response("Add Emploi from Offre Emploi")

'''Cette fonction sera lancée si vous pouvez de faire le web-scrapping'''
# @api_view(['POST'])
# def addMaterielleInformatique(request):
#     for nMI, iMI, pMI, dMI,aMI, vMI in itertools.zip_longest(nameMaterInfor,imageMaterInfor,priceMaterInfor,dateMaterInfor,annoceMaterInfor,villeMaterInfor):
#         mI = MaterielleInformatique(nameMatrInformatique=nMI, imageMatrInformatique=iMI,priceMatrInformatique=pMI,dateMatrInformatique=dMI,annoceMatrInformatique=aMI,villeMatrInformatique=vMI,activationAnnonce=1,idImmobilier="Materielle Informatique",emailUser="hajer-hajer@gmail.com")
#         mI.save()
#     return Response("Add Materielle Informatique")

class largeResultsSetPagination(PageNumberPagination): 
    page=10
    page_size_query_paramn ='page_size'
    max_page_size =500

@api_view(['POST'])

def registerUser(request):
    req = request.data
    passwordUser = req['password']
    username = req['username']
    email = req['email']
    # is_staff = req['is_staff']
    # is_active = req['is_active']
    responseList = []
    data = {}

    try:
        user = User.objects.create_user(username=username, email=email, password=passwordUser)
        user.is_active = False
        user.save()

        infoUser = User.objects.get(username=username)
        token = Token.objects.create(user=infoUser)

        data['status'] = infoUser.is_active
        getInfoToken = Token.objects.get(user=infoUser).key
        data['token'] = getInfoToken
        
        dateToday = datetime.today().strftime('%Y-%m-%d')
        notification = Notification(emailAdmin="hajer-hajer@gmail.com",emailMembre=email,contenu="New user added and we are looking for activation account",dateNotification=str(dateToday))
        notification.save()
        responseList.append({
            "status": status.HTTP_200_OK,
            "Message": "Add an new user with sucess",
            "data": data
        })

        return Response(responseList)
    except Exception as e:
        print(e)
        responseList.append({
            "status": status.HTTP_404_NOT_FOUND,
            "Message": "Attention you have this account please check the information",
        })

        return Response(responseList)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def activationAccount(request):
    # try:
    if request.user.is_staff is True:
        req = request.data
        email = req['email']
        userAccount = User.objects.get(email=email)
        userAccount.is_active = True
        userAccount.save()

        dateToday = datetime.today().strftime('%Y-%m-%d')
        notification = Notification(emailAdmin="hajer-hajer@gmail.com",emailMembre=email,contenu="The account has been successfully activated",dateNotification=str(dateToday))
        notification.save()
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Le compte "+email+" est activée",
        "data": {
        email
        }
    })
    # except:
    #     return Response({
    #         "status" : status.HTTP_404_NOT_FOUND,
    #         "message": "Vous n'avez pas le droit d'activer se compte"
    #     })


@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def updateUser(request):
    try:
        userAccount = request.user
        req = request.data
        passwordUser = req['password']
        confirmPassword = req['password_confirm']
        username = req['username']

        if(str(passwordUser) == str(confirmPassword)) and passwordUser!= "":
            userAccount.set_password(passwordUser)
            if userAccount.username != username and username != "":
                userAccount.username = username
            userAccount.save()
            dateToday = datetime.today().strftime('%Y-%m-%d')
            notification = Notification(emailAdmin="hajer-hajer@gmail.com",emailMembre=request.user.email,contenu="You have modified some user information",dateNotification=str(dateToday))
            notification.save()
            return Response({
            "status" : status.HTTP_200_OK,
            "message": "sucess"
            })
        elif (str(passwordUser) == str(confirmPassword)) and passwordUser == "":
            if userAccount.username != username and username != "":
                userAccount.username = username
                userAccount.save()
                dateToday = datetime.today().strftime('%Y-%m-%d')
                notification = Notification(emailAdmin="hajer-hajer@gmail.com",emailMembre=request.user.email,contenu="You have modified some user information",dateNotification=str(dateToday))
                notification.save()
                return Response({
                    "status" : status.HTTP_200_OK,
                    "message": "success"
                    })

        else:
            return Response({
            "status" : status.HTTP_200_OK,
            "message": "0 changes"
            })
    except Exception as e:
        print(e)
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Il y a une probleme faire attention !!!!"
        })
        
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def getListOfUser(request):
    responseList = []
    try:
        #Token et admin a compte
        if request.user.is_staff is True:
            users = User.objects.all()
            for u in users:
                if(u.email==request.user.email):
                    continue
                responseList.append({
                    "email": u.email,
                    "user_name": u.username,
                    "is_staff": u.is_staff,
                    "is_active": u.is_active,
                    
                })
        return Response({
            "status" : status.HTTP_200_OK,
            "message": "Les information de tous les utilisateurs",
            "data" :  responseList
        })
    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte"
        })


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def getListOfUserNotActivate(request):
    responseList = []
    try:
        if request.user.is_staff is True:
            users = User.objects.filter(is_active=False)
            for u in users:
                if(u.email==request.user.email):
                    continue
                responseList.append({
                    "email": u.email,
                    "user_name": u.username,
                    "is_staff": u.is_staff,
                    "is_active": u.is_active,
            
                })
        return Response({
            "status" : status.HTTP_200_OK,
            "message": "Les information de tous les utilisateurs",
            "data" :  responseList
        })
    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte"
        })

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def getListOfMembre(request):
    responseList = []
    try:
        if request.user.is_staff is True:
            users = User.objects.filter(is_active=True)
            for u in users:
                if(u.email==request.user.email):
                    continue
                responseList.append({
                    "email": u.email,
                    "user_name": u.username,
                    "is_staff": u.is_staff,
                    "is_active": u.is_active,
                    
                })
        return Response({
            "status" : status.HTTP_200_OK,
            "message": "Les information de tous les utilisateurs",
            "data" :  responseList
        })
    except Exception as e:
        print(e)
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte"
        })


@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def deleteUserUsingAdmin(request):
    try:
        if request.user.is_staff is True:
            req = request.data
            email = req['email']
            User.objects.filter(email=str(email)).delete()
            return Response({
                "status" : status.HTTP_200_OK,
                "message": "Le compte "+email+" à été supprimée avec sucess !!!",
                "data" : {
                    email
                }
            })
        else:
            return Response({
                "status" : status.HTTP_404_NOT_FOUND,
                "message": "Vous avez une erreur !!!",
            })
    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte"
        })


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def searchUser(request):
    responseList = []
    try:
        if request.user.is_staff is True:
            req = request.data
            username = req['username']
            users = User.objects.filter(username=username)
            print(users)
            for u in users:
                print(u.email)
                responseList.append({
                    "email": u.email,
                    "user_name": u.username,
                    "is_staff": u.is_staff,
                    "is_active": u.is_active,
                })
        return Response({
            "status" : status.HTTP_200_OK,
            "message": "Les information de tous les utilisateurs",
            "data" :  responseList
        })
    except Exception as e:
        print(e)
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte"
        })
        ############################################# Categories Function #############################################

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def addCategorieUsingAdmin(request):
    req = request.data
    # emailUser = req['emailUser']
    nomCategorie = req['nomCategorie']

    if request.user.is_staff is True:
        categorie = Categorie(nomCategorie=nomCategorie,)
        categorie.save()
    else:
        categorie = Categorie(nomCategorie=nomCategorie,)
        categorie.save()

        dateToday = datetime.today().strftime('%Y-%m-%d')
        notification = Notification(emailAdmin="hajer-hajer@gmail.com",emailMembre=request.user.email,contenu="An user add an Categorie you need an activation",dateNotification=str(dateToday))
        notification.save()
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'ajouter une nouvelle categorie (Changer le token de l'admin)!!"
        })

    return Response({
        "status" : status.HTTP_200_OK,
        "message": nomCategorie+" est ajoutée avec sucess !!",
    })

    return Response("Add Categorie sucess")


@api_view(['GET'])
def getCategorie(request):
    try:
        ca = Categorie.objects.all()
        serializer = CategorieSerializer(ca, many=True)
        return Response({
            "status" : status.HTTP_200_OK,
            "message": "Les information de tous les categories",
            "data" :  serializer.data
        })
    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous avez une erreur vérifier !!"
        })

@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def updateCategorie(request):
    req = request.data
    nomCategorie = req['nomCategorie']
    newNameCategorie = req['newNameCategorie']

    try:
        if request.user.is_staff is True:
            Categorie.objects.filter(nomCategorie=nomCategorie).update(nomCategorie=newNameCategorie)
        return Response({
            "status" : status.HTTP_200_OK,
            "message": "Le categorie "+nomCategorie+" est modifiée avec succées !!!",
        })
    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte"
        })

@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def deleteCategorie(request):
    req = request.data
    nomCategorie = req['nomCategorie']
    try:
        if request.user.is_staff is True:
            Categorie.objects.filter(nomCategorie=nomCategorie).delete()
        return Response({
            "status" : status.HTTP_200_OK,
            "message": "Le categorie "+nomCategorie+" est supprimée !!!",
        })
    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte"
        })


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def activationCategorieByAdmin(request):
    req = request.data
    nomCategorie = req['nomCategorie']
    try:
        if request.user.is_staff is True:
            Categorie.objects.filter(nomCategorie=nomCategorie).update(activationCategorie=True)
        return Response({
            "status" : status.HTTP_200_OK,
            "message": "Le categorie "+nomCategorie+" est activée !!!",
        })
    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte"
        })


#Ceci pour les simples utilisateurs
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getonlyActivationCategorie(request):
    categorieList = []
    try:
        if request.user.is_staff is True:
            categorie = Categorie.objects.filter(activationCategorie=True)
            for c in categorie:
                # print(m.emailMembre.firstNameUser)
                categorieList.append({
                    "nomCategorie": c.nomCategorie
                })  
        return Response({
            "status" : status.HTTP_200_OK,
            "message": "List of categories est activée !!!",
            "data": categorieList
        })
    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte"
        })
        
############################################# Annonce Voiture Functions #############################################

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def addNewMarque(request):
    req = request.data
    nomMarque = req['nomMarque']
    imageMarque = req['imageMarque'] # You should send it in base64 format
    mq = Marque(nomMarque=nomMarque,imageMarque=imageMarque)
    mq.save()
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Add new marque with sucess !!!"
    })

@api_view(['GET'])
def getMarque(request):
    mq = Marque.objects.all()
    serializer = MarqueSerializer(mq, many=True)
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Add new marque with sucess !!!",
        "data": serializer.data
    })

@api_view(['POST'])
def searchMarqueByName(request):
    req = request.data
    nomMarque = req['nomMarque']
    try:
        mq = Marque.objects.get(nomMarque=nomMarque)
        serializer = MarqueSerializer(mq, many=False)
        return Response({
            "status" : status.HTTP_200_OK,
            "message": "Les information du marque "+nomMarque+" !!!",
            "data": serializer.data
        })

    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "You have not this marque please try again"
        })


@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def updateMarque(request):
    req = request.data
    nomMarque = req['nomMarque']
    newNameMarque = req['newNameMarque']
    imageMarque = req['imageMarque']

    if Marque.objects.filter(nomMarque=nomMarque).update(nomMarque=newNameMarque,imageMarque=imageMarque) :
        return Response({
        "status" : status.HTTP_200_OK,
        "message": " marque est mettre à jour !!!",
            })
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Please check your Marque name"
            })
@api_view(['GET'])
#@permission_classes((IsAuthenticated,))
def getCountOfMarque(request):
    if request.user.is_staff is True:
        m = Marque.objects.all().count()
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Les nombres d'annonces du voiture neuf qui sont inclue dans la base !!",
        "data" :  {"nbr de marque": m}
    })  
      

@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def deleteMarque(request):
    req = request.data
    nomMarque = req['nomMarque']

    try:
        if request.user.is_staff is True:
            Marque.objects.filter(nomMarque=nomMarque).delete()
        return Response({
            "status" : status.HTTP_200_OK,
            "message": "La marque "+nomMarque+" est supprimée!!!",
        })
    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte"
        })
        

class VoitureALLtest(generics.ListAPIView):
    queryset =AnnonceVoiture.objects.all() 
    serializer_class = AnnonceVoitureSerializer
    pagination_class = largeResultsSetPagination

@api_view(['GET'])
def getAnnonceVoiture(request):
    av = AnnonceVoiture.objects.all()
    serializer = AnnonceVoitureSerializer(av, many=True)
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "List d'annonce de voiture !!!",
        "data": serializer.data
    })


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def addNewCar(request):
    req = request.data
    nomCategorie = req['nomCategorie']
    nomMarque = req['nomMarque']
    imageMarque = req['imageMarque'] # You should send it in base64 format
    nomVoiture = req['nomVoiture']
    disponible = req['disponible']
    prix = req['prix']
    image = req['image'] # You should send it in base64 format

    try:
        mq = Marque.objects.get(nomMarque=nomMarque)
    except:
        mnq = Marque(nomMarque=nomMarque,imageMarque=imageMarque)
        mnq.save()
        mq = Marque.objects.get(nomMarque=nomMarque)

    try:
        if request.user.is_staff is True:
            try:
                categorieInformation = Categorie.objects.get(nomCategorie=nomCategorie,activationCategorie=True)
            except:
                return Response("Pleas check the name of categorie or wait the activation of your annonce")
            
            anVoi = AnnonceVoiture(idVoiture=categorieInformation,nomMarque=mq,nomVoiture=nomVoiture,prix=prix,
            image=image,activationAnnonce=True,annoceWNScrappOfAdmin=True,emailUser=request.user,typeCar="New_Car")
            anVoi.save()

            annonceVoit = AnnonceVoiture.objects.filter(typeCar="New_Car",nomVoiture=nomVoiture)

            # print(annonceVoit[0])
            vn = VoitureNeuf(annonceVoiture=annonceVoit[0],disponible=disponible)
            vn.save()

            return Response({
                "status":status.HTTP_200_OK,
                "message": "Add new car with the email "+request.user.email+" !!!"
            })

        else:
            categorieInformation = Categorie.objects.get(nomCategorie=nomCategorie)
                      

            anVoi = AnnonceVoiture(idVoiture=categorieInformation,nomMarque=mq,nomVoiture=nomVoiture,prix=prix,
            image=image,activationAnnonce=False,annoceWNScrappOfAdmin=False,emailUser=request.user,typeCar="New_Car")
            anVoi.save()

            annonceVoit = AnnonceVoiture.objects.filter(typeCar="New_Car",nomVoiture=nomVoiture)

            vn = VoitureNeuf(annonceVoiture=annonceVoit[0],disponible=disponible)
            vn.save()


            # membreInformation = Membre.objects.get(emailMembre=emailUser)
            # admininformation = Administrateur.objects.get(emailAdmin="hajer-hajer@gmail.com")
            dateToday = datetime.today().strftime('%Y-%m-%d')
            notification = Notification(emailAdmin="hajer-hajer@gmail.com",emailMembre=request.user.email,contenu="You add a new annonce and we wait the activation of the admin",dateNotification=str(dateToday))
            notification.save()

            return Response({
                "status":status.HTTP_200_OK,
                "message": "Add new car with the email "+request.user.email+" !!!"
            })
    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte"
        })
        

class VoitureNeufALLtest(generics.ListAPIView):
    queryset =VoitureNeuf.objects.all() 
    serializer_class = VoitureNeufSerializer
    pagination_class = largeResultsSetPagination
#Cette méthode doit trvailler seulement pour l'administrateur
@api_view(['GET'])
def getVoitureNeuf(request):
    listFinal = []
    vn = VoitureNeuf.objects.all()
    for i in vn:
        # print(i.annonceVoiture_id)
        annonceVoit = AnnonceVoiture.objects.get(id=i.annonceVoiture_id,typeCar="New_Car")
        listFinal.append({
            "id_Voiture": annonceVoit.id,
            "Nom_Categorie": annonceVoit.idVoiture.nomCategorie,
            "Nom_Marque": annonceVoit.nomMarque.nomMarque,
            "Nom_Voiture": annonceVoit.nomVoiture,
            "Prix": annonceVoit.prix,
            "image": annonceVoit.image,
            "Activation_Annonce": annonceVoit.activationAnnonce,
            "Annoce_Without_Scrapping_Of_Admin": annonceVoit.annoceWNScrappOfAdmin,
            "Type_Car": annonceVoit.typeCar
        })
    
    return Response({
            "status" : status.HTTP_200_OK,
            "message": "Les information de tous les voitures neufs",
            "data" :  listFinal
        })

@api_view(['POST'])
def searchCarsNewByName(request):
    req = request.data
    nomVoiture = req['nomVoiture']

    nVN = AnnonceVoiture.objects.filter(nomVoiture=nomVoiture,activationAnnonce=True)
    serializer = AnnonceVoitureSerializer(nVN, many=True)
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Les information du voiture: "+nomVoiture,
        "data" :  serializer.data
    })

class VoitureNeufALLtest(generics.ListAPIView):
    queryset =VoitureNeuf.objects.all() 
    serializer_class = VoitureNeufSerializer
    pagination_class = largeResultsSetPagination

@api_view(['GET'])
def getVoitureNeufWithActivationOfAdmin(request):
    vn = AnnonceVoiture.objects.filter(activationAnnonce=True)
    serializer = AnnonceVoitureSerializer(vn, many=True)
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Les information du voiture neuf qui sont activée par admin ",
        "data" :  serializer.data
    })

class VoitureNeufALLtest(generics.ListAPIView):
    queryset =VoitureNeuf.objects.all() 
    serializer_class = VoitureNeufSerializer
    pagination_class = largeResultsSetPagination

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getVoitureNeufNotactivationOfAdmin(request):
    if request.user.is_staff is True:
        vn = AnnonceVoiture.objects.filter(activationAnnonce=False)
        serializer = AnnonceVoitureSerializer(vn, many=True)
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Les information du voiture neuf qui ne sont pas activée par admin ",
        "data" :  serializer.data
    })

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def activationVoitureNeufByAdmin(request):
    req = request.data
    nomVoiture = req['nomVoiture']
    try:
        if request.user.is_staff is True:
            AnnonceVoiture.objects.filter(nomVoiture=nomVoiture).update(activationAnnonce=True)
            return Response({
                "status" : status.HTTP_200_OK,
                "message": "La annonce du voiture "+nomVoiture+" est activée!!!",
            })
        else:
            return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas utiliser un compte admin vérifier svp"
        })
    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte"
        })

@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def updateNewCar(request):
    req = request.data
    nomVoiture = req['nomVoiture']
    newNameVoiture = req['newNameVoiture']
    disponible = req['disponible']
    prix = req['prix']
    image = req['image'] # You should send it in base64 format

    AnnonceVoiture.objects.filter(nomVoiture=nomVoiture).update(nomVoiture=newNameVoiture,prix=prix,image=image)
    
    anVoi = AnnonceVoiture.objects.get(nomVoiture=newNameVoiture)
    print(anVoi.id)
    vv = VoitureNeuf.objects.filter(annonceVoiture_id=anVoi.id).update(disponible=disponible)
    print(vv)
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Une nouvelle annonce de voiture neuf est mettre à jour"
    })

@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def deleteNewCar(request):
    req = request.data
    nomVoiture = req['nomVoiture']

    try:
        if request.user.is_staff is True:
            anVoi = AnnonceVoiture.objects.get(nomVoiture=nomVoiture)
            print(anVoi.id)
            VoitureNeuf.objects.filter(annonceVoiture_id=anVoi.id).delete()
            AnnonceVoiture.objects.filter(nomVoiture=nomVoiture).delete()
            return Response({
                "status" : status.HTTP_200_OK,
                "message": "La annonce du voiture "+nomVoiture+" a été supprimée par "+request.user.email+"!!",
            })
        else:
            anVoi = AnnonceVoiture.objects.get(nomVoiture=nomVoiture)
            print(anVoi.id)
            VoitureNeuf.objects.filter(annonceVoiture_id=anVoi.id).delete()
            AnnonceVoiture.objects.filter(nomVoiture=nomVoiture).delete()
            return Response({
            "status" : status.HTTP_200_OK,
            "message": "La annonce du voiture "+nomVoiture+" a été supprimée par "+request.user.email+"!!",
        })
    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte"
        })


class VoitureNeufALLtest(generics.ListAPIView):
    queryset =VoitureNeuf.objects.all() 
    serializer_class = VoitureNeufSerializer
    pagination_class = largeResultsSetPagination
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getVoitureNeufInsertWithMembre(request):
    req = request.data

    try:
        vn = AnnonceVoiture.objects.filter(emailUser=request.user.id)
        serializer = AnnonceVoitureSerializer(vn, many=True)
        return Response({
            "status" : status.HTTP_200_OK,
            "message": "Les information du voiture neuf insérer par un memebre ",
            "data" :  serializer.data
        })
    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Attention vous avez s'authentifier comme étant un admin"
        })

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getCountOfAnnonceOfNewCar(request):
    if request.user.is_staff is True:
        vn = VoitureNeuf.objects.all().count()
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Les nombres d'annonces du voiture neuf qui sont inclue dans la base !!",
        "data" :  {"nb_NewCar": vn}
    })
@api_view(['GET'])
def getAllVoitureNeufByMarque(request):
    listOfMarque = []
    listOfNumber = []
    marque = Marque.objects.all()
    for m in marque:
        listOfMarque.append(m.nomMarque)
        countNumber = AnnonceVoiture.objects.filter(nomMarque = m.nomMarque,typeCar="New_Car").count()
        listOfNumber.append(countNumber)
    
    resultFinale = dict(zip(listOfMarque, listOfNumber))

    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Tous les annonces de voitures neuf par marque !!",
        "data" :  resultFinale
    })




class VoitureNeufALLtest(generics.ListAPIView):
    queryset =VoitureNeuf.objects.all() 
    serializer_class = VoitureNeufSerializer
    pagination_class = largeResultsSetPagination
@api_view(['GET'])
def getVoitureNeufWithoutScrappingMethod(request):
    vn = AnnonceVoiture.objects.filter(annoceWNScrappOfAdmin=True,typeCar="New_Car")
    serializer = AnnonceVoitureSerializer(vn, many=True)
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Les annonces du voiture neuf qui sont inserer manuellement sans interaction avec notre algo de webscrappig !!",
        "data" :  serializer.data
    })


################################ Occasions Car ################################
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def addOccasionCar(request):
    req = request.data
    # emailUser = req['emailUser']
    nomCategorie = req['nomCategorie']
    nomMarque = req['nomMarque']
    imageMarque = req['imageMarque'] # You should send it in base64 format    
    nomVoiture = req['nomVoiture']
    prix = req['prix']
    image = req['image'] # You should send it in base64 format
    description = req['description']
    annee = req['annee']
    KMS = req['KMS']
    localite = req['localite']
    energie = req['energie']
    boiteVitesse = req['boiteVitesse']
    try:
        mq = Marque.objects.get(nomMarque=nomMarque)
    except:
        mnq = Marque(nomMarque=nomMarque,imageMarque=imageMarque)
        mnq.save()
        mq = Marque.objects.get(nomMarque=nomMarque)

    try:
        if request.user.is_staff is True:
            try:
                categorieInformation = Categorie.objects.get(nomCategorie=nomCategorie,activationCategorie=True)
            except:
                return Response("Pleas check the name of categorie or wait the activation of your annonce")
                
            anVoi = AnnonceVoiture(idVoiture=categorieInformation,nomMarque=mq,nomVoiture=nomVoiture,prix=prix,image=image,
            activationAnnonce=True,annoceWNScrappOfAdmin=True,emailUser=request.user,typeCar="Occasion_Car")
            anVoi.save()

            annonceVoit = AnnonceVoiture.objects.filter(typeCar="Occasion_Car",nomVoiture=nomVoiture)

            vo = VoitureOccasion(annonceVoiture=annonceVoit[0],description=description,annee=annee,KMS=KMS,localite=localite,energie=energie,boiteVitesse=boiteVitesse)
            vo.save() 

            return Response({
                "status":status.HTTP_200_OK,
                "message": "Add new occasion car with the email "+request.user.email+" !!!"
            })

        else:
            categorieInformation = Categorie.objects.get(nomCategorie=nomCategorie)
                        

            anVoi = AnnonceVoiture(idVoiture=categorieInformation,nomMarque=mq,nomVoiture=nomVoiture,prix=prix,image=image,
            activationAnnonce=False,annoceWNScrappOfAdmin=False,emailUser=request.user,typeCar="Occasion_Car")
            anVoi.save()

            annonceVoit = AnnonceVoiture.objects.filter(typeCar="Occasion_Car",nomVoiture=nomVoiture)
            vo = VoitureOccasion(annonceVoiture=annonceVoit[0],description=description,annee=annee,KMS=KMS,localite=localite,
            energie=energie,boiteVitesse=boiteVitesse)
            vo.save()


            # membreInformation = Membre.objects.get(emailMembre=emailUser)
            # admininformation = Administrateur.objects.get(emailAdmin="hajer-hajer@gmail.com")
            dateToday = datetime.today().strftime('%Y-%m-%d')
            notification = Notification(emailAdmin="hajer-hajer@gmail.com",emailMembre=request.user.email,contenu="We add a car occasion and we wait the activation of the admin",dateNotification=str(dateToday))
            notification.save()

            return Response({
                "status":status.HTTP_200_OK,
                "message": "Add new occasion car with the email "+request.user.email+" !!!"
            })
    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte"
        })

class VoitureOccasionALLtest(generics.ListAPIView):
    queryset =VoitureOccasion.objects.all() 
    serializer_class = VoitureOccasionSerializer
    pagination_class = largeResultsSetPagination
@api_view(['GET'])
def getVoitureOccasion(request):
    listFinal=[]
    vo = VoitureOccasion.objects.all()
    for i in vo:
        annonceVoit = AnnonceVoiture.objects.get(id=i.annonceVoiture_id)
        voitOcc = VoitureOccasion.objects.get(annonceVoiture_id=i.annonceVoiture_id,)
        listFinal.append({
            "id_Voiture": annonceVoit.id,
            "Nom_Categorie": annonceVoit.idVoiture.nomCategorie,
            "Nom_Marque": annonceVoit.nomMarque.nomMarque,
            "Nom_Voiture": annonceVoit.nomVoiture,
            "Prix": annonceVoit.prix,
            "image": annonceVoit.image,
            "Activation_Annonce": annonceVoit.activationAnnonce,
            "Annoce_Without_Scrapping_Of_Admin": annonceVoit.annoceWNScrappOfAdmin,
            #"Email_User": request.user.email,
            "Type_Car": annonceVoit.typeCar,
            "Description":voitOcc.description,
            "Annee_Pub":voitOcc.annee,
            "KMS":voitOcc.KMS,
            "Localisation":voitOcc.localite,
            "Energie":voitOcc.energie,
            "Boite_Vitesse":voitOcc.boiteVitesse
        })
    return Response({
            "status" : status.HTTP_200_OK,
            "message": "Les information de tous les voitures occasions",
            "data" :  listFinal
        })

class VoitureOccasionALLtest(generics.ListAPIView):
    queryset =VoitureOccasion.objects.all() 
    serializer_class = VoitureOccasionSerializer
    pagination_class = largeResultsSetPagination
#Cette méthode doit trvailler seulement pour le membre
@api_view(['GET'])
def getVoitureOccasionWithActivationOfAdmin(request):
    vn = AnnonceVoiture.objects.filter(activationAnnonce=True,typeCar="Occasion_Car")
    serializer = AnnonceVoitureSerializer(vn, many=True)
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Les information du voiture occasion qui sont activée par admin ",
        "data" :  serializer.data
    })



@api_view(['POST'])
def searchCarsOccasionByName(request):
    req = request.data
    nomVoiture = req['nomVoiture']

    nVN = AnnonceVoiture.objects.filter(nomVoiture=nomVoiture,typeCar="Occasion_Car",activationAnnonce=True)
    serializer = AnnonceVoitureSerializer(nVN, many=True)
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Les information du voiture occasion: "+nomVoiture,
        "data" :  serializer.data
    })

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def activationVoitureOccasionByAdmin(request):
    req = request.data
    nomVoiture = req['nomVoiture']

    try:
        if request.user.is_staff is True:
            AnnonceVoiture.objects.filter(nomVoiture=nomVoiture,typeCar="Occasion_Car").update(activationAnnonce=True)
            return Response({
                "status" : status.HTTP_200_OK,
                "message": "La annonce du voiture "+nomVoiture+" est activée!!!",
            })
        else:
            return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas utiliser un compte admin vérifier svp"
        })
    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte"
        })



@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def updateOccasionCar(request):
    req = request.data
    idVoiture = req['idVoiture']
    nomVoiture = req['nomVoiture']
    newNameVoiture= req['newNameVoiture']
    prix = req['prix']
    image = req['image'] # You should send it in base64 format
    description = req['description']
    annee = req['annee']
    KMS = req['KMS']
    localite = req['localite']
    energie = req['energie']
    boiteVitesse = req['boiteVitesse']

    AnnonceVoiture.objects.filter(id=idVoiture).update(nomVoiture=newNameVoiture,prix=prix,image=image)

    anVoi = AnnonceVoiture.objects.get(nomVoiture=newNameVoiture)
    print(anVoi.id)

    VoitureOccasion.objects.filter(annonceVoiture_id=anVoi.id).update(description=description,annee=annee,KMS=KMS,localite=localite,
    energie=energie,boiteVitesse=boiteVitesse)

    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Une nouvelle annonce de voiture occasion est mettre à jour"
    })

@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def deleteOccasionCar(request):
    req = request.data
    nomVoiture = req['nomVoiture']

    try:
        if request.user.is_staff is True:
            anVoi = AnnonceVoiture.objects.get(nomVoiture=nomVoiture)
            print(anVoi.id)
            VoitureOccasion.objects.filter(annonceVoiture_id=anVoi.id).delete()
            AnnonceVoiture.objects.filter(nomVoiture=nomVoiture,typeCar="Occasion_Car").delete()
            return Response({
                "status" : status.HTTP_200_OK,
                "message": "La annonce du voiture occasion "+nomVoiture+" a été supprimée par "+request.user.email+"!!",
            })
        else:
            anVoi = AnnonceVoiture.objects.get(nomVoiture=nomVoiture)
            print(anVoi.id)
            VoitureOccasion.objects.filter(annonceVoiture_id=anVoi.id).delete()
            AnnonceVoiture.objects.filter(nomVoiture=nomVoiture,typeCar="Occasion_Car").delete()
            return Response({
            "status" : status.HTTP_200_OK,
            "message": "La annonce du voiture "+nomVoiture+" a été supprimée par "+request.user.email+"!!",
        })
    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte"
        })

class VoitureOccasionALLtest(generics.ListAPIView):
    queryset =VoitureOccasion.objects.all() 
    serializer_class = VoitureOccasionSerializer
    pagination_class = largeResultsSetPagination
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getVoitureOccasionInsertWithMembre(request):
    req = request.data
    try:
        vn = AnnonceVoiture.objects.filter(emailUser=request.user.id,typeCar="Occasion_Car")
        serializer = AnnonceVoitureSerializer(vn, many=True)
        return Response({
            "status" : status.HTTP_200_OK,
            "message": "Les information du voiture neuf insérer par un memebre ",
            "data" :  serializer.data
        })
    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Attention vous avez s'authentifier comme étant un admin"
        })

class VoitureOccasionALLtest(generics.ListAPIView):
    queryset =VoitureOccasion.objects.all() 
    serializer_class = VoitureOccasionSerializer
    pagination_class = largeResultsSetPagination
@permission_classes((IsAuthenticated,))
@api_view(['GET'])
def getVoitureoccasionNotactivationOfAdmin(request):
    if request.user.is_staff is True:
        vn = AnnonceVoiture.objects.filter(activationAnnonce=False,typeCar="Occasion_Car")
        serializer = AnnonceVoitureSerializer(vn, many=True)
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Les information du voiture neuf qui ne sont pas activée par admin ",
        "data" :  serializer.data
    })

class VoitureOccasionALLtest(generics.ListAPIView):
    queryset =VoitureOccasion.objects.all() 
    serializer_class = VoitureOccasionSerializer
    pagination_class = largeResultsSetPagination
@api_view(['GET'])
def getVoitureOccasionWithoutScrappingMethod(request):
    vn = AnnonceVoiture.objects.filter(annoceWNScrappOfAdmin=True,typeCar="Occasion_Car")
    serializer = AnnonceVoitureSerializer(vn, many=True)
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Les annonces du voiture neuf qui sont inserer manuellement sans interaction avec notre algo de webscrappig !!",
        "data" :  serializer.data
    })

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getCountOfAnnonceOfOccasionCar(request):
    if request.user.is_staff is True:
        vn = VoitureOccasion.objects.all().count()
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Les nombres d'annonces du voiture neuf qui sont inclue dans la base !!",
        "data" :  {"nb_NewCar": vn}
    })
@api_view(['GET'])
def getAllVoitureOccasionByMarque(request):
    listOfMarque = []
    listOfNumber = []
    marque = Marque.objects.all()
    for m in marque:
        listOfMarque.append(m.nomMarque)
        countNumber = AnnonceVoiture.objects.filter(nomMarque = m.nomMarque,typeCar="Occasion_Car").count()
        listOfNumber.append(countNumber)
    
    resultFinale = dict(zip(listOfMarque, listOfNumber))

    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Tous les annonces de voitures neuf par marque !!",
        "data" :  resultFinale
    })

    
############################################# Annonce Immobilier Functions #############################################

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def addNewImmobilier(request):
    req = request.data
    nomCategorie = req['nomCategorie']
    nameImmobilier = req['nameImmobilier']
    imageImmobilier = req['imageImmobilier'] # You should send it in base64 format    
    priceImmobilier = req['priceImmobilier']
    dateImmobilier = req['dateImmobilier']
    annoceImmobilier = req['annoceImmobilier']
    villeImmobilier = req['villeImmobilier']


    try:
        if request.user.is_staff is True:
            try:
                categorieInformation = Categorie.objects.get(nomCategorie=nomCategorie)
            except:
                categorie = Categorie(nomCategorie=nomCategorie,activationCategorie=True)
                categorie.save()
                categorieInformation = Categorie.objects.get(nomCategorie=nomCategorie)

            im = Immobilier(nameImmobilier=nameImmobilier, imageImmobilier=imageImmobilier,priceImmobilier=priceImmobilier,
            dateImmobilier=dateImmobilier,annoceImmobilier=annoceImmobilier,villeImmobilier=villeImmobilier,
            annoceWNScrappOfAdmin=True,activationAnnonce=True,idImmobilier=categorieInformation,emailUser=request.user)
            im.save()

            return Response({
                "status" : status.HTTP_200_OK,
                "message": "La annonce du Immobilier "+nameImmobilier+" a été ajoutée avec succées par "+request.user.email+"!!",
                "data": {
                    "nomCategorie":nomCategorie,
                    "nameImmobilier":nameImmobilier,
                    "imageImmobilier":imageImmobilier,
                    "priceImmobilier":priceImmobilier,
                    "dateImmobilier":dateImmobilier,
                    "annoceImmobilier":annoceImmobilier,
                    "villeImmobilier":villeImmobilier
                }
            })
        else:
            try:
                categorieInformation = Categorie.objects.get(nomCategorie=nomCategorie)
            except:
                categorie = Categorie(nomCategorie=nomCategorie,activationCategorie=True)
                categorie.save()
                categorieInformation = Categorie.objects.get(nomCategorie=nomCategorie)

            im = Immobilier(nameImmobilier=nameImmobilier, imageImmobilier=imageImmobilier,priceImmobilier=priceImmobilier,
            dateImmobilier=dateImmobilier,annoceImmobilier=annoceImmobilier,villeImmobilier=villeImmobilier,activationAnnonce=False,
            annoceWNScrappOfAdmin=True,idImmobilier=categorieInformation,emailUser=request.user)
            im.save()
            
            dateToday = datetime.today().strftime('%Y-%m-%d')
            notification = Notification(emailAdmin="hajer-hajer@gmail.com",emailMembre=request.user,contenu="We add a new Immobilier and we wait the activation of the admin",dateNotification=str(dateToday))
            notification.save()

            return Response({
                "status" : status.HTTP_200_OK,
                "message": "La annonce du Immobilier "+nameImmobilier+" a été ajoutée avec succées par "+request.user.email+"!!",
                "data": {
                    "nomCategorie":nomCategorie,
                    "nameImmobilier":nameImmobilier,
                    "imageImmobilier":imageImmobilier,
                    "priceImmobilier":priceImmobilier,
                    "dateImmobilier":dateImmobilier,
                    "annoceImmobilier":annoceImmobilier,
                    "villeImmobilier":villeImmobilier
                }
            })
    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte"
        })

class ImmobilierALLtest(generics.ListAPIView):
    queryset =Immobilier.objects.all() 
    serializer_class = ImmobilierSerializer
    pagination_class = largeResultsSetPagination
@api_view(['GET'])
def getImmobilier(request):

    i = Immobilier.objects.all()
    serializer = ImmobilierSerializer(i, many=True)
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Les information de tous les Immobilier",
        "data" :  serializer.data
            })
@api_view(['POST'])
def searchImmobilierByName(request):
    req = request.data
    nameImmobilier = req['nameImmobilier']
    try:
        if request.user.is_staff is True:
            imo = Immobilier.objects.filter(nameImmobilier=nameImmobilier,activationAnnonce=True)
            serializer = ImmobilierSerializer(imo, many=True)
            return Response({
                    "status" : status.HTTP_200_OK,
                    "message": "Les information de l'immobilier "+nameImmobilier+" !!!",
                    "data" :  serializer.data
            })
        else:
            return Response({
                "status" : status.HTTP_404_NOT_FOUND,
                "message": "Vous n'avez pas le droit d'activer se compte",
            })
    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte"
        })

class ImmobilierALLtest(generics.ListAPIView):
    queryset =Immobilier.objects.all() 
    serializer_class = ImmobilierSerializer
    pagination_class = largeResultsSetPagination
#Cette méthode doit trvailler seulement pour le membre
@api_view(['GET'])
def getImmobilierWithActivationOfAdmin(request):
    try:
            imo = Immobilier.objects.filter(activationAnnonce=True)
            serializer = ImmobilierSerializer(imo, many=True)
            return Response({
                    "status" : status.HTTP_200_OK,
                    "message": "Les information de l'immobilier with activation of "+request.user.email+" !!!",
                    "data" :  serializer.data
            })

    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte"
        })

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def activationImmobilierByAdmin(request):
    req = request.data
    nameImmobilier = req['nameImmobilier']

    try:
        if request.user.is_staff is True:
            try:
                nameIm = Immobilier.objects.get(nameImmobilier=str(nameImmobilier))
                Immobilier.objects.filter(nameImmobilier=nameImmobilier).update(activationAnnonce=True)
                return Response({
                    "status" : status.HTTP_200_OK,
                    "message": "Les information de l'immobilier with activation of "+request.user.email+" !!!",
                    "data" :  {
                        "nameImmobilier" : nameImmobilier
                    }
                })
            except:
                return Response({
                "status" : status.HTTP_404_NOT_FOUND,
                "message": "Ce nom immibilier n'existe pas",
                })
        else:
            return Response({
                "status" : status.HTTP_404_NOT_FOUND,
                "message": "Vous n'avez pas le droit d'activer se compte",
            })
    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte",
        })

@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def updateImmobilier(request):
    req = request.data

    nameImmobilier = req['nameImmobilier']
    newnameImmobilier = req['newnameImmobilier']
    imageImmobilier = req['imageImmobilier']
    priceImmobilier = req['priceImmobilier'] # You should send it in base64 format
    dateImmobilier = req['dateImmobilier']
    annoceImmobilier = req['annoceImmobilier']
    villeImmobilier = req['villeImmobilier']

    try:
        im = Immobilier.objects.get(nameImmobilier=nameImmobilier)
        Immobilier.objects.filter(nameImmobilier=nameImmobilier).update(nameImmobilier=newnameImmobilier,imageImmobilier=imageImmobilier,
        priceImmobilier=priceImmobilier,dateImmobilier=dateImmobilier,annoceImmobilier=annoceImmobilier,villeImmobilier=villeImmobilier)

        return Response({
            "status" : status.HTTP_200_OK,
            "message": "Les information de l'immobilier with activation of "+request.user.email+" !!!",
            "data" :  {
                "newnameImmobilier" : newnameImmobilier,
                "imageImmobilier" : imageImmobilier,
                "priceImmobilier" : priceImmobilier,
                "dateImmobilier" : dateImmobilier,
                "annoceImmobilier" : annoceImmobilier,
                "villeImmobilier" : villeImmobilier
                }
            })
    except:
        return Response({
            "status": status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte",
        })

@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def deleteImmobilier(request):
    req = request.data
    nameImmobilier = req['nameImmobilier']
    try:
        if request.user.is_staff is True:
            try:
                im = Immobilier.objects.get(nameImmobilier=nameImmobilier)
                Immobilier.objects.filter(nameImmobilier=nameImmobilier).delete()
                return Response({
                    "status" : status.HTTP_200_OK,
                    "message": "L'immobilier"+ nameImmobilier + " a été supprimée avec succées par "+request.user.email+" !!!",
                    "data" :  {
                        "nameImmobilier" : nameImmobilier
                    }
                })
            except:
                return Response({
                    "status" : status.HTTP_404_NOT_FOUND,
                    "message": "L'immobilier "+nameImmobilier+" n'existe pas vérifier !!!",
                })    
        else:
            return Response({
                "status" : status.HTTP_404_NOT_FOUND,
                "message": "Vous n'avez pas le droit d'activer se compte",
            })
    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte",
        })
class ImmobilierALLtest(generics.ListAPIView):
    queryset =Immobilier.objects.all() 
    serializer_class = ImmobilierSerializer
    pagination_class = largeResultsSetPagination
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getImmobilierInsertWithMembre(request):
    im = Immobilier.objects.filter(emailUser=request.user.id,annoceWNScrappOfAdmin=False)
    serializer = ImmobilierSerializer(im, many=True)

    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Tous les annonces de Immobilier inséerer par membre !!",
        "data" :  serializer.data
    })

class ImmobilierALLtest(generics.ListAPIView):
    queryset =Immobilier.objects.all() 
    serializer_class = ImmobilierSerializer
    pagination_class = largeResultsSetPagination

@api_view(['GET']) 
@permission_classes((IsAuthenticated,))
def getImmobilierWithNotActivationOfAdmin(request):
    try:
        if request.user.is_staff is True:
            imo = Immobilier.objects.filter(activationAnnonce=False)
            serializer = ImmobilierSerializer(imo, many=True)
            return Response({
                "status" : status.HTTP_200_OK,
                "message": "Tous les annonces de Immobilier n'est pas activée par l'admin !!",
                "data" :  serializer.data
            })
        else:
            return Response({
                "status" : status.HTTP_404_NOT_FOUND,
                "message": "Vous n'avez pas le droit d'activer se compte",
            })
    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte",
        })

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getCountOfAnnonceOfImmobilier(request):
    if request.user.is_staff is True:
        im = Immobilier.objects.all().count()
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Tous les annonces de Immobilier dans notre base de données !!",
        "data" : {
            "nb_Immobilier": im
        } 
    })

class ImmobilierALLtest(generics.ListAPIView):
    queryset =Immobilier.objects.all() 
    serializer_class = ImmobilierSerializer
    pagination_class = largeResultsSetPagination
@api_view(['GET'])
def getImmobilierWithoutScrappingMethod(request):
    im = Immobilier.objects.filter(annoceWNScrappOfAdmin=True)
    serializer = ImmobilierSerializer(im, many=True)
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Tous les annonces de Immobilier qui en saisit manuellement sans l'interaction avec le webScrapping !!!",
        "data" : serializer.data
    })
    return Response(serializer.data)

class ImmobilierALLtest(generics.ListAPIView):
    queryset =Immobilier.objects.all() 
    serializer_class = ImmobilierSerializer
    pagination_class = largeResultsSetPagination
@api_view(['GET'])
def getImmobilierWithScrappingMethod(request):
    im = Immobilier.objects.filter(annoceWNScrappOfAdmin=False)
    serializer = ImmobilierSerializer(im, many=True)
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Tous les annonces de Immobilier qui sont insérer avec le webScrapping !!!",
        "data" : serializer.data
    })
    return Response(serializer.data)

############################################# Annonce Emploi Functions #############################################

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def addNewEmploi(request):
    req = request.data
    nomCategorie = req['nomCategorie']
    nameEmploi = req['nameEmploi']
    imageEmploi = req['imageEmploi'] # You should send it in base64 format    
    priceEmploi = req['priceEmploi']
    dateEmploi = req['dateEmploi']
    annoceEmploi = req['annoceEmploi']
    villeEmploi = req['villeEmploi']


    try:
        if request.user.is_staff is True:
            try:
                categorieInformation = Categorie.objects.get(nomCategorie=nomCategorie)
            except:
                categorie = Categorie(nomCategorie=nomCategorie,activationCategorie=True)
                categorie.save()
                categorieInformation = Categorie.objects.get(nomCategorie=nomCategorie)

            e = Emploi(nameEmploi=nameEmploi, imageEmploi=imageEmploi,priceEmploi=priceEmploi,
            dateEmploi=dateEmploi,annoceEmploi=annoceEmploi,villeEmploi=villeEmploi,
            annoceWNScrappOfAdmin=True,activationAnnonce=True,idEmploi=categorieInformation,emailUser=request.user)
            e.save()

            return Response({
                "status" : status.HTTP_200_OK,
                "message": "La annonce du Emploi "+nameEmploi+" a été ajoutée avec succées par "+request.user.email+"!!",
                "data": {
                    "nomCategorie":nomCategorie,
                    "nameEmploi":nameEmploi,
                    "imageEmploi":imageEmploi,
                    "priceEmploi":priceEmploi,
                    "dateEmploi":dateEmploi,
                    "annoceEmploi":annoceEmploi,
                    "villeEmploi":villeEmploi
                }
            })
        else:
            try:
                categorieInformation = Categorie.objects.get(nomCategorie=nomCategorie)
            except:
                categorie = Categorie(nomCategorie=nomCategorie,activationCategorie=True)
                categorie.save()
                categorieInformation = Categorie.objects.get(nomCategorie=nomCategorie)

            e = Emploi(nameEmploi=nameEmploi, imageEmploi=imageEmploi,priceEmploi=priceEmploi,
            dateEmploi=dateEmploi,annoceEmploi=annoceEmploi,villeEmploi=villeEmploi,activationAnnonce=False,
            annoceWNScrappOfAdmin=True,idEmploi=categorieInformation,emailUser=request.user)
            e.save()
            
            dateToday = datetime.today().strftime('%Y-%m-%d')
            notification = Notification(emailAdmin="hajer-hajer@gmail.com",emailMembre=request.user,contenu="We add a new Immobilier and we wait the activation of the admin",dateNotification=str(dateToday))
            notification.save()

            return Response({
                "status" : status.HTTP_200_OK,
                "message": "La annonce du Emploi "+nameEmploi+" a été ajoutée avec succées par "+request.user.email+"!!",
                "data": {
                    "nomCategorie":nomCategorie,
                    "nameEmploi":nameEmploi,
                    "imageEmploi":imageEmploi,
                    "priceEmploi":priceEmploi,
                    "dateEmploi":dateEmploi,
                    "annoceEmploi":annoceEmploi,
                    "villeEmploi":villeEmploi
                }
            })
    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte"
        })

class EmploiALLtest(generics.ListAPIView):
    queryset =Emploi.objects.all() 
    serializer_class = EmploiSerializer
    pagination_class = largeResultsSetPagination
#Cette méthode doit trvailler seulement pour l'administrateur
@api_view(['GET'])
def getEmploi(request):
    e = Emploi.objects.all()
    serializer = EmploiSerializer(e, many=True)
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Les information de tous les empoils",
        "data" :  serializer.data
    })

@api_view(['POST'])
def searchEmploiByName(request):
    req = request.data
    nameEmploi = req['nameEmploi']

    emp = Emploi.objects.filter(nameEmploi=nameEmploi,activationAnnonce=True)
    serializer = EmploiSerializer(emp, many=True)
    return Response({
            "status" : status.HTTP_200_OK,
            "message": "Les information de l'emploi "+nameEmploi+" !!!",
            "data" :  serializer.data
            })



class EmploiALLtest(generics.ListAPIView):
    queryset =Emploi.objects.all() 
    serializer_class = EmploiSerializer
    pagination_class = largeResultsSetPagination
#Cette méthode doit trvailler seulement pour le membre
@api_view(['GET'])
def getEmploiWithActivationOfAdmin(request):
    emp = Emploi.objects.filter(activationAnnonce=True)
    serializer = EmploiSerializer(emp, many=True)
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Les information de l'immobilier with activation of ",
        "data" :  serializer.data
    })

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def activationEmploiByAdmin(request):
    req = request.data
    nameEmploi = req['nameEmploi']

    try:
        if request.user.is_staff is True:
            try:
                Emploi.objects.get(nameEmploi=str(nameEmploi))
                Emploi.objects.filter(nameEmploi=nameEmploi).update(activationAnnonce=True)
                return Response({
                    "status" : status.HTTP_200_OK,
                    "message": "Les information de l'emploi with activation of "+request.user.email+" !!!",
                    "data" :  {
                        "nameEmploi" : nameEmploi
                    }
                })
            except:
                return Response({
                "status" : status.HTTP_404_NOT_FOUND,
                "message": "Ce nom emploie n'existe pas",
            })
        else:
            return Response({
                "status" : status.HTTP_404_NOT_FOUND,
                "message": "Vous n'avez pas le droit d'activer se compte",
            })
    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte",
        })

@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def updateEmploi(request):
    req = request.data
    nameEmploi = req['nameEmploi']
    newnameEmploi = req['newnameEmploi']
    imageEmploi = req['imageEmploi'] # You should send it in base64 format    
    priceEmploi = req['priceEmploi']
    dateEmploi = req['dateEmploi']
    annoceEmploi = req['annoceEmploi']
    villeEmploi = req['villeEmploi']

    try:
        em = Emploi.objects.get(nameEmploi=nameEmploi)
        Emploi.objects.filter(nameEmploi=newnameEmploi).update(nameEmploi=nameEmploi,imageEmploi=imageEmploi,
        priceEmploi=priceEmploi,dateEmploi=dateEmploi,annoceEmploi=annoceEmploi,villeEmploi=villeEmploi)

        return Response({
            "status" : status.HTTP_200_OK,
            "message": "Les information de l'immobilier with activation of "+request.user.email+" !!!",
            "data" :  {
                "newnameEmploi" : newnameEmploi,
                "imageEmploi" : imageEmploi,
                "priceEmploi" : priceEmploi,
                "dateEmploi" : dateEmploi,
                "annoceEmploi" : annoceEmploi,
                "villeEmploi" : villeEmploi
                }
            })
    except:
        return Response({
            "status": status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte",
        })

@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def deleteEmploi(request):
    req = request.data
    nameEmploi = req['nameEmploi']

    try:
        if request.user.is_staff is True:
            try:
                em = Emploi.objects.get(nameEmploi=nameEmploi)
                Emploi.objects.filter(nameEmploi=nameEmploi).delete()
                return Response({
                    "status" : status.HTTP_200_OK,
                    "message": "L'emploie "+ nameEmploi + " a été supprimée avec succées par "+request.user.email+" !!!",
                    "data" :  {
                        "nameEmploi" : nameEmploi
                    }
                })
            except:
                return Response({
                    "status" : status.HTTP_404_NOT_FOUND,
                    "message": "L'emploie "+nameEmploi+" n'existe pas vérifier !!!",
                })    
        else:
            return Response({
                "status" : status.HTTP_404_NOT_FOUND,
                "message": "Vous n'avez pas le droit d'activer se compte",
            })
    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte",
        })

class EmploiALLtest(generics.ListAPIView):
    queryset =Emploi.objects.all() 
    serializer_class = EmploiSerializer
    pagination_class = largeResultsSetPagination
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getEmploieInsertWithMembre(request):
    em = Emploi.objects.filter(emailUser=request.user.id)
    serializer = EmploiSerializer(em, many=True)
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Tous les annonces de emploie inséerer par membre !!",
        "data" :  serializer.data
    })

class EmploiALLtest(generics.ListAPIView):
    queryset =Emploi.objects.all() 
    serializer_class = EmploiSerializer
    pagination_class = largeResultsSetPagination
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getEmploiWithNotActivationOfAdmin(request):
    try:
        if request.user.is_staff is True:
            emp = Emploi.objects.filter(activationAnnonce=False)
            serializer = EmploiSerializer(emp, many=True)
            return Response({
                "status" : status.HTTP_200_OK,
                "message": "Tous les annonces de emploie n'est pas activée par l'admin !!",
                "data" :  serializer.data
            })
        else:
            return Response({
                "status" : status.HTTP_404_NOT_FOUND,
                "message": "Vous n'avez pas le droit d'activer se compte",
            })
    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte",
        })

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getCountOfAnnonceOfEmploi(request):
    if request.user.is_staff is True:
        em = Emploi.objects.all().count()
        return Response({
            "status" : status.HTTP_200_OK,
            "message": "Tous les annonces de emploie dans notre base de données !!",
            "data" : {
            "nb_Emploi": em
        } 
    })

class EmploiALLtest(generics.ListAPIView):
    queryset =Emploi.objects.all() 
    serializer_class = EmploiSerializer
    pagination_class = largeResultsSetPagination
@api_view(['GET'])
def getEmploiWithoutScrappingMethod(request):
    em = Emploi.objects.filter(annoceWNScrappOfAdmin=True)
    serializer = EmploiSerializer(em, many=True)
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Tous les annonces de emploie qui en saisit manuellement sans l'interaction avec le webScrapping !!!",
        "data" : serializer.data
    })
    return Response(serializer.data)

class EmploiALLtest(generics.ListAPIView):
    queryset =Emploi.objects.all() 
    serializer_class = EmploiSerializer
    pagination_class = largeResultsSetPagination
@api_view(['GET'])
def getEmploiWithScrappingMethod(request):
    em = Emploi.objects.filter(annoceWNScrappOfAdmin=False)
    serializer = EmploiSerializer(em, many=True)
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Tous les annonces de Immobilier qui sont insérer avec le webScrapping !!!",
        "data" : serializer.data
    })
    return Response(serializer.data)

############################################# Annonce Materielle Informatique Functions #############################################
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def addNewMaterielleInformatique(request):
    req = request.data
    nomCategorie = req['nomCategorie']
    nameMatrInformatique = req['nameMatrInformatique']
    imageMatrInformatique = req['imageMatrInformatique'] # You should send it in base64 format    
    priceMatrInformatique = req['priceMatrInformatique']
    dateMatrInformatique = req['dateMatrInformatique']
    annoceMatrInformatique = req['annoceMatrInformatique']
    villeMatrInformatique = req['villeMatrInformatique']
    try:
        if request.user.is_staff is True:
            try:
                categorieInformation = Categorie.objects.get(nomCategorie=nomCategorie)
            except:
                categorie = Categorie(nomCategorie=nomCategorie,activationCategorie=True)
                categorie.save()
                categorieInformation = Categorie.objects.get(nomCategorie=nomCategorie)
            mI = MaterielleInformatique(nameMatrInformatique=nameMatrInformatique, imageMatrInformatique=imageMatrInformatique,
            priceMatrInformatique=priceMatrInformatique,dateMatrInformatique=dateMatrInformatique,
            annoceMatrInformatique=annoceMatrInformatique,villeMatrInformatique=villeMatrInformatique,
            annoceWNScrappOfAdmin=True,activationAnnonce=True,idMaterielleInformatique=categorieInformation,
            emailUser=request.user)
            mI.save()
            return Response({
                "status" : status.HTTP_200_OK,
                "message": "La annonce du materielle informatique "+nameMatrInformatique+" a été ajoutée avec succées par "+request.user.email+"!!",
                "data": {
                    "nomCategorie":nomCategorie,
                    "nameMatrInformatique":nameMatrInformatique,
                    "imageMatrInformatique":imageMatrInformatique,
                    "priceMatrInformatique":priceMatrInformatique,
                    "dateMatrInformatique":dateMatrInformatique,
                    "annoceMatrInformatique":annoceMatrInformatique,
                    "villeMatrInformatique":villeMatrInformatique
                }
            })
        else:
            print('eeeeeee')
            try:
                categorieInformation = Categorie.objects.get(nomCategorie=nomCategorie)
            except:
                categorie = Categorie(nomCategorie=nomCategorie,activationCategorie=True)
                categorie.save()
                categorieInformation = Categorie.objects.get(nomCategorie=nomCategorie)
            
            mI = MaterielleInformatique(nameMatrInformatique=nameMatrInformatique, imageMatrInformatique=imageMatrInformatique,
            priceMatrInformatique=priceMatrInformatique,dateMatrInformatique=dateMatrInformatique,
            annoceMatrInformatique=annoceMatrInformatique,villeMatrInformatique=villeMatrInformatique,activationAnnonce=False,
            idMaterielleInformatique=categorieInformation,emailUser=request.user)
            mI.save()
            
            dateToday = datetime.today().strftime('%Y-%m-%d')
            notification = Notification(emailAdmin="hajer-hajer@gmail.com",emailMembre=request.user.email,contenu="We add a new MatrInformatique and we wait the activation of the admin",dateNotification=str(dateToday))
            notification.save()
            
            return Response({
                "status" : status.HTTP_200_OK,
                "message": "La annonce du materielle informatique "+nameMatrInformatique+" a été ajoutée avec succées par "+request.user.email+"!!",
                "data": {
                    "nomCategorie":nomCategorie,
                    "nameMatrInformatique":nameMatrInformatique,
                    "imageMatrInformatique":imageMatrInformatique,
                    "priceMatrInformatique":priceMatrInformatique,
                    "dateMatrInformatique":dateMatrInformatique,
                    "annoceMatrInformatique":annoceMatrInformatique,
                    "villeMatrInformatique":villeMatrInformatique
                }
            })

    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte",
        })

class MaterielleInformatiqueALLtest(generics.ListAPIView):
    queryset =MaterielleInformatique.objects.all() 
    serializer_class = MaterielleInformatiqueSerializer
    pagination_class = largeResultsSetPagination
@api_view(['GET'])
def getMaterielleInformatique(request):
    mI = MaterielleInformatique.objects.all()
    serializer = MaterielleInformatiqueSerializer(mI, many=True)
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Les information de tous les materielles informatiques",
        "data" :  serializer.data
        })
@api_view(['POST'])
def searchMaterielleInformatiqueByName(request):
    req = request.data
    nameMatrInformatique = req['nameMatrInformatique']
    mI = MaterielleInformatique.objects.filter(nameMatrInformatique=nameMatrInformatique)
    serializer = MaterielleInformatiqueSerializer(mI, many=True)
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Les information de materielle informatique "+nameMatrInformatique+" !!!",
        "data" :  serializer.data
         })

class MaterielleInformatiqueALLtest(generics.ListAPIView):
    queryset =MaterielleInformatique.objects.all() 
    serializer_class = MaterielleInformatiqueSerializer
    pagination_class = largeResultsSetPagination

@api_view(['GET'])
def getMaterielleInformatiqueWithActivationOfAdmin(request):
    matInfo = MaterielleInformatique.objects.filter(activationAnnonce=True)
    serializer = MaterielleInformatiqueSerializer(matInfo, many=True)
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Les information de materielle informatique with activation of !!!",
        "data" :  serializer.data
        })

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def activationMaterielleInformatiqueByAdmin(request):
    req = request.data
    nameMatrInformatique = req['nameMatrInformatique']

    try:
        if request.user.is_staff is True:
            try:
                MaterielleInformatique.objects.get(nameMatrInformatique=str(nameMatrInformatique))
                MaterielleInformatique.objects.filter(nameMatrInformatique=nameMatrInformatique).update(activationAnnonce=True)
                return Response({
                    "status" : status.HTTP_200_OK,
                    "message": "Les information de materielle informatique with activation of "+request.user.email+" !!!",
                    "data" :  {
                        "nameMatrInformatique" : nameMatrInformatique
                    }
                })
            except:
                return Response({
                "status" : status.HTTP_404_NOT_FOUND,
                "message": "Ce MatrInformatique n'existe pas",
            })
        else:
            return Response({
                "status" : status.HTTP_404_NOT_FOUND,
                "message": "Vous n'avez pas le droit d'activer se compte",
            })
    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte",
        })
        #if(emailUser=="hajer-hajer@gmail.com"):
         #   MaterielleInformatique.objects.filter(nameMatrInformatique=nameMatrInformatique).update(activationAnnonce=True)
        #else:
        #    return Response("This activation cannot be only with admin account")

    return Response("Your Voiture Occasion is activate")


@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def updateMatrInformatique(request):
    req = request.data

    nameMatrInformatique = req['nameMatrInformatique']
    newNameMatrInformatique = req['newNameMatrInformatique']
    imageMatrInformatique = req['imageMatrInformatique'] # You should send it in base64 format    
    priceMatrInformatique = req['priceMatrInformatique']
    dateMatrInformatique = req['dateMatrInformatique']
    annoceMatrInformatique = req['annoceMatrInformatique']
    villeMatrInformatique = req['villeMatrInformatique']

    try:
        mI = MaterielleInformatique.objects.get(nameMatrInformatique=nameMatrInformatique)
        MaterielleInformatique.objects.filter(nameMatrInformatique=nameMatrInformatique).update(nameMatrInformatique=newNameMatrInformatique,imageMatrInformatique=imageMatrInformatique,
        priceMatrInformatique=priceMatrInformatique,dateMatrInformatique=dateMatrInformatique,annoceMatrInformatique=annoceMatrInformatique,villeMatrInformatique=villeMatrInformatique)

        return Response({
            "status" : status.HTTP_200_OK,
            "message": "Les information de materielle informatique with activation of "+request.user.email+" !!!",
            "data" :  {
                "newNameMatrInformatique" : newNameMatrInformatique,
                "imageMatrInformatique" : imageMatrInformatique,
                "priceMatrInformatique" : priceMatrInformatique,
                "dateMatrInformatique" : dateMatrInformatique,
                "annoceMatrInformatique" : annoceMatrInformatique,
                "villeMatrInformatique" : villeMatrInformatique
                }
            })
    except Exception as e:
        print(e)
        return Response({
            "status": status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte",
        })

@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def deleteMatrInformatique(request):
    req = request.data
    nameMatrInformatique = req['nameMatrInformatique']

    try:
        if request.user.is_staff is True:
            try:
                mI = MaterielleInformatique.objects.get(nameMatrInformatique=nameMatrInformatique)
                MaterielleInformatique.objects.filter(nameMatrInformatique=nameMatrInformatique).delete()
                return Response({
                    "status" : status.HTTP_200_OK,
                    "message": "Le materielle informatique "+ nameMatrInformatique + " a été supprimée avec succées par "+request.user.email+" !!!",
                    "data" :  {
                        "nameMatrInformatique" : nameMatrInformatique
                    }
                })
            except:
                return Response({
                    "status" : status.HTTP_404_NOT_FOUND,
                    "message": "Le materielle informatique "+nameMatrInformatique+" n'existe pas vérifier !!!",
                })    
        else:
            return Response({
                "status" : status.HTTP_404_NOT_FOUND,
                "message": "Vous n'avez pas le droit d'activer se compte",
            })
    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte",
        })

class MaterielleInformatiqueALLtest(generics.ListAPIView):
    queryset =MaterielleInformatique.objects.all() 
    serializer_class = MaterielleInformatiqueSerializer
    pagination_class = largeResultsSetPagination
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getMaterielleInformatiqueWithNOTActivationOfAdmin(request):
    
    try:
        if request.user.is_staff is True:
            matInfo = MaterielleInformatique.objects.filter(activationAnnonce=False)
            serializer = MaterielleInformatiqueSerializer(matInfo, many=True)
            return Response({
                "status" : status.HTTP_200_OK,
                "message": "Tous les annonces de materielle informatique n'est pas activée par l'admin !!",
                "data" :  serializer.data
            })
        else:
            return Response({
                "status" : status.HTTP_404_NOT_FOUND,
                "message": "Vous n'avez pas le droit d'activer se compte",
            })
    except:
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous n'avez pas le droit d'activer se compte",
        })

class MaterielleInformatiqueALLtest(generics.ListAPIView):
    queryset =MaterielleInformatique.objects.all() 
    serializer_class = MaterielleInformatiqueSerializer
    pagination_class = largeResultsSetPagination
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getMaterielleInformatiqueInsertWithMembre(request):
    mi = MaterielleInformatique.objects.filter(emailUser=request.user)
    serializer = MaterielleInformatiqueSerializer(mi, many=True)
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Tous les materielle informatique inséerer par membre !!",
        "data" :  serializer.data
    })

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getCountOfAnnonceOfMaterielleInformatique(request):
    if request.user.is_staff is True:
        mI = MaterielleInformatique.objects.all().count()
        return Response({
            "status" : status.HTTP_200_OK,
            "message": "Tous les annonces de materielle informatique dans notre base de données !!",
            "data" : {
                "nb_MaterielleInformatique": mI
            } 
        })
class MaterielleInformatiqueALLtest(generics.ListAPIView):
    queryset =MaterielleInformatique.objects.all() 
    serializer_class = MaterielleInformatiqueSerializer
    pagination_class = largeResultsSetPagination
@api_view(['GET'])
def getMaterielleInformatiqueWithoutScrappingMethod(request):
    mi = MaterielleInformatique.objects.filter(annoceWNScrappOfAdmin=True)
    serializer = MaterielleInformatiqueSerializer(mi, many=True)
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Tous les annonces de materielle informatique qui en saisit manuellement sans l'interaction avec le webScrapping !!!",
        "data" : serializer.data
    })
    return Response(serializer.data)

class MaterielleInformatiqueALLtest(generics.ListAPIView):
    queryset =MaterielleInformatique.objects.all() 
    serializer_class = MaterielleInformatiqueSerializer
    pagination_class = largeResultsSetPagination
@api_view(['GET'])
def getMaterielleInformatiqueWithScrappingMethod(request):
    mi = MaterielleInformatique.objects.filter(annoceWNScrappOfAdmin=False)
    serializer = MaterielleInformatiqueSerializer(mi, many=True)
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Tous les annonces de materielle informatique qui en saisit manuellement sans l'interaction avec le webScrapping !!!",
        "data" : serializer.data
    })
    return Response(serializer.data)

############################################# Notifications #############################################
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getNotifications(request):
    if request.user.is_staff is True:
        notification = Notification.objects.filter()
        serializer = NotificationSerializer(notification, many=True)
    
    return Response({
        "status" : status.HTTP_200_OK,
        "message": "Tous les notifications de l'application!!!",
        "data" : serializer.data
    })
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getNotificationWithMemebre(request):
    notifList = []
    try:
        notif = Notification.objects.filter(emailMembre==request.user.email)
        for no in notif:
            notifList.append({
                "Email_Membre": no.emailMembre,
                "Contenu": no.contenu,
                "Date_Notification": no.dateNotification
            })
        return Response({
            "status" : status.HTTP_200_OK,
            "message": "Ceci la liste des notifications  "+request.user.email+"!!!",
            "data": notifList
        })
    except  Exception as e:
        print(e)
        return Response({
            "status" : status.HTTP_404_NOT_FOUND,
            "message": "Vous avez une erreur svp vérifier bien",
        })


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getCountOfAnnonceOfDB(request):
    if request.user.is_staff is True:
        vn = VoitureNeuf.objects.all().count()
        vo = VoitureOccasion.objects.all().count()
        im = Immobilier.objects.all().count()
        em = Emploi.objects.all().count()
        mI = MaterielleInformatique.objects.all().count()
        return Response({
            "status" : status.HTTP_200_OK,
            "message": "Le nombre totale d'annonce de different catégories!!!",
            "data": {
                "nb_NewCar": vn,
                "nb_VoitureOccasion":vo,
                "nb_Immobilier": im,
                "nb_Emploi": em,
                "nb_MaterielleInformatique": mI
        }
    })
