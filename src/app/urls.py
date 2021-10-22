from django.urls import path, include, re_path
from . import views
from app.data_tables import (
    PersonaTable,
    SocietaTable,
    DocumentoBachecaTable,
    ScadenzarioTable
)

urlpatterns = [
    # Rotte frontend
    path('', views.routes),
    path('bacheca/', views.routes),
    path('persone/', views.routes),
    path('societa/', views.routes),
    path('scadenzario/', views.routes),
    path('nuova_utenza/', views.nuova_utenza),
    path('account/', include('django.contrib.auth.urls')),
    path('favicon.ico', views.favicon),
    # path('anagrafica/', views.routes),
    # path('anagrafica_data', views.anagrafica_data), # POC rotta per query diretta

    path('mail_nuova_utenza/', views.routes),

    # Rotta download
    re_path(r'^download/', views.download),

    # Rotte backend
    path('getDocumentiBacheca', DocumentoBachecaTable.as_view(), name="listaDocumentiBacheca"),
    path('getPersone', PersonaTable.as_view(), name="listaPersone"),
    path('getSocieta', SocietaTable.as_view(), name="listaSocieta"),
    path('getScadenzario', ScadenzarioTable.as_view(), name="listaScadenzario"),
]
