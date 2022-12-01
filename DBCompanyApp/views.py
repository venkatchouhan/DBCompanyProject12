from django.shortcuts import render

# Create your views here.
from DBCompanyApp.models import Company
def companydata(request):
    complist=Company.objects.all()
    dict1={'complist':complist}
    return render(request, 'DBCompanyApp/company.html', context=dict1);