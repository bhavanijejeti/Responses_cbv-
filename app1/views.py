from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
# Create your views here.
def fbv(request):
    return HttpResponse('this is function based views')

class cbv(View):
    def get(self,request):
        return HttpResponse('this is a class based views')
    
def fbv_first(request):
    return render(request,'fbv_first.html')

class cbv_first(View):
    def get(self,request):
        return render(request,'cbv_first.html')

class TV(TemplateView):
    def get(self,request):
        return HttpResponse('this is a templateview')
