from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


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

    path('getAnnonceVoiture/', views.getAnnonceVoiture),
    
    path('addNewCar/',views.addNewCar),
    path('getVoitureNeuf/', views.getVoitureNeuf),
    path('searchCarsNewByName/', views.searchCarsNewByName),
    path('getVoitureNeufWithActivationOfAdmin/',views.getVoitureNeufWithActivationOfAdmin),
    path('getVoitureNeufNotactivationOfAdmin/',views.getVoitureNeufNotactivationOfAdmin),
    path('activationVoitureNeufByAdmin/',views.activationVoitureNeufByAdmin),
    path('updateNewCar/', views.updateNewCar),
    path('deleteNewCar/', views.deleteNewCar),
    path('getVoitureNeufInsertWithMembre/',views.getVoitureNeufInsertWithMembre),
    path('getCountOfAnnonceOfNewCar/',views.getCountOfAnnonceOfNewCar),
    path('getVoitureNeufWithoutScrappingMethod/',views.getVoitureNeufWithoutScrappingMethod),
    path('getAllVoitureNeufByMarque/',views.getAllVoitureNeufByMarque),

    path('addOccasionCar/',views.addOccasionCar),
    path('getVoitureOccasion/', views.getVoitureOccasion),
    path('getVoitureOccasionWithActivationOfAdmin/',views.getVoitureOccasionWithActivationOfAdmin),
    path('searchCarsOccasionByName/', views.searchCarsOccasionByName),
    path('activationVoitureOccasionByAdmin/',views.activationVoitureOccasionByAdmin),
    path('updateOccasionCar/',views.updateOccasionCar),
    path('deleteOccasionCar/', views.deleteOccasionCar),
    path('getVoitureOccasionInsertWithMembre/',views.getVoitureOccasionInsertWithMembre),
    path('getVoitureoccasionNotactivationOfAdmin/',views.getVoitureoccasionNotactivationOfAdmin),
    path('getVoitureOccasionWithoutScrappingMethod/',views.getVoitureOccasionWithoutScrappingMethod),
    path('getCountOfAnnonceOfOccasionCar/',views.getCountOfAnnonceOfOccasionCar),
    path('getAllVoitureOccasionByMarque/',views.getAllVoitureOccasionByMarque),

    ######################## Methods when we make some action for annonce Immobilier ########################
    path('addNewImmobilier/',views.addNewImmobilier),
    path('getImmobilier/', views.getImmobilier), #Cette méthode doit trvailler seulement pour l'administrateur
    path('searchImmobilierByName/',views.searchImmobilierByName), #Cette méthode doit trvailler seulement pour l'administrateur
    path('getImmobilierWithActivationOfAdmin/',views.getImmobilierWithActivationOfAdmin),#Cette méthode doit trvailler seulement pour l'administrateur
    path('activationImmobilierByAdmin/',views.activationImmobilierByAdmin),#Cette méthode doit trvailler seulement pour l'administrateur
    path('updateImmobilier/',views.updateImmobilier),
    path('deleteImmobilier/',views.deleteImmobilier),
    path('getImmobilierInsertWithMembre/',views.getImmobilierInsertWithMembre),
    path('getImmobilierWithNotActivationOfAdmin/',views.getImmobilierWithNotActivationOfAdmin),
    path('getCountOfAnnonceOfImmobilier/',views.getCountOfAnnonceOfImmobilier),
    path('getImmobilierWithoutScrappingMethod/',views.getImmobilierWithoutScrappingMethod),
    path('getImmobilierWithScrappingMethod/',views.getImmobilierWithScrappingMethod),

    ######################## Methods when we make some action for annonce Emploi ########################
    path('addNewEmploi/', views.addNewEmploi),
    path('getEmploi/', views.getEmploi),
    path('searchEmploiByName/',views.searchEmploiByName),
    path('getEmploiWithActivationOfAdmin/',views.getEmploiWithActivationOfAdmin),
    path('activationEmploiByAdmin/',views.activationEmploiByAdmin),
    path('updateEmploi/',views.updateEmploi),
    path('deleteEmploi/',views.deleteEmploi),
    path('getEmploieInsertWithMembre/',views.getEmploieInsertWithMembre),
    path('getEmploiWithNotActivationOfAdmin/',views.getEmploiWithNotActivationOfAdmin),
    path('getCountOfAnnonceOfEmploi/',views.getCountOfAnnonceOfEmploi),
    path('getEmploiWithoutScrappingMethod/',views.getEmploiWithoutScrappingMethod),
    path('getEmploiWithScrappingMethod/', views.getEmploiWithScrappingMethod),

    ######################## Methods when we make some action for annonce Materielle Informatique ########################
    path('addNewMaterielleInformatique/',views.addNewMaterielleInformatique),
    path('getMaterielleInformatique/',views.getMaterielleInformatique),
    path('searchMaterielleInformatiqueByName/',views.searchMaterielleInformatiqueByName),
    path('getMaterielleInformatiqueWithActivationOfAdmin/',views.getMaterielleInformatiqueWithActivationOfAdmin),
    path('activationMaterielleInformatiqueByAdmin/', views.activationMaterielleInformatiqueByAdmin),
    path('updateMatrInformatique/',views.updateMatrInformatique),
    path('deleteMatrInformatique/',views.deleteMatrInformatique),
    path('getMaterielleInformatiqueInsertWithMembre/',views.getMaterielleInformatiqueInsertWithMembre),
    path('getMaterielleInformatiqueWithNOTActivationOfAdmin/',views.getMaterielleInformatiqueWithNOTActivationOfAdmin),
    path('getCountOfAnnonceOfMaterielleInformatique/',views.getCountOfAnnonceOfMaterielleInformatique),
    path('getMaterielleInformatiqueWithoutScrappingMethod/',views.getMaterielleInformatiqueWithoutScrappingMethod),
    path('getMaterielleInformatiqueWithScrappingMethod/',views.getMaterielleInformatiqueWithScrappingMethod),
    
    ######################## Methods when we make some action for Notifications and all the annonce ########################
    path('getNotifications/',views.getNotifications),
    path('getCountOfAnnonceOfDB/',views.getCountOfAnnonceOfDB)

]
