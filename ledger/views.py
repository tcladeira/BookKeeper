from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def ledgerHome(request: HttpRequest) -> HttpResponse:
    return render(request, 'ledger/pages/ledgerhome.html')