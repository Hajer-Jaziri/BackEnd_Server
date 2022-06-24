from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from .views import VoitureALLtest, VoitureNeufALLtest, VoitureOccasionALLtest, ImmobilierALLtest, EmploiALLtest,MaterielleInformatiqueALLtest
urlpatterns = [
    
    ####################### Methods when we use the scraping algorithms ########################
    # path('addMarque/', views.addMarque),
    # path('addVoitureNeuf/', views.addVoitureNeuf),
    # path('addConcessionnaires/', views.addConcessionnaires),
    # path('addVoitureOccasion/', views.addVoitureOccasion),
    # path('addVendeurPro/', views.addVendeurPro),
    # path('addImmobilier/', views.addImmobilier),
    # path('addEmploi/', views.addEmploi),
    # path('addEmploiFromOffreEmploi/',views.addEmploiFromOffreEmploi),
    # path('addMaterielleInformatique/',views.addMaterielleInformatique),

    
    ######################## Methods when we make some action for an user or admin ########################
    path('registerUser/',views.registerUser, name="Register_User"),
    path('loginUser/',obtain_auth_token),
    path('activationAccount/',views.activationAccount, name="Activivation_Account"), #cette fonction utilisée seulement par l'admin parce que il est le controleur de l'application
    path('updateUser/',views.updateUser, name="Update_User"), #cette fonction utilisée seulement par l'admin ou le memebre
    path('getListOfUser/',views.getListOfUser, name="La_Liste_de_User_Pour_Admin"), #cette fonction utilisée seulement par l'admin parce que il est le controleur de l'application
    path('getListOfUserNotActivate/',views.getListOfUserNotActivate, name="La_List_de_User_Non_Activaté"),#cette fonction utilisée seulement par l'admin parce que il est le controleur de l'application
    path('getListOfMembre/',views.getListOfMembre, name="La_Liste_Of_Membre"),#cette fonction utilisée seulement par l'admin parce que il est le controleur de l'application
    path('deleteUserUsingAdmin/',views.deleteUserUsingAdmin, name="Delete_User_Using_Admin"),#cette fonction utilisée seulement par l'admin
    path('searchUser/',views.searchUser, name="Search_User_By_Email"),

    ######################### Methods when we make some action for categories ########################
    path('addCategorieUsingAdmin/',views.addCategorieUsingAdmin),
    path('getCategorie/',views.getCategorie), #C'est une fonction seulement l'admin peut l'acceder
    path('updateCategorie/',views.updateCategorie), #C'est une fonction seulement l'admin peut l'acceder
    path('deleteCategorie/',views.deleteCategorie), #C'est une fonction seulement l'admin peut l'acceder
    path('activationCategorieByAdmin/',views.activationCategorieByAdmin), #C'est une fonction seulement l'admin peut l'acceder
    path('getonlyActivationCategorie/',views.getonlyActivationCategorie),

    ######################### Methods when we make some action for annonce cars ########################

    path('addNewMarque/',views.addNewMarque),
    path('getMarque/', views.getMarque),#C'est une fonction seulement l'admin peut l'acceder
    path('searchMarqueByName/',views.searchMarqueByName),#C'est une fonction seulement l'admin peut l'acceder
    path('updateMarque/',views.updateMarque),#C'est une fonction seulement l'admin peut l'acceder
    path('deleteMarque/',views.deleteMarque),#C'est une fonction seulement l'admin peut l'acceder
    path('getCountOfMarque/',views.getCountOfMarque),#C'est une fonction seulement l'admin peut l'acceder


    path('getAnnonceVoiture/', VoitureALLtest.as_view()),
    path('addNewCar/',views.addNewCar),
    path('getVoitureNeuf/', VoitureNeufALLtest.as_view()),
    path('searchCarsNewByName/', views.searchCarsNewByName),
    path('getVoitureNeufWithActivationOfAdmin/',VoitureNeufALLtest.as_view()),
    path('getVoitureNeufNotactivationOfAdmin/',VoitureNeufALLtest.as_view()),
    path('activationVoitureNeufByAdmin/',views.activationVoitureNeufByAdmin),
    path('updateNewCar/', views.updateNewCar),
    path('deleteNewCar/', views.deleteNewCar),
    path('getVoitureNeufInsertWithMembre/',VoitureNeufALLtest.as_view()),
    path('getCountOfAnnonceOfNewCar/',views.getCountOfAnnonceOfNewCar),
    path('getVoitureNeufWithoutScrappingMethod/',VoitureNeufALLtest.as_view()),
    path('getAllVoitureNeufByMarque/',views.getAllVoitureNeufByMarque),
    
    path('addOccasionCar/',views.addOccasionCar),
    path('getVoitureOccasion/', VoitureOccasionALLtest.as_view()),
    path('getVoitureOccasionWithActivationOfAdmin/',VoitureOccasionALLtest.as_view()),
    path('searchCarsOccasionByName/', views.searchCarsOccasionByName),
    path('activationVoitureOccasionByAdmin/',VoitureOccasionALLtest.as_view()),
    path('updateOccasionCar/',views.updateOccasionCar),
    path('deleteOccasionCar/', views.deleteOccasionCar),
    path('getVoitureOccasionInsertWithMembre/',views.VoitureOccasionALLtest.as_view()),
    path('getVoitureoccasionNotactivationOfAdmin/',views.VoitureOccasionALLtest.as_view()),
    path('getVoitureOccasionWithoutScrappingMethod/',views.VoitureOccasionALLtest.as_view()),
    path('getCountOfAnnonceOfOccasionCar/',views.getCountOfAnnonceOfOccasionCar),
    path('getAllVoitureOccasionByMarque/',views.getAllVoitureOccasionByMarque),

    ######################## Methods when we make some action for annonce Immobilier ########################
    path('addNewImmobilier/',views.addNewImmobilier),
    path('getImmobilier/', ImmobilierALLtest.as_view()), #Cette méthode doit trvailler seulement pour l'administrateur
    path('searchImmobilierByName/',views.searchImmobilierByName), #Cette méthode doit trvailler seulement pour l'administrateur
    path('getImmobilierWithActivationOfAdmin/',ImmobilierALLtest.as_view()),#Cette méthode doit trvailler seulement pour l'administrateur
    path('activationImmobilierByAdmin/',views.activationImmobilierByAdmin),#Cette méthode doit trvailler seulement pour l'administrateur
    path('updateImmobilier/',views.updateImmobilier),
    path('deleteImmobilier/',views.deleteImmobilier),
    path('getImmobilierInsertWithMembre/',ImmobilierALLtest.as_view()),
    path('getImmobilierWithNotActivationOfAdmin/',ImmobilierALLtest.as_view()),
    path('getCountOfAnnonceOfImmobilier/',views.getCountOfAnnonceOfImmobilier),
    path('getImmobilierWithoutScrappingMethod/',ImmobilierALLtest.as_view()),
    path('getImmobilierWithScrappingMethod/',views.ImmobilierALLtest.as_view()),

    ######################## Methods when we make some action for annonce Emploi ########################
    path('addNewEmploi/', views.addNewEmploi),
    path('getEmploi/', EmploiALLtest.as_view()),
    path('searchEmploiByName/',views.searchEmploiByName),
    path('getEmploiWithActivationOfAdmin/',EmploiALLtest.as_view()),
    path('activationEmploiByAdmin/',views.activationEmploiByAdmin),
    path('updateEmploi/',views.updateEmploi),
    path('deleteEmploi/',views.deleteEmploi),
    path('getEmploieInsertWithMembre/',views.EmploiALLtest.as_view()),
    path('getEmploiWithNotActivationOfAdmin/',views.EmploiALLtest.as_view()),
    path('getCountOfAnnonceOfEmploi/',views.getCountOfAnnonceOfEmploi),
    path('getEmploiWithoutScrappingMethod/',EmploiALLtest.as_view()),
    path('getEmploiWithScrappingMethod/',EmploiALLtest.as_view()),

    ######################## Methods when we make some action for annonce Materielle Informatique ########################
    path('addNewMaterielleInformatique/',views.addNewMaterielleInformatique),
    path('getMaterielleInformatique/',MaterielleInformatiqueALLtest.as_view()),
    path('searchMaterielleInformatiqueByName/',views.searchMaterielleInformatiqueByName),
    path('getMaterielleInformatiqueWithActivationOfAdmin/',MaterielleInformatiqueALLtest.as_view()),
    path('activationMaterielleInformatiqueByAdmin/', views.activationMaterielleInformatiqueByAdmin),
    path('updateMatrInformatique/',views.updateMatrInformatique),
    path('deleteMatrInformatique/',views.deleteMatrInformatique),
    path('getMaterielleInformatiqueInsertWithMembre/',MaterielleInformatiqueALLtest.as_view()),
    path('getMaterielleInformatiqueWithNOTActivationOfAdmin/',MaterielleInformatiqueALLtest.as_view()),
    path('getCountOfAnnonceOfMaterielleInformatique/',views.getCountOfAnnonceOfMaterielleInformatique),
    path('getMaterielleInformatiqueWithoutScrappingMethod/',MaterielleInformatiqueALLtest.as_view()),
    path('getMaterielleInformatiqueWithScrappingMethod/',MaterielleInformatiqueALLtest.as_view()),
    
    
    ######################## Methods when we make some action for Notifications and all the annonce ########################
    path('getNotifications/',views.getNotifications),
    path('getNotificationWithMemebre/',views.getNotificationWithMemebre),

    path('getCountOfAnnonceOfDB/',views.getCountOfAnnonceOfDB)

]
