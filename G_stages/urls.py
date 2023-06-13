

from os import path
from . import views
from . import views 
from django.urls import path  
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import creer_groupe, autocomplete_etudiants
urlpatterns = [
    path('', views.login, name='login'),
    path('index', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
   


   # dep
    path('dep/<int:pk>/update/', views.depUpdateView.as_view(), name='dep_update'),
    path('dep/<int:pk>/delete/', views.depDeleteView.as_view(), name='delete_dep'),
    path('dep/', views.dep, name='dep'),
    path('create_dep/', views.depCreateView.as_view(), name='create_dep'),


    # entre
    path('entre/<int:pk>/update/', views.entreUpdateView.as_view(), name='entre_update'),
    path('entre/<int:pk>/delete/', views.entreDeleteView.as_view(), name='delete_entre'),
    path('entre/', views.entre, name='entre'),
    path('create_entre/', views.entreCreateView.as_view(), name='create_entre'),

    
    path('et/', views.et, name='et'),
    path('add_etudiant/', views.add_etudiant, name='add_etudiant'),
    # etud
    path('etud/<int:pk>/update/', views.etudUpdateView.as_view(), name='etud_update'),
    path('etud/<int:pk>/delete/', views.etudDeleteView.as_view(), name='delete_etud'),
    path('etud/', views.etud, name='etud'),
    path('createetud/', views.etudCreateView.as_view(), name='create_etud'),

     path('encours/', views.encours, name='encours'),



    
   # Type_Encadrant
    path('Type_Encadrant/<int:pk>/update/', views.Type_EncadrantUpdateView.as_view(), name='Type_Encadrant_update'),
    path('Type_Encadrant/<int:pk>/delete/', views.Type_EncadrantDeleteView.as_view(), name='delete_Type_Encadrant'),
    path('type_Encadrant/', views.type_Encadrant, name='type_Encadrant'),
    path('create_Type_Encadrant/', views.Type_EncadrantCreateView.as_view(), name='create_Type_Encadrant'),


    
   # Type_stage
    path('type_stage/<int:pk>/update/', views.type_stageUpdateView.as_view(), name='type_stage_update'),
    path('type_stage/<int:pk>/delete/', views.type_stageDeleteView.as_view(), name='delete_type_stage'),
    path('type_stage/', views.type_stage, name='type_stage'),
    path('create_type_stage/', views.type_stageCreateView.as_view(), name='create_type_stage'),

     #Simester
    path('simester/<int:pk>/update/', views.simesterUpdateView.as_view(), name='simester_update'),
    path('simester/<int:pk>/delete/', views.simesterDeleteView.as_view(), name='delete_simester'),
    path('simester/', views.simester, name='simester'),
    path('create_simester/', views.simesterCreateView.as_view(), name='create_simester'),


    # encadrant
    path('encadrant/<int:pk>/update/', views.encadrantUpdateView.as_view(), name='encadrant_update'),
    path('encadrant/<int:pk>/delete/', views.encadrantDeleteView.as_view(), name='delete_encadrant'),
    path('encadrant/', views.encadrant, name='encadrant'),
    path('createencadrant/', views.encadrantCreateView.as_view(), name='create_encadrant'),

    #etd
    path('etd/', views.etd, name='etd'),
    #encad
    path('encad/', views.encad, name='encad'),
     #stg
    path('stg/', views.stg, name='stg'),
     #stg
    path('stage/', views.stage, name='stage'),
    path('ajouter_groupe/',views.ajouter_groupe, name='ajouter_groupe'),
    path('ajouter_stage/',views.ajouter_stage, name='ajouter_stage'),
    path('ajouter_encd/',views.ajouter_encd, name='ajouter_encd'),

    
   
    path('import/', views.import_excel, name='import_excel'),
    path('view/', views.view_encadrent, name='view_encadrent'),

    path('creer-groupe/', creer_groupe, name='creer_groupe'),
    path('autocomplete-etudiants/', autocomplete_etudiants, name='autocomplete_etudiants'),

    path('export_excel/', views.export_excel, name='export_excel'),
    
    path('export_excel/', views.export_excel, name='export_excel'),
    
]