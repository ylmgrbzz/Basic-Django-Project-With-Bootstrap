from django.shortcuts import render,get_object_or_404
from .models import Urun

# Create your views here.

def home(request):
    urunler=Urun.objects.all()
    return render(request,'index.html',{'urunler':urunler})

def detay(request,urun_id):
    urungetir=get_object_or_404(Urun,pk=urun_id)
    return render(request,'detay.html',{'urun':urungetir})

def siparis(request,urun_id):
    urungetir=get_object_or_404(Urun,pk=urun_id)
    return render(request,'siparis.html',{'urun':urungetir})