from django.urls import path

from ledger.views import ledgerHome

urlpatterns = [
    path("", homepage := ledgerHome, name="ledger-home"),
]