from django.shortcuts import render
from .models import Company


# Create your views here.
def index(request):
    return render(request, 'training/index.html')


def company(request):
    company = Company.objects.all()
    return render(request,'training/company.html',{'company':company})
